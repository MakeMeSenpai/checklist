import os
import time

# Create our Checklist
checklist = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Purple"]
    #clothes: ["Pants", "Shirt", "L-sock", "R-sock", "L-shoe", "R-shoe", "Cloak"] 

# Define Functions
def create(item):
    # Create item code here
    checklist.append(item)

def read(index):
    # Read code here
    return checklist[index]

def update(index, item):
    # Update code here
    #index = colored('green')
    #item = colored('green')
    checklist[int(index)] = item 

def destroy(index):
    # Destroy code here
    checklist.pop(int(index))

def list_all_items():
    # Code to list all items in list
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    #Adds marked items as complete
    #index = colored('blue')
    print(f"√{checklist[int(index)]}", 'blue')

def mark_incomplete(index):
    #Adds marks items incomplete
    print(f"{checklist[int(index)]}")

def select(function_code):
    #create item
    if function_code == "C" or function_code == "c":       
        item_index = user_input("Create Item: ")
        time.sleep(1)
        os.system("clear")
        create(user_input)
        return True
    #Updates item
    if function_code == "U" or function_code == "u":
        item_index = user_input("Index Item: ")
        new_item = user_input("New Item: ")
        time.sleep(1)
        os.system("clear")
        update(item_index, new_item)
        return True
    #Destroy items
    elif function_code == "D" or function_code == "d":
        item_index = user_input("Index Number? ")
        time.sleep(1)
        os.system("clear")
        checklist.pop(item_index)
        return True
    # Read item
    elif function_code == "R" or function_code == "r":
        item_index = user_input("Index Number? ")
        #Remebering item_index must exist
        time.sleep(1)
        os.system("clear")
        read(item_index)
        return True
    #Prints items
    elif function_code == "P" or function_code == "p":
        time.sleep(1)
        os.system("clear")
        list_all_items()
        return True
    #Marks Complete
    elif function_code == "X" or function_code == "x":
        item_index = user_input("Index Number? ")
        time.sleep(1)
        os.system("clear")
        mark_completed(item_index)
        return True
    #Marks Incomplete
    elif function_code == "Z" or function_code == "z":
        item_index = user_input("Index Number? ")
        time.sleep(1)
        os.system("clear")
        mark_incomplete(item_index)
        return True
    #Exits program
    elif function_code == "Q" or function_code == "q":
        _ = "\033[31mExiting Program...\033[0m"
        time.sleep(1)
        os.system("clear")
        print(_) #escape code
        return False
    #catch all
    else:
        os.system("clear")
        print(user_input)

def user_input(prompt):
    #displays message in terminal for user reply
    user_input = input(prompt)
    return user_input
running = True
while running:
    selection = user_input(
        "Press C to add list, U to update list, D to remove list, X to mark done, and Z to mark incomplete. You can also use R to read, P to display list or Q to quite. ")
    running = select(selection)

#ToDO!
#Allow For user to use upper and lower case commands √
#Handle errors cuased by invalid user inputs √

#Stretch Challenges!
#clear terminal between user selections √
#***Thanks to https://www.w3resource.com/python-exercises/python-basic-exercise-99.php for python clearing help! 
#Add a function that checks and unchecks items in list √
#Display colored text in the terminal √ ***Thx Tanner for the help!

#Debug
#Colors are being interpreted as strings
#checklist is printing "0 <function user_input at 0x100df8dd0>" instead of "0 <created_item>" √
#Q does not quite program due to var running being out of scope √