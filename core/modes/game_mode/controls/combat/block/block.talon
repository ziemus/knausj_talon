tag: user.game_weapon_block
and mode: user.game
-
block:
    user.game_weapon_block_toggle()
block done:
    user.game_weapon_block_toggle(false)
^block state reset$:
    user.game_weapon_block_state_set(false)