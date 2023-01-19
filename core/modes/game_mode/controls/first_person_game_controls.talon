mode: user.game
and tag: user.first_person_game_controls
-
tag(): user.game_basic_movement
tag(): user.game_camera_controls
tag(): user.game_sprint_controls

#miscellanies movement
jump:
    user.game_jump()
crouch | duck:
	user.game_crouch()
roll | dodge | doo:
	user.game_dodge()
long roll | long dodge | [sausage] dog:
	user.game_long_dodge()
dive:
	user.game_dive_start()
dive done:
	user.game_dive_stop()

#basic interactions
use [it | that]:
    user.game_use()
(loot | search) (it | that):
	user.game_loot()
take | pick [up] | gather:
    user.game_take()
(take | pick [up] | gather) all:
	user.game_take_all()
talk (with | to):
    user.game_talk()

[fast] [equip | switch] {user.game_number_shortcuts}:
	key(game_number_shortcuts)
	
[weapon] reload | red:
    key(r)

(inventory | equipment | bag) [show]:
    user.game_inventory_show()
(character sheet | car sheet) [show]:
	user.game_character_sheet_show()
(journal | quest log) [show]:
	user.game_quest_log_show()