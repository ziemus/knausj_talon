tag: user.game_sprint_controls
and mode: user.game
-
(sprint | print) [toggle]:
    user.game_switch_sprint()
(sprint | print) start:
    user.game_switch_sprint(true)
(sprint | print) done:
    user.game_switch_sprint(false)
run [toggle]:
    user.game_start_running()
walk [toggle]:
    user.game_start_walking()