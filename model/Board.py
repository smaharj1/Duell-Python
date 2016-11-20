"""This class holds the board of duell"""
from model.Dice import Dice
from model.Coordinates import Coordinates
import math


class Board:

    def __init__(self, keys):
        self.TOTAL_ROWS = 8
        self.TOTAL_COLUMNS = 9
        self.god_mode = False
        self.board = [[None for x in range(
            0, self.TOTAL_COLUMNS)] for y in range(0, self.TOTAL_ROWS)]

        for i in range(0, self.TOTAL_ROWS):
            for j in range(0, self.TOTAL_COLUMNS):
                if i == 0:
                    self.board[i][j] = self.compute_dice(keys[j], j, True)
                elif i == self.TOTAL_ROWS - 1:
                    self.board[i][j] = self.compute_dice(keys[j], j, False)
                else:
                    self.board[i][j] = None

    def set_board(self, str_board):
        """Sets the board from the string representation of the board"""
        for i in range(0, self.TOTAL_ROWS):
            for j in range(0, self.TOTAL_COLUMNS):
                if str_board[i][j] == '0':
                    # Initialize the board as None
                    self.board[i][j] = None
                else:
                    # Initialize the board as the input given
                    self.board[i][j] = Dice(str_board[i][j])

    def get_dice_at(self, coord):
        return self.board[coord.get_row()][coord.get_col()]


    def move(self, old_position, new_position, direction):
        """Moves the dice to the desired location and returns the new dice if eaten"""
        old_row = old_position.row
        old_col = old_position.col
        new_row = new_position.row
        new_col = new_position.col

        is_computer = self.board[old_row][old_col].iscomputer

        frontal = new_row - old_row
        side = new_col - old_col

        if not is_computer:
            if direction == 'f':
                # Checks if the dice is rolled forward or backward and assigns
                # the rolling accordingly.
                for i in range(0, abs(frontal)):
                    if frontal < 0:
                        self.board[old_row][old_col].move_forward()
                    else:
                        self.board[old_row][old_col].move_backward()

                # Checks if the dice is rolled right or left and assigns the
                # rolling accordingly.
                for i in range(0, abs(side)):
                    if side > 0:
                        self.board[old_row][old_col].move_right()

                    else:
                        self.board[old_row][old_col].move_left()

            else:
                # Checks if the dice is rolled right or left and assigns the
                # rolling accordingly.
                for i in range(0, abs(side)):
                    if side > 0:
                        self.board[old_row][old_col].move_right()

                    else:
                        self.board[old_row][old_col].move_left()

                # Checks if the dice is rolled forward or backward and assigns
                # the rolling accordingly.
                for i in range(0, abs(frontal)):
                    if frontal < 0:
                        self.board[old_row][old_col].move_forward()

                    else:
                        self.board[old_row][old_col].move_backward()

        else:
            if direction == 'f':
                # Checks if the dice is rolled forward or backward and assigns
                # the rolling accordingly.
                for i in range(0, abs(frontal)):
                    if frontal > 0:
                        self.board[old_row][old_col].move_forward()

                    else:
                        self.board[old_row][old_col].move_backward()

                # Checks if the dice is rolled right or left and assigns the
                # rolling accordingly.
                for i in range(0, abs(side)):
                    if side < 0:
                        self.board[old_row][old_col].move_right()

                    else:
                        self.board[old_row][old_col].move_left()

            else:
                # Checks if the dice is rolled right or left and assigns the
                # rolling accordingly.
                for i in range(0, abs(side)):
                    if side < 0:
                        self.board[old_row][old_col].move_right()

                    else:
                        self.board[old_row][old_col].move_left()

                # Checks if the dice is rolled forward or backward and assigns
                # the rolling accordingly.
                for i in range(0, abs(frontal)):
                    if frontal > 0:
                        self.board[old_row][old_col].move_forward()

                    else:
                        self.board[old_row][old_col].move_backward()

        dice_ate = None
        # Adds the dice to the Cell and removes the dice from previous
        # location.
        if self.board[new_row][new_col] != None:
            # cout << "Dice is eaten!" << endl << endl
            dice_ate = self.board[new_row][new_col]
            self.board[new_row][new_col] = None

        self.board[new_row][new_col] = self.board[old_row][old_col]
        self.board[old_row][old_col] = None

        return dice_ate

    def is_legal(self, old_position, new_position, is_player_computer):
        """Checks if the move is legal"""
        old_row = old_position.row
        old_col = old_position.col
        new_row = new_position.row
        new_col = new_position.col

        # If the cell in the board is empty, return that it is empty.
        if self.board[old_row][old_col] is None:
            if not self.god_mode:
                print("The cell you clicked is empty")
            return False

        # Holds if the player is computer or human.
        is_computer = self.board[old_row][old_col].iscomputer

        # Check if the the user is trying to move other player's dice.
        if is_computer != is_player_computer:
            if not self.god_mode:
                print("It is not your die")
            return False

        # Checks if the user is trying to replace their own player by the
        # movement.
        if self.board[new_row][new_col] is not None:
            if (self.board[old_row][old_col].iscomputer and self.board[new_row][new_col].iscomputer) or (not self.board[old_row][old_col].iscomputer and not self.board[new_row][new_col].iscomputer):
                if not self.god_mode:
                    print("Hey, you are trying to replace your own player")
                return False

        return True

    def is_path_good(self, old_position, new_position, correctpaths):
        """Checks if the path is good"""
        old_row = old_position.row
        old_col = old_position.col
        new_row = new_position.row
        new_col = new_position.col

        frontal = new_row - old_row
        side = new_col - old_col

        if self.board[old_row][old_col] is None:
            return False

        # At this point, it is obvious that the frontal and side are going to
        # be good.
        if self.board[old_row][old_col].get_top() != abs(frontal) + abs(side):
            self.god_mode = False
            print(
                "The desired location cannot be reached by the number of moves available")
            return False

        index = 0

        # If it is the computer, then do the increments accordingly and check in each location
        # for the cells to be empty.
        temp_row = old_row
        temp_col = old_col

        # If frontal or side movement is not needed remove it as correct paths.
        if abs(frontal) == 0:
            correctpaths[0] = False
        if abs(side) == 0:
            correctpaths[1] = False

        # Loops frontal first and checks in each and every location if there
        # are any dices.
        for index in range(1, abs(frontal) + 1):
            j = 0
            if frontal < 0:
                j = -index
            else:
                j = index

            temp_row = old_row + j

            # This is if its the main location, just ignore this step.
            if temp_row == new_row and temp_col == new_col:
                continue

            # If there is a die on the way, indicate that path as not possible.
            if self.board[temp_row][temp_col] is not None:
                correctpaths[0] = False

        # Make a 90 degree turn if needed and if frontal path is going correct
        # until now.
        if correctpaths[0]:
            for index in range(1, abs(side)):
                j = 0
                if side < 0:
                    j = - index
                else:
                    j = index

                temp_col = old_col + j
                if self.board[temp_row][temp_col] is not None:
                    correctpaths[0] = False

        # Reset temp row and columns.
        temp_row = old_row
        temp_col = old_col

        # Loops through lateral movement first and checks if there are any
        # dices in each location.
        for index in range(1, abs(side) + 1):
            j = index
            if side < 0:
                j = -index

            temp_col = old_col + j

            # If its the main location, just ignore this step.
            if temp_row == new_row and temp_col == new_col:
                continue

            # If there is a dice on the way, indicate it as incorrect path.
            if self.board[temp_row][temp_col] is not None:
                correctpaths[1] = False

        # Make a 90 degree turn if needed and if frontal path is going correct
        # until now.
        if correctpaths[1]:
            for index in range(1, abs(frontal)):
                j = index
                if frontal < 0:
                    j = -index

                temp_row = old_row + j
                if self.board[temp_row][temp_col] is not None:
                    correctpaths[1] = False

        # Checks if both direction paths are incorrect.
        if not correctpaths[0] and not correctpaths[1]:
            print("There are hindrances on the path")
            self.god_mode = False

        self.god_mode = False

        # Returns true if either direction is true.
        return correctpaths[0] or correctpaths[1]

    def compute_dice(self, top, index, is_computer):
        """Computes the dice and returns it"""
        right = 3
        front = Dice.computefrontface(top, right)

        dice_name = ""
        if is_computer:
            dice_name = "C"
        else:
            dice_name = "H"

        if index == math.floor(self.TOTAL_COLUMNS / 2):
            dice_name += "11"
        else:
            dice_name = dice_name + str(top) + str(7 - front)

        return Dice(dice_name)
