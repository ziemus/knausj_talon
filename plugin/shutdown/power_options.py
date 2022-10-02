import os
from talon import actions, Module, ui

mod = Module()

def get_talon_voice():
    return ui.apps(pid=os.getpid())[0]

def short_sleep():
    actions.sleep('300ms')

def control_mouse_disable():
    actions.user.mouse_toggle_control_mouse(0)
    actions.sleep('1000ms')

def start_menu_power_action(key : str
                            , do_put_talon_to_sleep : bool = True
                            , do_shut_talon_down : bool = False
                            ):
    if do_put_talon_to_sleep:
        control_mouse_disable()
        actions.speech.disable()
    actions.user.start_menu_power_options_show()
    actions.key(key)
    if do_shut_talon_down:
        actions.user.talon_voice_quit()

@mod.action_class
class Actions:
    def start_menu_show():
        """"""
        actions.key('super-x')

    def start_menu_power_options_show():
        """Display shut down / sign out / sleep / lock menu"""
        actions.user.start_menu_show()
        short_sleep()
        actions.key('u')
        short_sleep()

    def start_menu_sleep():
        """"""
        start_menu_power_action('s')

    def start_menu_shut_down():
        """"""
        start_menu_power_action('u')

    def talon_voice_restart():
        """"""
        control_mouse_disable()
        talon_voice = get_talon_voice()
        os.startfile(talon_voice.exe)
        talon_voice.quit()

    def talon_voice_quit():
        """"""
        talon_voice = ui.apps(pid=os.getpid())[0]
        talon_voice.quit()
