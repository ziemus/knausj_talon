from talon import Module, actions

mod = Module()
mod.tag("game_trade")


@mod.action_class
class Actions:

    def game_trade():
        """Open trading dialogue. Defaults to user.game_talk()"""
        actions.user.game_talk()

    def game_trade_buy_item():
        """Buy an item. No binding by default."""
        return

    def game_trade_sell_item():
        """Sell an item. Defaults to user.game_trade_buy_item()"""
        actions.user.game_trade_buy_item()

    def game_trade_buy_multiple_items():
        """Buy multiple items. No binding by default."""
        return

    def game_trade_sell_multiple_items():
        """Sell multiple items. Defaults to user.game_trade_sell_multiple_items()"""
        actions.user.game_trade_sell_multiple_items()

    def game_trade_mark_to_sell():
        """Mark an item to sell. No binding by default."""
        return
