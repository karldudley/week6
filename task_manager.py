#=====importing libraries===========
from datetime import date, datetime
import os.path
from os import path

#=====Functions=======
def reg_user():
    print("\nRegister New User\n")
    # open user file to access existing usernames
    with open("user.txt", "r") as file:
        all_users = file.read()

    # create a list of users
    user_list = all_users.split("\n")

    # create variable to control while loop
    exists = True
    
    while exists:
        # ask user for login details
        username = input("New Username:\t")

        # loop through user_list to see if username already exists
        for user in user_list:
            if username == user.split(",")[0]:
                print("That username already exists. Please try again.\n")
                exists = True
                break
            exists = False

    # ask for password details
    password = input("New Password:\t")
    password_confirm = input("Confirm New Password:\t")

    if password == password_confirm:
        # open user file to append
        with open("user.txt", "a") as file:
            file.write(username + ", " + password + "\n")
        print("\nNew user created\n")
    else:
        print("\nThe passwords did not match\n")

def add_task():
    print("\nAdd New Task\n")
    # get task details from user
    username = input("Username:\t")
    title = input("Task Title:\t")
    desc = input("Description:\t")
    today = date.today()
    assigned_date = today.strftime("%d %b %Y")
    print("Assigned:\t" + assigned_date)
    due_date = input("Due Date:\t")

    # write new task to tasks.txt
    with open("tasks.txt", "a") as file:
        file.write(username + ", " + title + ", " + desc + ", " + assigned_date + ", " + due_date + ", " + "No" + "\n")

    print("\nNew task created\n")

def view_all():
    # read the tasks file
    with open("tasks.txt", "r") as file:
        all_tasks = file.read()
    
    # create a list of tasks
    task_list = all_tasks.split("\n")

    # print number of tasks (-1 to ignore final empty line)
    print(f"\nThere are currently {len(task_list)-1} tasks assigned to all users:\n")

    # loop through list of tasks and print to screen
    for pos, task in enumerate(task_list, 1):
        # split task into each seperate detail
        deets = task.split(', ')
        
        # break for loop if we reached the last line of the file
        if len(deets) <= 1:
            break

        # print in a readable format
        print(f'——————————[{pos}]——————————\n')
        print("Task:\t\t" + deets[1])
        print("Assigned to:\t" + deets[0])
        print("Date assigned:\t" + deets[3])
        print("Due Date:\t" + deets[4])
        print("Task Complete?\t" + deets[5])
        print("Description:\t" + deets[2])
        print("—————————————————————————\n")

def view_mine():
    tasks = False
    edit = False
    edit_data = ""
    choice = 0

    # read the tasks file and create a list of tasks
    with open("tasks.txt", "r") as file:
        task_list = file.readlines()

    # loop through list of tasks and print to screen
    for pos, task in enumerate(task_list, 1):
        # split task into each seperate detail
        deets = task.split(', ')
        
        # break for loop if we reached the last line of the file
        if len(deets) <= 1:
            break

        # skip output if it's not for this user
        if deets[0] != username:
            continue

        # print in a readable format
        tasks = True
        print(f'——————————[{pos}]——————————\n')
        print("Task:\t\t" + deets[1])
        print("Assigned to:\t" + deets[0])
        print("Date assigned:\t" + deets[3])
        print("Due Date:\t" + deets[4])
        print("Task Complete?\t" + deets[5])
        print("Description:\t" + deets[2])
        print("—————————————————————————\n")
    
    while tasks:
        choice = int(input("Select Task Number (0 to return to menu):\t"))-1
        if choice == -1:
            print("Returning to main menu...\n")
            break
        elif choice >= len(task_list) or choice < 0:
            print("Please choose a correct task number.\n")
            continue
        edit_data = task_list[choice]
        edit = True
        break

    while edit:
        output = f'——————————[SELECT AN OPTION]——————————\n'
        output += '1 - Edit due date \n'
        output += '2 - Edit user assigned \n'
        output += '3 - Mark as completed \n'
        output += '——————————————————————————————————————\n'

        option = int(input(output))

        if option <= 0 or choice > 3:
            print('You have selected an invalid option, try again.')
            continue

        if option == 2:
            split_data = edit_data.split(", ")
            if split_data[-1] != 'Yes\n':
                print(f"Current Assigned User:\t{split_data[0]}")
                split_data[0] = input("New Assigned User:\t")
                new_data = ", ".join(split_data)
                task_list[choice] = new_data
                print("\nNew user successfully assigned!\n")
            else:
                print("\nYou can't update a task that is complete!\n")
                break
        elif option == 1:
            split_data = edit_data.split(", ")
            if split_data[-1] != 'Yes\n':
                print(f"Current Due Date:\t{split_data[4]}")
                split_data[4] = input("New Due Date:\t\t")
                new_data = ", ".join(split_data)
                task_list[choice] = new_data
                print("\nDue Date successfully updated!\n")
            else:
                print("\nYou can't update a task that is complete!\n")
                break
        elif option == 3:
            split_data = edit_data.split(", ")
            split_data[-1] = 'Yes\n' # -1 because we want the end piece of data
            new_data = ", ".join(split_data)
            task_list[choice] = new_data
            print("\nTask successfully completed!\n")

        # write the updated tasks to file
        with open("tasks.txt", "w") as file:
            for task in task_list:
                file.write(task)
        break

    if not tasks:
        print("\nYou currently have no assigned tasks!\n")

def gen_reports():
    # read the tasks file and put in a list
    with open("tasks.txt", "r") as file:
        task_list = file.readlines()
    
    # loop through task_list to get data needed for reports
    complete = 0
    incomplete = 0
    late = 0
    for task in task_list:
        split_data = task.split(", ")
        # get number of complete and incomplete tasks
        if (split_data[-1] == "Yes\n"):
            complete += 1
        else:
            incomplete += 1

        # get overdue, incomplete tasks
        today = datetime.today()
        due_date_string = split_data[4]
        due_date_object = datetime.strptime(due_date_string, '%d %b %Y')
        completed = split_data[-1].strip("\n")
        if today > due_date_object and completed == "No":
            late += 1

    # write task data to the report
    with open("task_overview.txt", "w") as task_overview:
        # number of tasks
        task_overview.write(f"Total number of tasks:\t{len(task_list)}\n")

        # number of complete tasks
        task_overview.write(f"Completed tasks:      \t{str(complete)}\n")

        # number of incomplete tasks
        task_overview.write(f"Incomplete tasks:     \t{str(incomplete)}\n")

        # number of late tasks that are incomplete
        task_overview.write(f"Overdue tasks:        \t{str(late)}\n")

        # percentage of incomplete tasks
        task_overview.write(f"% Incomplete tasks:   \t{str(incomplete/len(task_list)*100)}%\n")

        # percentage of overdue tasks
        task_overview.write(f"% Overdue tasks:      \t{str(late/len(task_list)*100)}%\n")

    
    # read the user file and put in a list
    with open("user.txt", "r") as file:
        user_list = file.readlines()
    
    # write user data to the report
    with open("user_overview.txt", "w") as user_overview:
        # number of users
        user_overview.write(f"Total number of users:\t{len(user_list)}\n")

        # number of tasks
        user_overview.write(f"Total number of tasks:\t{len(task_list)}\n")
        # user_overview.write(f"User\tTasks\t% Assigned\t% Complete\t% Incomplete\t% Overdue\n")
        for user in user_list:
            tasks = 0
            completed = 0
            late = 0
            username = ""
            no_tasks = []

            for task in task_list:
                username = user.split(", ")[0]
                if username == task.split(", ")[0]:
                    tasks += 1

                # get completed tasks'
                if task.split(", ")[-1].strip("\n") == "Yes":
                    completed += 1

                # find out if overdue
                today = datetime.today()
                due_date_string = task.split(", ")[4]
                due_date_object = datetime.strptime(due_date_string, '%d %b %Y')
                if today > due_date_object and task.split(", ")[-1].strip("\n") == "Yes":
                    late += 1
            
            if tasks > 0:
                output = '---------------------------------------\n'
                output += f'User:        \t\t{username}\n'
                output += f'Tasks:       \t\t{tasks}\n'
                output += f'% Assigned:  \t\t{round(tasks/len(task_list)*100,2)}\n'
                output += f'% Complete:  \t\t{round(completed/tasks*100,2)}\n'
                output += f'% Incomplete:\t\t{round((tasks-completed)/tasks*100,2)}\n'
                output += f'% Overdue:   \t\t{round(late/tasks*100,2)}\n'

                user_overview.write(output)
            else:
                user_overview.write('---------------------------------------\n')
                user_overview.write(f"{username} has no assigned tasks.\n")
        user_overview.write('---------------------------------------\n')

    print("\nReports successfully generated!\n")

def view_stats():
    print("\n\tTask Manager Statistics\n")

    # if file exists, use to show stats, or else run reports first
    if path.exists("task_overview.txt") and path.exists("user_overview.txt"):
        print("Reports exist! Printing data...\n")

        # read the tasks file
        with open("task_overview.txt", "r") as file:
            task_list = file.readlines()

        print("\n\t\tTASKS OVERVIEW\n")
        for task in task_list:
            print(task)

        # read the user file
        with open("user_overview.txt", "r") as file:
            user_list = file.readlines()

        print("\n\t\tUSERS OVERVIEW\n")
        for user in user_list:
            print(user)
    else:
        print("Reports do not exist! Generating reports and printing data...\n")
        gen_reports()
        # read the tasks file
        with open("task_overview.txt", "r") as file:
            task_list = file.readlines()

        print("\n\t\tTASKS OVERVIEW\n")
        for task in task_list:
            print(task)

        # read the user file
        with open("user_overview.txt", "r") as file:
            user_list = file.readlines()

        print("\n\t\tUSERS OVERVIEW\n")
        for user in user_list:
            print(user)

#====Login Section====
print("Welcome to Task Manager\n")

# open user file so it can be read
user_file = open('user.txt', 'r')
all_users = user_file.read()
user_file.close()

# create a list of users containing username and password
users_list = all_users.split("\n")

# variable used to break while loop when correct details entered
breaker = False     

# loop until correct details entered
while True:
    # ask user for login details
    username = input("Username:\t")
    password = input("Password:\t")

    # check entered username and password against user list
    for user in users_list:
        deets = user.split(', ')
        if username == deets[0] and password == deets[1]:
            print("\nSuccessfully logged in!\n")
            breaker = True;
            break
    
    if breaker:
        break

    # give error message to say wrong details entered after for loop
    print("\nWrong credentials entered. Please try again...\n")

#====Main Menu====
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    
    if username == "admin":
        menu = input('''Select one of the following options below:

r - Register a user
a - Add a task
va - View all tasks
vm - View my tasks
gr - Generate reports
ds - View stats
e - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following options below:

a - Add a task
va - View all tasks
vm - View my tasks
e - Exit
: ''').lower()

    if menu == 'r' and username == "admin":
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()
    elif menu == 'gr' and username == "admin":
        gen_reports()
    elif menu == 'ds' and username == "admin":
        view_stats()
    elif menu == 'e':
        print('\nGoodbye!!!\n')
        exit()
    else:
        print("\nYou have made a wrong choice. Please try again...\n")
