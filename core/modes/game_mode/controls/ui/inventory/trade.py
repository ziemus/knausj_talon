from talon import Module, actions
from user.knausj_talon.core.modes.game_mode.binding.BindingExecutor import BindingExecutor

mod = Module()
mod.tag("game_trade")


@mod.action_class
class Actions:

    def game_trade():
        """Open trading dialogue. Defaults to user.game_talk()"""
        #TODO chaining more than 2 actions
        actions.user.game_talk()

    def game_trade_buy_item():
        """Buy an item. No binding by default."""
        BindingExecutor.execute("buy_item")

    def game_trade_sell_item():
        """Sell an item. Defaults to user.game_trade_buy_item()"""
        BindingExecutor.execute_or_substitute("sell_item", "buy_item")

    def game_trade_buy_multiple_items():
        """Buy multiple items. No binding by default."""
        BindingExecutor.execute("buy_multiple_items")

    def game_trade_sell_multiple_items():
        """Sell multiple items. Defaults to user.game_trade_buy_multiple_items()"""
        BindingExecutor.execute_or_substitute(
            "sell_multiple_items",
            "buy_multiple_items"
        )

    def game_trade_buy_number_of_items(number: int):
        """Buy a specified number of items.
        Defaults to calling game_trade_buy_item() a specified number of times."""
        for i in range(number):
            actions.user.game_trade_buy_item()

    def game_trade_sell_number_of_items(number: int):
        """Sell a specified number of items.
        Defaults to calling game_trade_sell_item() a specified number of times."""
        for i in range(number):
            actions.user.game_trade_sell_item()

    def game_trade_mark_to_sell():
        """Mark an item to sell. No binding by default."""
        BindingExecutor.execute("mark_to_sell")
