from os import path
import csv
from talon import actions, scope, ui, resource
from user.knausj_talon.code.user_settings import SETTINGS_DIR
from .BaseGame import BaseGame

DEFAULT_ICON_DIRECTORY = path.dirname(path.abspath(__file__)) + '/game_icons'

def get_icon_path(app_name: str, icon: str):
    if path.isfile(icon):
        return icon

    icon_ = icon + '.png'
    if path.isfile(icon_):
        return icon_

    icon_ = DEFAULT_ICON_DIRECTORY + '/' + icon
    if path.isfile(icon_):
        return icon_

    icon_ = DEFAULT_ICON_DIRECTORY + '/' + icon + '.png'
    if path.isfile(icon_):
        return icon_

    icon_ = DEFAULT_ICON_DIRECTORY + '/' + app_name + '.png'
    if path.isfile(icon_):
        return icon_

    return ''

def get_games():
    filename = 'games.csv'
    headers = ("AppName", "Icon")
    path = SETTINGS_DIR / filename

    if not path.is_file():
        with open(path, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)

    # Now read via resource to take advantage of talon's
    # ability to reload this script for us when the resource changes
    with resource.open(str(path), "r") as f:
        rows = list(csv.reader(f))

    mapping = {}
    if len(rows) >= 2:
        actual_headers = rows[0]
        if not actual_headers == list(headers):
            print(
                f'"{filename}": Malformed headers - {actual_headers}.'
                + f" Should be {list(headers)}. Ignoring row."
            )
        for row in rows[1:]:
            if len(row) == 0:
                # Windows newlines are sometimes read as empty rows. :champagne:
                continue
            if len(row) == 1:
                icon = app_name = row[0]
            else:
                app_name, icon = row[:2]
                if len(row) > 2:
                    print(
                        f'"{filename}": More than two values in row: {row}.'
                        + " Ignoring the extras."
                    )
            icon = get_icon_path(app_name, icon)
            game = BaseGame(app_name, icon)
            mapping[app_name] = game

    return mapping

class GameModeHelper:
    _current_game : BaseGame = None
    _games : dict[str :  BaseGame] = get_games()

    def add_active_game_icon():
        if GameModeHelper.is_current_game_active():
            icon = GameModeHelper._current_game.get_icon_path()
            actions.user.hud_add_status_icon('active_game', icon)

    def remove_active_game_icon():
        actions.user.hud_remove_status_icon('active_game')

    def is_game_mode():
        modes = scope.get('mode')
        return 'user.game' in modes and 'sleep' not in modes

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

    def get_game_from_library(app_name : str):
        game = None
        if GameModeHelper._is_game_in_library(app_name):
            icon = GameModeHelper._games[app_name]
            game = BaseGame(app_name, icon)
        return game

    def _is_game_in_library(app_name : str):
        return app_name in GameModeHelper._games.keys()

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

def on_app_launch(app):
    if app.name in GameModeHelper._games.keys():
        GameModeHelper._current_game = GameModeHelper._games[app.name]

ui.register('app_launch', on_app_launch)
