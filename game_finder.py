
# Import tkinter, tkinter.messagebox and json modules.
import tkinter
import tkinter.messagebox
import json


class ProgramGUI:

    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading and reading the data from the text file and creating the user interface.
        self.main = tkinter.Tk()
        self.main.title("Game Finder")  # give title to window
        self.main.minsize(200, 500)  # set minimum size of window

        try:
            # open data.txt file in read mode
            file = open("data.txt", "r")
            # load json content from file into self.data variable
            self.data = json.load(file)
            file.close()  # close file

        except BaseException as e:
            # if exception, show message "missing/invalid file"
            tkinter.messagebox.showerror("Error", "Missing/Invalid file")
            self.main.destroy()  # destroy main window if exception
            return  # return statement to quit in clean state

        # Design GUI
        # create Frames to adjust widgets properly in GUI
        # use padding for x and y side for frames
        self.inputFrame1 = tkinter.Frame(self.main, padx=8, pady=2)
        self.inputFrame2 = tkinter.Frame(self.main, padx=8, pady=2)
        self.inputFrame3 = tkinter.Frame(self.main, padx=8, pady=2)
        self.submitFrame = tkinter.Frame(self.main, padx=8, pady=8)
        self.matchFrame = tkinter.Frame(self.main, padx=8, pady=12)
        self.resultsFrame = tkinter.Frame(self.main, padx=8, pady=2)

        # for constraints label, set text with bold and 24 size, specify other options, pack constraints label
        tkinter.Label(self.main, text='Constraints:', width=12, justify='center', font=("bold", 24),
                      fg="#aa00ff").pack()
        # number of players label, set options, pack label with side= left option
        tkinter.Label(self.inputFrame1, width=25, text='Number of players:', justify='right', font=("", 12)).pack(
            side='left')
        # Entry widget for number of players, set  width to 5, pack with side = right
        self.players = tkinter.Entry(self.inputFrame1, width=5)
        self.players.pack(side='right')

        # Time availabel label, set options, pack label with side= left option
        tkinter.Label(self.inputFrame2, width=25, text="Time available (mins):", justify='right', font=("", 12)).pack(
            side='left')
        # Entry widget for time , set  width to 5, pack with side = right
        self.time = tkinter.Entry(self.inputFrame2, width=5)
        self.time.pack(side='right')

        # age of youngest player label, set options, pack label with side= left option
        tkinter.Label(self.inputFrame3, width=25, text="Age of youngest player:", justify='right', font=("", 12)).pack(
            side='left')
        # Entry widget for age of youngest player,set  width to 5, pack with side = right
        self.age = tkinter.Entry(self.inputFrame3, width=5)
        self.age.pack(side='right')

        # pack all frames
        self.inputFrame1.pack()
        self.inputFrame2.pack()
        self.inputFrame3.pack()

        # set submit button widget, set command to findGames, it will call findGames() function
        # pack button widget
        tkinter.Button(self.submitFrame, width=10, text="Submit", justify='center', font=("bold", 16),
                       command=self.findGames).pack()
        # pack Frame for submit button
        self.submitFrame.pack()

        # matching game label, justify to center, set font and color,
        # pack the label
        tkinter.Label(self.matchFrame, width=20, text="Matching Games:", justify='center', font=("bold", 24),
                      fg="#aa00ff").pack()
        self.matchFrame.pack()  # pack frame for matching games label

        # intialize self.values as a tkinter.StringVar()
        self.value = tkinter.StringVar()
        # results label, to show matching games to user, set self.value as a textvariable
        self.results = tkinter.Label(self.resultsFrame, justify='center', font=("", 16),
                                     fg="#0000ff", textvariable=self.value)
        # set initial value of self.value
        self.value.set("No criteria submitted")
        # pack self.results  with fill= both and expand =1
        self.results.pack(fill='both', expand=1)
        # pack resultsFrame
        self.resultsFrame.pack()
        # set focus to first Entry widget (players)
        self.players.focus_set()
        # start main loop of the program's GUI
        tkinter.mainloop()

    def findGames(self):
        # This method finds and displays games matching the criteria entered by the user.
        try:
            # get values inserted by user in entry widgets, store values into local variables
            players = int(self.players.get())
            time = int(self.time.get())
            age = int(self.age.get())
        except ValueError:  # handle exception like user entered non-integer values
            # show error messagebox
            tkinter.messagebox.showerror('Error', 'Invalid criteria specified')

        else:
            str1 = ""  # initialize str1 variable with empty string
            noMatches = 0  # initialize noMatches with 0
            for game in self.data:  # for loop in self.data
                # check for games which fits into criteria
                if (players >= game['min_players']) and (players <= game['max_players']) and (
                        time >= game['duration']) and (age >= game['min_age']):
                    # append games who match the criteria to str1, put \n to append games in new line
                    str1 = str1 + "\n" + str(game['name'])
                    # increase noMatches by 1 to count total number of games who match criteria
                    noMatches = noMatches + 1
            if noMatches == 0:  # if noMatches is still 0, print no matching games
                self.value.set("No matching games")
            else:  #
                # generate temp string to print how many games match criteria out of total number of games
                temp = str(noMatches) + " out of " + str(len(self.data)) + " games matched search\n"
                # append temp variable and str1, then set it to self.value
                self.value.set(temp + str1)


# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
