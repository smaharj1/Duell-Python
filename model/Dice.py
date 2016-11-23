"""This class holds the information of a single die"""
class Dice:
    """This class holds the information of a single die"""

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

    def is_computer(self):
        return self.iscomputer
        
    def get_value(self):
        """Gets the string representation of the die"""
        if self.iscomputer:
            return "C" + str(self.top) + str(self.right)
        else:
            return "H" + str(self.top) + str(self.right)

    def move_left(self):
        """Rolls the die to the left"""
        if not self.isking:
            tmp = self.top
            self.top = self.right
            self.right = 7 - tmp

    def move_right(self):
        """ROlls the die to the right"""
        if not self.isking:
            tmp = self.top
            self.top = 7 - self.right
            self.right = tmp

    def move_back(self):
        """Rolls the die backwards"""
        if not self.isking:
            tmp = self.top
            self.top = 7 - self.front
            self.front = tmp

    def move_forward(self):
        """Rolls the die forward"""
        if not self.isking:
            tmp = self.top
            self.top = self.front
            self.front = 7 - tmp

    def set_king(self):
        self.top = 1
        self.right = 1
        self.front = 1
        self.isking = True

    def set_killed(self):
        self.iskilled = True

    def get_top(self):
        return self.top
    
    def is_player_king(self):
        return self.isking

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
