""""""


class Player:

    def __init__(self, given_board):
        self._board = given_board
        self._prev_coordinates = None
        self._new_coordinates = None
        self._opponent_player = []
        self._current_player = []
        self._direction = 'f'
        self._both_direction_possible = True

    def _print_move(self, coord1, coord2, direction, is_computer):
        print("")
        if is_computer:
            current = "The computer"
        else:
            current = "You"

        if direction == 'f':
            dir1 = "frontally"
        else:
            dir1 = "laterally"

        print(current, " picked ", self._board.get_dice_at(
            coord1).get_value(), " at ", coord1.get_string(), " to roll. ")
        print("It rolled ", dir1, " first ")
