mode: user.game
and not mode: sleep
-
manual save:
	user.game_manual_save()
quicksave:
	user.game_quick_save()
quick load:
	user.game_quick_load()
menu [pause] | escape | back:
	user.game_menu()
enter:
    key(enter)