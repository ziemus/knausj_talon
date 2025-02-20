control mouse: tracking.control_toggle()
control off: user.mouse_sleep()
zoom mouse: tracking.control_zoom_toggle()
camera overlay: tracking.control_debug_toggle()
run calibration: tracking.calibrate()
touch:
    # close zoom if open
    tracking.zoom_cancel()
    mouse_click(0)
    # close the mouse grid if open
    user.grid_close()
    # End any open drags
    # Touch automatically ends left drags so this is for right drags specifically
    user.mouse_drag_end()

righty:
    # close zoom if open
    tracking.zoom_cancel()
    mouse_click(1)
    # close the mouse grid if open
    user.grid_close()

mid click | mick:
    # close zoom if open
    tracking.zoom_cancel()
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
    # close zoom if open
    tracking.zoom_cancel()
    key("{modifiers}:down")
    mouse_click(0)
    key("{modifiers}:up")
    # close the mouse grid
    user.grid_close()
<user.modifiers> righty:
    # close zoom if open
    tracking.zoom_cancel()
    key("{modifiers}:down")
    mouse_click(1)
    key("{modifiers}:up")
    # close the mouse grid
    user.grid_close()
(dub click | duke):
    # close zoom if open
    tracking.zoom_cancel()
	mouse_click()
	mouse_click()
	# close the mouse grid
	user.grid_close()
(trip click | trip lick | trick):
    # close zoom if open
    tracking.zoom_cancel()
    mouse_click()
    mouse_click()
    mouse_click()
    # close the mouse grid
    user.grid_close()
left drag | drag | drag start:
    # close zoom if open
    tracking.zoom_cancel()
    user.mouse_drag(0)
    # close the mouse grid
    user.grid_close()
right drag | righty drag:
    # close zoom if open
    tracking.zoom_cancel()
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
(wheel | scroll) downer <number_small>: user.mouse_scroll_down_continuous(number_small)
(wheel | scroll) downer: user.mouse_scroll_down_continuous()
(wheel | scroll) downer here <number_small>:
    user.mouse_move_center_active_window()
    user.mouse_scroll_down_continuous(number_small)
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
(wheel | scroll) upper <number_small>: user.mouse_scroll_up_continuous(number_small)
(wheel | scroll) upper: user.mouse_scroll_up_continuous()
(wheel | scroll) upper here <number_small>:
    user.mouse_move_center_active_window()
    user.mouse_scroll_up_continuous(number_small)
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

# To scroll with a hiss sound, set mouse_enable_hiss_scroll to true in settings.talon
mouse hiss up: user.hiss_scroll_up()
mouse hiss down: user.hiss_scroll_down()

# To scroll with a hiss sound, set mouse_enable_hiss_scroll to true in settings.talon
mouse hiss up: user.hiss_scroll_up()
mouse hiss down: user.hiss_scroll_down()

curse stay:
    user.mouse_stay_in_place(1)
curse come:
    user.mouse_stay_in_place(0)