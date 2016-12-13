"""This class holds the a complete single game"""
from random import randint
from model.Board import Board
from view.BoardView import BoardView as BView
from model.Human import Human
from model.Computer import Computer


class Game:

    def __init__(self, is_new_game, opened_board=None, is_computer_turn=None):
        master_list = [5, 1, 2, 6, 1, 6, 2, 1, 5]
        print("Going in here")
        if is_new_game:
            self.computer_turn = self.determine_turn()
            self.board = Board(master_list)
        else:
            self.computer_turn = is_computer_turn
            self.board = opened_board

        self.board_view = BView(self.board)

        self.is_done = False
        self.computer_win = True
        self.human = Human(self.board)
        self.computer = Computer(self.board)

    def get_board(self):
        return self.board

    def is_computer_turn(self):
        return self.computer_turn

    def start(self):
        """Starts the game and returns if the game has ended."""
        
        
        while not self.is_done:
            self.board_view.print_board()
            
            if self.computer_turn:
                print("It it computer's turn!\n")
            else:
                print("It is your turn! \n")
            keep_playing = self.ask_to_save()

            if keep_playing == 's':
                return False

            if self.computer_turn:
                dice_returned = self.computer.play()
                if dice_returned is not None:
                    if dice_returned.is_player_king():
                        self.is_done = True
                        self.computer_win = True
                        self.print_winner(self.computer_win)
                self.computer_turn = not self.computer_turn
            else:
                dice_returned = self.human.play()

                if dice_returned is not None:
                    if dice_returned.isking:
                        self.is_done = True
                        self.computer_win = False
                        self.print_winner(self.computer_win)
                self.computer_turn = not self.computer_turn
            
        self.board_view.print_board()
        
        return True

    def print_winner(self, computer_winner):
        print()
        print("####-----------------####--------------------####")
        if computer_winner:
            print("Computer WON!!!!!!")
            print("Sorry! Better luck next time!")
        else:
            print("You WON!!!!!!")
            print("Congratulations!")

    def ask_to_save(self):
        choice = ""

        while choice != 'p' and choice != 's':
            choice = input(
                "Do you want to keep playing the game or save the game? (S for save/P for keep playing)")
            choice = choice.lower()

        return choice

    def determine_turn(self):
        """Determines who goes first"""
        human_die = 0
        computer_die = 0

        while human_die == computer_die:
            user_input = 'p'

            while user_input != 'r':
                user_input = input("Please enter R to toss a die:: ")
                user_input = user_input.lower()

            human_die = randint(1, 6)
            print("You rolled ", human_die)

            computer_die = randint(1, 6)
            print("Computer rolled ", computer_die)

            if human_die == computer_die:
                print("It is a draw. Do it again!")

        if computer_die > human_die:
            print("Computer goes first!")
            return True
        else:
            print("You go first!")
            return False
