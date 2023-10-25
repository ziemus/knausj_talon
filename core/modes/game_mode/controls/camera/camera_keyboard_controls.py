from talon import settings, actions, Module, Context
from ...binding.ActiveBinding import ActiveBinding

mod = Module()
mod.tag("game_camera_keyboard_controls")

ctx = Context()
ctx.matches = """
mode: user.game
and tag: user.game_camera_keyboard_controls
"""
ctx.lists["user.game_camera_direction"] = {
    "left": "camera_left",
    "right": "camera_right",
    "up": "camera_up",
    "down": "camera_down",
    "let": "camera_left",
    "rye": "camera_right",
}

@ctx.action_class("user")
class Actions:
    def game_turn_camera(direction: str, cursor_movement_multiplier: float = None):
        input = ActiveBinding.get(direction)
        key = input.get("key")
        duration = input.get("hold")

        if cursor_movement_multiplier:
            duration *= cursor_movement_multiplier
            duration = int(duration)
        
        actions.user.game_hold_key_native(key, duration)

    def game_turn_camera_around():
        input = ActiveBinding.get("camera_turn_around")
        key = input.get("key")
        duration = input.get("hold")
        actions.user.game_hold_key_native(key, duration)