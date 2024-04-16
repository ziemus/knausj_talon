from talon import clip, actions, Module, Context, settings

mod = Module()
ctx = Context()

dictionary = mod.setting(
    "default_dictionary_url"
    , str
    , "https://www.merriam-webster.com/dictionary/"
)

@mod.action_class
class LookupActions:
    def web_dictionary_look_up(word: str, dict: str = None):
        """look the word up in the specified or default web dictionary"""
        browser = "firefox" #TODO 
        dict = dictionary.get() if dict is None else dict

        try:
            actions.mimic(f"focus {browser}")
        except:
            # FIXME
            actions.mimic(f"launch {browser}")
            actions.sleep("1000ms")
            actions.mimic(f"focus {browser}")
            actions.sleep("250ms")
            #close the master password prompt
            actions.key("esc")
        finally:
            actions.sleep("50ms")
            actions.app.tab_open()
            address = f"{dict}{word}"
            actions.browser.go(address)

    def web_dictionary_look_up_selection():
        """Look up the selected word in the default web dictionary"""
        word = actions.edit.selected_text()
        actions.user.web_dictionary_look_up(word)

    def web_dictionary_select_look_up():
        """Select the word at the cursor position
        then look it up in the default web dictionary"""
        for _ in range(2):
            actions.mouse_click()
        actions.user.web_dictionary_look_up_selection()
        
