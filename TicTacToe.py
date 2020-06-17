#Heading:
name = "TIC - TAC - TOE"	
print(name.center(67,'•'))
print("\t\t\t\t\t\t\t~Ameya Jain")
print()


#Board Sample:
	
print(" BOARD - SPOTS\t\t\t\tHow To Play?")
print(" -------------")		
print(" | 0 | 1 | 2 |\t\t•The player should choose the spot by the ")
print("  -----------\t\t number given in the board spot at left.")
print(" | 3 | 4 | 5 |\t\t•Please choose the correct numbers from 0-8")
print("  -----------\t\t and Enter for the next player's turn.")
print(" | 6 | 7 | 8 |\t\t•The 3 consecutive entries of X or O will")
print(" -------------\t\t win the game.")		
print()


	
	
def start():
	
	#Board playing function:
	board = [  0, 1, 2,
				  3, 4, 5,
				  6, 7, 8, ]
				
	def show():			
		print(" -------------")		
		print(" |",board[0],"|",board[1],"|",		board[2],	"|")
		print("  -----------")
		print(" |",board[3],"|",board[4],"|",					board[5],"|")
		print("  -----------")

		print(" |",board[6],"|",board[7],"|",					board[8],"|")
		print(" -------------")

		print()


	#X Player function:

	def x():

		print()
		player_x = int(input(" Player X --> "))

	
		if board[player_x] != 'X' and								board[player_x] != 'O' :
			board[player_x] = 'X'
		
		else:
			print("The spot choosen is already taken. Please choose another spot.")
			x()
		
		show()
	
		#Winner conditions:
		if board[0] == 'X' and board[1] == 'X' 			and board[2] == 'X':
			print("Player X wins.")
				
			print("\nIf you want to restart the game, enter Y and to exit the game,\nenter N")
			a = input("--> ")
			if a == 'y' or a == 'Y':
				start()
			elif a == 'n' or a == 'N':
				exit(0)
				
		elif board[0] == 'X' and board[4] == 'X' 			and board[8] == 'X':
			print("Player X wins.")
				
			print("\nIf you want to restart the game, enter Y and to exit the game,\nenter N")
			a = input("--> ")
			if a == 'y' or a == 'Y':
				start()
			elif a == 'n' or a == 'N':
				exit(0)
				
		elif board[0] == 'X' and board[3] == 'X' 			and board[6] == 'X':
			print("Player X wins.")
				
			print("\nIf you want to restart the game, enter Y and to exit the game,\nenter N")
			a = input("--> ")
			if a == 'y' or a == 'Y':
				start()
			elif a == 'n' or a == 'N':
				exit(0)
				
		elif board[1] == 'X' and board[4] == 'X' 			and board[7] == 'X':
			print("Player X wins.")
				
			print("\nIf you want to restart the game, enter Y and to exit the game,\nenter N")
			a = input("--> ")
			if a == 'y' or a == 'Y':
				start()
			elif a == 'n' or a == 'N':
				exit(0)
				
		elif board[2] == 'X' and board[4] == 'X' 			and board[6] == 'X':
			print("Player X wins.")
				
			print("\nIf you want to restart the game, enter Y and to exit the game,\nenter N")
			a = input("--> ")
			if a == 'y' or a == 'Y':
				start()
			elif a == 'n' or a == 'N':
				exit(0)
				
		elif board[2] == 'X' and board[5] == 'X' 			and board[8] == 'X':
			print("Player X wins.")
				
			print("\nIf you want to restart the game, enter Y and to exit the game,\nenter N")
			a = input("--> ")
			if a == 'y' or a == 'Y':
				start()
			elif a == 'n' or a == 'N':
				exit(0)
			
		elif board[3] == 'X' and board[4] == 'X' 			and board[5] == 'X':
			print("Player X wins.")
			
				
			print("\nIf you want to restart the game, enter Y and to exit the game,\nenter N")
			a = input("--> ")
			if a == 'y' or a == 'Y':
				start()
			elif a == 'n' or a == 'N':
				exit(0)
				
		elif board[6] == 'X' and board[7] == 'X' 			and board[8] == 'X':
			print("Player X wins.")
			
			print("\nIf you want to restart the game, enter Y and to exit the game,\nenter N")
			a = input("--> ")
			if a == 'y' or a == 'Y':
				start()
			elif a == 'n' or a == 'N':
				exit(0)
		
		
	
	
	#O Player function:

	def o():
		player_o = int(input(" Player O --> "))
		
		if board[player_o] != 'O' and 							board[player_o] != 'X':
			board[player_o] = 'O'
		
		else:
			print("The spot choosen is already taken. Please choose another spot.")
			o()
		show()
		
	
		
		#Winner conditions:
		if board[0] == 'O' and board[1] == 'O' 			and board[2] == 'O':
			print("Player O wins.")
				
			print("\nIf you want to restart the game, enter Y and to exit the game,\nenter N")
			a = input("--> ")
			if a == 'y' or a == 'Y':
				start()
			elif a == 'n' or a == 'N':
				exit(0)
				
		elif board[0] == 'O' and board[4] == 'O' 			and board[8] == 'O':
			print("Player O wins.")
				
			print("\nIf you want to restart the game, enter Y and to exit the game,\nenter N")
			a = input("--> ")
			if a == 'y' or a == 'Y':
				start()
			elif a == 'n' or a == 'N':
				exit(0)
				
		elif board[0] == 'O' and board[3] == 'O' 			and board[6] == 'O':
			print("Player O wins.")
				
			print("\nIf you want to restart the game, enter Y and to exit the game,\nenter N")
			a = input("--> ")
			if a == 'y' or a == 'Y':
				start()
			elif a == 'n' or a == 'N':
				exit(0)
				
		elif board[1] == 'O' and board[4] == 'O' 			and board[7] == 'O':
			print("Player O wins.")
				
			print("\nIf you want to restart the game, enter Y and to exit the game,\nenter N")
			a = input("--> ")
			if a == 'y' or a == 'Y':
				start()
			elif a == 'n' or a == 'N':
				exit(0)
				
		elif board[2] == 'O' and board[4] == 'O' 			and board[6] == 'O':
			print("Player O wins.")
				
			print("\nIf you want to restart the game, enter Y and to exit the game,\nenter N")
			a = input("--> ")
			if a == 'y' or a == 'Y':
				start()
			elif a == 'n' or a == 'N':
				exit(0)
				
		elif board[2] == 'O' and board[5] == 'O' 			and board[8] == 'O':
			print("Player O wins.")
				
			print("\nIf you want to restart the game, enter Y and to exit the game,\nenter N")
			a = input("--> ")
			if a == 'y' or a == 'Y':
				start()
			elif a == 'n' or a == 'N':
				exit(0)
				
		elif board[3] == 'O' and board[4] == 'O' 			and board[5] == 'O':
			print("Player O wins.")
				
			print("\nIf you want to restart the game, enter Y and to exit the game,\nenter N")
			a = input("--> ")
			if a == 'y' or a == 'Y':
				start()
			elif a == 'n' or a == 'N':
				exit(0)
				
		elif board[6] == 'O' and board[7] == 'O' 			and board[8] == 'O':
			print("Player O wins.")
				
			print("\nIf you want to restart the game, enter Y and to exit the game,\nenter N")
			a = input("--> ")
			if a == 'y' or a == 'Y':
				start()
			elif a == 'n' or a == 'N':
				exit(0)
				
	
	
	
	
	#Game loop for starting from x:
	while True:
		x()
		o()
		x()
		o()
		x()
		o()
		x()
		o()
		x()
		
		print("The game is tied.\nPlease play again")
		start()
	
	
	
#Final loop to start the game:	
start()
	