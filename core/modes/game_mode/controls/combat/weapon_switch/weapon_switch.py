from talon import Module, actions, Context
from user.knausj_talon.core.modes.game_mode.binding import BindingExecutor

mod = Module()
mod.tag("game_weapon_switch")
ctx = Context()


@mod.action_class
class Actions:

    def game_weapon_draw():
        """Draw weapon. Defaults to pressing h key"""
        BindingExecutor.execute("weapon_draw")

    def game_weapon_hide():
        """Hide drawn weapon. Defaults to calling actions.user.game_weapon_draw()"""
        BindingExecutor.execute_or_substitute("weapon_hide", "weapon_draw")

    def game_weapon_drop():
        """Drop used weapon. No binding by default."""
        BindingExecutor.execute("weapon_drop")

    def game_weapon_melee_show():
        """Show quick access menu for melee weapons or draw melee weapon.
        No binding by default"""
        BindingExecutor.execute("weapon_melee_show")

    def game_weapon_ranged_show():
        """Show quick access menu for ranged weapons or draw ranged weapon.
        No binding by default"""
        BindingExecutor.execute("weapon_ranged_show")

    def game_weapon_thrown_show():
        """Show quick access menu for thrown weapons or draw throne weapon.
        No binding by default"""
        BindingExecutor.execute("weapon_thrown_show")
