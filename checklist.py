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
def select(fuction_code):
    #create item
    if function_code == "C":
        item_index = user_input("Index Item: ")
        create(input_item)
    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number? ")
        #Remebering item_index must exist
        read(item_index)
    #Prints items
    elif function_code == "P":
        list_all_items()
    #catch all
    else:
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