from talon import fs
import json
from os import path


class HotswappableKeybinding:
    __keybindings_path: str
    __keybindings: dict[str, any]

    def __init__(self, keybindings_path: str):
        self.__keybindings_path = keybindings_path
        self.__get_keybinding(keybindings_path, "r")
        fs.watch(self.__keybindings_path, self.__get_keybinding)

    def __del__(self):
        fs.unwatch(self.__keybindings_path, self.__get_keybinding)
    
    def __get_keybinding(self, name, flags):
        """name and flags only necessary for use with
        fs.watch in the constructor/
        fs.unwatch in the destructor"""
        self.__keybindings = {}

        if(self.__keybindings_path == ""):
            return
        
        if not path.isfile(self.__keybindings_path):
            return
        
        with open(self.__keybindings_path, "r") as binding_file:
            self.__keybindings = json.load(binding_file)

    def get_binding(self, action: str = None):
        if action is None:
            return self.__keybindings
        else:
            return self.__keybindings[action]