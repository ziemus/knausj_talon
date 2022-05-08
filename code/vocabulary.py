import logging
from typing import Dict, Sequence

from talon import Context, Module, actions
from .user_settings import get_list_from_csv

mod = Module()
ctx = Context()

mod.list("vocabulary", desc="additional vocabulary words")

# "dictate.word_map" is used by `actions.dictate.replace_words` to rewrite words
# Talon recognized. Entries in word_map don't change the priority with which
# Talon recognizes some words over others.

# phrases_to_replace is a spoken form -> written form map, used by
# `user.replace_phrases` to rewrite words and phrases Talon recognized.
# This does not change the priority with which Talon recognizes
# particular phrases over others.
phrases_to_replace = get_list_from_csv(
    "words_to_replace.csv",
    headers=("Replacement", "Original"),
)

# "dictate.word_map" is used by `actions.dictate.replace_words`;
# a built-in Talon action similar to `replace_phrases`, but supporting
# only single-word replacements. Multi-word phrases are ignored.
ctx.settings["dictate.word_map"] = phrases_to_replace


# "user.vocabulary" is used to explicitly add words/phrases that Talon doesn't
# recognize. Words in user.vocabulary (or other lists and captures) are
# "command-like" and their recognition is prioritized over ordinary words.
ctx.lists["user.vocabulary"] = get_list_from_csv(
    "additional_words.csv", headers=("Word(s)", "Spoken Form (If Different)"),
)

# for quick verification of the reload
# print(str(ctx.settings["dictate.word_map"]))
# print(str(ctx.lists["user.vocabulary"]))

class PhraseReplacer:
    """Utility for replacing phrases by other phrases inside text or word lists.

    Replacing longer phrases has priority.

    Args:
      - phrase_dict: dictionary mapping recognized/spoken forms to written forms
    """

    def __init__(self, phrase_dict: Dict[str, str]):
        # Index phrases by first word, then number of subsequent words n_next
        phrase_index = dict()
        for spoken_form, written_form in phrase_dict.items():
            words = spoken_form.split()
            if not words:
                logging.warning("Found empty spoken form for written form"
                                f"{written_form}, ignored")
                continue
            first_word, n_next = words[0], len(words) - 1
            phrase_index.setdefault(first_word, {}) \
                        .setdefault(n_next, {})[tuple(words[1:])] = written_form

        # Sort n_next index so longer phrases have priority
        self.phrase_index = {
            first_word: list(sorted(same_first_word.items(), key=lambda x: -x[0]))
            for first_word, same_first_word in phrase_index.items()
        }

    def replace(self, input_words: Sequence[str]) -> Sequence[str]:
        input_words = tuple(input_words) # tuple to ensure hashability of slices
        output_words = []
        first_word_i = 0
        while first_word_i < len(input_words):
            first_word = input_words[first_word_i]
            next_word_i = first_word_i + 1
            # Could this word be the first of a phrase we should replace?
            for n_next, phrases_n_next in self.phrase_index.get(first_word, []):
                # Yes. Perhaps a phrase with n_next subsequent words?
                continuation = input_words[next_word_i : next_word_i + n_next]
                if continuation in phrases_n_next:
                    # Found a match!
                    output_words.append(phrases_n_next[continuation])
                    first_word_i += 1 + n_next
                    break
            else:
                # No match, just add the word to the result
                output_words.append(first_word)
                first_word_i += 1
        return output_words

    # Wrapper used for testing.
    def replace_string(self, text: str) -> str:
        return ' '.join(self.replace(text.split()))

# Unit tests for PhraseReplacer
rep = PhraseReplacer({
    'this': 'foo',
    'that': 'bar',
    'this is': 'stopping early',
    'this is a test': 'it worked!',
})
assert rep.replace_string('gnork') == 'gnork'
assert rep.replace_string('this') == 'foo'
assert rep.replace_string('this that this') == 'foo bar foo'
assert rep.replace_string('this is a test') == 'it worked!'
assert rep.replace_string('well this is a test really') == 'well it worked! really'
assert rep.replace_string('try this is too') == 'try stopping early too'
assert rep.replace_string('this is a tricky one') == 'stopping early a tricky one'

phrase_replacer = PhraseReplacer(phrases_to_replace)

@ctx.action_class('dictate')
class OverwrittenActions:
    def replace_words(words: Sequence[str]) -> Sequence[str]:
        try:
            return phrase_replacer.replace(words)
        except:
            # fall back to default implementation for error-robustness
            logging.error("phrase replacer failed!")
            return actions.next(words)
