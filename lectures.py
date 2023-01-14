num_rows = 3
num_cols = 4

# initialise a 2D list with default values
empty_grid = [[None] * num_cols for _ in range(num_rows)]

# assignn values
empty_grid[0][1] = 100

# creating and printing 2D or rectangular lists
student_scores = [  [89, 75, 98],
                    [45, 53, 65],
                    [80, 78, 82]    ]

row_index = 0
for row in student_scores:
    print(f"Term {row_index + 1}: ")
    row_index += 1
    for col in row:
        print(col, end = "% ")
    print()

# ragged list or non-rectangular list
ragged_list = [ [1, 2, 3],
                [4, 5, 6, 7, 8],
                [9, 10]           ]

rows = len(ragged_list)
for row in range(rows):
    cols = len(ragged_list[row])
    print("Row", row+1, "has", cols, "columns: ", end="")
    for col in range(cols):
        print(ragged_list[row][col], " ", end="")
    print()
