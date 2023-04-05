from talon import Module, Context, actions
mod = Module()
narrator_key_setting = mod.setting("windows_narrator_key", type=str, default="insert")
mod.list("windows_narrator_synonyms")
ctx = Context()
ctx.lists["user.windows_narrator_synonyms"] = ["narrator", "narrate", "nor"]

@mod.action_class
class Actions:
    def windows_narrator_action(keys: str):
        """"""
        narrator_key = narrator_key_setting.get()
        actions.key(f"{narrator_key}:down")
        actions.key(keys)
        actions.key(f"{narrator_key}:up")