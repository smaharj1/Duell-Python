"""
Name:  Sujil Maharjan                                    
Project : Project 1, Duell game                          
Class : Organization of Programming Language(CMPS 366-01)
Date : 10-5-2016                                         
"""
class Coordinates:
    """
    Function Name: Coordinates
    Purpose: Default Constructor

    Parameters: 
        r, an integer. It holds the row. 
        c, an integer. It holds the column.

    Return Value: none.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    def __init__(self, r, c):
        self.row = r
        self.col = c

    """
    Function Name: get_row
    Purpose: Gets the row number of the current coordinate 

    Parameters: None. 

    Return Value: Returns the row.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    def get_row(self):
        return self.row

    """
    Function Name: get_col
    Purpose: Gets the column number of the current coordinate 

    Parameters: None. 

    Return Value: Returns the column.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    def get_col(self):
        return self.col
        
    """
    Function Name: get_string
    Purpose: Gets the string representation of the coordinates  

    Parameters: None. 

    Return Value: Returns the column.

    Local Variables: None. 

    Algorithm: None.

    Assistance Received: none
    """
    def get_string(self):
        """Returns the string equivalent"""
        return str(8 - self.row ) + "," + str(self.col + 1)
