import win32api, win32con
from talon import Module

game_camera_module = Module()

setting_turn_around_delta = game_camera_module.setting(
    "game_turn_around_mouse_delta",
    type=int,
    default=0,
    desc=""" for each game there needs to be defined a particular horizontal delta
        that mouse needs to be moved by
        in order to turn the camera around

        basically the user needs to experiment a little
        and find the right value

        in my experience, it will never be perfectly accurate
        but it will be enough to play""")
setting_turn_horizontally_delta = game_camera_module.setting(
    "game_turn_horizontally_mouse_delta",
    type=int,
    default=0,
    desc=""" for each game there needs to be defined a particular horizontal delta
        that mouse needs to be moved by
        in order to turn the camera horizontally

        basically the user needs to experiment a little
        and find the right value

        in my experience, it will never be perfectly accurate
        but it will be enough to play""")
setting_turn_vertically_delta = game_camera_module.setting(
    "game_turn_vertically_mouse_delta",
    type=int,
    default=0,
    desc=""" for each game there needs to be defined a particular vertical delta
        that mouse needs to be moved by
        in order to turn the camera vertically

        basically the user needs to experiment a little
        and find the right value

        in my experience, it will never be perfectly accurate
        but it will be enough to play""")

game_camera_module.tag("game_camera_controls")


@game_camera_module.action_class
class CameraActions:

    def game_turn_camera_around():
        """WIP turn camera around"""
        dx = setting_turn_around_delta.get()
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, 0)

    def game_turn_camera(direction: str, is_small_movement: bool):
        """WIP turn camera"""
        dy = dx = 0
        if direction in ["right", "left"]:
            dx = setting_turn_horizontally_delta.get()
        elif direction in ["down", "up"]:
            dy = setting_turn_vertically_delta.get()

        if direction == "left":
            dx *= -1
        elif direction == "up":
            dy *= -1

        if is_small_movement:  # todo: make new settings for this
            dx = (int)(dx * 0.5)
            dy = (int)(dy * 0.5)

        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)