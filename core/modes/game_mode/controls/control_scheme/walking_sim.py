from talon import Module, Context, actions

mod = Module()
mod.tag("walking_sim_controls")

ctx = Context()
ctx.matches = """
tag: user.walking_sim_controls
and mode: all
"""

@ctx.action_class("user")
class FootSwitchActions:
    def foot_switch_olympus_top_down():
        actions.skip()

    def foot_switch_olympus_top_up(held: bool):
        actions.user.game_turn_camera_around()

    def foot_switch_olympus_center_down():
        actions.user.switch_game_movement(True)

    def foot_switch_olympus_center_up(held: bool):
        actions.user.switch_game_movement(False)

    def foot_switch_olympus_left_down():
        actions.user.game_turn_camera_start('left')

    def foot_switch_olympus_left_up(held: bool):
        actions.user.game_turn_camera_stop(True, False)

    def foot_switch_olympus_right_down():
        actions.user.game_turn_camera_start('right', 2.0)

    def foot_switch_olympus_right_up(held: bool):
        actions.user.game_turn_camera_stop(True, False)

    def foot_switch_pcsensor_center_down():
        actions.key("space:down")

    def foot_switch_pcsensor_center_up(held: bool):
        actions.key("space:up")

    # def foot_switch_pcsensor_left_down():
    #     actions.user.mouse_scroll_up_continuous()

    # def foot_switch_pcsensor_left_up(held: bool):
    #     actions.user.mouse_scroll_stop()

    # def foot_switch_pcsensor_right_down():
    #     actions.user.mouse_scroll_down_continuous()

    # def foot_switch_pcsensor_right_up(held: bool):
    #     actions.user.mouse_scroll_stop()