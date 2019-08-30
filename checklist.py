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
    index = 0
    for list_item in checklist:
        print("√{} {}".format(index, list_item))
        index += 1

def select(function_code):
    #create item
    if function_code == "C" | function_code == "c":        
        item_index = user_input("Index Item: ")
        time.sleep(1)
        os.system("clear")
        create(user_input)
    # Read item
    elif function_code == "R" | function_code == "r":
        item_index = user_input("Index Number? ")
        #Remebering item_index must exist
        time.sleep(1)
        os.system("clear")
        read(item_index)
    #Prints items
    elif function_code == "P" | function_code == "p":
        time.sleep(1)
        os.system("clear")
        list_all_items()
    #Exits program
    elif function_code == "Q" | function_code == "q":
        time.sleep(1)
        os.system("clear")
        print("Exiting program")
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
test()

running = True
while running:
    selection = user_input(
        "Press C to add list, R to read list, and P to display list. Or Q to quite.")
    select(selection)

#ToDO!
#Add Read, update and destroy options to select func 
#Allow For user to use upper and lower case commands √
#Handle errors cuased by invalid user inputs √

#Stretch Challenges!
#clear terminal between user selections √
#***Thanks to https://www.w3resource.com/python-exercises/python-basic-exercise-99.php for python clearing help! 
#Add a function that checks and unchecks items in list 
#Display colored text in the terminal 

#And As Always
#Improve your code!!