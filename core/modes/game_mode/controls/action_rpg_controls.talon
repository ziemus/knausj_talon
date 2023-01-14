tag: user.game_action_rpg
and mode: user.game
and not mode: sleep
-
settings():
	user.mouse_enable_pop_click = 0
	user.mouse_hide_mouse_gui = 1
    key_hold = 64.0
	key_wait = 16.0
    user.mouse_hold = 64000
	user.mouse_wait = 0
    user.game_noise_pop_binding_default = "move"
    user.game_noise_hiss_binding_default = "click"

tag(): user.first_person_game_controls
tag(): user.game_mouse_enabled
tag(): user.game_map
tag(): user.game_trade
tag(): user.game_arrow_keys_toggle_wsad_movement
tag(): user.game_quick_access_menu
tag(): user.game_mount
tag(): user.game_weapon_aim

#it may be more comfortable to move around using only pop as movement toggle
#while controlling the camera (in your field of view) with an air mouse
#(a cheap smart tv remote with gyroscopic mouse capabilities and a usb dongle)
#e.g. mounted on top of your headphone's headband or onto a hat
#occasionally helping yourself with the controls from the tag user.game_camera_controls
#when you have to turn around
noise binding exploration mode | noise explore | exploring:
	user.game_noise_control_switch("pop","move")
	user.game_noise_control_switch("hiss","click")
#in a fight switching movement direction by voice takes too much time
#and being able to move only in the direction of the camera is too restricting.
#If possible, it is encouraged to use some other kind of controller, like a set of 3 foot pedals.
#If holding pedals down for a long time poses an issue
#controls from the tag user.game_arrow_keys_toggle_wsad_movement
#allow the user to toggle movement and switch movement direction
#by just pressing them once without the need to hold them for a long time.
#See the comment on actions.user.game_movement_toggle_direction_switch(direction_key) for more details.
noise binding fight mode | noise fight | fighting:
	user.game_noise_control_switch("pop","dodge")
	user.game_noise_control_switch("hiss","long click")

#miscellanies movement
crouch | duck:
	user.game_crouch()
roll | dodge | dog:
	user.game_dodge()
dive:
	user.game_dive_start()
dive done:
	user.game_dive_stop()

#basic interactions
(loot | search) (it | that):
	user.game_loot()
take | pick [up] | gather:
    user.game_take()
(take | pick [up] | gather) all:
	user.game_take_all()
talk (with | to):
    user.game_talk()

#tools
[selected] tool [use]:
	user.game_tool_use()
tool [switch] left | zip:
	user.game_tool_switch_left()
tool [switch] right | zap | zoop:
	user.game_tool_switch_right()

#shortcuts
[fast] [equip | switch] {user.game_number_shortcuts}:
	key(game_number_shortcuts)
heal:
	user.game_heal()
crafting [show]:
	user.game_crafting_menu_show()
craft:
	user.game_craft()
(skill | perk) learn:
	user.game_skill_learn()
(skill | perk) unlearn:
	user.game_skill_unlearn()
(skill tree | character sheet | car sheet) [show]:
	user.game_character_sheet_show()
(journal | quest log) [show]:
	user.game_quest_log_show()
(notebook | notes | bestiary | glossary) [show]:
	user.game_bestiary_show()