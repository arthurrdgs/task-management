#=====importing libraries===========
from datetime import date #adding a module to get the current date

#====Login Section====

#creating 2 lists the will be used to store the usernames and passwords from user.txt
username_list = []
password_list = []

#opening the user.txt file
with open('user.txt', 'r') as login_details:
    
    #using for loop to get to every line in the file
    for line in login_details:
        line = line.strip('\n').split(', ')
        username_list.append(line[0])   #appending usernames to the usernames list and passwords to the passwords list
        password_list.append(line[1]) 
        
#asking the user for the username and using a while loop to check that it matches with a username from the list above        
username = input("Enter your username: ")
while username not in username_list:
    print("Your usarname is wrong!")
    username = input("Enter your username: ")

#after getting a correct username, asking the user for a password
#and checking that it matches to the correct username by using the indexes
if username in username_list:
    correct_password = password_list[username_list.index(username)]
    password = input("Enter your password: ")
    while password != correct_password:
        print("Your password is wrong, please try again: ")
        password = input("Enter your password: ")
print("You logged in!")

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if username == 'admin':
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    s - Display statistics
    e - Exit
    :\n ''').lower()
    else:
        menu = input('''Select one of the following Options below:
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    :\n ''').lower()

    if menu == 'r':
        
        #if the username is admin, as hes the only one that can use the 'r' funciton
        if username == 'admin':
            
            #asking the user for a new username, a password and a password check
            new_username = input("Enter your username: ")
            new_password = input("Enter your password: ")
            password_check = input("Enter your password again: ")

            #using if statement to check if both passwords match and if they do, adding the new user to the user.txt file
            if new_password == password_check:
                new_user = open('user.txt', 'a')
                new_user.write(f"\n{new_username}, {new_password}")
                new_user.close()
            else:
                print("Your passwords do not match!")
        else: 
            print("Sorry only the admin can register other users.")

            
    elif menu == 'a':
        
        #asking the user to enter:
        #the assigned user, the task title and description, the due date for the task, the current date and if task is completed.
        user_assigned = input("Type the username of the person you want to assign the task: ")
        task_title = input("Enter the task title: ")
        task_description = input("Enter the task description: ")
        task_date = input("Enter the due date for the task (DD/MM/YYYY): ")
        current_date = date.today()
        
        #opening the file with the append function to add every information collected above to the tasks.txt file
        with open('tasks.txt', 'a') as a_items:
            a_items.write(f"\n{user_assigned}, {task_title}, {task_description}, {current_date}, {task_date}, No")
        
    elif menu == 'va':
   
        #opening the file and printing every line in the tasks file
        with open('tasks.txt', 'r') as tasks_file:
            
            #formating the layout using \n and \t
            for line in tasks_file:
                line = line.split(", ")
                print("\n" + "_"*80 + "\n")
                print(f"\n Assigned user:\t\t {line[0]}")
                print(f"\n Task:\t\t\t {line[1]}")
                print(f"\n Date assigned:\t\t {line[3]}")
                print(f"\n Due date:\t\t {line[4]}")
                print("\n Task complete?\t\t No")
                print(f"\n Task description:\n  {line[2]}")
                print("\n"+"_"*80)

    elif menu == 'vm':
        
        with open('tasks.txt', 'r') as user:
            for line in user:
                line = line.strip('\n').split(", ")
                if line[0] == username:
                    print("\n" + "_"*80 + "\n")
                    print(f"\n Assigned user:\t\t {line[0]}")
                    print(f"\n Task:\t\t\t {line[1]}")
                    print(f"\n Date assigned:\t\t {line[3]}")
                    print(f"\n Due date:\t\t {line[4]}")
                    print("\n Task complete?\t\t No")
                    print(f"\n Task description:\n  {line[2]}")
                    print("\n"+"_"*80)
    
    elif menu == 's':
        #checking if the username = admin as he's the only one provided with the function 's'
        if username == 'admin':
            
            #creating variables for the total number of users and tasks
            total_users = 0
            total_tasks = 0
            
            #opening the files and adding the number of users and tasks to its respectives variables
            with open('user.txt', 'r') as users_number:
                for line in users_number:
                    total_users += 1
            with open('tasks.txt', 'r') as tasks_number:
                for line in tasks_number:
                    total_tasks += 1
            print(f"The total number of users are {total_users} and the total number of tasks are {total_tasks}.")
    
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    
    else:
        print("You have made a wrong choice, Please Try again")
