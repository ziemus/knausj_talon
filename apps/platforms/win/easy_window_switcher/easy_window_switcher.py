from talon import Context, actions, Module

mod = Module()
ctx = Context()

apps = mod.apps
apps.easy_window_switcher = """
os: windows
and app.name: Easy Window Switcher
os: windows
and app.exe: wincycle.exe
"""

ctx = Context()
ctx.matches = r"""
os: windows
user.running: Easy Window Switcher
"""


@ctx.action_class("app")
class AppActions:
    def window_next():
        actions.key("alt-`")

    def window_previous():
        actions.key("alt-shift-`")
