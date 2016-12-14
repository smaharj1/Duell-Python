"""
Name:  Sujil Maharjan                                    
Project : Project 1, Duell game                          
Class : Organization of Programming Language(CMPS 366-01)
Date : 10-5-2016                                         
"""
from random import randint
from model.Board import Board
from view.BoardView import BoardView as BView
from model.Human import Human
from model.Computer import Computer


class Game:
    """
    Function Name: Game
    Purpose: Default Constructor 

    Parameters: 
        is_new_game, a boolean. It holds if it is a new game
        opened_board, a Board object. It holds the board if the board was opened
        is_computer_turn, a boolean. It holds if it is computer's turn

    Return Value: Returns the row.

    Local Variables: 
        master_list, an array. It holds the master list. 

    Algorithm: None.

    Assistance Received: none
    """
    def __init__(self, is_new_game, opened_board=None, is_computer_turn=None):
        master_list = [5, 1, 2, 6, 1, 6, 2, 1, 5]
        print("Going in here")
        if is_new_game:
            self.computer_turn = self.determine_turn()
            self.board = Board(master_list)
        else:
            self.computer_turn = is_computer_turn
            self.board = opened_board

        self.board_view = BView(self.board)

        self.is_done = False
        self.computer_win = True
        self.human = Human(self.board)
        self.computer = Computer(self.board)

    """
    Function Name: get_board
    Purpose: Gets the board 

    Parameters: None. 

    Return Value: Returns the board.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    def get_board(self):
        return self.board

    """
    Function Name: is_computer_turn
    Purpose: Checks if it is computer's turn 

    Parameters: None. 

    Return Value: Returns true if it is computer's turn.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    def is_computer_turn(self):
        return self.computer_turn

    """
    Function Name: start
    Purpose: Starts the round of a tournament 

    Parameters: None. 

    Return Value: Returns true if the game ended. It returns false if the game was saved.

    Local Variables: None. 

    Algorithm: 
        1. Play the Human
        2. Play the computer

    Assistance Received: none
    """
    def start(self):
        """Starts the game and returns if the game has ended."""
        
        
        while not self.is_done:
            self.board_view.print_board()
            
            if self.computer_turn:
                print("It it computer's turn!\n")
            else:
                print("It is your turn! \n")
            keep_playing = self.ask_to_save()

            if keep_playing == 's':
                return False

            if self.computer_turn:
                dice_returned = self.computer.play()
                if dice_returned is not None:
                    if dice_returned.is_player_king():
                        self.is_done = True
                        self.computer_win = True
                        self.print_winner(self.computer_win)
                self.computer_turn = not self.computer_turn
            else:
                dice_returned = self.human.play()

                if dice_returned is not None:
                    if dice_returned.isking:
                        self.is_done = True
                        self.computer_win = False
                        self.print_winner(self.computer_win)
                self.computer_turn = not self.computer_turn
            
        self.board_view.print_board()
        
        return True

    """
    Function Name: print_wimmer
    Purpose: Prints the winner of the round 

    Parameters: 
        computer_winner, a boolean. It holds if the computer is a winner

    Return Value: None.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    def print_winner(self, computer_winner):
        print()
        print("####-----------------####--------------------####")
        if computer_winner:
            print("Computer WON!!!!!!")
            print("Sorry! Better luck next time!")
        else:
            print("You WON!!!!!!")
            print("Congratulations!")

    """
    Function Name: ask_to_save
    Purpose: Prompts the user if they want to save the game.  

    Parameters: None. 

    Return Value: Returns user's choice

    Local Variables: 
        choice, a character. It holds user's choice

    Algorithm: None.

    Assistance Received: none
    """
    def ask_to_save(self):
        choice = ""

        while choice != 'p' and choice != 's':
            choice = input(
                "Do you want to keep playing the game or save the game? (S for save/P for keep playing)")
            choice = choice.lower()

        return choice

    """
    Function Name: determine_turn
    Purpose: It determines who to play first 

    Parameters: None. 

    Return Value: Returns true if the computer goes first. 

    Local Variables: 
        human_die, an integer. It holds the score for human.
        computer_die, an integer. It holds the score for computer  

    Algorithm: None.

    Assistance Received: none
    """
    def determine_turn(self):
        """Determines who goes first"""
        human_die = 0
        computer_die = 0

        while human_die == computer_die:
            user_input = 'p'

            while user_input != 'r':
                user_input = input("Please enter R to toss a die:: ")
                user_input = user_input.lower()

            human_die = randint(1, 6)
            print("You rolled ", human_die)

            computer_die = randint(1, 6)
            print("Computer rolled ", computer_die)

            if human_die == computer_die:
                print("It is a draw. Do it again!")

        if computer_die > human_die:
            print("Computer goes first!")
            return True
        else:
            print("You go first!")
            return False
