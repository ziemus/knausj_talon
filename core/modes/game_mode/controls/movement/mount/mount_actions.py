from talon import actions, Module
from user.knausj_talon.core.modes.game_mode.GameModeHelper import GameModeHelper
from user.knausj_talon.core.modes.game_mode.binding.BindingExecutor import BindingExecutor

mod = Module()
mod.tag("game_mount")


@mod.action_class
class Actions:

    def game_mount():
        """Begin mounted ride.
        Defaults to user.game_use if not overridden"""
        BindingExecutor.execute_or_substitute("mount", "use")

    def game_dismount():
        """Get off your high horse.
        Defaults to user.game_mount if not overridden."""
        #TODO chaining more than 2
        if GameModeHelper.is_no_binding("dismount"):
            actions.user.game_mount()
        else:
            BindingExecutor.execute("dismount")

    def game_mount_ride_faster():
        """Defaults to user.game_switch_sprint(True) if not overridden."""
        if GameModeHelper.is_no_binding("mount_ride_faster"):
            actions.user.game_switch_sprint(True)
        else:
            BindingExecutor.execute("mount_ride_faster")

    def game_mount_ride_slower():
        """Defaults to user.game_switch_sprint(False) if not overridden."""
        if GameModeHelper.is_no_binding("mount_ride_slower"):
            actions.user.game_switch_sprint(False)
        else:
            BindingExecutor.execute("mount_ride_slower")

    def game_mount_stop():
        """Defaults to user.switch_game_movement(False) if not overridden."""
        if GameModeHelper.is_no_binding("mount_stop"):
            actions.user.switch_game_movement(False)
        else:
            BindingExecutor.execute("mount_stop")