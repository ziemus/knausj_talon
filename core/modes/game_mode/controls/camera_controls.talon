tag: user.game_camera_controls
and mode: user.game
-
[camera] [turn] <user.arrow_key>:
    user.game_turn_camera('{arrow_key}', 0)
[camera] [turn] (little | lil | small) <user.arrow_key>:
    user.game_turn_camera('{arrow_key}', 1)
[camera] [turn] (around | round):
    user.game_turn_camera_around()