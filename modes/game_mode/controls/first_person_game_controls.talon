mode: user.game
and tag: user.first_person_game_controls
-
tag(): user.game_basic_movement
tag(): user.game_camera_controls
tag(): user.game_sprint_controls

jump | joe | ja:
    user.game_jump()
inventory | equipment | bag:
    key(i)
use:
    key(e)