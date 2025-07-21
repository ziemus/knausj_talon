from talon import Module, Context, actions

mod = Module()
mod.tag("game_foot_switch_first_person")

ctx = Context()
ctx.matches = """
tag: user.game_foot_switch_first_person
"""

@ctx.action_class("user")
class FootSwitchActions:
    def foot_switch_olympus_top_down():
        actions.user.toggle_hold_key("s")

    def foot_switch_olympus_top_up(held: bool):
        actions.user.toggle_hold_key("s")

    def foot_switch_olympus_center_down():
        actions.user.toggle_hold_key("w")

    def foot_switch_olympus_center_up(held: bool):
        actions.user.toggle_hold_key("w")

    def foot_switch_olympus_left_down():
        actions.skip()

    def foot_switch_olympus_left_up(held: bool):
        actions.user.game_turn_camera("left")

    def foot_switch_olympus_right_down():
        actions.skip()

    def foot_switch_olympus_right_up(held: bool):
        actions.user.game_turn_camera("right")

    def foot_switch_pcsensor_center_down():
        actions.user.toggle_hold_key("space")

    def foot_switch_pcsensor_center_up(held: bool):
        actions.user.toggle_hold_key("space")

    def foot_switch_pcsensor_left_down():
        actions.user.toggle_hold_key("a")
        
    def foot_switch_pcsensor_left_up(held: bool):
        actions.user.toggle_hold_key("a")
               
    def foot_switch_pcsensor_right_down():
        actions.user.toggle_hold_key("d")

    def foot_switch_pcsensor_right_up(held: bool):
        actions.user.toggle_hold_key("d")