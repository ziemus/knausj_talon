from talon import ui, Module, Context, registry, actions, imgui, cron

mod = Module()
mod.apps.ditto = """
os: windows
and app.name: Ditto
os: windows
and app.exe: Ditto.exe
"""

ctx_running = Context()
ctx_running.matches = r"""
user.running: Ditto
user.running: Ditto.exe
"""

ctx_focused = Context()
ctx_focused.matches = r"""
app: ditto
"""


@ctx_running.action_class("user")
class UserRunningActions:
    def system_show_clipboard():
        """opens the systems default clipboard or equivalent"""
        actions.key("ctrl-`")


@ctx_focused.action_class("user")
class UserFocusedActions:
    def pick(number: int):
        actions.key(f"down:{number - 1} enter")
