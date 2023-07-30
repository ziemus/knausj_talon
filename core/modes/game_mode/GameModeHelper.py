from talon import actions, scope, ui
from talon.ui import App
from .BaseGame import BaseGame
from .game_library.game_library import GameLibrary
from .binding.ActiveBinding import ActiveBinding

class GameModeHelper:

    def add_active_game_icon():
        if GameModeHelper.is_current_game_active():
            icon = GameLibrary._current_game.get_icon_path()
            actions.user.hud_add_status_icon("active_game", icon)

    def game_hud_add_sprint_icon(is_sprint: bool):
        if is_sprint:
            icon = 'game_run'
        else:
            icon = 'game_walk'
        actions.user.hud_add_status_icon("game_sprint_state", icon)

    def game_hud_remove_icons():
        actions.user.hud_remove_status_icon("active_game")
        actions.user.hud_remove_status_icon("game_sprint_state")

    def is_game_mode():
        modes = scope.get("mode")
        return "user.game" in modes

    def is_current_game_active_and_game_mode():
        return GameModeHelper.is_game_active_and_game_mode(GameLibrary._current_game)

    def is_game_active_and_game_mode(game: BaseGame):
        is_game_focused = GameModeHelper.is_game_active(game)
        return is_game_focused and GameModeHelper.is_game_mode()

    def is_current_game_active():
        return GameModeHelper.is_game_active(GameLibrary._current_game)

    def is_game_active(game: BaseGame):
        if game is None:
            return False
        return ui.active_app().name == game.get_app_name()

    def get_game_from_library(app: App):
        game = None
        if GameModeHelper.is_game_in_library(app.name):
            icon = GameLibrary._games[app.name]
            game = BaseGame(app.name, icon)
        return game
    
    def get_current_game():
        return GameLibrary._current_game
    
    def get_binding(action_name: str = None):
        return ActiveBinding.get(action_name)
    
    def is_no_binding(action_name: str):
        return ActiveBinding.is_no_binding(action_name)

    def is_binding(action_name: str):
        return ActiveBinding.is_binding(action_name)

    def is_game_in_library(app: App):
        return app.name in GameLibrary._games.keys()


def on_app_deactivate(deactivated_app):
    if GameLibrary.is_app_current_game(deactivated_app):
        GameModeHelper.game_hud_remove_icons()


ui.register("app_deactivate", on_app_deactivate)