from os import path
import csv
from talon import resource
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

def get_games():
    filename = "games.csv"
    headers = ("AppName", "Icon", "BindingJsonPath")
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
            print(f'"{filename}": Malformed headers - {actual_headers}.' +
                  f" Should be {list(headers)}. Ignoring row.")
        for row in rows[1:]:
            if len(row) == 0:
                # Windows newlines are sometimes read as empty rows. :champagne:
                continue
            elif len(row) >= 3:
                app_name, icon, binding_path = row[:3]
                if len(row) > 3:
                    print(f'"{filename}": More than three values in row: {row}.' +
                          " Ignoring the extras.")
            elif len(row) < 3:
                print(f'"{filename}": Less than three values in row: {row}.' +
                          " Ignoring the row.")
                continue
            icon = get_icon_path(app_name, icon)
            game = BaseGame(app_name, icon, binding_path)
            mapping[app_name] = game

    return mapping

games: dict[str:BaseGame] = get_games()