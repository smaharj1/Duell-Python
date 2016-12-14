"""
Name:  Sujil Maharjan                                    
Project : Project 1, Duell game                          
Class : Organization of Programming Language(CMPS 366-01)
Date : 10-5-2016                                         
"""
from model.Player import Player
from model.TreeNode import TreeNode
from model.Coordinates import Coordinates


class Human(Player):
    """
    Function Name: Human
    Purpose: Default Constructor

    Parameters: None.

    Return Value: none

    Local Variables: none

    Algorithm: None.

    Assistance Received: none
    """
    def __init__(self, board):
        super().__init__(board, False)

    """
    Function Name: play
    Purpose: Plays the game for the human

    Parameters: none

    Return Value: Returns a dice if human move eats a die

    Local Variables: 
        direction, a character. It holds the direction of the movement. 
        paths, an array. It holds the paths possible. 
        dice_ate, a Dice object. It holds a dice that was eaten. 

    Algorithm: None.

    Assistance Received: none
    """
    def play(self):

        print("\n It is your turn. Please choose the coordinates ")

        #Ask if the user needs help
        self.help_portal()

        self._god_mode = False
        valid = False

        # Loop and find the valid coordinates from the user
        while not valid:
            coord_1 = self.get_coordinates("first")
            coord_2 = self.get_coordinates("destination")

            paths = [True, True]

            if self._board.is_legal(coord_1, coord_2, False) and self._board.is_path_good(coord_1, coord_2, paths):
                valid = True

        direction = 'k'

        # Only ask the user for path choice if the user has that choice. 
        if paths[0] and paths[1]:
            while direction != 'f' and direction != 'l':
                direction = input(
                    "Do you want to move FRONTAL or LATERAL first? (F/L)")
                direction = direction.lower()
        else:
            if paths[0]:
                direction = 'f'
            else:
                direction = 'l'

        self._print_move(coord_1, coord_2, direction, False, "")
        dice_ate = self._board.move(coord_1, coord_2, direction)

        return dice_ate

    """
    Function Name: get_coordinates
    Purpose: Gets the coordinates from the user

    Parameters: 
        given, a string. It holds values of if it is first or destination.

    Return Value: REturns the coordinates user entered. 

    Local Variables: 
        inputs, an array. It holds the user's entries
        user_coord, a Coordinates object. It holds the user coordinates that was found. 

    Algorithm: None.

    Assistance Received: none
    """
    def get_coordinates(self, given):
        valid = False
        inputs = []

        while not valid:
            message = "Please give " + given + " coordinates from 1 1 to 8 9 :: "
            user_input = input(message)
            coords = user_input.split()

            inputs = [x.strip() for x in coords]

            if inputs[0] < '0' or inputs[0] > '9' or inputs[1] < '0' or inputs[1] > '9':
                print("Error: Please give correct coordinates")
                continue

            inputs[0] = int(inputs[0])
            inputs[1] = int(inputs[1])
            if inputs[0] > 0 and inputs[0] < 9 and inputs[1] > 0 and inputs[1] < 10:
                valid = True

        inputs[0] = self._board.TOTAL_ROWS - inputs[0] + 1
        user_coord = Coordinates(inputs[0] - 1, inputs[1] - 1)
        return user_coord

    """
    Function Name: refresh_players
    Purpose: Refreshes the current states of the board and stores all the current and opponent player's dices

    Parameters: None.

    Return Value: none.

    Local Variables: None. 

    Algorithm: 
        1. Loop through all the cells in the board 
        2. If the cell has computer's die, store it to current
        3. If the cell has human's die, store it to opponent

    Assistance Received: none
    """
    def refresh_players(self):
        self._opponent_player = []
        self._current_player = []

        for i in range(0, self._board.TOTAL_ROWS):
            for j in range(0, self._board.TOTAL_COLUMNS):
                coord = Coordinates(i, j)
                die = self._board.get_dice_at(coord)
                if die is not None:
                    if die.is_computer():
                        self._opponent_player.append(TreeNode(die, i, j))
                    else:
                        self._current_player.append(TreeNode(die, i, j))

    """
    Function Name: help_portal
    Purpose: Asks the user if they need help

    Parameters: None

    Return Value: none

    Local Variables: userInput, a character. It holds the user input. 

    Algorithm: None.

    Assistance Received: none
    """
    def help_portal(self):
        valid = False

        while not valid:
            userInput = input("Do you want help? (Y for yes or N for no)")
            userInput = userInput.lower()

            if userInput == 'y' or userInput == 'n':
                valid = True

        if userInput == 'y':
            # Perform the help algorithm here.
            self._god_mode = True
            
            self.perform_algorithmic_move()

    """
    Function Name: perform_algorithmic_move
    Purpose: Performs the algorithm so that it can suggest the user the move. 

    Parameters: None

    Return Value: none

    Local Variables: 
        dice_ate, a Dice object. It holds the dice that was eaten
        reason, a string. It holds the reason for making the move
        threat_node, a TreeNode object. It holds the node tha pose threat to the king 

    Algorithm: 
        1. Check if you can win 
        2. Check if your king is in threat, 
            1. Remove the threat 
            2. Make a blocking move
        3. Check if you can eat other player's dice, and eat it
        4. Make an offensive move

    Assistance Received: none
    """
    def perform_algorithmic_move(self):
        self.refresh_players()
        dice_ate = None

        # Checks if the computer can win the game. If it can, then win the
        # game.
        if self._can_win():
            reason = "because it led to winning"
            self._print_move(self._prev_coordinates, self._new_coordinates,
                             self._direction, False, reason)

        else:
            threat_node = self._king_in_threat()
            # Checks if there are any threats to the king. If there is, then try to eat the
            # threat. Or block its move.
            if threat_node is not None:
                if self._can_eat_threat(threat_node):
                    reason = "because it led eating the threat to the king"
                    self._print_move(self._prev_coordinates, self._new_coordinates,
                                    self._direction, False, reason)
                    return

                elif self._can_block(threat_node):
                    reason = "because it blocked from eating your King"
                    self._print_move(self._prev_coordinates, self._new_coordinates,
                                     self._direction, False, reason)
                    return

            # Tries to eat opponent's dice if it is possible
            if self._can_eat_opponent():
                reason = "because it ate computer's dice."
                self._print_move(self._prev_coordinates, self._new_coordinates,
                                 self._direction, False, reason)
                return

            self._safe_offense()

            reason = "because there are no dice that the you could eat"
            self._print_move(self._prev_coordinates, self._new_coordinates,
                             self._direction, False, reason)
