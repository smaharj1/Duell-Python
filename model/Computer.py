""""""
from model.Player import Player
from model.Coordinates import Coordinates
from model.TreeNode import TreeNode


class Computer(Player):

    def __init__(self, board):
        super().__init__(board, True)

    def play(self):
        self.refresh_players()

        dice_ate = None

        # Checks if the computer can win the game. If it can, then win the
        # game.
        if self._can_win():
            reason = "because it led to winning condition"
            self._print_move(self._prev_coordinates, self._new_coordinates,
                             self._direction, True, reason)
            dice_ate = self._board.move(self._prev_coordinates,
                                        self._new_coordinates, self._direction)
            return dice_ate

        threat_node = self._king_in_threat()
        # Checks if there are any threats to the king. If there is, then try to eat the
        # threat. Or block its move.
        if threat_node is not None:
            if self._can_eat_threat(threat_node):
                reason = "because it led eating the threat to the king"
                self._print_move(self._prev_coordinates, self._new_coordinates,
                                 self._direction, True, reason)
                dice_ate = self._board.move(self._prev_coordinates,
                                            self._new_coordinates, self._direction)
                return dice_ate
            elif self._can_block(threat_node):
                reason = "because it blocked from eating my King"
                self._print_move(self._prev_coordinates, self._new_coordinates,
                                 self._direction, True, reason)
                dice_ate = self._board.move(self._prev_coordinates,
                                            self._new_coordinates, self._direction)
                return dice_ate

        # Tries to eat opponent's dice if it is possible
        if self._can_eat_opponent():
            reason = "because it ate your dice."
            self._print_move(self._prev_coordinates, self._new_coordinates,
                             self._direction, True, reason)
            dice_ate = self._board.move(
                self._prev_coordinates, self._new_coordinates, self._direction)
            return dice_ate

        self._safe_offense()

        reason = "because there are no dice that the computer could eat"
        self._print_move(self._prev_coordinates, self._new_coordinates, self._direction, True, reason)
        dice_ate = self._board.move(self._prev_coordinates, self._new_coordinates, self._direction)

        return dice_ate

    def refresh_players(self):
        self._opponent_player = []
        self._current_player = []

        for i in range(0, self._board.TOTAL_ROWS):
            for j in range(0, self._board.TOTAL_COLUMNS):
                coord = Coordinates(i, j)
                die = self._board.get_dice_at(coord)
                if die is not None:
                    if die.is_computer():
                        self._current_player.append(TreeNode(die, i, j))
                    else:
                        self._opponent_player.append(TreeNode(die, i, j))
