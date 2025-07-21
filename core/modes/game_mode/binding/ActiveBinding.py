from talon import app
from .HotswappableKeybinding import HotswappableKeybinding
from ..game_library.game_library import GameLibrary


class ActiveBinding:
    default_keybinding_path = "./user/knausj_talon/core/modes/game_mode/binding/default.json"
    default_keybinding: HotswappableKeybinding = HotswappableKeybinding(default_keybinding_path)
    
    def get(action: str = None):
        keybinding = GameLibrary.get_current_game().get_binding()
        if action not in keybinding.keys():
            keybinding = ActiveBinding.default_keybinding.get_binding()
        if action not in keybinding.keys():
            app.notify("Undefined binding", f"for action: {action}")
        return keybinding.get(action)
    
    def get_alternative(primary: str, secondary: str):
        custom = GameLibrary.get_current_game().get_binding()
        default = ActiveBinding.default_keybinding.get_binding()
        keybinding = custom
        action = primary
        if primary in custom.keys():
            keybinding = custom
            action = primary
        elif secondary in custom.keys():
            keybinding = custom
            action = secondary
        elif primary in default.keys():
            keybinding = default
            action = primary
        elif secondary in default.keys():
            keybinding = default
            action = secondary
        else:
            app.notify("Undefined binding", f"action: {primary} with substitute action: {secondary}")
        return keybinding.get(action)
        
    def is_no_binding(action_name: str):
        return ActiveBinding.get(action_name) is None

    def is_binding(action_name: str):
        return not ActiveBinding.is_no_binding(action_name)