from threading import Lock
import win32api, win32con
from talon import actions, scope, Context, ui, ctrl
from talon.types import Point2d
from .game_mode import game_mode_module
from .GameModeHelper import GameModeHelper

# TODO get current user.game_directions list according to the active context
current_game_movement_direction = "w"
is_moving: bool = False
lock_is_moving = Lock()
is_sprinting: bool = False
lock_is_sprinting = Lock()
WIN_API_SCREEN_RESOLUTION: float = 65535.0


def _start_game_movement():
    """Start moving in game direction. Not thread safe."""
    global is_moving, current_game_movement_direction
    actions.user.hold_game_key(current_game_movement_direction)
    is_moving = True


def _stop_game_movement():
    """Stop in-game movement by releasing all movement keys (according to the active context). Not thread safe."""
    global is_moving
    directions = actions.user.get_game_movement_keys()
    for key in directions:
        actions.user.release_game_key(key)
    is_moving = False


def _set_game_movement_direction(new_direction: str):
    """Sets the key currently used to move in game. Not thread safe."""
    global current_game_movement_direction
    current_game_movement_direction = new_direction


def _on_app_launch_close(app):
    if GameModeHelper._is_game_in_library(app):
        actions.user.game_sprint_state_reset()
        actions.user.game_movement_state_reset()
        actions.user.release_held_game_keys()


ui.register("app_close", _on_app_launch_close)
ui.register("app_launch", _on_app_launch_close)


@game_mode_module.action_class
class GameActions:

    def switch_game_movement(do_turn_on: bool = None):
        """toggle or switch game movement on/off. Thread safe."""
        global is_moving, lock_is_moving
        with lock_is_moving:
            do_turn_on = not is_moving if do_turn_on is None else do_turn_on
            if do_turn_on:
                _start_game_movement()
            else:
                _stop_game_movement()

    def set_game_movement_direction(new_direction: str):
        """Sets the key currently used to move in game. Thread safe."""
        global lock_is_moving
        with lock_is_moving:
            _set_game_movement_direction(new_direction)

    def switch_game_movement_direction(new_direction: str):
        """Switches the key currently used to move in game. Continues moving in the new direction if movement is active. Thread safe."""
        global is_moving, lock_is_moving
        with lock_is_moving:
            _set_game_movement_direction(new_direction)
            if is_moving:
                _stop_game_movement()
                _start_game_movement()

    def game_turn_camera_around():
        """WIP turn camera around"""
        dx = actions.user.game_get_mouse_delta_x_for_turning_camera_around()
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, 0)

    def game_get_mouse_delta_x_for_turning_camera_around():
        """ for each game there needs to be defined a particular horizontal delta
        that mouse needs to be moved by
        in order to turn the camera around

        this action needs to be overridden with game-specific contexts

        basically the user needs to experiment a little
        and find the right value

        in my experience, it will never be perfectly accurate
        but it will be enough to play"""
        pass

    def game_jump():
        """"""
        actions.user.press_game_key("space")

    def game_switch_sprint(do_turn_on: bool = None):
        """"""
        global is_sprinting, lock_is_sprinting
        with lock_is_sprinting:
            do_turn_on = not is_sprinting if do_turn_on is None else do_turn_on
            toggle_sprint_key = actions.user.game_get_switch_sprint_key()
            if do_turn_on and not is_sprinting:
                actions.user.press_game_key(toggle_sprint_key)
                is_sprinting = True
            elif not do_turn_on and is_sprinting:
                actions.user.press_game_key(toggle_sprint_key)
                is_sprinting = False

    def game_sprint_state_reset():
        """Resets is_sprinting to False
        in case the game overrides sprint behavior
        after, for example, a loading screen
        which would mess up the execution of 'run' and 'walk' commands
        with the default game_switch_sprint()"""
        global is_sprinting, lock_is_sprinting
        with lock_is_sprinting:
            is_sprinting = actions.user.game_get_default_sprint_state()

    def game_get_default_sprint_state():
        """see GameActions.game_sprint_state_reset()
        to be overridden with game specific contexts"""
        return False

    def game_movement_state_reset():
        """Resets is_moving to False
        in case the game overrides movement behavior
        after, for example, a loading screen
        or the user exits the game (or the game mode) without stopping the movement
        which would mess up the execution of 'go' and 'stop' commands
        with the default game_switch_movement()"""
        global is_moving, lock_is_moving
        with lock_is_moving:
            is_moving = False

    def game_get_switch_sprint_key():
        """Default binding in game mode
        to be overridden with game specific contexts or in-game controls"""
        return "\\"

    def game_use():
        """"""
        actions.user.press_game_key('e')

    def game_click():
        """"""
        ctrl.mouse_click(0)

    def press_game_key(key: str):
        """"""
        actions.key(key)

    def hold_game_key(key: str, duration: str = None):
        """Hold key infinitely or for the specified duration"""
        actions.key(key + ":down")
        if duration is None:
            return
        actions.sleep(duration)
        actions.user.release_game_key(key)

    def release_game_key(key: str):
        """"""
        actions.key(key + ":up")

    def release_held_game_keys():
        """"""
        for key in actions.user.get_held_game_keys():
            actions.user.release_game_key(key)

    def get_game_movement_keys():
        """this method must be overridden with game-specific contexts
        unless the game movement is the standard WSAD

        It should return the same list of values
        as the context for the specific game
        stores under context.lists['user.game_directions']
        until talon allows to obtain the list directly
        """
        # TODO get current user.game_directions list according to the active context
        # Or create tags or different types of movement controls: arrows
        # and apply contexts for them specificly, overriding this method too
        return []

    def get_held_game_keys():
        """
        Returns a list of frequently held (long pressed) keys in games
        so that they can be released upon exiting from game mode.
        May be overridden with contexts to suit a specific game.
        """
        keys = ["shift", "a", "d", "w", "s", "e", "q", "up", "down", "left", "right"]
        return keys
