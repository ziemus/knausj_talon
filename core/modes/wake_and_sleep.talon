#defines the commands that sleep/wake Talon
mode: all
-
^welcome back$:
    user.mouse_wake()
    user.history_enable()
    user.talon_mode()
^sleep all [<phrase>]$:
    user.switcher_hide_running()
    user.history_disable()
    user.homophones_hide()
    user.help_hide()
    user.mouse_sleep()
    speech.disable()
    user.engine_sleep()
^mouse off drowse$:
    user.mouse_sleep()
    speech.disable()
^drowse [<phrase>]$: speech.disable()
^(way key | wakey | wakeup | wake up | talon wake)$:
    speech.enable()
    user.hud_enable()
^wake mouse$:
    speech.enable()
    tracking.control_toggle(1)
    user.hud_enable()