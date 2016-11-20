"""This class models the tournament"""
from model.Game import Game
from model.FileHandler import FileHandler
from model.Board import Board
import os


class Tournament:
    """This class models the tournament"""

    def __init__(self):
        self.totalgames = 0
        self.humanscore = 0
        self.computerscore = 0
        self.fileHandler = FileHandler()

    @staticmethod
    def printwelcomemessage():
        """Prints the welcome message"""
        print("Welcome to the wonderful game of Duell")
        print("We are very delighted that you chose to play this game")
        print("---------------------------x---------------------------\n")

    def startgame(self):
        """Starts the game"""

        userinput = 'a'
        gamecomplete = True

        while userinput != 'y' and userinput != 'o':
            userinput = input(
                "Do you want to start a new game (Y) or open existing (O)? :: ")
            userinput = userinput.lower()

        if userinput == 'y':
            self.totalgames = self.totalgames + 1
            newgame = Game(True, None, None)
        else:
            master_list = [5, 1, 2, 6, 1, 6, 2, 1, 5]
            new_board = Board(master_list)
            computer_turn = True

            filename = "ooo"
            while not os.path.exists("./" + filename):
                filename = input(
                    "Please enter the name of the file you want to open: ")

            # Opens the file and inputs
            self.fileHandler.open_game(filename, new_board)

            # Setting the results to the class variables
            self.computerscore = self.fileHandler.get_computer_score()
            self.humanscore = self.fileHandler.get_human_score()
            computer_turn = self.fileHandler.get_is_computer()

            newgame = Game(False, new_board, computer_turn)

        gamecomplete = newgame.start()

        if gamecomplete:
            if newgame.computer_win:
                self.computerscore = self.computerscore + 1
            else:
                self.humanscore = self.humanscore + 1
        else:
            # save the current game.
            print()
