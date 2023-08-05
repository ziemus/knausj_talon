tag: user.game_weapon_aim
and mode: user.game
and not mode: sleep
-
aim [toggle] | am | um:
	user.game_weapon_aim_toggle()
aim start:
    user.game_weapon_aim_toggle(true)
aim done:
	user.game_weapon_aim_toggle(false)