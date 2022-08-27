from threading import Lock
from talon import actions, scope, Context
from .game_mode import game_mode_module
from .GameModeHelper import GameModeHelper


# TODO get current user.game_directions list according to the active context
current_game_movement_direction = 'w'
is_moving : bool = False
lock_is_moving = Lock()
is_sprinting : bool = False
lock_is_sprinting = Lock()

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

def _set_game_movement_direction(new_direction : str):
    """Sets the key currently used to move in game. Not thread safe."""
    global current_game_movement_direction
    current_game_movement_direction = new_direction

@game_mode_module.action_class
class GameActions:
    def switch_game_movement(do_turn_on : bool = None):
        """toggle or switch game movement on/off. Thread safe."""
        global is_moving, lock_is_moving
        with lock_is_moving:
            do_turn_on = not is_moving if do_turn_on is None else do_turn_on
            if do_turn_on:
                _start_game_movement()
            else:
                _stop_game_movement()

    def set_game_movement_direction(new_direction : str):
        """Sets the key currently used to move in game. Thread safe."""
        global lock_is_moving
        with lock_is_moving:
            _set_game_movement_direction(new_direction)

    def switch_game_movement_direction(new_direction : str):
        """Switches the key currently used to move in game. Continues moving in the new direction if movement is active. Thread safe."""
        global is_moving, lock_is_moving
        with lock_is_moving:
            _set_game_movement_direction(new_direction)
            if is_moving:
                _stop_game_movement()
                _start_game_movement()

    def game_jump():
        """"""
        actions.user.press_game_key('space')

    def game_switch_sprint(do_turn_on : bool = None):
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
            is_sprinting = False

    def game_get_switch_sprint_key():
        """Default binding in game mode to be overridden with game specific contexts or in game controls"""
        return '\\'

    def press_game_key(key : str):
        """"""
        actions.key(key)

    def hold_game_key(key : str, duration : str = None):
        """Hold key infinitely or for the specified duration"""
        actions.key(key + ':down')
        if duration is None:
            return
        actions.sleep(duration)
        actions.user.release_game_key(key)

    def release_game_key(key : str):
        """"""
        actions.key(key + ':up')

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
        keys = [
            'shift'
            , 'a'
            , 'd'
            , 'w'
            , 's'
            , 'e'
            , 'q'
            , 'up'
            , 'down'
            , 'left'
            , 'right'
        ]
        return keys


