"""
Name:  Sujil Maharjan                                    
Project : Project 1, Duell game                          
Class : Organization of Programming Language(CMPS 366-01)
Date : 10-5-2016                                         
"""
import math
from model.Dice import Dice
from model.Coordinates import Coordinates


class Board:
    """
    Function Name: Board
    Purpose: Default Constructor

    Parameters: 
        keys, an array. It holds the array of all the top faces given.

    Return Value: none.

    Local Variables: 
        d, pointer of Dice. It temporarily creates a new dice.

    Algorithm:
        1. Randomly initialize the board with very basic dices.

    Assistance Received: none
    """
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

    """
    Function Name: set_board
    Purpose: To set the board according to the given values by the user.
        This will change the locations of the dice on the board.

    Parameters:
        str_board, a string of board values. It holds 2D array of values that should fill the board.

    Return Value: Returns true if it successfully fills the board.

    Local Variables: None.

    Algorithm:
        1. Loops through each square and fills it with the values gotten from user.

    Assistance Received: none
    """
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

    """
    Function Name: get_dice_at
    Purpose: To get the dice at the given coordinates

    Parameters:
        coord, a Coordinates object. This holds the x and y coordinates

    Return Value: Returns the dice at the give coordinates 

    Local Variables: None

    Algorithm:
        1. Loops through each square and fills it with the values gotten from user.

    Assistance Received: none
    """
    def get_dice_at(self, coord):
        return self.board[coord.get_row()][coord.get_col()]

    """
    Function Name: move
    Purpose: To move the dice from the given row and column to the desired row and column.

    Parameters:
        old_position, a coordinate. It holds the old position information
        new_position, a coordinate. It holds the new position coordinates. 
        direction, a character. It holds the direction that the user wants to move.

    Return Value: Returns the pointer to the dice that has been eaten if any. Else, returns null.

    Local Variables: 
        old_row, an integer. It holds the row number of old coordinates. 
        old_col, an integer. It holds the column number of the old coordinates. 
        new_row, an integer. It holds the row number of new coordinates. 
        new_col, an integer. It holds the column number of new coordinates. 
        is_computer, boolean. It holds if the player is computer or not.
        frontal, an integer. It holds the total frontal value of movement.
        side, an integer. It holds the side value of the movement.

    Algorithm:
        1. Compute the frontal movement. Frontal and backward are calculated as positive/negative.
        2. Compute the side movement. 
        3. If computer, move front means move down and if human, vice versa.
        4. Same as above for lateral movement.
        5. Roll dices with the computed values.
        6. Move the dice to different cells.

    Assistance Received: none
    """
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

    """
    Function Name: algo_is_legal
    Purpose: To check if the path is legal. This is for automated process.

    Parameters:
        old_position, a coordinate. It holds the old position information
        new_position, a coordinate. It holds the new position coordinates. 
        is_player_computer, a boolean. It holds if the player is human or a computer. 

    Return Value: Returns true if the move from one location to another is legal.

    Local Variables: none.

    Algorithm: none.

    Assistance Received: none
    """
    def algo_is_legal(self, old_position, new_position, is_player_computer):
        self.god_mode = True
        return self.is_legal(old_position, new_position, is_player_computer)

    """
    Function Name: is_legal
    Purpose: To check if the movement from one location to another is legal according to players.
        Verifies if the selections are empty, replacing own player, or moving others dice. 

    Parameters:
        old_position, a coordinate. It holds the old position information
        new_position, a coordinate. It holds the new position coordinates. 
        is_player_computer, a boolean. It holds if the player is human or a computer

    Return Value: Returns true if the movement is legal.

    Local Variables:
        old_row, an integer. It holds old row number. 
        old_col, an integer. It holds old column number. 
        new_row, an integer. It holds the new row number. 
        new_col, an integer. It holds the new column number. 

    Algorithm:
        1. Check if the selection made is empty.
        2. Check if current player is trying to move other player's dice.
        3. Check if current player is trying to remove its own player.

    Assistance Received: none
    """
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

    """
    Function Name: algo_path_good
    Purpose: To check the path for automated process of verification of path. 

    Parameters:
        old_position, a coordinate. It holds the old position information
        new_position, a coordinate. It holds the new position coordinates. 
        is_player_computer, a boolean. It holds if the player is human or a computer

    Return Value: Returns true if the path from one location to another is true.

    Local Variables: none.

    Algorithm: none.

    Assistance Received: none
    """
    def algo_path_good(self, old_position, new_position, correct_paths):
        self.god_mode = True

        return self.is_path_good(old_position, new_position, correct_paths)

    """
    Function Name: is_path_good
    Purpose: To check if the path is good. It checks if there are any distractions on the way.

    Parameters:
        old_position, a coordinate. It holds the old position information
        new_position, a coordinate. It holds the new position coordinates. 
        correctpaths, a boolean array. It holds the boolean values for if both frontal
            and lateral moves can be made

    Return Value: Returns true if the path is possible.

    Local Variables:
        frontal, an integer. It holds the total frontal movement that needs to be made.
        side,  an integer. It holds the lateral movement needed.
        old_row, an integer. It holds old row number. 
        old_col, an integer. It holds old column number. 
        new_row, an integer. It holds the new row number. 
        new_col, an integer. It holds the new column number. 

    Algorithm:
        1. Make a frontal move first and then lateral. 
        2. Store if the path is possible.
        3. Make a lateral move first and then frontal.
        3. Store if the path is possible.

    Assistance Received: none
    """
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

            if not self.god_mode:
                print(
                    "The desired location cannot be reached by the number of moves available")

            self.god_mode = False
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
            if not self.god_mode:
                print("There are hindrances on the path")
            self.god_mode = False

        self.god_mode = False

        # Returns true if either direction is true.
        return correctpaths[0] or correctpaths[1]

    """
    Function Name: compute_dice
    Purpose: Computes the dice given only the top and the index. It is called during the
        first process.

    Parameters:
        top, an integer. It holds the top face of the die. 
        index, an integer. It holds the index number of the die. 
        is_computer, a boolean. It tells if the die is computer's or human's

    Return Value: Returns true if the path is possible.

    Local Variables:
        right, an integer. It holds the right face. 
        front, an integer. It holds the front face of the die 

    Algorithm: None

    Assistance Received: none
    """
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

    """
    Function Name: get_path_coordinates
    Purpose: Computes all of the coordinates in the path from one die to another die. 
        It returns all the paths as an array.

    Parameters:
        from_node, a Coordinates. It holds the values for where we are moving the die from. 
        to, a Coordinates. It holds the values for where we are moving the die to. 

    Return Value: Returns the array with all the paths.

    Local Variables:
        row1, an integer. It holds the from row number
        row2, an integer. It holds the to row number
        col1, an integer. It holds the from column number
        col2, an integer. It holds the to column number 

    Algorithm:
        1. Go horizontally first then capture all the coordinates of the path if the move is legal in that direction
        2. Go frontal first then capture all the coordinates of the path if the move is legal.

    Assistance Received: none
    """
    def get_path_coordinates(self, from_node, to):
        # Initialization of directions and the answer arraylist.
        directions = [True, True]
        path_coordinates = []

        row1 = from_node.get_row()
        col1 = from_node.get_col()
        row2 = to.get_row()
        col2 = to.get_col()

        # Checks if the path is good. If it is, then go through each path and
        # record the location.
        if self.algo_path_good(from_node, to, directions):

            if directions[0] == True:
                # This is when frontal is first
                if row1 < row2:
                    for i in range(row1 + 1, row2 + 1):
                        if col1 == col2 and i == row2:
                            continue
                        path_coordinates.append(Coordinates(i, col1))
                elif row1 > row2:
                    for i in range(row1 - 1, row2 - 1, -1):
                        if col1 == col2 and i == row1:
                            continue
                        path_coordinates.append(Coordinates(i, col1))

                if col1 < col2:
                    for i in range(col1 + 1, col2):
                        path_coordinates.append(Coordinates(row2, i))
                elif col1 > col2:
                    for i in range(col1 - 1, col2, -1):
                        path_coordinates.append(Coordinates(row2, i))
            elif directions[1] == True:
                # This is when lateral is first
                if col1 < col2:
                    for i in range(col1 + 1, col2 + 1):
                        if row1 == row2 and i == col1:
                            continue
                        path_coordinates.append(Coordinates(row1, i))
                elif col1 > col2:
                    for i in range(col1 - 1, col2 - 1, -1):
                        if row1 == row2 and i == col2:
                            continue
                        path_coordinates.append(Coordinates(row1, i))
                if row1 < row2:
                    for i in range(row1 + 1, row2):
                        path_coordinates.append(Coordinates(i, col2))
                elif row1 > row2:
                    for i in range(row1 - 1, row2, -1):
                        path_coordinates.append(Coordinates(i, col2))

        # Returns the path coordinates.
        return path_coordinates
