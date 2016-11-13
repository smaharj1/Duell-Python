"""This class models the tournament"""
class Tournament:
    """This class models the tournament"""

    def __init__(self):
        self.totalgames = 0
        self.humanscore = 0
        self.computerscore = 0

    @staticmethod
    def printwelcomemessage():
        """Prints the welcome message"""
        print("Welcome to the wonderful game of Duell")
        print("We are very delighted that you chose to play this game")
        print("---------------------------x---------------------------\n")

    def startgame(self):
        """Starts the game"""

        userinput = 'a'
        gamecomplete = True

        while userinput != 'y' and userinput != 'o':
            userinput = input("Do you want to start a new game (Y) or open existing (O)? :: ")
            userinput = userinput.lower()

        if userinput == 'y':
            self.totalgames = self.totalgames+1
            newgame = Game()

        gamecomplete = newgame.start()
