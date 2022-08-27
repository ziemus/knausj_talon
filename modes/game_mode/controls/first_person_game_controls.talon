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
    user.switch_game_movement(1)
stop|freeze:
    user.switch_game_movement(0)
jump|joe|ja:
    user.game_jump()
[toggle] (sprint|run|fast) (hold|press):
    user.hold_game_key('shift')
[toggle] (walk|slow) hold:
    user.release_game_key('shift')
[toggle] (sprint|run|fast):
    user.game_switch_sprint(1)
[toggle] (walk|slow):
    user.game_switch_sprint(0)

#Resets is_sprinting to False
#in case the game overrides sprint behavior
#after, for example, a loading screen
#which would mess up the execution of 'run' and 'walk' commands
#with the default game_switch_sprint()
^sprint state reset$:
    user.game_sprint_state_reset() 