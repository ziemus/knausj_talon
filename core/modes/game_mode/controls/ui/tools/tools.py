from talon import Module, actions, Context
from user.knausj_talon.core.modes.game_mode.binding.BindingExecutor import BindingExecutor

mod = Module()
mod.tag("game_tools")
mod.list("game_tool_keyword")
ctx = Context()
ctx.lists["user.game_tool_keyword"] = {"tool", "trap"}


@mod.action_class
class Actions:

    def game_tool_use():
        """Use selected tool or trap, like in a souls-like game.
        As not every game has this mechanic, it's left blank to be overridden if needed."""
        BindingExecutor.execute("tool_use")