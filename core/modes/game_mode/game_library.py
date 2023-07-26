from os import path
import csv
from talon import fs
from talon.ui import App
from user.knausj_talon.core.user_settings import SETTINGS_DIR
from .BaseGame import BaseGame

DEFAULT_ICON_DIRECTORY = path.dirname(path.abspath(__file__)) + "/game_icons"

def get_icon_path(app_name: str, icon: str):
    if path.isfile(icon):
        return icon

    icon_ = icon + ".png"
    if path.isfile(icon_):
        return icon_

    icon_ = DEFAULT_ICON_DIRECTORY + "/" + icon
    if path.isfile(icon_):
        return icon_

    icon_ = DEFAULT_ICON_DIRECTORY + "/" + icon + ".png"
    if path.isfile(icon_):
        return icon_

    icon_ = DEFAULT_ICON_DIRECTORY + "/" + app_name + ".png"
    if path.isfile(icon_):
        return icon_

    return ""

game_library_filename = "games.csv"
game_library_headers = ("AppName", "Icon", "BindingJsonPath")
game_library_path = SETTINGS_DIR / game_library_filename

games: dict[str:BaseGame] = {}

def get_games(file_name, _flags):
    if not game_library_path.is_file():
        with open(game_library_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(game_library_headers)

    with open(game_library_path) as f:
        rows = list(csv.reader(f))

    games.clear()
    if len(rows) >= 2:
        actual_headers = rows[0]
        if not actual_headers == list(game_library_headers):
            print(f'"{game_library_filename}": Malformed headers - {actual_headers}.' +
                  f" Should be {list(game_library_headers)}. Ignoring row.")
        for row in rows[1:]:
            if len(row) == 0:
                # Windows newlines are sometimes read as empty rows. :champagne:
                continue
            elif len(row) >= 3:
                app_name, icon, binding_path = row[:3]
                if len(row) > 3:
                    print(f'"{game_library_filename}": More than three values in row: {row}.' +
                          " Ignoring the extras.")
            elif len(row) < 3:
                print(f'"{game_library_filename}": Less than three values in row: {row}.' +
                          " Ignoring the row.")
                continue
            icon = get_icon_path(app_name, icon)
            game = BaseGame(app_name, icon, binding_path)
            games[app_name] = game

get_games(game_library_path, "r")

fs.watch(game_library_path, get_games)