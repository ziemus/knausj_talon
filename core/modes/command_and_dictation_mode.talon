mode: command
mode: dictation
mode: user.game
-
^dictation mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    user.gdb_disable()
^command mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    user.disable_game_mode()
    mode.enable("command")
    sleep(100ms)
    user.command_mode_set_up()
^game mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.disable("dictation")
    user.enable_game_mode()
