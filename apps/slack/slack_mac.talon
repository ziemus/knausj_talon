os: mac
app: slack
-
tag(): user.messaging
tag(): user.emoji
# Workspace
workspace <number>: key("cmd-{number}")
# Channel
go info: key(cmd-shift-i)
# Navigation
focus (move | next): key(ctrl-`)
go next: key(f6)
go messages: key(cmd-shift-k)
go threads: key(cmd-shift-t)
go shortcuts: key(cmd-/)
go back: key(cmd-[)
go forward: key(cmd-])
go stars: key(cmd-shift-s)
go unread: key(cmd-shift-a)
go (previous | last): key(shift-tab)
go activity: key(cmd-shift-m)
(slack | lack) directory: key(cmd-shift-e)

# Messaging
grab left: key(shift-up)
grab right: key(shift-down)
add line: key(shift-enter)
(slack | lack) (slap | slaw | slapper): key(cmd-right shift-enter)
(slack | lack) (react | reaction): key(cmd-shift-\)
(insert command | commandify): key(cmd-shift-c)
insert code: insert("```")
(slack | lack) (bull | bullet | bulleted) [list]: key(cmd-shift-8)
(slack | lack) (number | numbered) [list]: key(cmd-shift-7)
(slack | lack) (quotes | quotation): key(cmd-shift->)
bold: key(cmd-b)
(italic | italicize): key(cmd-i)
(strike | strikethrough): key(cmd-shift-x)
(slack | lack) snippet: key(cmd-shift-enter)
# Calls
([toggle] mute | unmute): key(m)
(slack | lack) ([toggle] video): key(v)
(slack | lack) invite: key(a)

# Miscellaneous
bar left: key(cmd-shift-d)
bar right: key(cmd-.)
