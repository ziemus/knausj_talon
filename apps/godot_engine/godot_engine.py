from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.godot_engine = r"""
app.name: Godot Engine
"""

ctx.matches = r"""
app: godot_engine
"""

# @mod.action_class
# class Actions:
