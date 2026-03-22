

button_kill = [
    " _________ ",
    "|         |",
    "|  Attack |",
    "|_________|"
]


button_spare = [
    " _________ ",
    "|         |",
    "|  Spare  |",
    "|_________|"
]

space = [
    "           ",
    "           ",
    "           ",
    "           "
]
kill_button = ""

for line_kill, space_line, line_spare in zip(button_kill, space, button_spare):
    kill_button+=line_kill + space_line + line_spare+"\n"


