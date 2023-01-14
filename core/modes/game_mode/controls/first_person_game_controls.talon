mode: user.game
and tag: user.first_person_game_controls
-
tag(): user.game_basic_movement
tag(): user.game_camera_controls
tag(): user.game_sprint_controls

jump:
    user.game_jump()
(inventory | equipment | bag) [show]:
    user.game_inventory_show()
use [it | that]:
    user.game_use()