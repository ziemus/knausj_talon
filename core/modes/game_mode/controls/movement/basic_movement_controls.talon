tag: user.game_basic_movement
and mode: user.game
-
[movement] [direction] [switch] {user.game_directions}:
    user.switch_game_movement_direction(game_directions)

move [continue]:
    user.switch_game_movement(true)
freeze | stop | top :
    user.switch_game_movement(false)

go {user.game_directions}:
    user.game_movement_go(game_directions)
go:
    user.game_movement_go("move_forward")
get:
    user.game_movement_go("move_backward")
gel:
    user.game_movement_go("strife_left")
gar | jar:
    user.game_movement_go("strife_right")