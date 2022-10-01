from threading import Lock
from user.knausj_talon.modes.game_mode.GameModeHelper import GameModeHelper
from talon import Module, Context, actions, noise, settings

mod = Module()
mod.list("game_noises")
mod.list("game_noise_controls")

ctx = Context()
noises = ('pop', 'hiss')
ctx.lists['user.game_noises'] = noises
noise_controls = {
    'jump': 'jump',
    'move': 'move',
    'use': 'use',
    'touch': 'click',
    'click': 'click',
    'duke': 'double click',
    'double click': 'double click',
    'off': 'off'
}
ctx.lists['user.game_noise_controls'] = noise_controls

binding: dict[str, str] = {'pop': 'click', 'hiss': 'off'}
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


@mod.action_class
class GameNoiseActions:

    def game_before_on_pop():
        """customizable behavior before on pop executes its default game binding"""
        pass

    def game_after_on_pop():
        """customizable behavior after on pop executes its default game binding"""
        pass

    def game_before_on_hiss():
        """customizable behavior before on hiss executes its default game binding"""
        pass

    def game_after_on_hiss():
        """customizable behavior after on hiss executes its default game binding"""
        pass

    def game_noise_control_reset():
        """reset to default"""
        global binding, lock_binding
        with lock_binding:
            pop_binding = setting_pop_default.get()
            hiss_binding = setting_hiss_default.get()
            binding = {"pop": pop_binding, "hiss": hiss_binding}

    def game_noise_control_switch(noise: str, control: str):
        """switch noise binding"""
        global noises, noise_controls, binding, lock_binding

        if not (noise in noises and control in noise_controls.values()):
            # print a warning or notify
            return

        with lock_binding:
            binding[noise] = control


def _execute_noise_binding(noise, is_active):
    global binding
    action = binding[noise]

    if action == 'move':
        if noise == 'pop':
            actions.user.switch_game_movement()
        elif noise == 'hiss':
            actions.user.switch_game_movement(is_active)

    elif is_active:
        if action == 'jump':
            actions.user.game_jump()
        elif action == 'use':
            actions.user.game_use()
        elif action == 'click':
            actions.user.game_click()
        elif action == 'double click':
            actions.user.game_click(0, 2)


def on_pop(_):
    global lock_binding

    if not GameModeHelper.is_current_game_active_and_game_mode():
        return

    with lock_binding:
        actions.user.game_before_on_pop()
        if not settings.get("user.mouse_enable_pop_click"):
            _execute_noise_binding('pop', True)
        actions.user.game_after_on_pop()


def on_hiss(is_active):
    global lock_binding

    if not GameModeHelper.is_current_game_active_and_game_mode():
        return

    with lock_binding:
        actions.user.game_before_on_hiss()
        if not settings.get("user.mouse_enable_hiss"):
            _execute_noise_binding('hiss', is_active)
        actions.user.game_after_on_hiss()


noise.register("pop", on_pop)
noise.register("hiss", on_hiss)