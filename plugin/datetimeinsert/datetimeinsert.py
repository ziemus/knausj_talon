import datetime
import time
from talon import Module

mod = Module()


@mod.action_class
class Actions:
    def time_format(fmt: str = None) -> str:
        """Return the current time, formatted.
        fmt: strftime()-style format string, defaults to ISO format."""
        now = datetime.datetime.now()
        if fmt is None:
            return now.isoformat()
        return now.strftime(fmt)

    def time_format_utc(fmt: str = None) -> str:
        """Return the current UTC time, formatted.
        fmt: strftime()-style format string, defaults to ISO format."""
        now = datetime.datetime.utcnow()
        if fmt is None:
            return now.isoformat()
        return now.strftime(fmt)

    def time_epoch_seconds() -> int:
        """"""
        now = time.time_ns()
        return int(now / 1000000)

    def time_epoch_millis() -> int:
        """"""
        now = time.time_ns()
        return int(now / 1000)