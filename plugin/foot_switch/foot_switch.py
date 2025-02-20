from talon import Module, actions, cron
import time

HOLD_TIMEOUT = 0.2

OLYMPUS_LEFT = 0
OLYMPUS_CENTER = 1
OLYMPUS_RIGHT = 2
OLYMPUS_TOP = 3

PCSENSOR_LEFT = 4
PCSENSOR_CENTER = 5
PCSENSOR_RIGHT = 6

FOOT_SWITCH_INDEX_MAX = PCSENSOR_RIGHT + 1

DOWN = 0
UP = 1

mod = Module()
current_state = [UP, UP, UP, UP, UP, UP, UP]
last_state = [UP, UP, UP, UP, UP, UP, UP]
timestamps = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]


def on_interval():
    for key in range(FOOT_SWITCH_INDEX_MAX):
        if last_state[key] != current_state[key]:
            last_state[key] = current_state[key]

            if current_state[key] == DOWN:
                call_down_action(key)
            else:
                held = time.perf_counter() - timestamps[key] > HOLD_TIMEOUT
                call_up_action(key, held)


# In a hotkey event, eg "key(ctrl:down)", any key you press with key/insert
# actions will be combined with ctrl since it's still held. Just updating a
# boolean in the actual hotkey event and reading it asynchronously with cron
# gets around this issue.
cron.interval("16ms", on_interval)


def call_down_action(key: int):
    if key == OLYMPUS_LEFT:
        actions.user.foot_switch_olympus_left_down()
    elif key == OLYMPUS_CENTER:
        actions.user.foot_switch_olympus_center_down()
    elif key == OLYMPUS_RIGHT:
        actions.user.foot_switch_olympus_right_down()
    elif key == OLYMPUS_TOP:
        actions.user.foot_switch_olympus_top_down()
    elif key == PCSENSOR_LEFT:
        actions.user.foot_switch_pcsensor_left_down()
    elif key == PCSENSOR_CENTER:
        actions.user.foot_switch_pcsensor_center_down()
    elif key == PCSENSOR_RIGHT:
        actions.user.foot_switch_pcsensor_right_down()


def call_up_action(key: int, held: bool):
    if key == OLYMPUS_LEFT:
        actions.user.foot_switch_olympus_left_up(held)
    elif key == OLYMPUS_CENTER:
        actions.user.foot_switch_olympus_center_up(held)
    elif key == OLYMPUS_RIGHT:
        actions.user.foot_switch_olympus_right_up(held)
    elif key == OLYMPUS_TOP:
        actions.user.foot_switch_olympus_top_up(held)
    elif key == PCSENSOR_LEFT:
        actions.user.foot_switch_pcsensor_left_up(held)
    elif key == PCSENSOR_CENTER:
        actions.user.foot_switch_pcsensor_center_up(held)
    elif key == PCSENSOR_RIGHT:
        actions.user.foot_switch_pcsensor_right_up(held)

@mod.action_class
class Actions:
    # Key events. Don't touch these.

    def foot_switch_down_event(key: int):
        """Foot switch key down event. Left(0), Center(1), Right(2), Top(3)"""
        timestamps[key] = time.perf_counter()
        current_state[key] = DOWN

    def foot_switch_up_event(key: int):
        """Foot switch key up event. Left(0), Center(1), Right(2), Top(3)"""
        current_state[key] = UP

    # Foot switch button actions. Modify these to change button behavior.

    def foot_switch_olympus_top_down():
        """Foot switch button top:down"""
        actions.user.mouse_scroll_up_continuous()

    def foot_switch_olympus_top_up(held: bool):
        """Foot switch button top:up"""
        actions.user.mouse_scroll_stop()

    def foot_switch_olympus_center_down():
        """Foot switch button center:down"""
        actions.user.mouse_scroll_down_continuous()

    def foot_switch_olympus_center_up(held: bool):
        """Foot switch button center:up"""
        actions.user.mouse_scroll_stop()

    def foot_switch_olympus_left_down():
        """Foot switch button left:down"""
        actions.user.mouse_drag(0)

    def foot_switch_olympus_left_up(held: bool):
        """Foot switch button left:up"""
        actions.user.mouse_drag_end()
        # if it fails try
        # if held:
        #     actions.user.mouse_drag_toggle(0)
        # else:
        #     actions.mouse_click(0)

    def foot_switch_olympus_right_down():
        """Foot switch button right:down"""
        actions.user.mouse_drag(1)

    def foot_switch_olympus_right_up(held: bool):
        """Foot switch button right:up"""
        actions.user.mouse_drag_end()

    def foot_switch_pcsensor_center_down():
        """Foot switch button center:down"""
        actions.skip()

    def foot_switch_pcsensor_center_up(held: bool):
        """Foot switch button center:up"""
        if not held:
            actions.tracking.control_toggle()

    def foot_switch_pcsensor_left_down():
        """Foot switch button left:down"""
        actions.skip()

    def foot_switch_pcsensor_left_up(held: bool):
        """Foot switch button left:up"""
        if not held:
            actions.speech.toggle()

    def foot_switch_pcsensor_right_down():
        """Foot switch button right:down"""
        actions.skip()

    def foot_switch_pcsensor_right_up(held: bool):
        """Foot switch button right:up"""
        if not held:
            actions.key("super-h")
            actions.mimic("drowse")
