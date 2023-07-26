from os import path
import csv
from talon import fs, ui
from pathlib import Path
from ..BaseGame import BaseGame

SCRIPT_DIR = path.dirname(path.abspath(__file__))

class GameLibrary:    
    _DEFAULT_ICON_DIRECTORY = f"{SCRIPT_DIR}/game_icons"
    _GAME_LIBRARY_FILENAME = f"{SCRIPT_DIR}/games.csv"
    _GAME_LIBRARY_HEADERS = ("AppName", "Icon", "BindingJsonPath")
    _GAME_LIBRARY_PATH = Path(_GAME_LIBRARY_FILENAME)

    _games: dict[str:BaseGame] = {}
    _current_game: BaseGame = None

    def __get_icon_path(app_name: str, icon: str):
        if path.isfile(icon):
            return icon

        icon_ = icon + ".png"
        if path.isfile(icon_):
            return icon_

        icon_ = GameLibrary._DEFAULT_ICON_DIRECTORY + "/" + icon
        if path.isfile(icon_):
            return icon_

        icon_ = GameLibrary._DEFAULT_ICON_DIRECTORY + "/" + icon + ".png"
        if path.isfile(icon_):
            return icon_

        icon_ = GameLibrary._DEFAULT_ICON_DIRECTORY + "/" + app_name + ".png"
        if path.isfile(icon_):
            return icon_

        return ""

    def get_games(file_name, _flags):
        if not GameLibrary._GAME_LIBRARY_PATH.is_file():
            with open(GameLibrary._GAME_LIBRARY_PATH, "w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(GameLibrary._GAME_LIBRARY_HEADERS)

        with open(GameLibrary._GAME_LIBRARY_PATH) as f:
            rows = list(csv.reader(f))

        GameLibrary._games.clear()
        if len(rows) >= 2:
            actual_headers = rows[0]
            if not actual_headers == list(GameLibrary._GAME_LIBRARY_HEADERS):
                print(f'"{GameLibrary._GAME_LIBRARY_FILENAME}": Malformed headers - {actual_headers}.' +
                    f" Should be {list(GameLibrary._GAME_LIBRARY_HEADERS)}. Ignoring row.")
            
            for row in rows[1:]:
                if len(row) == 0:
                    # Windows newlines are sometimes read as empty rows. :champagne:
                    continue
                elif len(row) >= 3:
                    app_name, icon, binding_path = row[:3]
                    if len(row) > 3:
                        print(f'"{GameLibrary._GAME_LIBRARY_FILENAME}": More than three values in row: {row}.' +
                            " Ignoring the extras.")
                elif len(row) < 3:
                    print(f'"{GameLibrary._GAME_LIBRARY_FILENAME}": Less than three values in row: {row}.' +
                            " Ignoring the row.")
                    continue
                icon = GameLibrary.__get_icon_path(app_name, icon)
                game = BaseGame(app_name, icon, binding_path)
                GameLibrary._games[app_name] = game


GameLibrary.get_games(GameLibrary._GAME_LIBRARY_PATH, "r")

fs.watch(GameLibrary._GAME_LIBRARY_PATH, GameLibrary.get_games)

def _track_current_game(app_name: str):
    if app_name in GameLibrary._games.keys():
        GameLibrary._current_game = GameLibrary._games[app_name]
        print(app_name)


def track_current_game(app):
    _track_current_game(app.name)


ui.register("app_launch", track_current_game)
ui.register("app_activate", track_current_game)

def update_current_game(name, flags):
    """Update current game on game library change.
    Needed to effectively update the active binding on current_game
    after changing its binding path in the game library file.
    Without updating the current game after changing the library there's a chance
    current_game would still be set to a BaseGame without a binding."""
    if GameLibrary.current_game is None:
        return
    app_name = GameLibrary.current_game.get_app_name()
    _track_current_game(app_name)


fs.watch(GameLibrary._GAME_LIBRARY_PATH, update_current_game)