""""""
from model.Board import Board


class BoardView:

    def __init__(self, b):
        self.board = b

    def print_board(self):
        print("-----------------------------------------------------------------------------------------")
        board_object = self.board
        for i in range(board_object.TOTAL_ROWS):
            print(str(8 - i), "\t|", end="")
            for j in range(board_object.TOTAL_COLUMNS):
                temp = board_object.board[i][j]

                if temp is None:
                    print("0\t", end="")
                else:
                    print(temp.get_value(), "\t", end="")
            print("")
        # print("\n")
        print("-------------------------------------------------------------------------------------------")
        for i in range(board_object.TOTAL_COLUMNS):
            print("\t", str(i + 1), end="")
        print("")
