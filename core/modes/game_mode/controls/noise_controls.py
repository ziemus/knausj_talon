from threading import Lock
from user.knausj_talon.core.modes.game_mode.GameModeHelper import GameModeHelper
from talon import Module, Context, actions, noise, settings

mod = Module()
mod.list("game_noises")
mod.list("game_noise_controls")

ctx = Context()
noises = ("pop", "hiss")
ctx.lists["user.game_noises"] = noises
noise_action_names = {
    "jump": "jump",
    "move": "move",
    "dodge": "dodge",
    "use": "use",
    "touch": "click",
    "click": "click",
    "duke": "double click",
    "double click": "double click",
    "long click": "long click",
    "off": "off",
    "default": "default",
}
ctx.lists["user.game_noise_controls"] = noise_action_names

action_name_to_action = {
    "jump":
        lambda _: actions.user.game_jump(),
    "move":
        lambda _: actions.user.switch_game_movement(),
    "dodge":
        lambda _: actions.user.game_dodge(),
    "use":
        lambda _: actions.user.game_use(),
    "click":
        lambda _: actions.user.game_click(0, 1),
    "long click":
        lambda is_active: actions.user.game_press_mouse(button=0, down=is_active),
    "double click":
        lambda _: actions.user.game_click(0, 2),
}

hotswappable_binding: dict[str, str] = {"pop": "default", "hiss": "default"}
lock_binding = Lock()

setting_pop_default = mod.setting(
    "game_noise_pop_binding_default",
    type=str,
    default="click",
    desc="""Default pop binding for hot-swappable game mode noise controls.
        See the list of available bindings under user.game_noise_controls.""")

setting_hiss_default = mod.setting(
    "game_noise_hiss_binding_default",
    type=str,
    default="off",
    desc="""Default hiss binding for hot-swappable game mode noise controls.
        See the list of available bindings under user.game_noise_controls.""")

default_noise_settings = {"pop": setting_pop_default, "hiss": setting_hiss_default}


@mod.action_class
class GameNoiseActions:

    def game_before_on_pop():
        """customizable behavior before on pop executes its default game binding"""
        return 0

    def game_after_on_pop():
        """customizable behavior after on pop executes its default game binding"""
        return 0

    def game_before_on_hiss():
        """customizable behavior before on hiss executes its default game binding"""
        return 0

    def game_after_on_hiss():
        """customizable behavior after on hiss executes its default game binding"""
        return 0

    def game_noise_control_reset():
        """reset to default"""
        global hotswappable_binding, lock_binding
        with lock_binding:
            hotswappable_binding = {"pop": "default", "hiss": "default"}

    def game_noise_control_switch(noise: str, control: str):
        """switch noise binding"""
        global noises, noise_action_names, hotswappable_binding, lock_binding

        if not (noise in noises and control in noise_action_names.values()):
            # print a warning or notify
            return

        with lock_binding:
            hotswappable_binding[noise] = control


def _execute_noise_binding(noise, is_active):
    global hotswappable_binding
    action_name = hotswappable_binding[noise]

    if action_name == "default":
        action_name = default_noise_settings[noise].get()
    if action_name == "off":
        return

    does_action_require_input = action_name == "long click" or (action_name == "move" and
                                                                noise == "hiss")

    if does_action_require_input:
        action_name_to_action[action_name](is_active)
    elif is_active:
        action_name_to_action[action_name](True)


def on_pop(_):
    global lock_binding

    if not GameModeHelper.is_game_mode():
        return

    with lock_binding:
        actions.user.game_before_on_pop()
        if not settings.get("user.mouse_enable_pop_click"):
            _execute_noise_binding("pop", True)
        actions.user.game_after_on_pop()


def on_hiss(is_active):
    global lock_binding

    if not GameModeHelper.is_game_mode():
        return

    with lock_binding:
        actions.user.game_before_on_hiss()
        if not settings.get("user.mouse_enable_hiss"):
            _execute_noise_binding("hiss", is_active)
        actions.user.game_after_on_hiss()


noise.register("pop", on_pop)
noise.register("hiss", on_hiss)