#==================================================
# DECLARE FUNCTIONS

# main function
def minesweeper(level):
    # initialise a 2D list with default values
    num_rows = len(level)
    num_cols = len(level[0])
    solution = [[0] * num_cols for _ in range(num_rows)]

    # convert level to numbers grid
    row_index = 0
    for r_count, row in enumerate(level, start = 0):
        row_index += 1
        for c_count, col in enumerate(row, start = 0):
            if col == "#":
                solution[r_count][c_count] = "#"

    # update values
    for r in range (0, num_rows-1):
        for c in range (0, num_cols-1):
            value = l(r, c, solution)
            if value == '#':
                updateValues(r, c, solution, num_rows, num_cols)

    # return result
    return solution

# Adds 1 to all of the squares around a bomb.
def updateValues(rn, c, b, num_rows, num_cols):
    # Row above
    if rn-1 > -1:
        r = b[rn-1]
        
        if c-1 > -1:
            if not r[c-1] == '#':
                r[c-1] += 1

        if not r[c] == '#':
            r[c] += 1

        if num_cols > c+1:
            if not r[c+1] == '#':
                r[c+1] += 1

    # Same row 
    r = b[rn]

    if c-1 > -1:
        if not r[c-1] == '#':
            r[c-1] += 1

    if num_cols > c+1:
        if not r[c+1] == '#':
            r[c+1] += 1

    # Row below
    if num_rows > rn+1:
        r = b[rn+1]

        if c-1 > -1:
            if not r[c-1] == '#':
                r[c-1] += 1

        if not r[c] == '#':
            r[c] += 1

        if num_cols > c+1:
            if not r[c+1] == '#':
                r[c+1] += 1

# Get the value of a coordinate on the grid
def l(r, c, b):
    row = b[r]
    c = row[c]
    return c

#==================================================
# RUN MINESWEEPER

# create levels
level_1 =      [    ["-", "#", "-", "-", "-"],
                    ["-", "#", "-", "#", "-"],
                    ["-", "-", "-", "-", "-"],
                    ["#", "-", "#", "#", "-"],
                    ["-", "-", "-", "-", "-"]    ]

#Introduction
print('\nWelcome to MineSweeper!')
print('=============================\n')

# print level
print("\nLEVEL 1\n")
row_index = 0
for row in level_1:
    row_index += 1
    for col in row:
        print(col, end = " ")
    print()

# call function
solution = minesweeper(level_1)

# print solution
print("\nSOLUTION\n")
row_index = 0
for row in solution:
    row_index += 1
    for col in row:
        print(col, end = " ")
    print()
