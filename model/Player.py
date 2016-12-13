""""""
from model.TreeNode import TreeNode
from model.Coordinates import Coordinates


class Player:

    def __init__(self, given_board, is_computer):
        self._board = given_board
        self._prev_coordinates = None
        self._new_coordinates = None
        self._opponent_player = []
        self._current_player = []
        self._direction = 'f'
        self._is_player_computer = is_computer
        self._both_direction_possible = True
        self._god_mode = False

    def _print_move(self, coord1, coord2, direction, is_computer, reason):
        print("")
        if is_computer:
            current = "The computer"
        else:
            if self._god_mode:
                current = "You should"
            else:
                current = "You "

        if direction == 'f':
            dir1 = "frontally"
        else:
            dir1 = "laterally"

        print(current, " picked ", self._board.get_dice_at(
            coord1).get_value(), " to roll from ", coord1.get_string(), " to " +coord2.get_string() +" " + reason)
        print("Roll is ", dir1, " first ")

    def __nullify_suggestion(self):
        self._prev_coordinates = None
        self._new_coordinates = None

    def _safe_offense(self):
        self.__nullify_suggestion()

        if self._is_player_computer:
            for row in range(self._board.TOTAL_ROWS - 1, -1, -1):
                for col in range(self._board.TOTAL_COLUMNS - 1, -1, -1):
                    if self.__can_reach_location(self._opponent_player, row, col) is None:
                        temp = self.__can_reach_location(
                            self._current_player, row, col)

                        if temp is not None:
                            self._prev_coordinates = temp.get_coordinates()
                            self._new_coordinates = Coordinates(row, col)
                            return True
        else:
            for row in range(self._board.TOTAL_ROWS):
                for col in range(self._board.TOTAL_COLUMNS):
                    if self.__can_reach_location(self._opponent_player, row, col) is None:
                        temp = self.__can_reach_location(
                            self._current_player, row, col)

                        if temp is not None:
                            self._prev_coordinates = temp.get_coordinates()
                            self._new_coordinates = Coordinates(row, col)
                            return True
        return False

    def __can_reach_location(self, player_dice, row, col):
        self.__nullify_suggestion()

        for index in range(len(player_dice)):
            temp = player_dice[index]
            coord = Coordinates(row, col)
            temp_dir = [True, True]
            if self._board.algo_path_good(temp.get_coordinates(), coord, temp_dir):
                if self._board.algo_is_legal(temp.get_coordinates(), coord, temp.get_dice().is_computer()):
                    return temp
        return None

    def _can_eat_opponent(self):
        self.__nullify_suggestion()

        for oppIndex in range(len(self._opponent_player)):
            temp = self._opponent_player[oppIndex]

            if self.__can_eat(self._current_player, temp):
                return True
        return False

    def _can_block(self, threat_node):
        self.__nullify_suggestion()

        path_coordinates = []
        current_king = self.__get_current_player_king()

        path_coordinates = self._board.get_path_coordinates(
            threat_node.get_coordinates(), current_king.get_coordinates())

        for i in range(0, len(self._current_player)):
            current = self._current_player[i]
            if current.get_dice().is_player_king():
                continue
            #print(str(len(path_coordinates)), " is the length of paths available")
            for j in range(0, len(path_coordinates)):
                temp_dir = [True, True]
                #print("Current node is ", current.get_dice().get_value())
                if self._board.algo_path_good(current.get_coordinates(), path_coordinates[j], temp_dir):
                    self._prev_coordinates = current.get_coordinates()
                    self._new_coordinates = path_coordinates[j]
                    return True
        return False

    def _king_in_threat(self):
        player_king = self.__get_current_player_king()

        if player_king is None:
            return None

        for i in range(0, len(self._opponent_player)):
            temp = self._opponent_player[i]

            temp_dir = [True, True]

            if self._board.algo_path_good(temp.get_coordinates(), player_king.get_coordinates(), temp_dir):
                return temp

        return None

    def _can_eat_threat(self, threat_node):
        if threat_node is None:
            return False

        self.__nullify_suggestion()

        if self.__can_eat(self._current_player, threat_node):
            return True

        return False

    def __can_eat(self, player_dices, threat_node):
        for index in range(0, len(player_dices)):
            temp = player_dices[index]
            temp_dir = [True, True]

            if self._board.algo_path_good(temp.get_coordinates(), threat_node.get_coordinates(), temp_dir):
                self._prev_coordinates = temp.get_coordinates()
                self._new_coordinates = threat_node.get_coordinates()
                self.__set_direction(temp_dir)
                return True
        return False

    def __set_direction(self, directions):
        if directions[0]:
            self._direction = 'f'
        else:
            self._direction = 'l'

    def _can_win(self):
        opponent_king = self.__get_opponent_king()

        if self._is_player_computer:
            win_location = Coordinates(7, 4)
        else:
            win_location = Coordinates(0, 4)

        self.__nullify_suggestion()

        for index in range(0, len(self._current_player)):
            temp_node = self._current_player[index]

            temp_direction = [True, True]

            if self._board.algo_path_good(temp_node.get_coordinates(), opponent_king.get_coordinates(), temp_direction):
                self._prev_coordinates = temp_node.get_coordinates()
                self._new_coordinates = opponent_king.get_coordinates()
                if temp_direction[0]:
                    self._direction = 'f'
                else:
                    self._direction = 'l'
                return True
            elif self._board.algo_path_good(temp_node.get_coordinates(), win_location, temp_direction):
                self._prev_coordinates = temp_node.get_coordinates()
                self._new_coordinates = win_location
                if temp_direction[0]:
                    self._direction = 'f'
                else:
                    self._direction = 'l'
                return True
        return False

    def __get_opponent_king(self):
        for i in range(0, len(self._opponent_player)):
            # if self._opponent_player[i] not None:
            if self._opponent_player[i].get_dice().is_player_king():
                return self._opponent_player[i]

        return None

    def __get_current_player_king(self):
        for i in range(0, len(self._opponent_player)):
            # if self._opponent_player[i] not None:
            if self._current_player[i].get_dice().is_player_king():
                return self._current_player[i]

        return None
