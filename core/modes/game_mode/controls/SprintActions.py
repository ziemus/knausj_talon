from threading import Lock
from talon import actions, Module
from ..GameModeHelper import GameModeHelper

game_sprint_module = Module()

setting_sprint_toggle_key = game_sprint_module.setting(
    "game_sprint_toggle_key",
    type=str,
    default="capslock",
    desc="""Keyname for the key that switches sprint on/off. Caps Lock by default.""")
setting_default_sprint_state = game_sprint_module.setting(
    "game_sprint_state_default",
    type=bool,
    default=False,
    desc="""Helps in tracking the in-game sprint/walk state.
        See the comment on GameActions.game_sprint_state_reset() for more information.
        Sho5uld be set to true when the default in-game behavior is running instead of walking (e.g. in Antichamber).
        By default false.""")

game_sprint_module.tag("game_sprint_controls")

is_sprinting: bool = False
lock_is_sprinting = Lock()


@game_sprint_module.action_class
class SprintActions:

    def game_switch_sprint(do_turn_on: bool = None):
        """"""
        global is_sprinting, lock_is_sprinting
        with lock_is_sprinting:
            do_turn_on = not is_sprinting if do_turn_on is None else do_turn_on
            toggle_sprint_key = setting_sprint_toggle_key.get()
            if do_turn_on and not is_sprinting:
                actions.user.press_game_key(toggle_sprint_key)
                is_sprinting = True
            elif not do_turn_on and is_sprinting:
                actions.user.press_game_key(toggle_sprint_key)
                is_sprinting = False

            GameModeHelper.game_hud_add_sprint_icon(is_sprinting)

    def game_sprint_state_reset():
        """Resets is_sprinting to default value
        in case the game overrides sprint behavior
        after, for example, a loading screen
        which would mess up the execution of 'run' and 'walk' commands
        with the default game_switch_sprint()
        that tracks the current in game sprinting state"""
        global is_sprinting, lock_is_sprinting
        with lock_is_sprinting:
            is_sprinting = setting_default_sprint_state.get()
            GameModeHelper.game_hud_add_sprint_icon(is_sprinting)
