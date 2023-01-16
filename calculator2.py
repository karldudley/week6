# FUNCTIONS =======================
def manual_entry():
    # list to hold values and operator to pass to function
    values = []

    # get user input, values and operator
    # first number
    while True:
        try:
            num1 = int(input("\nEnter your first number:\t\t"))
            values.append(num1)
            break
        except ValueError:
            print("Oops! That was not a valid number. Try again...")

    # second number
    while True:
        try:
            num2 = int(input("Enter your second number:\t\t"))
            values.append(num2)
            break
        except ValueError:
            print("Oops! That was not a valid number. Try again...")

    # operator
    while True:
        operator = input("Enter the operator (+, -, *, /):\t")
        if operator == "+" or operator == "-" or operator == "*" or operator == "/":
            values.append(operator)
            break
        else:
            print("You entered an incorrect operator, please try again...")

    # print result and write to file as append. File created automatically if it doesn't exist
    file_out_print(do_calculation(values))

def file_entry():
    # ask user for the filename
    user_file = input("\nEnter filename you want to read:\t")
    file = None
    try:
        # open file
        file = open(user_file, 'r')
        print("\nFile found. Calculating...\n")

        # put the sums in a list
        sums_list = file.readlines()

        # loop through list of tasks and print to screen
        for pos, sums in enumerate(sums_list, 1):
            # split task into each seperate detail
            values = sums.strip("\n").split(',')
            print(f"--------- {pos} ----------")
            file_out_print(do_calculation(values))

        # close file
        if file is not None:
            file.close()
    except FileNotFoundError as error:
        print("\n"+str(error)+"\n")
        print("Returning to main menu...\n")

def file_out_print(result):
    if result == -1:
        print("\n"+"This line contained an incorrect operator. Please check file."+"\n")
    else:
        print("\n"+result+"\n")
        with open("calculator_history.txt", "a") as file:
            file.write(result+"\n")

def do_calculation(values):
    num1 = int(values[0])
    num2 = int(values[1])
    operator = values[2]

    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2
    elif operator == "/":
        answer = num1 / num2
    else:
        return -1

    return f"{num1} {operator} {num2} = {round(answer,2)}"

# PROGRAM START =======================
#Introduction
print('\nWelcome to Calculator!')
print('=============================\n')

while True:
    choice = input('''Select one of the following options below:

r - Read equations from a new text file
m - Manually enter numbers and operator
e - Exit Calculator
: ''').lower()

    if choice == 'r':
        file_entry()
    elif choice == 'm':
        manual_entry()
    elif choice == 'e':
        print('\nGoodbye!!!\n')
        exit()
    else:
        print("\nYou have made a wrong choice. Please try again...\n")
