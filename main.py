from rooms import rooms_id
from player import *
import game_functions as gf    # all functions are referred as 'gf' now
from game_content import *

# all game loops and events are tested and ran here

current_room = rooms_id['lobby']
print(opening_dialogue["description"])

# main game loop
while True:
    # this is just a test to see if this function can run
    gf.print_room(current_room)
    break


