tag: user.game_trade
and mode: user.game
and not mode: sleep
-
trade with:
    user.game_trade()
buy (it | that):
	user.game_trade_buy_item()
sell (it | that):
	user.game_trade_sell_item()
buy many:
	user.game_trade_buy_multiple_items()
sell many:
	user.game_trade_sell_multiple_items()
buy <digits>:
	user.game_trade_buy_number_of_items(digits)
sell <digits>:
	user.game_trade_sell_number_of_items(digits)
mark [to] sell:
	user.game_trade_mark_to_sell()