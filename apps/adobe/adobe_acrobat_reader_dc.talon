app: adobe_acrobat_reader_dc
-
# Set tags
tag(): user.tabs
tag(): user.pages

up: key(pageup)
down: key(pagedown)
fullscreen: key(ctrl-l)
reading mode: key(ctrl-h)
lil up: key(up:20)
lil down: key(down:20)
go page: key(shift-ctrl-n)

go page <user.number_string>:
	key(shift-ctrl-n)
	sleep(50ms)
	insert(number_string)
	key(enter)