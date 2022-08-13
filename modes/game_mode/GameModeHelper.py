from os import path
from talon import actions, scope, ui

from .BaseGame import BaseGame

class GameModeHelper:
    _current_game : BaseGame = None

    def set_current_game(game : BaseGame):
        """Sets the _current_game to game
        the idea behind this is to automate displaying active game icon on the status bar (talon hud)
        by on_app_activate and on_app_deactivate
        so new event handles that do the same job
        don't have to be registered for each game

        For this to work one needs to register an event handle
        on app_launch for each game
        that calls this method with the appropriate game
        instead of both on_app_activate and on_app_deactivate
        """
        GameModeHelper._current_game = game

    def add_active_game_icon():
        if GameModeHelper.is_current_game_active():
            icon = GameModeHelper._current_game.get_icon_path()
            actions.user.hud_add_status_icon('active_game', icon)

    def remove_active_game_icon():
        actions.user.hud_remove_status_icon('active_game')

    def is_game_mode():
        modes = scope.get('mode')
        return 'user.game' in modes and 'sleep' not in modes

    def release_held_keys():
        for key in actions.user.get_pressed_game_keys():
            actions.key(key + ':up')

    def get_game_talonscript_directory(file):
        # FIXME: return actual games directory and eliminate passing the __file__ variable each time
        return path.dirname(path.abspath(file))

    def is_current_game_active_and_game_mode():
        return GameModeHelper.is_game_active_and_game_mode(GameModeHelper._current_game)

    def is_game_active_and_game_mode(game : BaseGame):
        is_game_focused = GameModeHelper.is_game_active(game)
        return is_game_focused and GameModeHelper.is_game_mode()

    def is_current_game_active():
        return GameModeHelper.is_game_active(GameModeHelper._current_game)

    def is_game_active(game : BaseGame):
        if game is None:
            return False
        return ui.active_app().name == game.get_app_name()

def on_app_activate(_):
    if GameModeHelper.is_current_game_active_and_game_mode():
        GameModeHelper.add_active_game_icon()

def on_app_deactivate(deactivated_app):
    game = GameModeHelper._current_game
    if game is None:
        return
    is_deactivated_game = deactivated_app.name == game.get_app_name()
    if is_deactivated_game and GameModeHelper.is_game_mode():
        GameModeHelper.remove_active_game_icon()

ui.register('app_activate', on_app_activate)
ui.register('app_deactivate', on_app_deactivate)
