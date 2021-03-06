"""
Name:  Sujil Maharjan                                    
Project : Project 1, Duell game                          
Class : Organization of Programming Language(CMPS 366-01)
Date : 10-5-2016                                         
"""
from model.Game import Game
from model.FileHandler import FileHandler
from model.Board import Board
import os


class Tournament:
    """
    Function Name: Tournament
    Purpose: Default Constructor

    Parameters: None

    Return Value: none.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    def __init__(self):
        self.totalgames = 0
        self.humanscore = 0
        self.computerscore = 0
        self.file_handler = FileHandler()

    """
    Function Name: printwelcomemessage()
    Purpose: Prints the welcome message

    Parameters: None

    Return Value: none.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    @staticmethod
    def printwelcomemessage():
        """Prints the welcome message"""
        print("Welcome to the wonderful game of Duell")
        print("We are very delighted that you chose to play this game")
        print("---------------------------x---------------------------\n")

    """
    Function Name: startgame
    Purpose: Starts the tournament

    Parameters: none

    Return Value: none.

    Local Variables: 
        userinput, a character. It holds the user input for opening a game or starting a new one
        gamecomplete, a boolean. It determines if the game is completed or not 
        new_board, a Board object. It is a board if a file is opened
        filename, a string. It holds the name of the file 
        newgame, a Game object. It starts a game and holds all the information of one instance of the game 

    Algorithm: None.

    Assistance Received: none
    """
    def startgame(self):
        """Starts the game"""

        userinput = 'a'
        gamecomplete = True

        userinput = input(
            "Do you want to start a new game (Y) or open existing (O)? :: ")
        userinput = userinput.lower()

        while userinput == 'y' or userinput == 'o':
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

                    if not os.path.exists("./"+ filename):
                        print("The requested file is not found. Please enter again.")

                # Opens the file and inputs
                self.file_handler.open_game(filename, new_board)

                # Setting the results to the class variables
                self.computerscore = self.file_handler.get_computer_score()
                self.humanscore = self.file_handler.get_human_score()
                computer_turn = self.file_handler.get_is_computer()

                newgame = Game(False, new_board, computer_turn)

            gamecomplete = newgame.start()

            if gamecomplete:
                if newgame.computer_win:
                    self.computerscore = self.computerscore + 1
                else:
                    self.humanscore = self.humanscore + 1

                userinput = "a"
                while userinput != 'y' and userinput != 'n':
                    userinput = input(
                        "Do you want to start another round?(Y/N) :: ")
                    userinput = userinput.lower()

                print("\nThank you for playing Duell. \nThe total score is:")
                print("Human: ", str(self.humanscore))
                print("Computer: ", str(self.computerscore))
                print("\n-------------------------------------------------")
                
                if self.humanscore > self.computerscore:
                    print("You won the tournament!")
                elif self.humanscore < self.computerscore:
                    print("The computer won the tournament!")
                else:
                    print("The tournament is a draw")
                print("-----------------------------------------------------")
            else:
                userinput = "n"
                # save the current game.
                filename = input(
                    "Please enter the name of the file with any extension you like: ")
                self.file_handler.save_game(filename, newgame.get_board(
                ), newgame.is_computer_turn(), self.computerscore, self.humanscore)

                print("Game successfully saved! Come back soon!")

        
