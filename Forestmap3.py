from Generating_Forest_Function import *
# Define the default box component for a regular cell


def update_box(name):
    default_box = [
        " ________ ",
        "|        |",
        "|        |",
        "|        |"
    ]
    name = name.split()

    for i in range(len(name)):
        line = list(default_box[i+1])
        nameLine = list(name[i])
        for j in range(len(name[i])):
            line[j+1] = nameLine[j]
        default_box[i+1] = "".join(line)
    return default_box



# Define the top-left cell ("You are here")
start_box = [
    " ________ ",
    "|        |",
    "|You are |",
    "|  here  |"
]

# Define the bottom-right cell ("Wise Goblin")
end_box = [
    " ________ ",
    "|Grekthor|",
    "|  the   |",
    "|  Sage  |"
]

forest_map_print = "Enter Forest here\n"
# Define the number of rows and columns for the grid
rows, cols = 5, 5

# Print each row of the grid
for r in range(rows):
    # Print each line of the boxes in the current row
    for line_idx in range(4):  # Each box has 4 lines
        row_line = ""
        for c in range(cols):
            # Determine if we are at the top-left or bottom-right cell
            if r == rows - 1 and c == cols - 1:
                row_line += end_box[line_idx]
            else:
                room_box = update_box(forest[r][c].get_Name())
                row_line += room_box[line_idx]
        forest_map_print += row_line
        forest_map_print += "\n"
    # No extra line between rows for seamless grid