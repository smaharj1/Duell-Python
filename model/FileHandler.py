""""""
import os


class FileHandler:

    def __init__(self):
        """Sets the initial file handler"""
        self.computer_score = 0
        self.human_score = 0
        self.computer_turn = True

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
