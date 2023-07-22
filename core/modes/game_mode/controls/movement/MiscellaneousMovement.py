from talon import actions, Module, ctrl
from user.knausj_talon.core.modes.game_mode.binding import BindingExecutor
from user.knausj_talon.core.modes.game_mode import GameModeHelper

mod = Module()


@mod.action_class
class MiscellaneousMovement():
    def game_jump(is_hold: bool = None):
        """if is_hold is not provided or None, perform a basic jump.
        If is_hold is True, press the jump key down indefinitely
        If is_hold is False, release the jump key.
        Key defaults to space."""
        #TODO 
        key = GameModeHelper.get_current_game().get_binding("jump")
        if is_hold is None:
            actions.key(key)
        else:
            ctrl.key_press(key, down=is_hold, up=not is_hold)

    def game_crouch():
        """Duck or crouch"""
        BindingExecutor.execute("crouch")

    def game_dodge():
        """Dodge roll. Defaults to pressing ctrl."""
        BindingExecutor.execute("dodge")

    def game_long_dodge():
        """Long dodge roll. Defaults to pressing the ctrl key for 650 milliseconds."""
        BindingExecutor.execute("long_dodge")

    def game_dive_start():
        """Start diving"""
        BindingExecutor.execute("dive_start")

    def game_dive_stop():
        """Stop diving"""
        BindingExecutor.execute("dive_stop")