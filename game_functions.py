# all game functions will be placed in this file
import rooms
import game_content as gc    # game_content is referred as 'gc'
import player


def print_room(room):
    """Will take a room as an argument, and display all of its contents"""
    print()
    print('You are in the ' + room['name'].upper())
    print()


def print_dialogue(dialogue):
    """Will take a form of dialogue as argument, and display it properly"""
    print()
    print(dialogue.upper())
    print()
    
def move(direction):
     if direction in rooms[exits]:
            return rooms[exits[direction]]["name"]
 
        
            
        
