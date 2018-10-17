# all game functions will be placed in this file
import rooms
import game_content as gc    # game_content is referred as 'gc'
import player
import items
from main import current_dialogue, current_room    # global variables to update
import string


def print_room(room):
    """Will take a room as an argument, and display all of its contents"""
    print()
    print('You are in the ' + room['name'].upper())
    print()


def print_dialogue(dialogue):
    """Will take a form of dialogue as an argument, and display it properly"""
    print()
    print(dialogue.upper())
    print()


def exit_leads_to(exits, direction):
    """This will take a dictionary of exits, and a direction from the user"""
    return rooms.rooms_id[exits[direction]]['name']


def move(exits, direction):
    return rooms.rooms_id[exits[direction]]


def print_room_items(room):
    """Will take room item(s) as an argument, and will output them properly"""
    print()
    print('You find in the room ' + room['items'])


def print_inventory(inventory):
    """Will take the player's inventory and print out the items names'"""
    store_string = ''
    for value in inventory:
        if value == inventory[-1]:
            store_string = store_string + value['name'] + '.'
            break
        store_string = store_string + value['name'] + ', '
    print('You have: ' + store_string)


def remove_whitespace(text):
    """will remove beginning and trailing whitespace from input"""
    return text.strip()


def remove_punct(text):
    """will remove all forms of punctuation that is in the text"""
    punctuation = string.punctuation
    for letter in text:
        if letter in punctuation:
            text = text.replace(letter, '')
    return text


def normal_input(user_input):
    """Will take the user input and firstly remove punctuation, then the
    whitespace and then lastly return it as a list, so it can therefore be
    processed in execute command"""
    user_input = remove_punct(user_input)
    user_input = remove_whitespace(user_input)
    normal_lst = user_input.split()
    return normal_lst


    

def riddle_1():
    x = input("I'm tall when I'm young and I'm short when I'm old. What am I?")
    if x == ("candle") or ("a candle"):
        take()
        
def take():
    #take key and display:
    
    print("")
    print("                      :sdmNNNds/`                                                                           ")
    print("                    -dMNho//oyNMm/                                                                          ")
    print("                   -NMd-      .yMM/                                                                         ")
    print("                   oMM:        `MMh                                                                         ")
    print("             `:oyhhmMMs        :MMy                                                                         ")
    print("           `omMNdhhmMMm:    .-sNMd--`.oo:                                                                   ")
    print("           oMMh-   `:+.`sdyomMMMNdNMdmMMMoooooooooooo++++++oooooooooooooooooooooooooooooooooooooooo+-oso.   ")
    print("           dMM-        /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMh   ")
    print("           +MMh-`  `:+.`sdyomMMMNdNMdmMMMooooooooooooooooooooosssssssssssssssssssssssssdMMMMMMmyssys/yhs-   ")
    print("            +mMNdhhmMMm:    .-sNMd--`.oo:                                         yyyyydMMMMMMmyyyyy`       ")
    print("             `:oyyymMMo        /MMs                                              `dNMMMMMMMMMMMMMMNd`       ")
    print("                   sMM:        `MMh                                               /dMMMMMMMMMMMMMMd+`       ")
    print("                   -NMd-      .hMM/                                              `MMMMNyyMMMMyyNMMMM.       ")
    print("                    -dMNho//ohNMm/                                               `MMMMm  NMMM  dMMMM.       ")
    print("                      :sdmNNNds/`                                                `mmmmh  dmmm  ymmmm`       ")
    print("")
    print("    ")
    print("   ")
    print("   ")
    print("                                                       ")                                        
    print("                                                        ")                                       
    print("        `:`   :`  -/+/-   --    :`      `://:`   .://-  .//////.     `:.      `:   :` :////`--   --  s.   ")  
    print("         od` sy .do-.-sd` sy    N:    `yy:..:/  yh-..+m-`.-yh..`    +om+      /m -h+  mo--- -m: :m.  N-    ") 
    print("          +dsy  sh     m/ sy    N:    +d  .--- :N`    sh   sy         d+      /Nsy`   my++:  .m+m.   N-   ")  
    print("           sd   sh     N/ sy    N:    +m  .-od :N`    yy   sy         d+      /m:d/   m+``    -M-    m.    ") 
    print("           oh   .ds:-/hs  -m+-:sh      sh+::yd  sh/-:sh`   sy       -:ds:`    /m `sh. ms:::`  .M`   `o.     ")
    print("           `.     .::-`     -::`         -::.    `-:-`     ..       -----`    `.   .. .----`   -     :`   ")  
        
        

def print_menu():

    print("You can:")
    for values in current_room['items']:
        print("TAKE " + values.get('name'))
    for values in player.inventory:
        print("DROP " + values.get('name'))
