"""This class holds the a complete single game"""
from random import randint
from model.Board import Board
from view.BoardView import BoardView as BView


class Game:

    def __init__(self):
        master_list = [5, 1, 2, 6, 1, 6, 2, 1, 5]

        self.board = Board(master_list)

        self.board_view = BView(self.board)
        self.computer_turn = self.determine_turn()
        self.is_done = False
        self.computer_win = True

    def determine_turn(self):
        human_die = 0
        computer_die = 0

        while human_die == computer_die:
            user_input = 'p'

            while user_input != 'r':
                user_input = input("Please enter R to toss a die")
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
        else :
            print("You go first!")
            return False
