os: windows
and app.name: Scrivener
and app.exe: Scrivener.exe
-
# add items
(document|doc) add:
    key(ctrl-n)
folder add:
    key(alt-shift-n)

# import files
file import:
    key(ctrl-shift-i)
image [[from] file] (add|insert):
    key(super-shift-i)

# footnotes and comments
(comment|come) (add|insert):
    key(shift-f4)
(footnote|foot|note) (add|insert):
    key(shift-f5) 
(comment|come|footnote|foot|note) show:
    key(alt:down)
    mouse_click(0)
    key(alt:up)

# navigation
(document|doc) [go] (next|ness):
    key(alt-shift-down)
(document|doc) [go] (previous|prev|back):
    key(alt-shift-up)
(history|hiss) [go] (next|ness|forward|for):
    key(ctrl-])
(history|hiss) [go] (previous|prev|back):
    key(ctrl-[)
(enclosing|enclose|close) group [go]:
    key(super-ctrl-r)
editor selection [go]:
    key(super-shift-each)
binder reveal:
    key(super-shift-r)
[binder] [selection] expand:
    key(right)
[binder] [selection] collapse:
    key(left)

# inspector
(inspector|inspect) [show|toggle|hide]:
    key(alt-shift-i)
(inspector|inspect|in) notes [show]:
    key(super-alt-h)
(inspector|inspect|in) bookmarks [show]:
    key(super-alt-n)
(inspector|inspect|in) meta [data] [show]:
    key(super-alt-j)
(inspector|inspect|in) snap [shots] [show]:
    key(alt-shift-m)
(inspector|inspect|in) (comments|footnotes) [show]:
    key(super-alt-k)
(inspector|inspect|in) synopsis [show]:
    key(super-alt-i)
(inspector|inspect|in) keywords [show]:
    key(super-alt-l)

# view modes
(composition|comp) mode [toggle]:
    key(f11)
(scrivenings|scrivening|scriv) [show|toggle|hide]:
    key(ctrl-1)
(corkboard|cork|board) [show|toggle|hide]:
    key(ctrl-2)
(outliner|outline) [show|toggle|hide]:
    key(ctrl-3)
(header|head) view [show|toggle|hide]:
    key(super-shift-h)
(footer|foot) view [show|toggle|hide]:
    key(super-shift-f)

# corkboard
(corkboard|cork|board) edges label [color] [use|show|toggle|hide]:
    key(f9)
(corkboard|cork|board) [index] card label [color] [use|show|toggle|hide]:
    key(ctrl-f9)
(corkboard|cork|board) status [stamps] [show|toggle|hide]:
    key(alt-f9)
(corkboard|cork|board) keyword [color] [show|toggle|hide]:
    key(shift-f9)

# splits
split (no|none|close):
    key(ctrl-')
split [vertically|vertical|ver]:
    key(ctrl-")
split (horizontally|horizontal|hore):
    key(ctrl-+)
split [document|doc] [open] (right|bottom|down):
    key(alt-shift-o)
split [document|doc] [open] (left|top|up):
    key(ctrl-shift-o)

script mode [toggle]:
    key(ctrl-8)

menu search:
    key(shift-f1)