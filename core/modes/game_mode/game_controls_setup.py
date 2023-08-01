from talon import actions, ui
from .controls.movement.BasicMovementActions import _nullify_current_movement_direction_key
from .GameModeHelper import GameModeHelper

def game_cleanup():
    actions.user.game_weapon_aim_toggle(False)
    actions.user.game_weapon_block_toggle(False)
    actions.user.game_switch_sprint(False)
    actions.user.switch_game_movement(False)
    actions.user.release_held_game_keys()

def _on_app_launch_close(app):
    if GameModeHelper.is_game_in_library(app):
        actions.user.custom_game_setup()
        game_cleanup()
        _nullify_current_movement_direction_key()
        actions.user.game_noise_control_reset()


ui.register("app_close", _on_app_launch_close)
ui.register("app_launch", _on_app_launch_close)


def window_focus_cleanup(app):
    if GameModeHelper.is_game_in_library(app):
        game_cleanup()


ui.register("app_activate", window_focus_cleanup)
ui.register("app_deactivate", window_focus_cleanup)