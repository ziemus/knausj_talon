from talon import actions
from ..GameModeHelper import GameModeHelper

class BindingExecutor:
    def __parse(keys: str):
        #TODO TIMINGS
        return keys.split(";")

    def execute(action: str):
        binding = GameModeHelper.get_current_game().get_binding(action)
        presses = BindingExecutor.__parse(binding)
        for keys in presses:
            #TODO TIMINGS
            actions.key(keys)
        