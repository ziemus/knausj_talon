from talon import actions, ctrl, settings, Module

basic_game_actions_module = Module()

basic_game_actions_module.tag("game_character_sheet")
basic_game_actions_module.tag("game_mouse_enabled")
basic_game_actions_module.tag("first_person_game_controls")
basic_game_actions_module.list("game_number_shortcuts")


@basic_game_actions_module.action_class
class BasicGameActions:

    def game_jump():
        """"""
        actions.user.press_game_key("space")

    def game_use():
        """"""
        actions.user.press_game_key('e')

    def game_character_sheet_show():
        """"""
        actions.user.press_game_key('c')

    def game_click(button: int = 0, times: int = 1, hold: int = None):
        """Clicks specified number of times.
        Waits betwen each click for the time period of hold.
        This way it intgrates better with most games."""
        wait = settings.get("user.mouse_wait")
        if hold is None:
            hold = settings.get("user.mouse_hold")
        for i in range(times):
            ctrl.mouse_click(button, hold=hold, wait=wait)

    def game_press_mouse(button: int, down: bool):
        """"""
        up = not down
        ctrl.mouse_click(button, down=down, up=up)

    def press_game_key(key: str):
        """"""
        actions.key(key)

    def hold_game_key(key: str, duration: str = None):
        """Hold key infinitely or for the specified duration"""
        actions.key(key + ":down")
        if duration is None:
            return
        actions.sleep(duration)
        actions.user.release_game_key(key)

    def game_hold_key_native(key: str, duration: int = None):
        """Hold key infinitely or for the specified duration"""
        if duration is None:
            ctrl.key_press(key, down=True)
            return
        ctrl.key_press(key, hold=duration)

    def release_game_key(key: str):
        """"""
        actions.key(key + ":up")

    def release_held_game_keys():
        """"""
        for key in actions.user.get_held_game_keys():
            actions.user.release_game_key(key)

    def get_held_game_keys():
        """
        Returns a list of frequently held (long pressed) keys in games
        so that they can be released upon exiting from game mode.
        May be overridden with contexts to suit a specific game.
        """
        keys = ["shift", "a", "d", "w", "s", "e", "q", "up", "down", "left", "right"]
        return keys

    def custom_game_setup():
        """additional setup to be overridden using contexts"""
        return 0

    def custom_game_cleanup():
        """additional cleanup to be overridden using contexts"""
        return 0