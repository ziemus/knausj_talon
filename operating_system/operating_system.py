from talon import Context, Module, actions
import os


mod = Module()
mod.list("launch_command", desc="List of applications to launch")
mod.list("directories", desc="List of directories")
ctx = Context()
ctx.lists["self.launch_command"] = {}
ctx.lists["self.directories"] = {}


@mod.action_class
class Actions:
    def exec(command: str):
        """Run command"""
        os.system(command)

    def system_shutdown():
        """Shutdown operating system"""

    def system_restart():
        """Restart operating system"""

    def system_hibernate():
        """Hibernate operating system"""

    def system_lock():
        """Locks the OS"""

    def system_show_desktop():
        """Reveals the desktop"""

    def system_task_manager():
        """starts the task manager"""

    def system_task_view():
        """Mission control/super-tab equivalent"""

    def system_switcher():
        """Mission control/ctl-alt-tab equivalent"""

    def system_search():
        """Triggers system search (e.g. spotlight/powerrunner)"""
    
    def system_last_application():
        """triggers alt-tab"""

    def system_open_directory(path: str):
        """opens directory in default file manager"""

    def system_show_clipboard():
        """opens the systems default clipboard or equivalent"""
