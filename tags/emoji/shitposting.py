import exrex

from talon import Module

mod = Module()

@mod.action_class
class Actions:
    def keybash(max_length: int = 70) -> str:
        """generate a random string as if keybashing"""
        length = '{25,' + str(max_length) + '}'
        return exrex.getone('([a-zA-Z]|[!@#$%^&*]|[a-zA-Z]|[a-zA-Z]|[0-9])' + length)
