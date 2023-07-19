import json
from os import path
from talon import resource

def get_keybinding(path_str: str):
    binding = {}
    is_path_not_empty = not path_str == ""
    if not path.isfile(path_str) and is_path_not_empty:
        print(f"no such file: {path_str}")
    if is_path_not_empty:
        #FIXME figure out index error after changing the binding file
        #with resource.open(path_str, "r") as binding_file:
        with open(path_str, "r") as binding_file:
            binding = json.load(binding_file)
        print(f"{binding}")
    return binding

class BaseGame:
    __app_name: str
    __icon_path: str
    __keybindings: dict[str, any]

    def __init__(self, app_name: str, icon_path: str, keybindings_path: str):
        self.__app_name = app_name
        self.__icon_path = icon_path
        self.__keybindings = get_keybinding(keybindings_path)

    def get_app_name(self):
        """should return the same value as App.name of the game so that it can be automatically detected"""
        return self.__app_name

    def get_icon_path(self):
        return self.__icon_path
    
    def get_binding(self, action: str = None):
        if action is None:
            return self.__keybindings
        else:
            return self.__keybindings[action]
