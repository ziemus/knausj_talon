mode: all
-
^mouse off drowse$:
    tracking.control_toggle(false)
    speech.disable()
^wake mouse$:
    speech.enable()
    tracking.control_toggle(true)
    user.hud_enable()
