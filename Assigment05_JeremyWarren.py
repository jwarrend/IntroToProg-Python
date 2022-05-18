# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <YOUR NAME HERE>,<DATE>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"
objFile = None  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
# objFile= open(strFile, "w")
dicRow = {"Task": "Mow", "Priority": "Medium"}
lstTable = [dicRow]

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        for row in lstTable:
            objFile = (strFile, "r")
            print(row["Task"] + "," + row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strTask = input("Input Task: ")
        strPriority = input("Input Priority: ")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove an item from the list/Table
    elif strChoice.strip() == '3':
        removeTask = input("Task to Remove: ")
        for row in lstTable:
            if row["Task"].lower() == removeTask.lower():
                lstTable.remove(row)
                print("row removed")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        objFile.write(strTask + "," + strPriority + '\n')
        objFile.close()
        print("Data has been saved")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input('Thank You')
        break  # and Exit the program
