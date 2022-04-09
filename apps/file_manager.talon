tag: user.file_manager
-
title force: user.file_manager_refresh_title()
manager show: user.file_manager_toggle_pickers()
manager close: user.file_manager_hide_pickers()
manager refresh: user.file_manager_update_lists()
go {user.directories}: user.file_manager_open_directory(directories)
go back [<number_small>]: 
    number = number_small or 1    
    user.file_manager_go_back()
    repeat(number - 1)
forward [<number_small>]:
    number = number_small or 1
    user.file_manager_go_forward()
    repeat(number - 1)
root [<number_small>]: 
    number = number_small or 1
    user.file_manager_open_parent()
    repeat(number - 1)
# folder <number_small>$: 
#     directory = user.file_manager_get_directory_by_index(number_small - 1)
#     user.file_manager_open_directory(directory)
skim {user.file_manager_directories}: user.file_manager_open_directory(file_manager_directories)
file {user.file_manager_files}: user.file_manager_open_file(file_manager_files)
grab file {user.file_manager_files}: user.file_manager_select_file(file_manager_files)
grab folder {user.file_manager_directories}: user.file_manager_select_directory(file_manager_directories)
# file <number_small>: 
#     file = user.file_manager_get_file_by_index(number_small - 1)
#     user.file_manager_open_file(file)
# grab folder <number_small>: 
#     directory = user.file_manager_get_directory_by_index(number_small - 1)
#     user.file_manager_select_directory(directory)
# grab file <number_small>: 
#     file = user.file_manager_get_file_by_index(number_small - 1)
#     user.file_manager_select_file(file)


copy path {user.file_manager_files}:
    user.file_manager_select_file(file_manager_files)
    sleep(200ms)
    user.file_manager_copy_path()

copy path {user.file_manager_directories}:
    user.file_manager_select_directory(file_manager_directories)
    sleep(200ms)
    user.file_manager_copy_path()

copy path:
    user.file_manager_copy_path()

#new folder
folder new [<user.text>]: 
    user.file_manager_new_folder(text  or "")

#show properties
properties show: user.file_manager_show_properties()

# open terminal at location
terminal here: user.file_manager_terminal_here()

folder next: user.file_manager_next_folder_page()
folder last: user.file_manager_previous_folder_page()

file next: user.file_manager_next_file_page()
file last: user.file_manager_previous_file_page()

