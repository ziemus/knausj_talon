from talon import actions, scope, ui, fs, settings
from talon.ui import App
from .BaseGame import BaseGame
from .game_library import games, game_library_path

class GameModeHelper:
    _current_game: BaseGame = None

    def add_active_game_icon():
        if GameModeHelper.is_current_game_active():
            icon = GameModeHelper._current_game.get_icon_path()
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
        return GameModeHelper.is_game_active_and_game_mode(GameModeHelper._current_game)

    def is_game_active_and_game_mode(game: BaseGame):
        is_game_focused = GameModeHelper.is_game_active(game)
        return is_game_focused and GameModeHelper.is_game_mode()

    def is_current_game_active():
        return GameModeHelper.is_game_active(GameModeHelper._current_game)

    def is_game_active(game: BaseGame):
        if game is None:
            return False
        return ui.active_app().name == game.get_app_name()

    def get_game_from_library(app: App):
        game = None
        if GameModeHelper._is_game_in_library(app.name):
            icon = games[app.name]
            game = BaseGame(app.name, icon)
        return game
    
    def get_current_game():
        return GameModeHelper._current_game
    
    def _set_current_game(game: BaseGame):
        GameModeHelper._current_game = game

    def _is_game_in_library(app: App):
        return app.name in games.keys()


def track_current_game(app_name: str):
    if app_name in games.keys():
        cg_updated = games[app_name]
        GameModeHelper._set_current_game(cg_updated)


def on_app_launch(app):
    track_current_game(app.name)


def on_app_activate(_):
    on_app_launch(_)
    if GameModeHelper.is_current_game_active_and_game_mode():
        is_sprinting = settings.get("user.game_sprint_state_default")
        GameModeHelper.game_hud_add_sprint_icon(is_sprinting)
        GameModeHelper.add_active_game_icon()


def on_app_deactivate(deactivated_app):
    game = GameModeHelper._current_game
    if game is None:
        return
    is_deactivated_game = deactivated_app.name == game.get_app_name()
    if is_deactivated_game and GameModeHelper.is_game_mode():
        GameModeHelper.game_hud_remove_icons()


def update_current_game(name, flags):
    """Update current game on game library change.
    Needed to effectively update the active binding on GameModeHelper._current_game
    after changing its binding path in the game library file.
    Without updating the current game after changing the library there's a chance
    GameModeHelper._current_game would still be set to a BaseGame without a binding."""
    cg = GameModeHelper.get_current_game()
    if cg is None:
        return
    app_name = cg.get_app_name()
    track_current_game(app_name)


ui.register("app_launch", on_app_launch)
ui.register("app_activate", on_app_activate)
ui.register("app_deactivate", on_app_deactivate)
fs.watch(game_library_path, update_current_game)