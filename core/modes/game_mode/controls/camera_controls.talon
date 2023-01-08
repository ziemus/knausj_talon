tag: user.game_camera_controls
and mode: user.game
-
[camera] [turn] <user.arrow_key>:
    user.game_turn_camera('{arrow_key}')
[camera] [turn] (tiny | tea) <user.arrow_key>:
    user.game_turn_camera('{arrow_key}', 0.25)
[camera] [turn] (little | lil | lee | small) <user.arrow_key>:
    user.game_turn_camera('{arrow_key}', 0.5)
[camera] [turn] (big | be) <user.arrow_key>:
    user.game_turn_camera('{arrow_key}', 1.25)
[camera] [turn] (around | round):
    user.game_turn_camera_around()