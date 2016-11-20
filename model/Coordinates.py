"""This holds the coordinates"""
class Coordinates:

    def __init__(self, r, c):
        self.row = r
        self.col = c

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col
        
    def get_string(self):
        """Returns the string equivalent"""
        return str(8 - self.row ) + "," + str(self.col + 1)
