import random, time, copy, os

# NEED TO FINISH
# https://replit.com/talk/learn/How-to-program-MineSweeper-in-Python-fully-explained-in-depth-tutorial/9397

#Introduction
print('\nWelcome to MineSweeper!')
print('=============================\n')

#Sets up the game.
def reset():
    #The solution grid.
    b = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    print('''
MAIN MENU
=========

-> For instructions on how to play, type 'I'
-> To play immediately, type 'P'
''')

    choice = input('Type here: ').upper()

    if choice == 'I':
        os.system('cls')
        print("Instructions. TO DO\n")
        #Prints instructions.
        # print(open('instructions.txt', 'r').read())

        input('Press [enter] when ready to play. ')
        
    elif choice != 'P':
        os.system('cls')
        reset()

    for n in range (0, 10):
        placeBomb(b)

    # print
    print()
    row_index = 0
    for row in b:
        row_index += 1
        for col in row:
            print(col, end = " ")
        print()

    for r in range (0, 9):
        for c in range (0, 9):
            value = l(r, c, b)
            if value == '*':
                updateValues(r, c, b)
    # print
    print()
    row_index = 0
    for row in b:
        row_index += 1
        for col in row:
            print(col, end = " ")
        print()

#Places a bomb in a random location.
def placeBomb(b):
    r = random.randint(0, 8)
    c = random.randint(0, 8)
    #Checks if there's a bomb in the randomly generated location. If not, it puts one there. If there is, it requests a new location to try.
    currentRow = b[r]
    if not currentRow[c] == '*':
        currentRow[c] = '*'
    else:
        placeBomb(b)

#Adds 1 to all of the squares around a bomb.
def updateValues(rn, c, b):

    #Row above.
    if rn-1 > -1:
        r = b[rn-1]
        
        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 9 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1

    #Same row.    
    r = b[rn]

    if c-1 > -1:
        if not r[c-1] == '*':
            r[c-1] += 1

    if 9 > c+1:
        if not r[c+1] == '*':
            r[c+1] += 1

    #Row below.
    if 9 > rn+1:
        r = b[rn+1]

        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 9 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1

#Gets the value of a coordinate on the grid.
def l(r, c, b):
    return b[r][c]

reset()
