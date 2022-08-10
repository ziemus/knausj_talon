from os import path
from talon import Module, actions, scope
from user.talon_hud.content.programming_language_poller import remove_statusbar_programming_icon

mod = Module()
mod.mode("game", "Gaming Mode that doesn't accept regular commands")

@mod.action_class
class GameModeActions:
    def enable_game_mode():
        """Switches the game mode on"""
        remove_statusbar_programming_icon()
        actions.mode.enable("user.game")
        GameModeHelper.add_active_game_icon()
        actions.user.custom_game_setup()
        
    def disable_game_mode():
        """Switches the game mode off"""
        # Make sure the shift key is no longer pressed when switching back to normal
        GameModeHelper.release_pressed_keys()
        GameModeHelper.remove_active_game_icon()
        actions.user.custom_game_cleanup()
        actions.mode.disable("user.game")       

    def custom_game_setup():
        """additional setup to be overridden using contexts"""
        return 0
        
    def custom_game_cleanup():
        """additional cleanup to be overridden using contexts"""
        return 0
    
    def get_game_icon_path():
        """Returns path to icon; to be overridden using contexts"""
        return ''

    def get_pressed_game_keys():
        """
        Returns a list of frequently pressed keys in games
        so that they can be released upon exiting from game mode.
        May be overridden with contexts to suit a specific game.
        """
        keys = [ 'shift'
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

class GameModeHelper:
    def add_active_game_icon():
        icon = actions.user.get_game_icon_path()
        if not icon == '':
            actions.user.hud_add_status_icon('active_game', icon)

    def remove_active_game_icon():
        actions.user.hud_remove_status_icon('active_game')

    def is_game_mode():
        return 'user.game' in scope.get('mode')

    def release_pressed_keys():
        for key in actions.user.get_pressed_game_keys():
            actions.key(key + ':up')
        
    def get_game_talonscript_directory(file):
        # FIXME: return actual games directory and eliminate passing the __file__ variable each time
        return path.dirname(path.abspath(file))