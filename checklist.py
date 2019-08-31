from termcolor import colored
import os
import time

# Create our Checklist
checklist = []

# Define Functions
def create(item):
    # Create item code here
    checklist.append(item)

def read(index):
    # Read code here
    return checklist[index]

def update(index, item):
    # Update code here
    index = colored('green')
    item = colored('green')
    checklist[index] = item 

def destroy(index):
    # Destroy code here
    checklist.pop(index)

def list_all_items():
    # Code to list all items in list
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    #Adds marked items as complete
    index = colored('blue')
    print(f"√{index}")

def mark_incomplete(index):
    #Adds marks items incomplete
    print(f"{index}")

def select(function_code):
    #create item
    if function_code == "C" or function_code == "c":        
        item_index = user_input("Index Item: ")
        time.sleep(1)
        os.system("clear")
        create(user_input)
    #Updates item
    if function_code == "U" or function_code == "u":
        item_index = user_input("Index Item: ")
        new_item = user_input("New Item: ")
        time.sleep(1)
        os.system("clear")
        update(item_index, new_item)
    #Destroy items
    elif function_code == "D" or function_code == "d":
        item_index = user_input("Index Number? ")
        time.sleep(1)
        os.system("clear")
        checklist.pop(item_index)
    # Read item
    elif function_code == "R" or function_code == "r":
        item_index = user_input("Index Number? ")
        #Remebering item_index must exist
        time.sleep(1)
        os.system("clear")
        read(item_index)
    #Prints items
    elif function_code == "P" or function_code == "p":
        time.sleep(1)
        os.system("clear")
        list_all_items()
    #Marks Complete
    elif function_code == "X" or function_code == "x":
        item_index = user_input("Index Number? ")
        time.sleep(1)
        os.system("clear")
        mark_completed(item_index)
    #Marks Incomplete
    elif function_code == "Z" or function_code == "z":
        item_index = user_input("Index Number? ")
        time.sleep(1)
        os.system("clear")
        mark_incomplete(item_index)
    #Exits program
    elif function_code == "Q" or function_code == "q":
        _ = "Exiting Program"
        _ = colored('red')
        time.sleep(1)
        os.system("clear")
        print(_)
        running = False
    #catch all
    else:
        time.sleep(1)
        os.system("clear")
        print("Error, Unknown command" + user_input)

def user_input(prompt):
    #displays message in terminal for user reply
    user_input = input(prompt)
    return user_input

def test():
    # Your tests here
    create("purple sox")
    create("red cloak")
    print(read(0))
    print(read(1))
    update(0, "purple socks")
    destroy(1)
    print(read(0))
    print(read(1))
    list_all_items()

#runs test
#test()

running = True
while running:
    selection = user_input(
        "Press C to add list, U to update list, D to remove list, X to mark done, and Z to mark incomplete. You can also use R to read, P to display list or Q to quite. ")
    select(selection)

#ToDO!
#Allow For user to use upper and lower case commands √
#Handle errors cuased by invalid user inputs √

#Stretch Challenges!
#clear terminal between user selections √
#***Thanks to https://www.w3resource.com/python-exercises/python-basic-exercise-99.php for python clearing help! 
#Add a function that checks and unchecks items in list √
#Display colored text in the terminal √ ***Thx Tanner for the help!