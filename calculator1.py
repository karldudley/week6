#Introduction
print('\nWelcome to Calculator!')
print('=============================\n')

# get user input, values and operator
# first number
while True:
    try:
        num1 = int(input("Enter your first number:\t\t")) 
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")

# second number
while True:
    try:
        num2 = int(input("Enter your second number:\t\t")) 
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")

# operator
while True:
    operator = input("Enter the operator (+, -, *, /):\t")
    if operator == "+":
        answer = num1 + num2
        break
    elif operator == "-":
        answer = num1 - num2
        break
    elif operator == "*":
        answer = num1 * num2
        break
    elif operator == "/":
        # deal with divide by zero error
        if num2 == 0:
            print("You can not divide by zero, please choose another operator")
            continue
        else:
            answer = num1 / num2
            break
    else:
        print("You entered an incorrect operator, please try again")

# print result and write to file as append. File created automatically if it doesn't exist
result = f"{num1} {operator} {num2} = {round(answer,2)}"
print(result)
with open("calculator_history.txt", "a") as file:
    file.write(result+"\n")

