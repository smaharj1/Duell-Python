""""""
from model.Coordinates import Coordinates


class TreeNode:

    """
    Function Name: TreeNode
    Purpose: Default Constructor

    Parameters: 
        die, a Dice object. It holds a dice 
        r, an integer. It holds the row number 
        c, an integer. It holds the column number

    Return Value: none.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    def __init__(self, die, r, c):
        self.dice = die
        self.row = r
        self.col = c
        self.coordinates = Coordinates(r, c)

    """
    Function Name: get_dice
    Purpose: Returns the dice

    Parameters: None

    Return Value: Returns the die.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    def get_dice(self):
        return self.dice
    
    """
    Function Name: get_coordinates
    Purpose: Returns the coordinates

    Parameters: None

    Return Value: Returns the coordinates.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    def get_coordinates(self):
        return self.coordinates