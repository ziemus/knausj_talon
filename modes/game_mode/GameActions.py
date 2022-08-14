from talon import actions, scope, Context
from .game_mode import game_mode_module
from .GameModeHelper import GameModeHelper

default_game_mode_context = Context()
default_game_mode_context.lists['user.game_directions'] = {
    'north': 'w'
    , 'south': 's'
    , 'west': 'a'
    , 'east': 'd'
}

# TODO get current user.game_directions list according to the active context
current_game_movement_direction = default_game_mode_context.lists['user.game_directions']['north']
is_moving : bool = False

@game_mode_module.action_class
class GameActions:
    def start_game_movement():
        """Start moving in game direction"""
        global is_moving, current_game_movement_direction
        is_moving = True
        actions.user.hold_game_key(current_game_movement_direction)

    def stop_game_movement():
        """Stop in-game movement by releasing all movement keys (according to the active context)"""
        global is_moving
        is_moving = False
        directions = actions.user.get_game_movement_keys()
        for key in directions:
            actions.user.release_game_key(key)

    def set_game_movement_direction(new_direction : str):
        """Sets the key currently used to move in game"""
        global current_game_movement_direction
        current_game_movement_direction = new_direction

    def switch_game_movement_direction(new_direction : str):
        """Switches the key currently used to move in game. Continues moving in the new direction if movement is active"""
        global is_moving
        actions.user.set_game_movement_direction(new_direction)
        if is_moving:
            actions.user.stop_game_movement()
            actions.user.start_game_movement()

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
        keys = ['w' , 's' , 'a' , 'd']
        return keys

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


