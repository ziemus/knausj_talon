app: windows_explorer
app: windows_file_browser
-
tag(): user.file_manager
^go <user.letter>$: user.file_manager_open_volume("{letter}:")
go app data: user.file_manager_open_directory("%AppData%")
go program files: user.file_manager_open_directory("%programfiles%")
go app folder: user.file_manager_open_directory("shell:AppsFolder")
go cursor less config: user.file_manager_open_directory("%AppData%/Talon/user/cursorless-settings")
go startup: user.file_manager_open_directory("shell:startup")
go common startup: user.file_manager_open_directory("shell:common startup")
terminal admin: key(alt f s a)
address bar: key(alt-d)
copy address: 
    key(alt-d ctrl-c)
extra large view:
    key(ctrl-shift-1)
large view:
    key(ctrl-shift-2)
medium view:
    key(ctrl-shift-3)
small view:
    key(ctrl-shift-3)
list view:
    key(ctrl-shift-5)
detail view:
    key(ctrl-shift-6)

