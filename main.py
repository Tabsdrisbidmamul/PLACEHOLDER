from rooms import rooms_id
from player import *
import game_functions as gf    # all functions are referred as 'gf' now

# all game loops and events are tested and ran here

current_room = rooms_id['lobby']

# main game loop
while True:
    gf.print_room(current_room)

    
