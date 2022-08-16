from talon import Module, actions
from user.talon_hud.content.programming_language_poller import remove_statusbar_programming_icon

from .GameModeHelper import GameModeHelper

game_mode_module = Module()
game_mode_module.mode("game", "Gaming Mode that doesn't accept regular commands")
game_mode_module.list('game_directions')
game_mode_module.tag('first_person_game_controls')

@game_mode_module.action_class
class GameModeActions:
    def enable_game_mode():
        """Switches the game mode on"""
        remove_statusbar_programming_icon()
        actions.mode.enable("user.game")
        GameModeHelper.add_active_game_icon()
        actions.user.custom_game_setup()

    def disable_game_mode():
        """Switches the game mode off"""
        actions.user.release_held_game_keys()
        GameModeHelper.remove_active_game_icon()
        actions.user.custom_game_cleanup()
        actions.mode.disable("user.game")

    def custom_game_setup():
        """additional setup to be overridden using contexts"""
        return 0

    def custom_game_cleanup():
        """additional cleanup to be overridden using contexts"""
        return 0
