""""""
from model.Coordinates import Coordinates


class TreeNode:

    def __init__(self, die, r, c):
        self.dice = die
        self.row = r
        self.col = c
        self.coordinates = Coordinates(r, c)

    def get_dice(self):
        return self.dice
    
    def get_coordinates(self):
        return self.coordinates