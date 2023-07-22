from talon import Module, actions
from user.knausj_talon.core.modes.game_mode.binding.BindingExecutor import BindingExecutor

mod = Module()
mod.tag("game_map")


@mod.action_class
class Actions:

    def game_map_show():
        """Show game map. M by default."""
        BindingExecutor.execute("map_show")

    def game_map_hide():
        """Hide game map. Defaults to user.game_map_show() if not overridden."""
        BindingExecutor.execute_or_substitute("map_hide", "map_show")

    def game_map_marker_place():
        """Place a marker on the map. RMB by default."""
        BindingExecutor.execute("map_marker_place")

    def game_map_marker_clear():
        """Clear a marker from the map. Defaults to user.game_map_marker_place() if not overridden."""
        BindingExecutor.execute_or_substitute("map_marker_clear", "map_marker_place")

    def game_map_center():
        """Center game map. G by default."""
        BindingExecutor.execute("map_center")

    def game_map_rotate():
        """Rotate game map. Not bound by default, needs to be overridden."""
        BindingExecutor.execute("map_rotate")

    def game_map_floor_up():
        """Center game map. Page up by default."""
        BindingExecutor.execute("map_level_up")

    def game_map_floor_down():
        """Center game map. Page down by default."""
        BindingExecutor.execute("map_level_down")

    def game_map_filters_show():
        """Show list of map filters. Tab by default."""
        BindingExecutor.execute("map_filters_show")

    def game_map_filters_hide():
        """Hide list of map filters. Defaults to user.game_map_filters_show() if not overridden."""
        BindingExecutor.execute_or_substitute("map_filters_hide", "map_filters_show")

    def game_map_filter_toggle():
        """Turn a single map filter on/off. Needs to be overridden, otherwise it doesn't do anything."""
        BindingExecutor.execute("map_filter_toggle")

    def game_map_filters_toggle_all():
        """Turn all map filters on/off. Needs to be overridden, otherwise it doesn't do anything."""
        BindingExecutor.execute("map_filters_toggle_all")

    def game_map_zoom_in():
        """Zoom in the map. Defaults to a singular scroll up.
        Adjust the setting: user.mouse_wheel_down_amount to adjust the zoom amount."""
        #TODO 
        actions.user.mouse_scroll_up()

    def game_map_zoom_out():
        """Zoom out the map. Defaults to a singular scroll down.
        Adjust the setting: user.mouse_wheel_down_amount to adjust the zoom amount."""
        #TODO 
        actions.user.mouse_scroll_down()

    def game_map_zoom_in_continuous():
        """Zoom in the map continuously. Defaults to a singular scroll up.
        Adjust the setting: user.mouse_continuous_scroll_amount to adjust the zoom amount.
        """
        #TODO 
        actions.user.mouse_scroll_up_continuous()

    def game_map_zoom_out_continuous():
        """Zoom out the map continuously. Defaults to a singular scroll down.
        Adjust the setting: user.mouse_continuous_scroll_amount to adjust the zoom amount.
        """
        #TODO 
        actions.user.mouse_scroll_down_continuous()

    def game_map_zoom_continuous_stop():
        """Stop continuous map zoom. Defaults to user.mouse_scroll_stop().
        See also the settings: user.mouse_enable_pop_stops_scroll, user.mouse_enable_hiss_stops_scroll"""
        #TODO 
        actions.user.mouse_scroll_stop()
