"""
Name:  Sujil Maharjan
Project : Project 1, Duell game
Class : Organization of Programming Language(CMPS 366-01)
Date : 10-5-2016
"""
import os
from model.Coordinates import Coordinates

class FileHandler:

    """
    Function Name: FileHandler
    Purpose: Default Constructor

    Parameters: None. 

    Return Value: none.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    def __init__(self):
        """Sets the initial file handler"""
        self.computer_score = 0
        self.human_score = 0
        self.computer_turn = True

    """
    Function Name: save_game
    Purpose: Saves the game according to user's choice of file name

    Parameters: 
        filename, a string. It holds the name of the file. 
        board, a Board object. It holds the board. 
        is_computer_turn, a boolean. It holds if it is computer's turn
        computer_score, an integer. It holds the computer score. 
        human_score, an integer. It holds the human score. 

    Return Value: none.

    Local Variables: 
        save_file, a file. It holds the file properties. 
        output, a string. It holds the string representation of one row of the board 

    Algorithm: None.

    Assistance Received: none
    """
    def save_game(self, filename, board, is_computer_turn, computer_score, human_score):
        """Saves the current game"""
        save_file = open(filename, "w")

        save_file.write("Board: \n")

        for i in range(0, board.TOTAL_ROWS):
            output = ""
            for j in range(0, board.TOTAL_COLUMNS):
                coord = Coordinates(i, j)
                if board.get_dice_at(coord) is not None:
                    output += " " +board.get_dice_at(coord).get_value() +" "
                else:
                    output += "  0  "

            save_file.write(output)
            save_file.write("\n")

        save_file.write("\n")
        temp = "Computer Wins: " + str(computer_score)
        save_file.write(temp)
        save_file.write("\n")
        temp = "Human Wins: " + str(human_score)
        save_file.write(temp)

        if is_computer_turn:
            save_file.write("\nNext Player: Computer")
        else:
            save_file.write("\nNext Player: Human")

        save_file.close()

    """
    Function Name: open_game
    Purpose: Opens the game given the filename

    Parameters: 
        filename, a string. It holds the filename. 
        board, a Board object. It holds the board object. 

    Return Value: none.

    Local Variables: 
        index, an integer. It holds the line number of the text file read. 
        board_str, an array. It holds the board as a string

    Algorithm: None.

    Assistance Received: none
    """
    def open_game(self, filename, board):
        index = 0

        board_str = [[None for x in range(
            0, board.TOTAL_COLUMNS)] for y in range(0, board.TOTAL_ROWS)]

        # Since reading is done by default, only open the filename
        for line in open(filename):
            if "Board" in line:
                index = 0
                continue

            if index < 8:
                split_line = line.split()

                for i in range(0, 9):
                    board_str[index][i] = split_line[i]

                index = index + 1
                continue

            if "Computer Wins" in line:
                split_line = line.split()
                self.computer_score = int(split_line[len(split_line) - 1])

            if "Human Wins" in line:
                split_line = line.split()
                self.human_score = int(split_line[len(split_line) - 1])

            if "Next" in line:
                split_line = line.split()
                if split_line[len(split_line) - 1] == "Human":
                    self.computer_turn = False
                else:
                    self.computer_turn = True

        board.set_board(board_str)
        return None

    """
    Function Name: get_computer_score
    Purpose: Returns the computer score

    Parameters: None. 

    Return Value: Returns the computer score.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    def get_computer_score(self):
        return self.computer_score

    """
    Function Name: get_human_score
    Purpose: Returns the human score

    Parameters: None. 

    Return Value: Returns the human score.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    def get_human_score(self):
        return self.human_score

    """
    Function Name: get_is_computer
    Purpose: Returns if it is computer's turn

    Parameters: None. 

    Return Value: Returns if it is computer's turn.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    def get_is_computer(self):
        return self.computer_turn
