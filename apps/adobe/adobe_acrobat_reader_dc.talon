app: adobe_acrobat_reader_dc
-
# Set tags
tag(): user.tabs
tag(): user.pages

# it is shorter to say up and doo instead of go up and go down
up: key(pageup)
day: key(pagedown)
# it is easier to say pre and nes than prev or previous and next
pre: key(ctrl-pageup)
nes: key(ctrl-pagedown)
fullscreen: key(ctrl-l)
reading mode: key(ctrl-h)
lil up: key(up:20)
lil day: key(down:20)
go page: key(shift-ctrl-n)
page by page: key(alt-v p:2)

go page <user.number_string>:
	key(shift-ctrl-n)
	sleep(50ms)
	insert(number_string)
	key(enter)
