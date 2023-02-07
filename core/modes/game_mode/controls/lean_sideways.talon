mode: user.game
and tag: user.game_lean_sideways
-
#start/stop leaning left or change leaning direction from right to left
see [left]:
	user.game_lean_sideways("left")
#start/stop leaning right or change leaning direction from left to right
see right | sir:
	user.game_lean_sideways("right")
#start/stop leaning right or left
upright:
	user.game_lean_sideways_stop()