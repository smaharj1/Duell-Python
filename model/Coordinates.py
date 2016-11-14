"""This holds the coordinates"""
class Coordinates:

    def __init__(self, r, c):
        self.row = r
        self.col = c

    def get_string(self):
        """Returns the string equivalent"""
        return str(self.row + 1) + "," + str(self.col + 1)
