from threading import Lock
from user.knausj_talon.modes.game_mode.GameModeHelper import GameModeHelper
from talon import Module, Context, actions, noise

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

binding = None
lock_binding = Lock()


def _noise_control_reset():
    global binding, lock_binding
    with lock_binding:
        binding = {'pop': 'click', 'hiss': 'off'}


_noise_control_reset()


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
        _noise_control_reset()

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
            actions.user.game_click()
            actions.sleep('50ms')
            actions.user.game_click()


def on_pop(_):
    global lock_binding

    if actions.user.is_default_eye_mouse_noise_behavior():
        return
    if not GameModeHelper.is_current_game_active_and_game_mode():
        return

    with lock_binding:
        actions.user.game_before_on_pop()
        _execute_noise_binding('pop', True)
        actions.user.game_after_on_pop()


def on_hiss(is_active):
    global lock_binding

    if actions.user.is_default_eye_mouse_noise_behavior():
        return
    if not GameModeHelper.is_current_game_active_and_game_mode():
        return

    with lock_binding:
        actions.user.game_before_on_hiss()
        _execute_noise_binding('hiss', is_active)
        actions.user.game_after_on_hiss()


noise.register("pop", on_pop)
noise.register("hiss", on_hiss)
