while True:
    try:
        x = int(input("Enter a number: ")) 
        print(f"You entered {x}. Great!")
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")

file = None
try:
    file = open("input.txt", 'r')
    print("The file was found")
except FileNotFoundError as error:
    print("The file was not found")
    print(error)
finally:
    if file is not None:
        file.close()
        print("The file was closed")
    else:
        print("No file to close")

num = int(input("Please enter a value greater than 10: "))
if num < 10:
    raise Exception('num was less than 10. The value of num was: {}'.format(num))
