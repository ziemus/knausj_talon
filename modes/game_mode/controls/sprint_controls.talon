tag: user.game_sprint_controls
and mode: user.game
-
(sprint | run | fast) (hold | press) [toggle]:
    user.hold_game_key('shift')
(walk | slow) (hold | press) [toggle]:
    user.release_game_key('shift')
(sprint | run | fast) [toggle]:
    user.game_switch_sprint(1)
(walk | slow) [toggle]:
    user.game_switch_sprint(0)
#Resets is_sprinting to False
#in case the game overrides sprint behavior
#after, for example, a loading screen
#which would mess up the execution of 'run' and 'walk' commands
#with the default game_switch_sprint()
^sprint state reset$:
    user.game_sprint_state_reset()
^movement state reset$:
    user.game_movement_state_reset()