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

    def _print_move(self, coord1, direction, is_computer, reason):
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
            coord1).get_value(), " at ", coord1.get_string(), " to roll " + reason)
        print("It rolled ", dir1, " first ")

    def __nullify_suggestion(self):
        self._prev_coordinates = None
        self._new_coordinates = None

    def _can_block(self, threat_node):
        self.__nullify_suggestion()

        path_coordinates = []
        current_king = self.__get_current_player_king()

        path_coordinates = self._board.get_path_coordinates(threat_node.get_coordinates(), current_king.get_coordinates())

        for i in range(0, len(self._current_player)):
            current = self._current_player[i]
            if current.get_dice().is_player_king():
                continue
            #print(str(len(path_coordinates)), " is the length of paths available")
            for j in range(0, len(path_coordinates)):
                temp_dir = [True, True]
                print("Current node is ", current.get_dice().get_value())
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
        for index in range (0, len(player_dices)):
            temp = player_dices[index]
            temp_dir = [True, True]

            if self._board.algo_path_good(temp.get_coordinates(), threat_node.get_coordinates(), temp_dir):
                self._prev_coordinates = temp.get_coordinates()
                self._new_coordinates = threat_node.get_coordinates()
                return True
        return False

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
