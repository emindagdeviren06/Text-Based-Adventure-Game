final_map = ""


# Define the box and arrow components
box1 = [
    " ________ ",
    "|        |",
    "|Tower 1 |",
    "|________|"
]

box2 = [
    " ________ ",
    "|        |",
    "|Tower 2 |",
    "|________|"
]

arrow = [
    "                                ",
    "                                ",
    "                                ",
]

# Print the boxes and arrow line by line
for line1, arrow_line, line2 in zip(box1, arrow, box2):
    final_map += line1 + arrow_line + line2 +"\n"
# Define the boxes components
box1 = [
    "   ________ ",
    "  | Kings  |",
    "  | room   |",
    "  |________|"
]

box2 = [
    " ________ ",
    "|princess|",
    "|  room  |",
    "|________|"
]

box3 = [
    " ________ ",
    "| prince |",
    "|  room  |",
    "|________|"
]

box4 = [
    " ________ ",
    "|        |",
    "|  toilet|",
    "|________|"
]

# Print the boxes line by line
for line1, line2, line3, line4 in zip(box1, box2, box3, box4):
    final_map += line1 + " " + line2 + " " + line3 + " " + line4 +"\n"

# Define the large box with sections
large_box = [
    "   ______________________________________________ ",
    "  |                                              |",
    "  |                Great Hall                    |",
    "  |______________________________________________|"
]

# Print the large box line by line
for line in large_box:
    final_map += line + "\n"

# Define the boxes components
box1 = [
    "    ________________ ",
    "   |                |",
    "   |  Kitchen       |",
    "   |________________|"
]

box2 = [
    " ____________ ",
    "|            |",
    "|Store Room  |",
    "|____________|"
]

box3 = [
    " ________ ",
    "|        |",
    "| Chapel |",
    "|________|"
]

# Print the boxes line by line
for line1, line2, line3 in zip(box1, box2, box3):
    final_map += line1 + " " + line2 + " " + line3 +"\n"

# Define the box components
box1 = [
    "   __________________ ",
    " |                   |",
    " |  Courtyard        |",
    " |___________________|"
]

box2 = [
    " ____________________ ",
    "|                    |",
    "|  Dungeon           |",
    "|____________________|"
]

# Print the boxes line by line
for line1, line2 in zip(box1, box2):
    final_map += line1 + "  " + line2 +"\n"  # Adjust spacing as needed

# Define the box and arrow components
box1 = [
    " ________ ",
    "|        |",
    "|Tower 3 |",
    "|________|"
]

box2 = [
    " ________ ",
    "|        |",
    "|Tower 4 |",
    "|________|"
]

arrow = [
    "                               ",
    "                               ",
    "                               ",
]

# Print the boxes and arrow line by line

for line1, arrow_line, line2 in zip(box1, arrow, box2):
    final_map += line1 + arrow_line + line2 +"\n"

