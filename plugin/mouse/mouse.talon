control mouse: tracking.control_toggle()
control off: user.mouse_sleep()
zoom mouse: tracking.control_zoom_toggle()
camera overlay: tracking.control_debug_toggle()
run calibration: tracking.calibrate()
touch:
    mouse_click(0)
    # close the mouse grid if open
    user.grid_close()
    # End any open drags
    # Touch automatically ends left drags so this is for right drags specifically
    user.mouse_drag_end()

righty:
    mouse_click(1)
    # close the mouse grid if open
    user.grid_close()

mid click | mick:
	mouse_click(2)
	# close the mouse grid
	user.grid_close()

#see keys.py for modifiers.
#defaults
#command
#control
#option = alt
#shift
#super = windows key
<user.modifiers> touch:
    key("{modifiers}:down")
    mouse_click(0)
    key("{modifiers}:up")
    # close the mouse grid
    user.grid_close()
<user.modifiers> righty:
    key("{modifiers}:down")
    mouse_click(1)
    key("{modifiers}:up")
    # close the mouse grid
    user.grid_close()
(dub click | duke):
	mouse_click()
	mouse_click()
	# close the mouse grid
	user.grid_close()
(trip click | trip lick | trick):
	mouse_click()
	mouse_click()
	mouse_click()
	# close the mouse grid
	user.grid_close()
left drag | drag:
    user.mouse_drag(0)
    # close the mouse grid
    user.grid_close()
right drag | righty drag:
    user.mouse_drag(1)
    # close the mouse grid
    user.grid_close()
end drag | drag end: user.mouse_drag_end()
(wheel | scroll) down: user.mouse_scroll_down()
(wheel | scroll) down here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_down()
(wheel | scroll) tiny [down]: user.mouse_scroll_down(0.2)
(wheel | scroll) tiny [down] here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_down(0.2)
(wheel | scroll) downer: user.mouse_scroll_down_continuous()
(wheel | scroll) downer here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_down_continuous()
(wheel | scroll) up: user.mouse_scroll_up()
(wheel | scroll) up here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_up()
(wheel | scroll) tiny up: user.mouse_scroll_up(0.2)
(wheel | scroll) tiny up here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_up(0.2)
(wheel | scroll) upper: user.mouse_scroll_up_continuous()
(wheel | scroll) upper here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_up_continuous()
(wheel | scroll) gaze: user.mouse_gaze_scroll()
(wheel | scroll) gaze here:
    user.mouse_move_center_active_window()
    user.mouse_gaze_scroll()
(wheel | scroll) stop: user.mouse_scroll_stop()
(wheel | scroll) stop here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_stop()
(wheel | scroll) left: user.mouse_scroll_left()
(wheel | scroll) left here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_left()
(wheel | scroll) tiny left: user.mouse_scroll_left(0.5)
(wheel | scroll) tiny left here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_left(0.5)
(wheel | scroll) right: user.mouse_scroll_right()
(wheel | scroll) right here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_right()
(wheel | scroll) tiny right: user.mouse_scroll_right(0.5)
(wheel | scroll) tiny right here:
    user.mouse_move_center_active_window()
    user.mouse_scroll_right(0.5)
copy mouse position: user.copy_mouse_position()
curse no:
    # Command added 2021-12-13, can remove after 2022-06-01
    app.notify("Please activate the user.mouse_cursor_commands_enable tag to enable this command")

curse stay:
    user.mouse_stay_in_place(1)
curse come:
    user.mouse_stay_in_place(0)