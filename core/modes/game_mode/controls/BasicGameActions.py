from talon import actions, ctrl, settings, Module

basic_game_actions_module = Module()

basic_game_actions_module.tag("game_character_sheet")
basic_game_actions_module.tag("game_mouse_enabled")


@basic_game_actions_module.action_class
class BasicGameActions:

    def game_crouch():
        """Duck or crouch"""
        actions.key("c")

    def game_dodge():
        """Dodge roll. Defaults to pressing ctrl."""
        actions.key("ctrl")

    def game_long_dodge():
        """Long dodge roll. Defaults to pressing the ctrl key for 650 milliseconds."""
        actions.user.press_game_key("ctrl", 1, 650000)

    def game_dive_start():
        """Start diving"""
        actions.key("ctrl:down")

    def game_dive_stop():
        """Stop diving"""
        actions.key("ctrl:up")

    def game_take():
        """Take an object. Defaults to user.game_use if not overridden."""
        actions.user.game_use()

    def game_take_all():
        """Take all selected objects. Defaults to user.game_take() if not overridden."""
        actions.user.game_take()

    def game_talk():
        """Talk to an NPC.
        Defaults to user.game_use if not overridden."""
        actions.user.game_use()

    def game_loot():
        """Loot an object. Defaults to user.game_use if not overridden."""
        actions.user.game_use()

    def game_jump(is_hold: bool = None):
        """if is_hold is not provided or None, perform a basic jump.
        If is_hold is True, press the jump key down indefinitely
        If is_hold is False, release the jump key.
        Key defaults to space."""
        if is_hold is None:
            actions.key("space")
        else:
            ctrl.key_press("space", down=is_hold, up=not is_hold)

    def game_use():
        """Basic use/interact with an object"""
        actions.key("e")

    def game_character_sheet_show():
        """Show character sheet"""
        actions.key("c")

    def game_heal():
        """Shortcut for healing.
        Not every game has healing or quick potion use shortcut
        so this action is only there to be overridden if needed
        without having to declare a new voice command.
        The return value does not matter.
        Returns 0 by default to stop talon from outputting errors to log."""
        return 0

    def game_potion_drink():
        """Shortcut for potion drinking.
        Not every game has quick potion use shortcut
        so this action is only there to be overridden if needed
        without having to declare a new voice command.
        The return value does not matter.
        Returns 0 by default to stop talon from outputting errors to log."""
        return 0

    def game_stealth_kill():
        """Perform a stealth kill.
        No binding by default, needs to be overridden if needed.
        The return value does not matter.
        Returns 0 by default to stop talon from outputting errors to log."""
        return 0

    def game_craft():
        """Craft an object.
        Not every game has crafting mechanics
        so this action is only there to be overridden if needed
        without having to declare a new voice command"""
        return

    def game_manual_save():
        """"""
        return

    def game_quick_save():
        """"""
        actions.key("f5")

    def game_quick_load():
        """Load quick save. Left blank to be overridden if needed."""
        return

    def game_menu():
        """"""
        actions.key("escape")

    def game_inventory_show():
        """Show or had inventory"""
        actions.key("i")

    def game_crafting_menu_show():
        """Show or hide crafting menu"""
        actions.key("o")

    def game_quest_log_show():
        """Show or hide quest log or journal"""
        actions.key("j")

    def game_bestiary_show():
        """Show or hide glossary/bestiary/index/notebook"""
        actions.key("n")

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

    def press_game_key(key: str, times: int = 1, hold: int = None):
        """Press key specified number of times,
        optionally holding for the specified number of microseconds each time.
        If hold is Non then hold defaults to the key_hold setting"""
        hold = settings.get("key_hold") if hold is None else hold
        for i in range(times):
            wait = 0 if i == 0 else hold
            ctrl.key_press(key, hold=hold, wait=wait)

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