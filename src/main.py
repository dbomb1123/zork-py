# Main game file

import zork

def Play_Zork():
    returns = [1, True]
    
    while returns[1] == True:
        if returns[0] == 1: 
            returns = zork.spawn_point()
            
        if returns[0] == 2:
            returns = zork.north_of_house()

        if  returns[0] == 3:
            returns = zork.southwest()
            
        if returns[0] == 4:
            returns = zork.east_grating()
            
        if returns[0] == 5:
            returns = zork.cave()
            
        if returns[0] == 6:
            returns = zork.end_game()

        if returns[0] == 7:            
            returns = zork.back_house()
            
        if returns[0] == 8:
            returns = zork.kitchen()

        if  returns[0] == 9:
            returns = zork.attic()
            
        if returns[0] == 10:
            returns = zork.maze_front()
            
        if returns[0] == 11:
            returns = zork.maze_int()
            
        if returns[0] == 12:
            returns = zork.easter()
            
        else:
            death()

    if returns[2] == True:
        returns[0] = 1
        loop = 1
        Play_zork()
        
        
def death():  
    dead_inp = input("Do you want to continue? Y/N ")
    if dead_inp.lower() == ("n"):
        exit()
    if dead_inp.lower() == ("y"):
        Play_Zork()


print("---------------------------------------------------------")
print("Welcome to Zork - The Unofficial Python Version.")
        
Play_Zork()


def PrintOutput(s):
    print("OUTPUT", s)
