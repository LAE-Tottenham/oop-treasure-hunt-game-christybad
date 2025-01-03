from place import *
from player import *
from item import *

class Game():
    def __init__(self):
        self.current_place = None
        # add more atributes as needed

    def setup(self):
        # here you will setup your Game
        # places
        room1 = Place('Outside the Palace',1)
        room2 = Place('Inside the Palace',2)
        room3 = Place('Queen Elizabethany II\'s Throne Room',3,True)
        room4 = Plce('G,1)


        home.add_next_place(garden)
        home.add_next_place(bedroom)
        bedroom.add_next_place(bathroom)
        garden.add_next_place(shed)
        # etc. 
        
        # items
        hammer = Item('Hammer')
        pen = Item('Pen')

        home.add_item(hammer)
        bedroom.add_item(pen)

        # home will be our starting place
        self.current_place = home
        
        # finish the setup function...

    def start(self):
        print("Welcome to my game...")
        name = input("Enter player name: ")
        print(f"{name}, you are playing as a mad scientist trying to be the first to discover time travel.
               With all your efforts, you manage to build a time machine and test it out by going back in
               time by a few seconds. But Oh no! Your machine malfunctioned and sent you back way further than 
              expected. And even worse, the sheer force of your machine has killed a man! Upon further inspection of the man's ID
              you discover that you have killed your grandfather from the past! in a desperate attempt to reverse 
              this you make the attempt to travel back to the future but discover that your time machine has gone 
              up in pieces with some pieces missing. according to your calculations, different components of your
               time machine has been caught in different centuries, you must travel through each one to rebuild your
               time machine and go back in time to stop the tragic fate of your grandfather taking place. But wait.. if your
               grandfather has died, how would your mother given birth to you? Should you even exist? you begin to
               feel your life matter slowly wear away. Find all the pieces before its too late!\n Do you have what it takes?")
        
        player = Player(name)

        print("You are currently in " + self.current_place.name)
        self.current_place.show_next_places()
        opt = input("""
What would you like to do?
1. Go to a place
2. Pickup item
3. Check inventory
etc.      
""")
        if opt == "1":
            # add code
            pass
        elif opt == "2":
            # add code
            pass
        elif opt == "3":
            # add code
            pass
            
game = Game()

game.start()