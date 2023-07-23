from typing import Union
from talon import actions, app, settings
from .HotswappableKeybinding import HotswappableKeybinding
from ..GameModeHelper import GameModeHelper

default_keybinding_path = "./user/knausj_talon/core/modes/game_mode/binding/default.json"
default_keybinding: HotswappableKeybinding = HotswappableKeybinding(default_keybinding_path)

mouse_button_str = {
    "LEFT": 0,
    "RIGHT": 1,
    "MIDDLE": 2,
    "MID": 2,
    "LMB": 0,
    "RMB": 1,
    "MMB": 2,
}

mouse_wheel_directions = {
    "up": -1,
    "down": 1,
    -1: -1,
    1: 1
}

class BindingExecutor:

    def __get_mouse_button(button: Union[int, str]):
        if isinstance(button, str):
            return mouse_button_str.get(button.upper())
        return button

    def __get_input_value(input, value_id):
        value = input.get(value_id)
        try:
            setting = value.get("setting")
            return settings.get(setting)
        except AttributeError:
            return value

    def __execute_input(input):
        is_simple = isinstance(input, str)
        if is_simple:
            actions.key(input)
            return
    
        mouse = BindingExecutor.__get_input_value(input, "mouse_button")
        mouse = BindingExecutor.__get_mouse_button(mouse)
        key = BindingExecutor.__get_input_value(input, "key")
        wheel_direction = BindingExecutor.__get_input_value(input, "wheel_direction")
        wheel_amount = BindingExecutor.__get_input_value(input, "wheel_amount")
        is_hold_down = BindingExecutor.__get_input_value(input, "hold_down")
        duration = BindingExecutor.__get_input_value(input, "duration")
        times = BindingExecutor.__get_input_value(input, "times")

        wheel_direction = 1 if wheel_direction is None else wheel_direction
        times = 1 if times is None else times

        is_mouse_button = not mouse is None
        is_wheel = not (wheel_direction is None and wheel_amount is None)
        is_duration = not duration is None
        is_held_released = not is_hold_down is None

        if is_mouse_button:
            if is_held_released:
                actions.user.game_press_mouse(mouse, is_hold_down)
            else:
                actions.user.game_click(mouse, times, duration)
            return
        
        if is_wheel:
            direction = mouse_wheel_directions.get(wheel_direction)
            wheel_amount *= direction
            actions.mouse_scroll(y=wheel_amount)
            return 
        # assumed keyboard input
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
        inputs = binding[action]
        is_series = isinstance(inputs, list)
        if is_series:
            for input in inputs:
                BindingExecutor.__execute_input(input)
            return
        BindingExecutor.__execute_input(inputs)
        
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
        