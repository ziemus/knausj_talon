from threading import Lock
from talon import actions, Module
from ....GameModeHelper import GameModeHelper
from user.knausj_talon.core.modes.game_mode.binding.BindingExecutor import BindingExecutor

game_sprint_module = Module()

setting_default_sprint_state = game_sprint_module.setting(
    "game_sprint_state_default",
    type=bool,
    default=False,
    desc="""Helps in tracking the in-game sprint/walk state.
        See the comment on GameActions.game_sprint_state_reset() for more information.
        Should be set to true when the default in-game behavior is running instead of walking (e.g. in Antichamber).
        By default false.""")

game_sprint_module.tag("game_sprint_controls")

is_sprinting: bool = False


@game_sprint_module.action_class
class SprintActions:

    def game_switch_sprint(do_turn_on: bool = None):
        """If do_turn_on is True, start sprinting.
        If do_turn_on is is False, stop sprinting.
        If do_turn_on is None, the action toggles between sprinting/not sprinting, based on tracked sprint state.

        This action should be called instead of actions.user.game_sprint_start
        and actions.user.game_sprint_stop if any of those 2 get overridden.
        This action shouldn't be overridden. Doing so may desynchronize the tracked sprint state.

        This function does not handle any sprinting logic. It defaults to calling
        actions.user.game_sprint_start() or actions.user.game_sprint_stop().
        Its main purpose is to be called upon the shorthand "sprint"/"print" voice command
        instead of "sprint start" and "sprint done" to shorten the voice commands
        necessary for such a basic game interaction.

        Tracks sprint state independently of underlying action calls
        in case the main logic needs to be overridden."""
        global is_sprinting
        do_turn_on = not is_sprinting if do_turn_on is None else do_turn_on

        if do_turn_on:
            actions.user.game_sprint_start()
        else:
            actions.user.game_sprint_stop()

        is_sprinting = do_turn_on
        GameModeHelper.game_hud_add_sprint_icon(is_sprinting)

    def game_sprint_start():
        """Start sprinting.
        Executes "sprint_toggle" (if provided in binding) or "sprint_start".
        May be overridden to implement custom sprint start game mechanic.
        Tracks sprint state if not overridden."""
        global is_sprinting
        BindingExecutor.execute_or_substitute("sprint_toggle", "sprint_start")
        is_sprinting = True  # in case game_switch_sprintgets overridden
        GameModeHelper.game_hud_add_sprint_icon(is_sprinting)

    def game_sprint_stop():
        """Stop sprinting.
        Executes "sprint_toggle" (if provided in binding) or "sprint_stop".
        May be overridden to implement custom sprint stop game mechanic.
        Tracks sprint state if not overidden."""
        global is_sprinting
        BindingExecutor.execute_or_substitute("sprint_toggle", "sprint_stop")
        is_sprinting = False  # in case game_switch_sprintgets overridden
        GameModeHelper.game_hud_add_sprint_icon(is_sprinting)

    def game_start_running():
        """Start running. Executes "run" binding.
        If no binding for "run" is provided,
        calls actions.user.game_switch_sprint(True)
        as in most games running means the same as sprinting."""
        if GameModeHelper.is_no_binding("run"):
            actions.user.game_switch_sprint(True)
        else:
            BindingExecutor.execute("run")

    def game_start_walking():
        """Stop running. Executes "walk" binding.
        If no binding for "walk" is provided,
        calls actions.user.game_switch_sprint(False)."""
        if GameModeHelper.is_no_binding("walk"):
            actions.user.game_switch_sprint(False)
        else:
            BindingExecutor.execute("walk")

    def game_sprint_state_reset():
        """Resets is_sprinting to default"""
        global is_sprinting
        is_sprinting = setting_default_sprint_state.get()
        GameModeHelper.game_hud_add_sprint_icon(is_sprinting)
