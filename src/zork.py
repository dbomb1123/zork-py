import items

def Play_Zork():
	loop = 1
	print("---------------------------------------------------------")
	print("Welcome to Zork - The Unofficial Python Version.")

	while alive == True:
		# First Input function
                def spawn_point():
                        if loop == 1:
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
                        elif second.lower() == ("read leaflet"):
                        	print("---------------------------------------------------------")
                        	print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
                        elif second.lower() == ("kick the bucket"):
                        	print("---------------------------------------------------------")
                        	print("You die.")
                        	print("---------------------------------------------------------")
                        	alive = False

                        else:
                        	print("---------------------------------------------------------")      
                # North of House
                def north_of_house():
                        if loop == 2:
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

                        else:
                        	print("---------------------------------------------------------")

		# Southwest Loop
		def southwest():
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


                        else:
				print("---------------------------------------------------------")
		

		# East Loop and Grating Input
		def east_grating():
			if loop == 4:
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

			else:
				print("---------------------------------------------------------")	


		# Grating Loop and Cave Input
		def cave():
			if loop == 5:
				print("---------------------------------------------------------")
				print("You are in a tiny cave with a dark, forbidding staircase leading down.")
				print("There is a skeleton of a human male in one corner.")
				cave_inp = input("What do you do? ")

			if cave_inp.lower() == ("descend staircase"):
				loop = 6
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
			elif cave_inp.lower() == ("scale staircase"):
				loop = 6
				end_game()
			elif cave_inp.lower() == ("kick the bucket"):
				print("---------------------------------------------------------")
				print("You die.")
				print("---------------------------------------------------------")
                                alive = False

			elif cave_inp.lower() == ("scale staircase"):
				loop = 6
				end_game()
			else:
				print("---------------------------------------------------------")


		# End of game
		def end_game():
			if loop == 6:
				print("---------------------------------------------------------")
				print("You have entered a mud-floored room.")
				print("Lying half buried in the mud is an old trunk, bulging with jewels.")
				last_inp = input("What do you do? ")

			if last_inp.lower() == ("open trunk"):
				print("---------------------------------------------------------")
				print("You have found the Jade Statue and have completed your quest!")
			elif last.inp.lower() == ("kick the bucket"):
				print("---------------------------------------------------------")
				print("You die.")
				print("---------------------------------------------------------")
				
			else:
				print("---------------------------------------------------------")
			
			# Exit loop at the end of game
			exit_inp = input("Do you want to continue? Y/N ")
			if exit_inp.lower() == ("n"):
				exit()
			if exit_inp.lower() == ("y"):
				Play_Zork()
	alive = True
	
	def death():
                dead_inp = input("Do you want to continue? Y/N ")
        if dead_inp.lower() == ("n"):
		exit()
	if dead_inp.lower() == ("y"):
		Play_Zork()

        if alive == False:
                death()
