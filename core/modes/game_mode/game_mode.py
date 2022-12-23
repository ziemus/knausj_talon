from talon import Module, actions
from user.talon_hud.content.programming_language_poller import (
    remove_statusbar_programming_icon,)

from .GameModeHelper import GameModeHelper

game_mode_module = Module()
game_mode_module.mode("game", "Gaming Mode that doesn't accept regular commands")
game_mode_module.list("game_directions")
game_mode_module.list("game_number_shortcuts")
game_mode_module.tag("first_person_game_controls")
game_mode_module.tag("game_basic_movement")
game_mode_module.tag("game_camera_controls")
game_mode_module.tag("game_sprint_controls")
game_mode_module.tag("game_character_sheet")
game_mode_module.tag("game_mouse_enabled")
setting_turn_around_delta = game_mode_module.setting(
    "game_turn_around_mouse_delta",
    type=int,
    default=0,
    desc=""" for each game there needs to be defined a particular horizontal delta
        that mouse needs to be moved by
        in order to turn the camera around

        basically the user needs to experiment a little
        and find the right value

        in my experience, it will never be perfectly accurate
        but it will be enough to play""")
setting_turn_horizontally_delta = game_mode_module.setting(
    "game_turn_horizontally_mouse_delta",
    type=int,
    default=0,
    desc=""" for each game there needs to be defined a particular horizontal delta
        that mouse needs to be moved by
        in order to turn the camera horizontally

        basically the user needs to experiment a little
        and find the right value

        in my experience, it will never be perfectly accurate
        but it will be enough to play""")
setting_turn_vertically_delta = game_mode_module.setting(
    "game_turn_vertically_mouse_delta",
    type=int,
    default=0,
    desc=""" for each game there needs to be defined a particular vertical delta
        that mouse needs to be moved by
        in order to turn the camera vertically

        basically the user needs to experiment a little
        and find the right value

        in my experience, it will never be perfectly accurate
        but it will be enough to play""")
setting_sprint_toggle_key = game_mode_module.setting(
    "game_sprint_toggle_key",
    type=str,
    default="capslock",
    desc="""Keyname for the key that switches sprint on/off. Caps Lock by default.""")
setting_default_sprint_state = game_mode_module.setting(
    "game_sprint_state_default",
    type=bool,
    default=False,
    desc="""Helps in tracking the in-game sprint/walk state.
        See the comment on GameActions.game_sprint_state_reset() for more information.
        Sho5uld be set to true when the default in-game behavior is running instead of walking (e.g. in Antichamber).
        By default false.""")
setting_default_movement_direction = game_mode_module.setting(
    "game_default_movement_key",
    type=str,
    default="w",
    desc="""Default movement key.
    Can be modified so that you don't have to issue the movement direction change command
    by voice after launching the game every time.""")
@game_mode_module.action_class
class GameModeActions:

    def enable_game_mode():
        """Switches the game mode on"""
        remove_statusbar_programming_icon()
        actions.mode.enable("user.game")
        GameModeHelper.add_active_game_icon()

    def disable_game_mode():
        """Switches the game mode off"""
        actions.user.release_held_game_keys()
        actions.user.game_sprint_state_reset()
        GameModeHelper.game_hud_remove_icons()
        actions.user.game_movement_state_reset()
        actions.mode.disable("user.game")

    def custom_game_setup():
        """additional setup to be overridden using contexts"""
        return 0

    def custom_game_cleanup():
        """additional cleanup to be overridden using contexts"""
        return 0