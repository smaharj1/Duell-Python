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
