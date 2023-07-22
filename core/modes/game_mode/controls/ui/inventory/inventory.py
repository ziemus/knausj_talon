from talon import Module, actions
from user.knausj_talon.core.modes.game_mode.binding.BindingExecutor import BindingExecutor

mod = Module()
mod.tag("game_inventory_tabs")
mod.list("game_inventory_tabs", desc="Tab names for inventory sections/tabs.")


@mod.action_class
class Actions:

    def game_inventory_tab_go(game_inventory_tabs: str):
        """Go to the specified inventory section."""
        return 0

    def game_inventory_tab_next():
        """Go to the next inventory tab."""
        BindingExecutor.execute("inventory_tab_next")

    def game_inventory_tab_previous():
        """Go to the previous inventory tab."""
        BindingExecutor.execute("inventory_tab_previous")

    def game_inventory_show():
        """Show or had inventory"""
        BindingExecutor.execute("inventory_show")
