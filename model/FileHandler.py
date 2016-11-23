""""""
import os
from model.Coordinates import Coordinates


class FileHandler:

    def __init__(self):
        """Sets the initial file handler"""
        self.computer_score = 0
        self.human_score = 0
        self.computer_turn = True

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

    def get_computer_score(self):
        return self.computer_score

    def get_human_score(self):
        return self.human_score

    def get_is_computer(self):
        return self.computer_turn
