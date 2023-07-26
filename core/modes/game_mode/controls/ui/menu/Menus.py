from talon import actions, Module
from user.knausj_talon.core.modes.game_mode.binding.BindingExecutor import BindingExecutor

mod = Module()


@mod.action_class
class Menus:
    def game_manual_save():
        """"""
        BindingExecutor.execute("manual_save")

    def game_quick_save():
        """"""
        BindingExecutor.execute("quick_save")

    def game_quick_load():
        """Load quick save. Left blank to be overridden if needed."""
        BindingExecutor.execute("quick_load")

    def game_menu():
        """"""
        BindingExecutor.execute("menu")

    def game_character_sheet_show():
        """Show character sheet"""
        BindingExecutor.execute("character_sheet_show")

    def game_crafting_menu_show():
        """Show or hide crafting menu"""
        BindingExecutor.execute("crafting_menu_show")

    def game_quest_log_show():
        """Show or hide quest log or journal"""
        BindingExecutor.execute("quest_log_show")

    def game_bestiary_show():
        """Show or hide glossary/bestiary/index/notebook"""
        BindingExecutor.execute("bestiary_show")