from talon import Context, Module, actions

mod = Module()
mod.apps.scrivener3 = """
os: windows
and app.name: Scrivener
and app.exe: Scrivener.exe
"""

context = Context()
context.matches = """
app: scrivener3
"""


@context.action_class("edit")
class Actions:

    def paste_match_style():
        actions.key("ctrl-shift-v")