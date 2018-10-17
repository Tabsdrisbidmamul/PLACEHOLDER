# all game functions will be placed in this file
import rooms
import game_content as gc    # game_content is referred as 'gc'
import player
import items
from main import current_dialogue, current_room    # global variables to update


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

    
def move(direction):
     if direction in rooms[exits]:
            return rooms[exits[direction]]["name"]
 
        

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

def take(X):
    #take key and display:
    
    print(                                                                                                    
              :sdmNNNds/`                                                                           
            -dMNho//oyNMm/                                                                          
           -NMd-      .yMM/                                                                         
           oMM:        `MMh                                                                         
     `:oyhhmMMs        :MMy                                                                         
   `omMNdhhmMMm:    .-sNMd--`.oo:                                                                   
   oMMh-   `:+.`sdyomMMMNdNMdmMMMoooooooooooo++++++oooooooooooooooooooooooooooooooooooooooo+-oso.   
   dMM-        /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMh   
   +MMh-`  `:+.`sdyomMMMNdNMdmMMMooooooooooooooooooooosssssssssssssssssssssssssdMMMMMMmyssys/yhs-   
    +mMNdhhmMMm:    .-sNMd--`.oo:                                         yyyyydMMMMMMmyyyyy`       
     `:oyyymMMo        /MMs                                              `dNMMMMMMMMMMMMMMNd`       
           sMM:        `MMh                                               /dMMMMMMMMMMMMMMd+`       
           -NMd-      .hMM/                                              `MMMMNyyMMMMyyNMMMM.       
            -dMNho//ohNMm/                                               `MMMMm  NMMM  dMMMM.       
              :sdmNNNds/`                                                `mmmmh  dmmm  ymmmm`       
        
        
        
        
                                                                                                     
                                                                                                    
`:`   :`  -/+/-   --    :`      `://:`   .://-  .//////.     `:.      `:   :` :////`--   --  s.     
 od` sy .do-.-sd` sy    N:    `yy:..:/  yh-..+m-`.-yh..`    +om+      /m -h+  mo--- -m: :m.  N-     
  +dsy  sh     m/ sy    N:    +d  .--- :N`    sh   sy         d+      /Nsy`   my++:  .m+m.   N-     
   sd   sh     N/ sy    N:    +m  .-od :N`    yy   sy         d+      /m:d/   m+``    -M-    m.     
   oh   .ds:-/hs  -m+-:sh      sh+::yd  sh/-:sh`   sy       -:ds:`    /m `sh. ms:::`  .M`   `o.     
   `.     .::-`     -::`         -::.    `-:-`     ..       -----`    `.   .. .----`   -     :`     
        
        
        
                                                                                                    
    )
