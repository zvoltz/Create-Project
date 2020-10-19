import PySimpleGUI as sg
import random
from nltk.corpus import words
class TicTacToe():

    def checkwin(self, grid):
        for i in range(3):
            if grid[i] == grid[i+3] == grid[i+6] and grid[i] != " ":
                return grid[i]
        for j in range(0, 6, 3):
            if grid[j] == grid[j+1] == grid[j+2] and grid[j] != " ":
                return grid[j]
        if grid[0] == grid[4] == grid[8] and grid[0] != " " or \
                grid[2] == grid[4] == grid[6] and grid[2] != " ":
            return grid[4]
        for i in range(9):
            if(grid[i]==" "):
                return False
        else:
            return "Tie"

    def buttonMethod(self,button_num,grid,turn):
        if turn ==0 and grid[button_num]==" ":
            grid[button_num]="X"
            return 1
        elif turn ==1 and grid[button_num]==" ":
            grid[button_num]="O"
            return 0

    def __init__(self):
        grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        turn=0
        stop=True

        layout = [  [sg.Button(" ",key="button_0"),
            sg.Button(" ", key="button_1"), sg.Button(" ", key="button_2") ],
                [sg.Button(" ", key="button_3"), sg.Button(" ", key="button_4"),
                sg.Button(" ", key="button_5")],
                [sg.Button(" ", key="button_6"), sg.Button(" ", key="button_7"),
                sg.Button(" ", key="button_8")]]

        window2 = sg.Window("TicTactoe", layout)

        while stop:
            event, values = window2.read()
            if event in("button_0"):
                turn =(self.buttonMethod(0,grid,turn))
                window2["button_0"].update(text=grid[0])
            if event in("button_1"):
                turn=(self.buttonMethod(1,grid,turn))
                window2["button_1"].update(text=grid[1])
            if event in("button_2"):
                turn=(self.buttonMethod(2,grid,turn))
                window2["button_2"].update(text=grid[2])
            if event in("button_3"):
                turn=(self.buttonMethod(3,grid,turn))
                window2["button_3"].update(text=grid[3])
            if event in("button_4"):
                turn=(self.buttonMethod(4,grid,turn))
                window2["button_4"].update(text=grid[4])
            if event in("button_5"):
                turn=(self.buttonMethod(5,grid,turn))
                window2["button_5"].update(text=grid[5])
            if event in("button_6"):
                turn=(self.buttonMethod(6,grid,turn))
                window2["button_6"].update(text=grid[6])
            if event in("button_7"):
                turn=(self.buttonMethod(7,grid,turn))
                window2["button_7"].update(text=grid[7])
            if event in("button_8"):
                turn=(self.buttonMethod(8,grid,turn))
                window2["button_8"].update(text=grid[8])
            if(self.checkwin(grid)!=False):
                stop=False
                window2.close()
                if(self.checkwin(grid)=="Tie"):
                    if(sg.popup_yes_no("Tie Game! Want to play again?")=="Yes"):
                        self.__init__()
                elif(sg.popup_yes_no(self.checkwin(grid) + " wins! Want to play again?")=="Yes"):
                    self.__init__()

class GuessNumber():
    def start(self):
        layout = [ [sg.Text("Pick a difficulty:")],
                [sg.Text("Easy = 1-50 Medium = 1-100 Hard = 1-1,000 Insane = 1-100,000")],
                [sg.Button("Easy"),sg.Button("Medium"),sg.Button("Hard"),sg.Button("Insane")]]
        window3 = sg.Window("Pick a difficulty", layout)
        while True:
            event, values = window3.read()
            if event in ("Easy"):
                window3.close()
                return(random.randrange(1,51))
            if event in ("Medium"):
                window3.close()
                return(random.randrange(1,101))
            if event in ("Hard"):
                window3.close()
                return(random.randrange(1,1001))
            if event in ("Insane"):
                window3.close()
                return(random.randrange(1,100001))

    def __init__(self):
        num = self.start()
        count=0
        stop=True
        guesses=["Guesses:"]

        layout = [[sg.Text("Try to guess the number I'm thinking of: ", key="AboveText")],
                [sg.Text("Guesses:", key="Guess", size=(50,1))],
                [sg.InputText()],
                [sg.Button("Submit",bind_return_key=True)]]
        window4 = sg.Window("Guess my number", layout)
        while stop:
            event, values = window4.read()
            if event in ("Submit"):
                guesses.append(values[0])
        #Yes, it intentionally cuts off and stops showing the new guesses after a certain amount, I didn't want the window to expand a lot unnecessarily
                window4["Guess"].update(" ".join(guesses))
                if(num>int(values[0])):
                    window4["AboveText"].update("Too low! Try again")
                    count+=1
                elif(num<int(values[0])):
                    window4["AboveText"].update("Too high! Try again")
                    count+=1
                else:
                    stop=False
                    window4.close()
                    if(sg.popup_yes_no("You win! It took you " + str(count+1) + " tries. Do you want to play again to beat your score?")=="Yes"):
                        self.__init__()

class Hangman():
    def check_win(self, word):
        for x in word:
            if x == "_":
                return False
        return True

    def __init__(self):
        word_list = words.words()
        # according to nltk, there are 236736
        hiddenWord = word_list[random.randrange(0, 236735)].lower()
        blanks = []
        guesses = ["Guesses:"]
        imageName = ["hangman", 0, ".png"]
        stop=True
        for x in hiddenWord:
            blanks.append("_")
        layout = [[sg.Text("Guess my word!", key="AboveText")],
                [sg.Text(" ".join(blanks), key="Underscores")],
                [sg.Text("Guesses:", key="Guess", size=(78,1))],
                [sg.InputText()],
                [sg.Button("Submit",bind_return_key=True)],
                [sg.Image(filename=r"hangman0.png", key="image")]]
        window5 = sg.Window("Hangman", layout)
        while stop:
            event, values=window5.read()
            count=0
            runWrong = True
            for x in hiddenWord:
                if values[0]==x:
                    blanks[count]=x
                    window5["Underscores"].update(" ".join(blanks))
                    if(self.check_win(blanks)):
                        window5.close()
                        if(sg.popup_yes_no("You win! The word was " + hiddenWord + ". Do you want to play again?")=="Yes"):
                            self.__init__()
                        stop=False
                    runWrong = False
                count+=1
            for i in guesses:
                if values[0]==i:
                    break
                else:
                    guesses.append(values[0])
                    window5["Guess"].update(" ".join(guesses))
                    break
            if(runWrong):
                imageName[1]+=1
                if(imageName[1]==7):
                    window5.close()
                    if(sg.popup_yes_no("You lose! The word was " + hiddenWord + ". Do you want to play again?")=="Yes"):
                        self.__init__()
                    stop=False
                if(stop):
                    fileName = imageName[0] + str(imageName[1]) + imageName[2]
                    window5["image"].update(filename=fileName)


class Gameshub():
    layout = [  [sg.Text('Pick a game!')],
            [sg.Button("Tic Tac Toe") ],
            [sg.Button("Guess my number")],
            [sg.Button("Hangman")]]

    window = sg.Window("Games", layout)

    while True:
        event, values = window.read()
        if event in ("Tic Tac Toe"):
            TicTacToe()
        if event in ("Guess my number"):
            GuessNumber()
        if event in("Hangman"):
            Hangman()
    window.close()

Gameshub()
