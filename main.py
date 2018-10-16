from rooms import rooms_id
from player import *
import game_functions as gf    # all functions are referred as 'gf' now
import game_content as gc    # all dialogue are referred as 'gc' now

# all game loops and events are tested and ran here
# main game loop


def game():
    current_room = rooms_id['lobby']
    current_dialogue = gc.opening_dialogue['description']
    while True:
        # this is just a test to see if this function can run
        gf.print_dialogue(current_dialogue)
        gf.print_room(current_room)
        break


if __name__ == '__main__':
    game()

#test

