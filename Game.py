'''
	CREATED ON: 14/7/2020

	FINISHED ON: 22/7/2020
'''

import pygame
from random import randrange
from time import sleep

pygame.mixer.init()


#GLOBAL VARIABLES
WIDTH = 500
HEIGHT = 500


#LOADING SPRITES
icon = pygame.image.load('sprites/icon.png')
backgroundSprite = pygame.image.load('sprites/background.png')
playButtonSprite = pygame.image.load('sprites/playbutton.png')
optionsButtonSprite = pygame.image.load('sprites/optionsbutton.png')
quitButtonSprite = pygame.image.load('sprites/quitbutton.png')
titleLabelSprite = pygame.image.load('sprites/titlelabel.png')
oneplayerButtonSprite = pygame.image.load('sprites/oneplayerbutton.png')
twoplayersButtonSprite = pygame.image.load('sprites/twoplayersbutton.png')
backButtonSprite = pygame.image.load('sprites/backbutton.png')
gridSprite = pygame.image.load('sprites/grid.png')
xSprite = pygame.image.load('sprites/x.png')
xTurnSprite = pygame.image.load('sprites/x_turn.png')
xWinsSprite = pygame.image.load('sprites/x_wins.png')
oSprite = pygame.image.load('sprites/o.png')
oTurnSprite = pygame.image.load('sprites/o_turn.png')
oWinsSprite = pygame.image.load('sprites/o_wins.png')
drawWinsSprite = pygame.image.load('sprites/draw_wins.png')
playAgainSprite = pygame.image.load('sprites/playagainbutton.png')
mainmenuSprite = pygame.image.load('sprites/mainmenubutton.png')
youtTurnSprite = pygame.image.load('sprites/your_turn.png')

#LOADING AUDIO
buttonClickSound = pygame.mixer.Sound('music/mouse_click.wav')
tickClickSound = pygame.mixer.Sound('music/clock_ticking.wav')





class Button:  #A SIMPLE BUTTON THAT IS LOADED FROM TWO SPRITES - NORMAL AND CLICKED
	def __init__(self, xPos, yPos, width, height, buttonSprite):
		self.xPos = xPos
		self.yPos = yPos
		self.width = width
		self.height = height
		self.buttonSprite = buttonSprite



	def draw_button(self, screen):
		screen.blit(self.buttonSprite, (self.xPos, self.yPos)) #BLITS THE BUTTON ON THE X POS AND Y POS USING A SPRITE



	def is_clicked(self, event): #RETURNS A TRUE VALUE IF CLICKED
		mouseX = pygame.mouse.get_pos()[0]
		mouseY = pygame.mouse.get_pos()[1]
		if event.type == pygame.MOUSEBUTTONDOWN:
			if mouseX > self.xPos and mouseX < self.xPos + self.width:
				if mouseY > self.yPos and mouseY < self.yPos + self.height:
					return True 
		return False





class Label: #A SIMPLE LABEL WITH NO CLICK DETECTION
	def __init__(self, xPos, yPos, labelSprite):
		self.xPos = xPos
		self.yPos = yPos
		self.labelSprite = labelSprite



	def draw_label(self, screen):
		screen.blit(self.labelSprite, (self.xPos, self.yPos))





class TextLabel:
    def __init__(self, text_color, x, y, text, text_size, text_font):
        self.text_color = text_color
        self.x = x
        self.y = y
        self.text = text
        self.text_size = text_size
        self.text_font = text_font

    def draw_text_label(self,surface):
        font = pygame.font.SysFont(self.text_font, self.text_size)
        text = font.render(self.text, 1, self.text_color)
        surface.blit(text, (self.x, self.y))





class ClickDetector:  #A DETECTOR THAT DETECTS... CLICKS....?
	def __init__(self, xPos, yPos, width, height):
		self.xPos = xPos
		self.yPos = yPos
		self.width = width
		self.height = height



	def is_clicked(self, event): #RETURNS A TRUE VALUE IF CLICKED
		mouseX = pygame.mouse.get_pos()[0]
		mouseY = pygame.mouse.get_pos()[1]
		if event.type == pygame.MOUSEBUTTONDOWN:
		    if mouseX > self.xPos and mouseX < self.xPos + self.width:
		        if mouseY > self.yPos and mouseY < self.yPos + self.height:
		            return True
		return False





#MAIN CLASS
class MainGame:
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption('Tic Tac Toe')
		pygame.display.set_icon(icon)
		
		self.x_player_score = 0
		self.o_player_score = 0



	def Menu(self): #LOADS THE MAIN MENU
		running = True

		#MAIN MENU BUTTONS
		play_button = Button(125,150,250,104,playButtonSprite) 
		options_button = Button(125,260,250,104,optionsButtonSprite)
		quit_button = Button(125,380,250,104,quitButtonSprite)

		title_label = Label(70, 10, titleLabelSprite)


		while running:

			self.screen.fill((0,0,0))

			for event in pygame.event.get():
				if(event.type == pygame.QUIT):
					running = False

				#IF BUTTON IS CLICKED CHECKERS
				if play_button.is_clicked(event):
					buttonClickSound.play() 
					running = False
					self.ChooseGameplay()

				if options_button.is_clicked(event): 
					buttonClickSound.play() 

				if quit_button.is_clicked(event): 
					buttonClickSound.play() 
					running = False


			self.screen.blit(backgroundSprite, (0,0)) #BLITS THE BACKGROUND


			#DRAWS THE BUTTONS
			play_button.draw_button(self.screen)
			options_button.draw_button(self.screen)
			quit_button.draw_button(self.screen)

			title_label.draw_label(self.screen)

			pygame.display.update()



	def ChooseGameplay(self): 
		running = True

		#CHOOSE YOUR GAMEPLAY (1P OR 2P)
		oneplayer_button = Button(125,150,250,104,oneplayerButtonSprite) 
		twoplayer_button = Button(125,300,250,104,twoplayersButtonSprite)
		back_button = Button(10,10,100,100,backButtonSprite)

		while running:

			self.screen.fill((0,0,0))

			for event in pygame.event.get():
				if(event.type == pygame.QUIT):
					running=False

				#IF BUTTON IS CLICKED CHECKERS
				if oneplayer_button.is_clicked(event):
					buttonClickSound.play() 
					running = False
					self.OnePlayer(1)

				if twoplayer_button.is_clicked(event):
					buttonClickSound.play() 
					running = False
					self.TwoPlayer(randrange(1,3))

				if back_button.is_clicked(event):
					buttonClickSound.play() 
					running = False
					self.Menu()


			self.screen.blit(backgroundSprite, (0,0)) #BLITS THE BACKGROUND

			#DRAWS THE BUTTONS
			oneplayer_button.draw_button(self.screen)
			twoplayer_button.draw_button(self.screen)
			back_button.draw_button(self.screen)

			pygame.display.update()



	def OnePlayer(self,turn):
		running = True
		grid = [
			[0,0,0],
			[0,0,0],
			[0,0,0]
		]
		checking_grid = [     #GRID USED TO CHECK IF GAME IS OVER
			[0,0,0],
			[0,0,0],
			[0,0,0]
		]
		x_counts = 0
		o_counts = 0

		taken_squares = 0			
		isWin = False



		while running:

			self.screen.fill((0,0,0))
			self.screen.blit(backgroundSprite, (0,0))


			grid_label = Label(90,90,gridSprite).draw_label(self.screen)

			if turn == 1:
				yourTurnLabel = Label(160,10,youtTurnSprite).draw_label(self.screen)

			x_score_label = TextLabel((255,0,0),160,60,f"X - {self.x_player_score}",40,"comicsans").draw_text_label(self.screen)
			o_score_label = TextLabel((0,255,0),290,60,f"{self.o_player_score} - O",40,"comicsans").draw_text_label(self.screen)


			#COMPUTER MOVES

			#CHECKS HORIZONTAL WIN
			if turn == 2:
				for y_index, y_value in enumerate(grid):
					for x_index, x_value in enumerate(y_value):
						if(grid[y_index][x_index]==1):
							x_counts += 1
						if(grid[y_index][x_index]==2):
							o_counts += 1
						
						if turn == 2:
							if x_counts == 2:
								try:
									grid[y_index][y_value.index(0)]=2
									turn = 1
								except ValueError:
									pass
							if o_counts == 2:
								try:
									grid[y_index][y_value.index(0)]=2
									turn = 1
								except ValueError:
									pass
					o_counts = 0
					x_counts = 0



			#CHECKS FOR A VERTICAL WIN
			if turn == 2:
				y_side = []
				for y_index, y_value in enumerate(grid):
					for x_index, x_value in enumerate(y_value):
						y_side.append(grid[x_index][y_index])
						if(grid[x_index][y_index]==1):
							x_counts += 1
						if(grid[x_index][y_index]==2):
							o_counts += 1

							
						if turn == 2:
							if x_counts == 2:
								try:
									grid[y_side.index(0)][y_index]=2
									turn = 1
								except ValueError:
									pass
							if o_counts == 2:
								try:
									grid[y_side.index(0)][y_index]=2
									turn = 1
								except ValueError:
									pass
					y_side.clear()
					o_counts = 0
					x_counts = 0



			#CHECKS IF THE CENTER IS EMPTY
			if turn == 2:
				if grid[1][1] == 0:
					grid[1][1] = 2
					turn = 1


			#CHECKS IF THE CORNERS ARE EMPTY
			for g in [0,0],[0,2],[2,0],[2,2]:
				if grid[g[0]][g[1]] == 0:
					if turn == 2:
						grid[g[0]][g[1]] = 2
						turn = 1

			#CHECKS IF THE EDGES ARE EMPTY
			for g in [0,1],[1,0],[1,2],[2,1]:
				if grid[g[0]][g[1]] == 0:
					if turn == 2:
						grid[g[0]][g[1]] = 2
						turn = 1




			for event in pygame.event.get():
				if(event.type==pygame.QUIT):
					running=False

				if turn == 1:
					for y in range(100,315,105):
						for x in range(100,315,105):
							if(grid[int((y+5)/105)-1][int((x+5)/105)-1]==0): #IF THE CLICK DETECTOR HASNT BEEN ALREADY CLICKED
								click_detector = ClickDetector(x,y,90,90) #PLACES CLICK DETECTORS ON THE GRID

								if(click_detector.is_clicked(event)):
									tickClickSound.play()
									turn = 2 #SWITCHES TO O (COMPUTER) PLAYER'S TURN
									grid[int((y+5)/105)-1][int((x+5)/105)-1]=1 #TURNS THE CORRESPONDING VALUE ON THE GRID TO 1 (WHICH IS X)



			#ACTUALLY DRAWS THE X'S AND THE O'S
			for y_index,y_value in enumerate(grid): 
				for x_index,x_value in enumerate(y_value):
					if x_value == 1:
						xLabel = Label((x_index+1)*105-5,(y_index+1)*105-5, xSprite).draw_label(self.screen)
					if x_value == 2:
						oLabel = Label((x_index+1)*105-5,(y_index+1)*105-5, oSprite).draw_label(self.screen)



			#CHECKS FOR A WIN HORIZONTALLY
			for y_value in range(0,3):
				for x_value in range(0,3):
					if(grid[y_value][x_value]==1):
						x_counts += 1
					if(grid[y_value][x_value]==2):
						o_counts += 1
				if x_counts == 3:
					self.WinScreen(1,True)
					isWin=True
					running=False
				if o_counts == 3:
					self.WinScreen(2,True)
					isWin=True
					running=False
				o_counts = 0
				x_counts = 0


			#CHECKS FOR A WIN VERTICALLY
			for y_value in range(0,3):
				for x_value in range(0,3):
					if(grid[x_value][y_value]==1):
						x_counts += 1
					if(grid[x_value][y_value]==2):
						o_counts += 1
				if x_counts == 3:
					self.WinScreen(1,True)
					isWin=True
					running=False
				if o_counts == 3:
					self.WinScreen(2,True)
					isWin=True
					running=False
				o_counts = 0
				x_counts = 0


			#CHECKS FOR A WIN DIAGONALLY
			if(grid[0][0]==1 and grid[1][1]==1 and grid[2][2]==1) or (grid[0][2]==1 and grid[1][1]==1 and grid[2][0]==1):
				self.WinScreen(1,True)
				isWin=True
				running=False
			if(grid[0][0]==2 and grid[1][1]==2 and grid[2][2]==2) or (grid[0][2]==2 and grid[1][1]==2 and grid[2][0]==2):
				self.WinScreen(2,True)
				isWin=True
				running=False


			#CHECK IF THE SQUARES ARE TAKEN, THIS IS USED LATER ON TO CHECK IF THE GAME IS OVER
			for y_index,y_value in enumerate(grid):
				for x_index,x_value in enumerate(y_value):
					if x_value != 0 and checking_grid[y_index][x_index] != 1:
						'''I MADE A CHECKING GRID SO THAT IT DOESNT JUST LOOP OVER THE SAME SQUARE 
						9 TIMES AND JUST CAUSE A GAME OVER WHEN THE GAME ISNT ACTUALLY OVER '''
						checking_grid[y_index][x_index] = 1 
						taken_squares += 1


			#IF ALL THE SQUARES ARE TAKEN AND THERE IS NO WINNER THEN END THE GAME AS A DRAW
			if taken_squares == 9 and isWin == False:
				self.WinScreen(0,True)
				running=False


			pygame.display.update()






	def TwoPlayer(self,turn):
		running = True
		grid = [              #ACTUAL X AND O GRID
			[0,0,0],
			[0,0,0],
			[0,0,0]
		]
		checking_grid = [     #GRID USED TO CHECK IF GAME IS OVER
			[0,0,0],
			[0,0,0],
			[0,0,0]
		]
		x_counts = 0
		o_counts = 0
		taken_squares = 0
		isWin = False


		while running:
			
			self.screen.fill((0,0,0))
			self.screen.blit(backgroundSprite, (0,0)) #BLITS THE BACKGROUND
			
			#DEFINING OBJECTS
			grid_label = Label(90,90,gridSprite).draw_label(self.screen)

			#DRAWS TURN LABELS
			if turn == 1:
				xTurnLabel = Label(160,10,xTurnSprite).draw_label(self.screen)
			if turn == 2:
				oTurnLabel = Label(160,10,oTurnSprite).draw_label(self.screen)

			x_score_label = TextLabel((255,0,0),160,60,f"X - {self.x_player_score}",40,"comicsans").draw_text_label(self.screen)
			o_score_label = TextLabel((0,255,0),290,60,f"{self.o_player_score} - O",40,"comicsans").draw_text_label(self.screen)

			for event in pygame.event.get():
				if(event.type==pygame.QUIT):
					running=False

				for y in range(100,315,105):
					for x in range(100,315,105):
						if(grid[int((y+5)/105)-1][int((x+5)/105)-1]==0): #IF THE CLICK DETECTOR HASNT BEEN ALREADY CLICKED
							click_detector = ClickDetector(x,y,90,90) #PLACES CLICK DETECTORS ON THE GRID

							if(click_detector.is_clicked(event)):
								tickClickSound.play()
								if turn == 1:
									turn = 2 #SWITCHES TO O PLAYER'S TURN
									grid[int((y+5)/105)-1][int((x+5)/105)-1]=1 #TURNS THE CORRESPONDING VALUE ON THE GRID TO 1 (WHICH IS X)
								elif turn == 2:
									turn = 1 #SWITCHES TO X PLAYER'S TURN
									grid[int((y+5)/105)-1][int((x+5)/105)-1]=2 #TURNS THE CORRESPONDING VALUE ON THE GRID TO 2 (WHICH IS O)

			#ACTUALLY DRAWS THE XS AND OS ON THE GRID
			for y_index,y_value in enumerate(grid): 
				for x_index,x_value in enumerate(y_value):
					if x_value == 1:
						xLabel = Label((x_index+1)*105-5,(y_index+1)*105-5, xSprite).draw_label(self.screen)
					if x_value == 2:
						oLabel = Label((x_index+1)*105-5,(y_index+1)*105-5, oSprite).draw_label(self.screen)


			#CHECKS FOR A WIN HORIZONTALLY
			for y_value in range(0,3):
				for x_value in range(0,3):
					if(grid[y_value][x_value]==1):
						x_counts += 1
					if(grid[y_value][x_value]==2):
						o_counts += 1
				if x_counts == 3:
					self.WinScreen(1,False)
					isWin=True
					running=False
				if o_counts == 3:
					self.WinScreen(2,False)
					isWin=True
					running=False
				o_counts = 0
				x_counts = 0


			#CHECKS FOR A WIN VERTICALLY
			for y_value in range(0,3):
				for x_value in range(0,3):
					if(grid[x_value][y_value]==1):
						x_counts += 1
					if(grid[x_value][y_value]==2):
						o_counts += 1
				if x_counts == 3:
					self.WinScreen(1,False)
					isWin=True
					running=False
				if o_counts == 3:
					self.WinScreen(2,False)
					isWin=True
					running=False
				o_counts = 0
				x_counts = 0


			#CHECKS FOR A WIN DIAGONALLY
			if(grid[0][0]==1 and grid[1][1]==1 and grid[2][2]==1) or (grid[0][2]==1 and grid[1][1]==1 and grid[2][0]==1):
				self.WinScreen(1,False)
				isWin=True
				running=False
			if(grid[0][0]==2 and grid[1][1]==2 and grid[2][2]==2) or (grid[0][2]==2 and grid[1][1]==2 and grid[2][0]==2):
				self.WinScreen(2,False)
				isWin=True
				running=False


			#CHECK IF THE SQUARES ARE TAKEN, THIS IS USED LATER ON TO CHECK IF THE GAME IS OVER
			for y_index,y_value in enumerate(grid):
				for x_index,x_value in enumerate(y_value):
					if x_value != 0 and checking_grid[y_index][x_index] != 1:
						'''I MADE A CHECKING GRID SO THAT IT DOESNT JUST LOOP OVER THE SAME SQUARE 
						9 TIMES AND JUST CAUSE A GAME OVER WHEN THE GAME ISNT ACTUALLY OVER '''
						checking_grid[y_index][x_index] = 1 
						taken_squares += 1


			#IF ALL THE SQUARES ARE TAKEN AND THERE IS NO WINNER THEN END THE GAME AS A DRAW
			if taken_squares == 9 and isWin == False:
				self.WinScreen(0,False)
				running=False
			

			pygame.display.update()





	def WinScreen(self,winner,isSinglePlayer):
		running = True

		if winner == 1:
			self.x_player_score += 1
		if winner == 2:
			self.o_player_score += 1
		
		while running:
			self.screen.fill((0,0,0))

			self.screen.blit(backgroundSprite, (0,0)) #BLITS THE BACKGROUND

			playAgain_button = Button(120,150,250,104,playAgainSprite)
			mainMenu_button = Button(120,270,250,104,mainmenuSprite)

			for event in pygame.event.get():
				if(event.type==pygame.QUIT):
					running=False

				if playAgain_button.is_clicked(event):
					buttonClickSound.play() 
					if winner == 1:
						if isSinglePlayer == False:
							self.TwoPlayer(2)
						else:
							self.OnePlayer(2)
					if winner == 2:
						if isSinglePlayer == False:
							self.TwoPlayer(1)
						else:
							self.OnePlayer(1)
					if winner == 0:
						if isSinglePlayer == False:
							self.TwoPlayer(randrange(1,3))
						else:
							self.OnePlayer(randrange(1,3))
					running=False


				if mainMenu_button.is_clicked(event):
					buttonClickSound.play() 
					self.x_player_score -= self.x_player_score 
					self.o_player_score -= self.o_player_score
					self.Menu()
					running=False



			if winner == 1:
				xLabel = Label(100,30,xWinsSprite)
				xLabel.draw_label(self.screen)
			if winner == 2:
				oLabel = Label(100,30,oWinsSprite)
				oLabel.draw_label(self.screen)
			if winner == 0:
				dLabel = Label(100,30,drawWinsSprite)
				dLabel.draw_label(self.screen)



			playAgain_button.draw_button(self.screen)
			mainMenu_button.draw_button(self.screen)


			pygame.display.update()





if __name__ == '__main__':
	game = MainGame().Menu() #LOAD THE MAIN MENU
	pygame.quit()
	quit()