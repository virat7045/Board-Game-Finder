
# Import the json module to allow read and write data in JSON format.
import json


# This function repeatedly prompts for input until an integer is entered.
def inputInt(prompt):
    while True:  # infinite loop
        try:
            # ask user to give input, convert input to integer, store it in userInput
            userInput = int(input(prompt))
            if userInput > 0:  # minimum value is 1
                break
            else:
                print("Invalid input, minimum accepted number is 1 ")
        except ValueError as v:
            print("Invalid input, numbers only accepted ")
    return userInput # return user input


# This function repeatedly prompts for input until something other than whitespace is entered.
def inputSomething(prompt):
    while True:  # infinite loop
        userInput = input(prompt)  # ask user for input
        if len(userInput.strip()) > 0:  # strip user input, length should be greater than 0
            break
        else:
            print("Invalid input ")
    return str(userInput)  # return user input as a string


# This function opens "data.txt" in write mode and writes the data to it in JSON format.
def saveData(dataList):
    try:
        file = open("data.txt", "w")  # open file in write modes
        json.dump(dataList, file, indent=4)  # dump dataList into file
        file.close()  # close file
    except BaseException as e:  # handle exception and show error message
        print("Error while Saving data.")


# open data.txt Json file in read mode, load file content into data variable
try:
    file = open("data.txt", "r")
    data = json.load(file)
    file.close()  # close file

# if any exception, set data variable as a empty list
except BaseException as e:
    data = []  # empty list

# Print welcome message, then enter the endless loop which prompts the user for a choice.
print('Welcome to the Game Finder Admin Program.')
while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower()  # convert input to lower case

    if choice == 'a':  # if user choose 'add'
        # call inputSomething function to ask user to input, name of game
        name = inputSomething("Name of Game: ")
        # call inputInt function to ask user to input, minimum players, maximum players, duration and age
        minPlayers = inputInt("Minimum number of players: ")
        maxPlayers = inputInt("Maximum number of players: ")
        duration = inputInt("Average duration of game in minutes: ")
        minAge = inputInt("Minimum recommended player age: ")

        # temp variable to make dictionary of all user inputs with appropriate keys
        temp = {'name': name,
                'min_players': minPlayers,
                'max_players': maxPlayers,
                'duration': duration,
                'min_age': minAge}
        # append dictionary to data variable
        data.append(temp)
        # call saveData function to save updated data into data.txt file
        saveData(data)


    elif choice == 'l':  # if user choose 'list'
        # List the current games.
        if len(data) > 0:  # check if data variable is empty or not
            print("List of Games:")
            for index, game in enumerate(data):  # loop in data variable
                # add 1 in index and then print index and name
                print("\t" + str(index + 1) + ") " + game['name'])
        else:  # if data is empty, print no games saved
            print("There are no Games Saved")


    elif choice == 's':  # if user choose 'search'
        # Search the current games.
        if len(data) > 0:  # check if data variable is empty or not
            # ask user for what game to search with inputSomething function
            searchTerm = inputSomething("Type a game name to search for: ").lower()
            print("Search results:")
            resultsFound = 0  # initialize resultsFound as 0
            for index, game in enumerate(data):  # loop in data variable
                # use find to search for substring which match data in game
                if str(game['name']).find(searchTerm) >= 0:
                    # add 1 in index and then print index and game name if match
                    print("\t" + str(index + 1) + ") " + game['name'])
                    resultsFound = 1  # increase resultsFound by 1
            if resultsFound == 0:  # if value of resultsFound is not changed, print no games found
                print("\tNo matching games found.")
        else:  # if data is empty, print no games saved
            print("There are no Games Saved")


    elif choice == 'v':  # if user choose 'view'
        # View a game.
        if len(data) > 0:  # check if data variable is empty or not
            # call inputInt function to get user input for viewIndex
            # decrease viewIndex by 1
            viewIndex = inputInt("Game number to view: ") - 1
            if len(data) > viewIndex:  # check if viewIndex is less than length of data variable
                print(data[viewIndex]['name'])  # print game name
                # print minimum and maximum players, duration and minimum age for specified index
                print(
                    "\tPlayers: " + str(data[viewIndex]['min_players']) + " - " + str(data[viewIndex]['max_players']))
                print("\tDuration: " + str(data[viewIndex]['duration']) + " minutes")
                print("\tMinimum age: " + str(data[viewIndex]['min_age']))
            else:  # if viewIndex out bounds data length, print invalid index number
                print("Invalid index number")
        else:  # if data is empty, print no games saved
            print("There are no Games Saved")


    elif choice == 'd':  # if user choose 'delete'
        # Delete a game.
        if len(data) > 0:  # check if data variable is empty or not
            # call inputInt function to get user input for delete index
            # decrease deleteIndex by 1
            deleteIndex = inputInt("Game number to delete: ") - 1
            if len(data) > deleteIndex:  # check if deleteIndex is less than length of data variable
                del data[deleteIndex]  # del data at specified index
                # call saveData function to save updated data into data.txt file
                saveData(data)
                print("Game deleted.")
            else:  # if deleteIndex out bounds data length, print invalid index number
                print("Invalid index number")
        else:  # if data is empty, print no games saved
            print("There are no Games Saved")


    elif choice == 'q':  # if user choose to 'quit'
        # Quit the program.
        print("Goodbye!")  # print 'Goodbye!' message
        break  # break the loop to get outside of while loop


    else:  # if user enters invalid input
        # Print "invalid choice" message.
        print("Invalid choice")
