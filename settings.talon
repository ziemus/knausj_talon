-
settings(): 
    #adjust the scale of the imgui to my liking
    imgui.scale = 3.5
    # enable if you'd like the picker gui to automatically appear when explorer has focus
    user.file_manager_auto_show_pickers = 0
    #set the max number of command lines per page in help
    user.help_max_command_lines_per_page = 50
    # set the max number of contexts display per page in help
    user.help_max_contexts_per_page = 20
    # The default amount used when scrolling continuously
    user.mouse_continuous_scroll_amount = 80
    #stop continuous scroll/gaze scroll with a pop
    user.mouse_enable_pop_stops_scroll = 1
    #enable pop click with 'control mouse' mode
    user.mouse_enable_pop_click = 1
    #When enabled, the 'Scroll Mouse' GUI will not be shown.
    user.mouse_hide_mouse_gui = 0
    #hide cursor when mouse_wake is called to enable zoom mouse
    user.mouse_wake_hides_cursor = 0
    #the amount to scroll up/down (equivalent to mouse wheel on Windows by default)
    user.mouse_wheel_down_amount = 120
    #mouse grid and friends put the number one on the bottom left (vs on the top left)
    user.grids_put_one_bottom_left = 1
    # the number of lines of command history to display by default
    user.command_history_display = 2
    # the number of lines of command history to keep in total;
    # "command history more" to display all of them, "command history less" to restore
    user.command_history_size = 50
    speech.record_all = 1
    speech.timeout = .400

    #clickless mouse settings
    # user.clickless_mouse_radius = 20
    # user.clickless_mouse_dwell_time = 0.25
    # user.clickless_mouse_idle_time_before_display = 0.25
    # user.clickless_mouse_auto_hide_time = 1.0
    #end clickless mouse settings
    # speech.gain = 6
    
# Uncomment this to enable the curse yes/curse no commands (show hide mouse cursor). See issue #688.
# tag(): user.mouse_cursor_commands_enable

# uncomment tag to enable mouse grid
tag(): user.cursorless_experimental_snippets
tag(): talon_plugins.eye_zoom_mouse.zoom_mouse_noise
# tag(): talon_plugins.eye_zoom_mouse.zoom_mouse_pedal
tag(): user.cursorless_experimental_snippets



