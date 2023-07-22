from talon import actions, Module
from user.knausj_talon.core.modes.game_mode.binding.BindingExecutor import BindingExecutor

mod = Module()


@mod.action_class
class Interactions:

    def game_take():
        """Take an object. Defaults to user.game_use if not overridden."""
        BindingExecutor.execute_or_substitute("take", "use")

    def game_take_number(digits: int):
        """Take a specified number of objects.
        Defaults to calling user.game_take() the specified number of times."""
        for i in range(digits):
            actions.user.game_take()

    def game_take_all():
        """Take all selected objects. Defaults to user.game_take() if not overridden."""
        #TODO chain more than 2
        BindingExecutor.execute_or_substitute("take_all", "take")
   
    def game_loot():
        """Loot an object. Defaults to user.game_use if not overridden."""
        BindingExecutor.execute_or_substitute("loot", "use")

    def game_talk():
        """Talk to an NPC.
        Defaults to user.game_use if not overridden."""
        BindingExecutor.execute_or_substitute("talk", "use")

    def game_interactable_objects_highlight_start():
        """Highlight interactable objects, defaults to pressing tab."""
        BindingExecutor.execute("interactable_objects_highlight_start")

    def game_interactable_objects_highlight_stop():
        """Stop highlighting interactable objects.
        Defaults to calling actions.user.game_interactable_objects_highlight_start()."""
        BindingExecutor.execute_or_substitute(
            "interactable_objects_highlight_stop",
            "interactable_objects_highlight_start"
        )

    def game_use():
        """Basic use/interact with an object (e by default)"""
        BindingExecutor.execute("use")

    def game_long_use():
        """Hold use/interact key (e by default) for approximately half a second"""
        BindingExecutor.execute("long_use")

    def game_hold_use():
        """hold use/interact key indefinitely (e by default)"""
        BindingExecutor.execute("hold_use")

    def game_release_use():
        """release use/interact key (e by default)"""
        BindingExecutor.execute("release_use")