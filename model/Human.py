""""""
from model.Player import Player
from model.Coordinates import Coordinates


class Human(Player):

    def __init__(self, board):
        super().__init__(board)

    def play(self):

        print("\n It is your turn. Please choose the coordinates ")

        valid = False

        while not valid:
            coord_1 = self.get_coordinates("first")
            coord_2 = self.get_coordinates("destination")

            paths = [True, True]

            if self._board.is_legal(coord_1, coord_2, False) and self._board.is_path_good(coord_1, coord_2, paths):
                valid = True

        direction = 'k'

        if paths[0] and paths[1]:
            while direction != 'f' and direction != 'l':
                direction = input(
                    "Do you want to move FRONTAL or LATERAL first? (F/L)")
        else:
            if paths[0]:
                direction = 'f'
            else:
                direction = 'l'

        self._print_move(coord_1,coord_2, direction, False)
        dice_ate = self._board.move(coord_1, coord_2, direction)

        return dice_ate

    def get_coordinates(self, given):
        valid = False
        inputs = []

        while not valid:
            message = "Please give " + given + " coordinates from 1 1 to 8 9 :: "
            user_input = input(message)
            coords = user_input.split()
            inputs = [int(x.strip()) for x in coords]

            if inputs[0] > 0 and inputs[0] < 9 and inputs[1] > 0 and inputs[1] < 10:
                valid = True

        inputs[0] = self._board.TOTAL_ROWS - inputs[0] + 1
        user_coord = Coordinates(inputs[0] - 1, inputs[1] - 1)
        return user_coord
