from talon import Context, Module

module = Module()
module.tag("wsad_game_controls")
context = Context()
context.matches = """
tag: user.wsad_game_controls
"""
context.lists["user.game_directions"] = {
    "north": "w",
    "no": "w",
    "knee": "w",
    "south": "s",
    "sun": "s",
    "saw": "s",
    "so": "s",
    "west": "a",
    "way": "a",
    "we": "a",
    "east": "d",
    "eye": "d",
    "aye": "d",
    "I": "d",
}


@context.action_class("user")
class Actions:

    def get_game_movement_keys():
        return ["w", "s", "a", "d"]
