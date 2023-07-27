from typing import Union
from talon import actions, settings
from .ActiveBinding import ActiveBinding

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
        is_wheel = not wheel_amount is None
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
        
        if is_held_released:
            if is_hold_down:
                actions.user.game_hold_key_native(key)
            else:
                actions.user.release_game_key(key)
        elif is_duration:
            actions.user.press_game_key(key, times, duration)
        else:
            actions.key(f"{key}:{times}")

    def __execute_inputs(inputs):
        is_series = isinstance(inputs, list)
        if is_series:
            for input in inputs:
                BindingExecutor.__execute_input(input)
            return
        BindingExecutor.__execute_input(inputs)
    
    def execute(action: str):
        inputs = ActiveBinding.get(action)
        BindingExecutor.__execute_inputs(inputs)
        
    def execute_or_substitute(primary_action: str, secondary_action: str):
        inputs = ActiveBinding.get_alternative(primary_action, secondary_action)
        BindingExecutor.__execute_inputs(inputs)
        