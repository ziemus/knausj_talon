tag: user.game_camera_controls
and mode: user.game
-
[camera] [turn] <user.arrow_key>:
    user.hold_game_key('{arrow_key}', '283ms')
[camera] [turn] (around | round):
    user.game_turn_camera_around()
[camera] [turn] (around | round) <user.arrow_key>:
    user.hold_game_key('{arrow_key}', '460ms')