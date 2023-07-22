from talon import actions
from .HotswappableKeybinding import HotswappableKeybinding
from ..GameModeHelper import GameModeHelper

default_keybinding_path = "./user/knausj_talon/core/modes/game_mode/binding/default.json"
default_keybinding: HotswappableKeybinding = HotswappableKeybinding(default_keybinding_path)


class BindingExecutor:
    def __parse(keys: str):
        #TODO TIMINGS
        return keys.split(";")

    def __execute(keybinding, action):
        keypresses = BindingExecutor.__parse(keybinding[action])
        for keys in keypresses:
            #TODO TIMINGS
            actions.key(keys)

    def execute(action: str):
        keybinding = GameModeHelper.get_current_game().get_binding()
        if action not in keybinding.keys():
            keybinding = default_keybinding.get_binding()
        BindingExecutor.__execute(keybinding, action)
        
    def execute_or_substitute(primary_action: str, secondary_action: str):
        custom = GameModeHelper.get_current_game().get_binding()
        default = default_keybinding.get_binding()
        if primary_action in custom.keys():
            BindingExecutor.__execute(custom, primary_action)
        elif secondary_action in custom.keys():
            BindingExecutor.__execute(custom, secondary_action)
        elif primary_action in default.keys():
            BindingExecutor.__execute(default, primary_action)
        else:
            BindingExecutor.__execute(default, secondary_action)

        