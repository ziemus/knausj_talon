title: /Apache JMeter/
-
toggle: key(ctrl-t)

zoom in:
	key(alt-o)
	key(alt-i)

zoom out:
	key(alt-o)
	key(alt-u)

thread group: key(ctrl-0)
request: key(ctrl-1)
regex: key(ctrl-2)
assert: key(ctrl-3)
post processor: key(ctrl-6)
pre processor: key(ctrl-7)
debug sampler: key(ctrl-8)
result tree: key(ctrl-9)
expand:	key(right)
collapse: key(left)
duplicate: key(shift-ctrl-c)
remove: key(delete)

remove yes:
	key(delete)
	sleep(500ms)
	key(alt-y)

run fast:
	key(alt-r)
	key(alt-n)

run time:
	key(ctrl-r)

stop test:
	key(ctrl-.)

shutdown test:
	key(ctrl-,)

clean find:
	key(alt-s)
	key(alt-r)
	key(alt-s)
	key(alt-r)

var:
	insert("${}")
	key(left)

prop:
	insert("${__P()")
	insert("}")
	key(left:2)

funk:
	insert('${')
	insert('__()}')
	key(left:3)

simple controller:
	mouse_click(1)
	sleep(10ms)
	#add
	key(down)
	key(right)
	sleep(10ms)
	#controllers
	key(down)
	key(right)
	sleep(10ms)
	#simple controller
	key(down:13)
	key(enter)
	