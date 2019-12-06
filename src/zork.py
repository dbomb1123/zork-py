import items

# First Input function
def spawn_point():
	loop = 1
	alive = True
	win = False
	print("---------------------------------------------------------")
	print("You are standing in an open field west of a white house, with a boarded front door.")
	print("You can see a small lake to the north.")
	print("(A secret path leads southwest into the forest.)")
	print("There is a Small Mailbox.")
	second = input("What do you do? ")
	
	if second.lower() == ("take mailbox"):
		print("---------------------------------------------------------")
		print("It is securely anchored.")
	elif second.lower() == ("open mailbox"):
		print("---------------------------------------------------------")
		print("Opening the small mailbox reveals a leaflet.")
	elif second.lower() == ("go north"):
		loop = 2
		north_of_house()
	elif second.lower() == ("open door"):
		print("---------------------------------------------------------")
		print("The door cannot be opened.")
	elif second.lower() == ("take boards"):
		print("---------------------------------------------------------")
		print("The boards are securely fastened.")
	elif second.lower() == ("look at house"):
		print("---------------------------------------------------------")
		print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
	elif second.lower() == ("go southwest"):
		loop = 3
		southwest()
	elif second.lower() == ('go east'):
		loop = 7
		back_house()
	elif second.lower() == ('12'):
		loop = 12
		easter()
	elif second.lower() == ("read leaflet"):
		print("---------------------------------------------------------")
		print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
	elif second.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		alive = False
		death()
	else:
		print("---------------------------------------------------------")
	return [loop, alive, win]

# North of House
def north_of_house():
	loop = 2
	alive = True
	win = False
	print("---------------------------------------------------------")
	print("You find yourself at the edge of a beautiful lake aside rolling hills.")
	print("A small pier juts out into the lake.")
	print("A fishing rod rests on the pier.")
	print("(You can see a white house in the distance to the south.)")
	north_house_inp = input("What do you do? ")

	if north_house_inp.lower() == ("go south"):
		loop = 1
		spawn_point()
	elif north_house_inp.lower() == ("swim"):
		print("---------------------------------------------------------")
		print("You don't have a change of clothes and you aren't here on vacation.")
	elif north_house_inp.lower() == ("fish"):
		print("---------------------------------------------------------")
		print("You spend some time fishing but nothing seems to bite.")
	elif north_house_inp.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		alive = False
		death()
	else:
		print("---------------------------------------------------------")
	return [loop, alive, win]

# Southwest Loop
def southwest():
	loop = 3
	alive = True
	win = False
	print("---------------------------------------------------------")
	print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
	forest_inp = input("What do you do? ")
                        	
	if forest_inp.lower() == ("go west"):
		print("---------------------------------------------------------")
		print("You would need a machete to go further west.")
	elif forest_inp.lower() == ("go north"):
		print("---------------------------------------------------------")
		print("The forest becomes impenetrable to the North.")
	elif forest_inp.lower() == ("go south"):
		print("---------------------------------------------------------")
		print("Storm-tossed trees block your way.")
	elif forest_inp.lower() == ("go east"):
		loop = 4
		east_grating()
	elif forest_inp.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		alive = False
		death()
	else:
		print("---------------------------------------------------------")
	return [loop, alive, win]
	
# East Loop and Grating Input
def east_grating():
	loop = 4
	alive = True
	win = False
	print("---------------------------------------------------------")
	print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
	print("There is an open grating, descending into darkness.")
	grating_inp = input("What do you do? ")
	if grating_inp.lower() == ("go south"):
		print("---------------------------------------------------------")
		print("You see a large ogre and turn around.")
	elif grating_inp.lower() == ("descend grating"):
		loop = 10
		cave()
	elif grating_inp.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		alive = False
		death()

	else:
		print("---------------------------------------------------------")	
	return [loop, alive, win]

# Grating Loop and Cave Input
def cave():
	loop = 5
	alive = True
	win = False
	print("---------------------------------------------------------")
	print("You are in a tiny cave with a dark, forbidding staircase leading down.")
	print('It seems like there are multiple ways to preceed though')
	print("There is a skeleton of a human male in one corner.")
	cave_inp = input("What do you do? ")
		
	if cave_inp.lower() == ("descend staircase"):
		loop = 6
		end_game()
	elif cave_inp.lower() == ("take skeleton"):
		print("---------------------------------------------------------")
		print("Why would you do that? Are you some sort of sicko?")
	elif cave_inp.lower() == ("smash skeleton"):
		print("---------------------------------------------------------")
		print("Sick person. Have some respect mate.")
	elif cave_inp.lower() == ("light up room"):
		print("---------------------------------------------------------")
		print("You would need a torch or lamp to do that.")
	elif cave_inp.lower() == ("break skeleton"):
		print("---------------------------------------------------------")
		print("I have two questions: Why and With What?")
	elif cave_inp.lower() == ("go down staircase"):
		loop = 6
		end_game()
	elif cave_inp.lower() == ('go south'):
		loop = 10
		print('you see a maze in the distance')
		maze_front()
	elif cave_inp.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		alive = False
		death()
	elif cave_inp.lower() == ("scale staircase"):
		loop = 6
		end_game()
	else:
		print("---------------------------------------------------------")
	return [loop, alive, win]

# End of game
def end_game():
	loop = 6
	alive = True
	win = False
	print("---------------------------------------------------------")
	print("You have entered a mud-floored room.")
	print("Lying half buried in the mud is an old trunk, bulging with jewels.")
	last_inp = input("What do you do? ")
		
	if last_inp.lower() == ("open trunk"):
		print("---------------------------------------------------------")
		print("You have found the Jade Statue and have completed your quest!")
	elif last_inp.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		alive = False
		death()
	else:
		print("---------------------------------------------------------")
			
	# Exit loop at the end of game
	exit_inp = input("Do you want to continue? Y/N ")
	if exit_inp.lower() == ("n"):
		exit()
	if exit_inp.lower() == ("y"):
		win = True
	return [loop, alive, win]

def back_house():
	loop = 7
	alive = True
	win = False
	print('You walk around the side of the house to see a more beaten down side of the house')
	print('There are a couple windows linning the siding, one of which is broken')
	print('The shutters on the window are lose')
	back_inp = input('What do you do? ')
	
	if back_inp.lower() == ('open window'):
		loop = 8
		print('Opening the rickety window you cllimb into the house')
		kitchen()
	elif back_inp.lower() == ('go west'):
		loop = 8
		print('Opening the rickety window you cllimb into the house')
		kitchen()
	elif back_inp.lower() == ('go south'):
		loop = 1
		spawn_point()
	elif back_inp.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		alive = False
		death()
	else:
		print("---------------------------------------------------------")
	return [loop, alive, win]
	
def kitchen():
	loop = 8
	alive = True
	win = False
	print("---------------------------------------------------------")	
	print('You find yourself in a dimly lit kitchen with dust covering the floor')
	print('A lantern rests on the kitchen island')
	print('Stairs lead up to another rooms')
	kitchen_inp = input('What will you do? ')

	if kitchen_inp.lower() == ('go up stairs'):
		loop = 9
		attic()
	elif kitchen_inp.lower() == ('go east'):
		loop = 7
		back_house()
	elif kitchen_inp.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		alive = False
		death()
	else:
		print("---------------------------------------------------------")
	return [loop, alive, win]

def attic():
	loop = 9
	alive = True
	win = False
	print("---------------------------------------------------------")
	print('You climb up the creaky stairs and find yourself in a small attic')
	print('You can see a maze from a window, aswell as a forest')
	print('But generally find absolutely nothing useful')
	attic_inp = input('What will you do? ')

	if attic_inp.lower() == ('go down'):
		loop = 8
		kitchen()
	elif attic_inp.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		alive = False
		death()
	else:
		print("---------------------------------------------------------")
	return [loop, alive, win]

def maze_front():
	loop = 10
	alive = True
	win = False
	print("---------------------------------------------------------")
	print('You reach the front of a strange maze, it doesnt appear to have been taken care of')
	print('You can see multiple paths on the inside, but there is also a small path to the north')
	mazefront_inp = input('What will you do? ')

	if mazefront_inp.lower() == ('go north'):
		loop = 5
		print('You follow the strange and rocky path')
		cave()
	elif mazefront_inp.lower() == ('go south'):
		loop = 11
		maze_int()
	elif mazefront_inp.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		alive = False
		death()
	else:
		print("---------------------------------------------------------")
	return [loop, alive, win]

def maze_int():
	loop = 11
	alive = True
	win = False
	print("---------------------------------------------------------")
	print('A couple steps into the maze and you can see it is pretty shabby')
	print('However, you can see a couple path ways through')
	print('Everything around you is dark, and you do not have a good feeling')
	maze_inp = input('What will you do? ')

	if maze_inp.lower() == ('go through the shrubs'):
		print('You end up on the other side with cuts and scrapes, but feel something soft')
		print('after a moment you realize the error of your ways')
		print('However, a glimmer of hope shines when you break through the floor you were standing on')
		loop = 12
		easter()
	elif maze_inp.lower() == ('go north'):
		print('You exit the maze and feel like you missed somthing')
		loop = 10
		maze_front()
	elif maze_inp.lower() == ('go west'):
		print('You seem to have ended up in a dire position with a chernobyl bat')
		alive = False
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		death()
	elif maze_inp.lower() == ('go east'):
		print('a moster makes a deligtful snack out of you')
		alive = False
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		death()
	elif maze_inp.lower() == ('go south'):
		print('The world goes black and suddenly your legs begin to burn')
		alive = False
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		death()
	elif maze_inp.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		alive = False
		death()
	else:
		print("---------------------------------------------------------")
	return [loop, alive, win]
def easter():
	loop = 12
	alive = True
	win = False
	print("---------------------------------------------------------")
	print('You find yourself in a strange room with all white walls')
	print('It seems like the lazy developers did not finish this section of the game')
	print('There is nothing in the room but what looks to be desings and items on the floor')
	print('It seems something was being planned here')
	print('You do find what looks to be a weapon')
	print('There is also a staircase along the weast side wall')
	easter_inp = input('What will you do? ')

	if easter_inp.lower() == ('go weast'):
		print('You go up the stairs and find yourself in a cave')
		loop = 5
		cave()
	elif easter_inp.lower() == ('go up'):
		print('Turns out you cant fly and go up, but the monster can come down')
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		alive = False
		death()
	elif easter_inp.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		alive = False
		death()
	else:
		print("---------------------------------------------------------")
	return [loop, alive, win]
def death():  
    dead_inp = input("Do you want to continue? Y/N ")
    if dead_inp.lower() == ("n"):
        exit()
    if dead_inp.lower() == ("y"):
        Play_Zork()

	

