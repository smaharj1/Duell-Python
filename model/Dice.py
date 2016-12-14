"""
Name:  Sujil Maharjan                                    
Project : Project 1, Duell game                          
Class : Organization of Programming Language(CMPS 366-01)
Date : 10-5-2016                                         
"""


class Dice:
    """
    Function Name: Dice
    Purpose: Default Constructor

    Parameters: 
        dice_name, a string. It holds the dice in string representation

    Return Value: none.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """

    def __init__(self, dice_name):
        self.top = ord(dice_name[1]) - ord('0')
        self.right = ord(dice_name[2]) - ord('0')

        if self.top == self.right:
            self.set_king()
        else:
            self.front = self.computefrontface(self.top, self.right)
            self.isking = False

        # Sets if it is a computer.
        if dice_name[0] == 'C':
            self.iscomputer = True
        else:
            self.iscomputer = False

        self.iskilled = False

    """
    Function Name: is_computer
    Purpose: Returns if the current dice is a computer die or not. 

    Parameters: None.
        
    Return Value: True if the die is computer die, else false.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """

    def is_computer(self):
        return self.iscomputer

    """
    Function Name: get_value
    Purpose: It returns the string representation of the die. 

    Parameters: None.
        
    Return Value: returns the string representation of the die.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """

    def get_value(self):
        """Gets the string representation of the die"""
        if self.iscomputer:
            return "C" + str(self.top) + str(self.right)
        else:
            return "H" + str(self.top) + str(self.right)

    """
    Function Name: move_left
    Purpose: It rolls the die left and updates the values. 

    Parameters: None. 
        
    Return Value: none.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """

    def move_left(self):
        """Rolls the die to the left"""
        if not self.isking:
            tmp = self.top
            self.top = self.right
            self.right = 7 - tmp

    """
    Function Name: move_right
    Purpose: It rolls the die right and updates the values. 

    Parameters: None. 
        
    Return Value: none.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """

    def move_right(self):
        """ROlls the die to the right"""
        if not self.isking:
            tmp = self.top
            self.top = 7 - self.right
            self.right = tmp

    """
    Function Name: move_backward
    Purpose: It rolls the die backward and updates the values. 

    Parameters: None. 
        
    Return Value: none.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """

    def move_backward(self):
        """Rolls the die backwards"""
        if not self.isking:
            tmp = self.top
            self.top = 7 - self.front
            self.front = tmp

    """
    Function Name: move_forward
    Purpose: It rolls the die forward and updates the values. 

    Parameters: None. 
        
    Return Value: none.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """

    def move_forward(self):
        """Rolls the die forward"""
        if not self.isking:
            tmp = self.top
            self.top = self.front
            self.front = 7 - tmp

    """
    Function Name: set_king
    Purpose: It sets the die as the king 

    Parameters: None. 

    Return Value: none.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    def set_king(self):
        self.top = 1
        self.right = 1
        self.front = 1
        self.isking = True

    """
    Function Name: set_killed
    Purpose: It sets the die as killed.  

    Parameters: None. 
        
    Return Value: none.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """  
    def set_killed(self):
        self.iskilled = True

    """
    Function Name: get_top
    Purpose: It gets the top value of the die.  

    Parameters: None. 
        
    Return Value: Returns the top value of the die.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """  
    def get_top(self):
        return self.top

    """
    Function Name: is_player_king
    Purpose: It checks if the player is a king.  

    Parameters: None. 
        
    Return Value: Returns true if the die is a king. Else, returns false.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """  
    def is_player_king(self):
        return self.isking

    """
    Function Name: computefrontface
    Purpose: It computes the front face from the given top and right values.  

    Parameters: 
        top, an integer. It holds the top value of the die. 
        right, an integer. It holds the right value of the die. 
        
    Return Value: Returns the front face value.

    Local Variables: 
        roles, an array. It holds the values of combinations that can happen in a die. 
        remain, an integer. 
        front, an integer. It holds the front face value.  

    Algorithm: 
        1. Get the top and right values.
        2. Get the remaining value on that basis and comparing with values in array roles. 

    Assistance Received: none
    """  
    @staticmethod
    def computefrontface(top, right):
        """Computes the front face of the die given the top and the right"""
        roles = [[3, 1, 4, 6, 3, 1, 4, 6], [
            1, 2, 6, 5, 1, 2, 6, 5], [2, 3, 5, 4, 2, 3, 5, 4]]

        remain = 0
        front = 0

        # Checks if top is 1 and right is 2 or its equivalent opposite. Then,
        # it finds the remaining.
        if top == 1 or 7 - top == 1:
            if right == 2 or 7 - right == 2:
                remain = 3
            else:
                remain = 2
        # Checks if top is 2 and right is 1 or its equivalent opposite. Then,
        # it finds the remaining.
        elif top == 2 or 7 - top == 2:
            if right == 1 or 7 - right == 1:
                remain = 3
            else:
                remain = 1
        # Checks if top is 3 and right is 1 or its equivalent opposite. Then,
        # it finds the remaining.
        else:
            # here top = 3
            if right == 1 or 7 - right == 1:
                remain = 2
            else:
                remain = 1

        # Compute front from remain found.
        for i in range(0, 3):
            for j in range(0, 8):
                if roles[i][j] == top:
                    if j + 1 < 8 and roles[i][j + 1] == right:
                        front = 7 - remain
                        break
                    elif j - 1 >= 0 and roles[i][j - 1] == right:
                        front = remain
                        break

        return front
