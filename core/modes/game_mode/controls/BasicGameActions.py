from talon import actions, ctrl, settings, Module

basic_game_actions_module = Module()

basic_game_actions_module.tag("game_character_sheet")
basic_game_actions_module.tag("game_mouse_enabled")
basic_game_actions_module.tag("first_person_game_controls")
basic_game_actions_module.list("game_number_shortcuts")


@basic_game_actions_module.action_class
class BasicGameActions:

    def game_crouch():
        """Duck or crouch"""
        actions.key("c")

    def game_dodge():
        """Dodge roll"""
        actions.key("ctrl")

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

    def game_jump():
        """Basic (single) jump"""
        actions.key("space")

    def game_use():
        """Basic use/interact with an object"""
        actions.key("e")

    def game_character_sheet_show():
        """Show character sheet/skill tree/ability menu etc."""
        actions.key("c")

    def game_skill_learn():
        """Learn a skill. No binding by default. Needs to be overridden."""
        return

    def game_skill_unlearn():
        """Unlearn a skill. Defaults to user.game_skill_learn()"""
        actions.user.game_skill_learn()

    def game_heal():
        """Shortcut for healing.
        Not every game has healing or quick potion use shortcut
        so this action is only there to be overridden if needed
        without having to declare a new voice command"""
        return

    def game_craft():
        """Craft an object.
        Not every game has crafting mechanics
        so this action is only there to be overridden if needed
        without having to declare a new voice command"""
        return

    def game_tool_use():
        """Use selected tool or trap, like in a souls-like game.
        As not every game has this mechanic, it's left blank to be overridden if needed."""
        return

    def game_tool_switch_left():
        """Switch selected tool or trap left, like in a souls-like game.
        As not every game has this mechanic, it's left blank to be overridden if needed."""
        return

    def game_tool_switch_right():
        """Switch selected tool or trap right, like in a souls-like game.
        As not every game has this mechanic, it's left blank to be overridden if needed."""
        return

    def game_manual_save():
        """"""
        return

    def game_quick_save():
        """"""
        actions.key("f5")

    def game_menu():
        """"""
        actions.key("escape")

    def game_inventory_show():
        """Show or had inventory"""
        actions.key("i")

    def game_skill_tree_show():
        """Show or hide skill tree menu"""
        actions.key("k")

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