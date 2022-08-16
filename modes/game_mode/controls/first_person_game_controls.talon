mode: user.game
and tag: user.first_person_game_controls
-
[turn] <user.arrow_key>:
    user.hold_game_key('{arrow_key}', '283ms')
[turn] (around|round):
    user.hold_game_key('left', '460ms')
[turn] (around|round) <user.arrow_key>:
    user.hold_game_key('{arrow_key}', '460ms')
[switch] [direction] {user.game_directions}:
    user.switch_game_movement_direction(game_directions)
go|move:
    user.start_game_movement()
stop|freeze:
    user.stop_game_movement()
jump|joe:
    user.press_game_key('space')
[toggle] (sprint|run):
    user.hold_game_key('shift')
[toggle] walk:
    user.release_game_key('shift')
