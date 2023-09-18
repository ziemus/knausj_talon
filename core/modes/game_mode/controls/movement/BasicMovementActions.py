from threading import Lock
from talon import actions, Module, Context
from ...binding.ActiveBinding import ActiveBinding

game_movement_module = Module()
game_movement_module.list("game_directions")
game_movement_module.tag("game_basic_movement")

FORWARD = "move_forward"
BACKWARD = "move_backward"
LEFT = "strife_left"
RIGHT = "strife_right"

game_directions = {
    "north": FORWARD,
    "south": BACKWARD,
    "west": LEFT,
    "east": RIGHT,
}

ctx = Context()
ctx.lists["user.game_directions"] = game_directions

current_game_movement_direction_key: str = None
is_moving: bool = False
lock_is_moving = Lock()


def _nullify_current_movement_direction_key():
    global current_game_movement_direction_key
    current_game_movement_direction_key = None


def _start_game_movement():
    """Start moving in game direction. Not thread safe."""
    global is_moving, current_game_movement_direction_key
    if current_game_movement_direction_key is None:
        current_game_movement_direction_key = ActiveBinding.get(FORWARD)
    actions.user.game_hold_key_native(current_game_movement_direction_key)
    is_moving = True


def _stop_game_movement():
    """Stop in-game movement by releasing all movement keys (according to the active context). Not thread safe."""
    global is_moving
    if not current_game_movement_direction_key is None:
        actions.user.release_game_key(current_game_movement_direction_key)
    for direction_id in [FORWARD, BACKWARD, LEFT, RIGHT]:
        key = ActiveBinding.get(direction_id)
        actions.user.release_game_key(key)
    is_moving = False


def _set_game_movement_direction(direction_id: str):
    """Sets the key currently used to move in game. Not thread safe."""
    global current_game_movement_direction_key
    key = ActiveBinding.get(direction_id)
    current_game_movement_direction_key = key


def _switch_game_movement(do_turn_on: bool = None):
    do_turn_on = not is_moving if do_turn_on is None else do_turn_on
    if do_turn_on:
        _start_game_movement()
    else:
        _stop_game_movement()


def _switch_game_movement_direction(direction_key: str):
    if is_moving:
        _stop_game_movement()
        _set_game_movement_direction(direction_key)
        _start_game_movement()
    else:
        _set_game_movement_direction(direction_key)

@game_movement_module.action_class
class GameActions:

    def switch_game_movement(do_turn_on: bool = None):
        """toggle or switch game movement on/off. Thread safe."""
        global is_moving, lock_is_moving
        with lock_is_moving:
            _switch_game_movement(do_turn_on)

    def set_game_movement_direction(new_direction: str):
        """Sets the key currently used to move in game. Thread safe."""
        global lock_is_moving
        with lock_is_moving:
            _set_game_movement_direction(new_direction)

    def switch_game_movement_direction(new_direction: str):
        """Switches the key currently used to move in game. Continues moving in the new direction if movement is active. Thread safe."""
        global is_moving, lock_is_moving
        with lock_is_moving:
            _switch_game_movement_direction(new_direction)

    def game_movement_toggle_direction_switch(direction_key: str):
        """Start movement in the given direction if not moving
        or stop movement if the direction is equal to the current direction and moving
        or change the current direction while continuing movement."""
        global is_moving, lock_is_moving
        with lock_is_moving:
            if direction_key == current_game_movement_direction_key:
                _switch_game_movement()
            else:
                _switch_game_movement_direction(direction_key)

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

    def game_movement_go(direction_id: str):
        """Start moving in the specified direction"""
        # let us assume it is a regular key like W/S/A/D
        global is_moving, lock_is_moving
        with lock_is_moving:
            _switch_game_movement(False)
            _set_game_movement_direction(direction_id)
            _switch_game_movement(True)
