tag: user.game_weapon_target_lock
and mode: user.game
and not mode: sleep
-
target lock [toggle] | tar:
	user.game_weapon_target_lock_toggle()
target lock start | tar start:
    user.game_weapon_target_lock_toggle(true)
target lock done | tar done:
	user.game_weapon_target_lock_toggle(false)
target lock previous | tar last | tat:
	user.game_weapon_target_lock_previous()
target lock next | tar neck | tech:
	user.game_weapon_target_lock_next()