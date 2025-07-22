app: obsidian
-
tag(): user.tabs

^prop add:
    key(ctrl-home enter ctrl-home)
    insert("---\n")

# subscript <user.prose> [over]:
#     user.paste("<sub>{prose}</sub>")

# superscript <user.prose> [over]:
#     user.paste("<sup>{prose}</sup>")

subscript <number_small> [over]:
    user.paste("<a href=\"#sub{number_small}\"><sub>[{number_small}]</sub></a>")
    key(ctrl-end enter)
    user.paste("<div id=\"sub{number_small}\"><sub>[{number_small}]</sub></div>")
    key(left:6)

superscript <number_small> [over]:
    user.paste("<a href=\"#sup{number_small}\"><sup>[{number_small}]</sup></a>")
    key(ctrl-end enter)
    user.paste("<div id=\"sup{number_small}\"><sup>[{number_small}]</sup></div>")
    key(left:6)

link: user.insert_snippet_by_name("wiki link")
ex link: user.insert_snippet_by_name("link")