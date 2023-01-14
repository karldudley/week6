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
except:
    print("The file was not found")
finally:
    if file is not None:
        file.close()
        print("The file was closed")
    else:
        print("No file to close")
