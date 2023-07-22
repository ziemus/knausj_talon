from talon import Module
from user.knausj_talon.core.modes.game_mode.binding.BindingExecutor import BindingExecutor

mod = Module()


@mod.action_class
class Crafting:

    def game_craft():
        """Craft an object.
        Not every game has crafting mechanics
        so this action is only there to be overridden if needed
        without having to declare a new voice command"""
        BindingExecutor.execute("craft")