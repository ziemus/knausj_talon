from talon import actions, app
from .HotswappableKeybinding import HotswappableKeybinding
from ..GameModeHelper import GameModeHelper

default_keybinding_path = "./user/knausj_talon/core/modes/game_mode/binding/default.json"
default_keybinding: HotswappableKeybinding = HotswappableKeybinding(default_keybinding_path)


class BindingExecutor:

    def __execute_input(input):
        is_simple = isinstance(input, str)
        if is_simple:
            actions.key(input)
            return
    
        mouse = input.get("mouse")
        key = input.get("key")
        is_hold_down = input.get("hold_down")
        duration = input.get("duration")
        times = input.get("times")
        times = 1 if times is None else times

        is_mouse = not mouse is None
        is_duration = not duration is None
        is_held_released = not is_hold_down is None

        if is_mouse:
            if is_held_released:
                actions.user.game_press_mouse(mouse, is_hold_down)
            else:
                actions.user.game_click(mouse, times, duration)
            return
        
        if is_duration:
            actions.user.press_game_key(key, times, duration)
        elif is_held_released:
            if is_hold_down:
                actions.user.game_hold_key_native(key)
            else:
                actions.user.release_game_key(key)
        else:
            actions.key(f"{key}:{times}")
        

    def __execute_inputs(binding, action):
        inputs = BindingExecutor.__parse(binding[action])
        is_series = isinstance(inputs, list)
        if is_series:
            for input in inputs:
                BindingExecutor.__execute_input(input)
            return
        BindingExecutor.__execute_input(input)
        
    def execute(action: str):
        keybinding = GameModeHelper.get_current_game().get_binding()
        if action not in keybinding.keys():
            keybinding = default_keybinding.get_binding()
        elif action not in default_keybinding.keys():
            app.notify("Undefined binding", f"for action: {action}")
            return
        
        BindingExecutor.__execute_inputs(keybinding, action)

        
        
    def execute_or_substitute(primary_action: str, secondary_action: str):
        custom = GameModeHelper.get_current_game().get_binding()
        default = default_keybinding.get_binding()
        if primary_action in custom.keys():
            BindingExecutor.__execute_inputs(custom, primary_action)
        elif secondary_action in custom.keys():
            BindingExecutor.__execute_inputs(custom, secondary_action)
        elif primary_action in default.keys():
            BindingExecutor.__execute_inputs(default, primary_action)
        elif secondary_action in default.keys():
            BindingExecutor.__execute_inputs(default, secondary_action)
        else:
            app.notify("Undefined binding", f"action: {primary_action} with substitute action: {secondary_action}")

        