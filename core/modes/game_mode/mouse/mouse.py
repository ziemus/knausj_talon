from talon import Module, cron, ctrl

mod = Module()

setting_mouse_hiss = mod.setting(
    "mouse_enable_hiss",
    type=bool,
    default=False,
    desc="enable default hiss behavior, false by default",
)
setting_mouse_enable_hiss_stops_scroll = mod.setting(
    "mouse_enable_hiss_stops_scroll",
    type=int,
    default=0,
    desc="When enabled, hiss stops continuous scroll modes (wheel upper/downer/gaze)",
)
setting_mouse_hold = mod.setting(
    "mouse_hold",
    type=int,
    default=16000,
    desc="nanoseconds to wait between mouse button press and release",
)
setting_mouse_wait = mod.setting(
    "mouse_wait",
    type=int,
    default=0,
    desc="nanoseconds to wait between consecutive mouse button release and press",
)

@mod.action_class
class Actions:
    
    def mouse_stay_in_place(is_stay: bool):
        """stay in place so that for example
        content that is not hoverable
        but activates on hover
        can be read without turning the eye tracker off only for a couple of seconds
        which in theory may damage it if done too frequently"""
        if is_stay:
            _start_stay_job()
        else:
            _stop_stay_job()

def _mouse_stay():
    ctrl.mouse_move(_stay_x, _stay_y, dx=0, dy=0)

_stay_job = None
_stay_x = 0
_stay_y = 0

def _start_stay_job():
    global _stay_job, _stay_x, _stay_y
    if _stay_job:
        return
    _stay_x, _stay_y = ctrl.mouse_pos()
    _stay_job = cron.interval("1ms", _mouse_stay)


def _stop_stay_job():
    global _stay_job
    if not _stay_job:
        return
    cron.cancel(_stay_job)
    _stay_job = None