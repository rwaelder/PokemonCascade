import os, pygame
from pygame.locals import *
from saveLoad import load_map_square
from trainer import MainPlayer
from helpers import load_image



class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.load_sprites()
		self.image = self.standDown
		self.image = pygame.transform.scale(self.image, (BOXSIZE, BOXSIZE))
		self.rect = self.image.get_rect()
		self.x = 45
		self.y = 45
		self.moved = False
		self.lastMove = (0,0)

		self.isWalking = True
		self.isRunning = False
		self.isBiking = False
		self.isSurfing = False
		self.facing = (0, 1)

	def load_sprites(self):
		self.standDown = load_image('trainers/Player_and_Pokemon/2_1.png')
		self.standLeft = load_image('trainers/Player_and_Pokemon/2_2.png')
		self.standRight = load_image('trainers/Player_and_Pokemon/2_3.png')
		self.standUp = load_image('trainers/Player_and_Pokemon/2_4.png')

		self.walkDown1 = load_image('trainers/Player_and_Pokemon/1_1.png')
		self.walkDown2 = load_image('trainers/Player_and_Pokemon/3_1.png')

		self.walkLeft1 = load_image('trainers/Player_and_Pokemon/1_2.png')
		self.walkLeft2 = load_image('trainers/Player_and_Pokemon/3_2.png')

		self.walkRight1 = load_image('trainers/Player_and_Pokemon/1_3.png')
		self.walkRight2 = load_image('trainers/Player_and_Pokemon/3_3.png')

		self.walkUp1 = load_image('trainers/Player_and_Pokemon/1_4.png')
		self.walkUp2 = load_image('trainers/Player_and_Pokemon/3_4.png')

	def update(self, move):
		self.update_sprite(move)
		self.x += move[0]
		self.y += move[1]
		left, top = left_top_coords_of_box(7, 5)
		self.image = pygame.transform.scale(self.image, (BOXSIZE, BOXSIZE))
		self.rect.x = left
		self.rect.y = top
		self.lastMove = move

	def update_sprite(self, move):
		if move == (0, -1):
			if self.moved:
				self.image = self.walkUp2
			else:
				self.image = self.walkUp1
			self.moved = not self.moved

		elif move == (0, 1):
			if self.moved:
				self.image = self.walkDown2
			else:
				self.image = self.walkDown1
			self.moved = not self.moved

		elif move == (-1, 0):
			if self.moved:
				self.image = self.walkLeft2
			else:
				self.image = self.walkLeft1
			self.moved = not self.moved

		elif move == (1, 0):
			if self.moved:
				self.image = self.walkRight2
			else:
				self.image = self.walkRight1
			self.moved = not self.moved

		elif move == (0, 0):
			if self.lastMove == (0, -1):
				self.image = self.standUp
			elif self.lastMove == (0, 1):
				self.image = self.standDown
			elif self.lastMove == (-1, 0):
				self.image = self.standLeft
			elif self.lastMove == (1, 0):
				self.image = self.standRight

		if move != (0, 0):
			self.facing = move
		self.image = pygame.transform.scale(self.image, (BOXSIZE, BOXSIZE))

	def turn(self, move):
		if move == (0, 0):
			return
		elif move == (0, -1):
			self.image = self.standUp
		elif move == (0, 1):
			self.image = self.standDown
		elif move == (-1, 0):
			self.image = self.standLeft
		elif move == (1, 0):
			self.image = self.standRight

		if move != (0, 0):
			self.facing = move

		self.image = pygame.transform.scale(self.image, (BOXSIZE, BOXSIZE))

	def get_position(self):
		return self.x, self.y

def tuple_add(var1, var2):
	var3 = []
	for i in range(len(var1)):
		var3.append(var1[i] + var2[i])

	return tuple(var3)

def left_top_coords_of_box(boxx, boxy):
	left = boxx * (BOXSIZE) + XMARGIN
	top = boxy * (BOXSIZE) + YMARGIN
	return (left, top)

def interact(mainMap, player):
	interaction = mainMap.interact(player)


# def draw_map(mapImages, displayArea):

# 	width = len(displayArea)
# 	height = len(displayArea[0])
	
# 	for x in range(width):
# 		for y in range(height):
# 			tileX, tileY = displayArea[x][y]
# 			tileImage = mapImages[tileX][tileY]
# 			left, top = left_top_coords_of_box(x, y)

# 			DISPLAYSURF.blit(tileImage, (left, top))

def draw_map(mainMap, displayArea):
	image = mainMap.draw_screen(displayArea, tileSize=BOXSIZE)
	DISPLAYSURF.blit(image, (0,0))

def draw_mapImages(mapImages, offset):
	width = len(mapImages)
	height = len(mapImages[0])

	for x in range(width):
		for y in range(height):
			left, top = left_top_coords_of_box(x-2, y-2)
			DISPLAYSURF.blit(mapImages[x][y], (left-offset[0], top-offset[1]))

def update_map(mainMap, mapImages, player, move):
	mapImages = mainMap.load_relevant_tiles(player, mapImages, move, tileSize=BOXSIZE)

	return mapImages

def load_map(mapSquare):
	mapSize = len(mapSquare)
	scaleSize = BOXSIZE

	mapImages = []
	for x in range(mapSize):
		column = []
		for y in range(mapSize):
			tileImage = mapSquare[x][y].draw(scaleSize)
			
			column.append(tileImage)
		mapImages.append(column)
	return mapImages


def main():
	global DISPLAYSURF, FPSCLOCK, FPS

	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	FPS = 30

	global XMARGIN, YMARGIN, BOXSIZE

	width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

	windowHeight = int(0.6 * height)
	windowWidth = int(1.5 * windowHeight)

	XMARGIN = YMARGIN = 0
	BOXSIZE = int( (windowWidth / 15))

	DISPLAYSURF = pygame.display.set_mode((windowWidth, windowHeight))
	pygame.display.set_caption('Map Test')

	player = Player()

	playerSprite = pygame.sprite.Group()
	playerSprite.add(player)

	startX = player.get_position()[0] - 7
	endX = startX + 15

	startY = player.get_position()[1] - 5
	endY = startY + 11



	mainMap = load_map_square('main_map')
	mapSquare = mainMap.tiles
	mapImages = mainMap.new_screen_images_array(player, tileSize=BOXSIZE)



	global mapCoords
	mapCoords = []
	for x in range(len(mapSquare)):
		column = []
		for y in range(len(mapSquare)):
			column.append((x, y))
		mapCoords.append(column)


	count = 0
	maxCount = 4
	running = True
	lastKeys = None
	while running:
		# offsetX, offsetY = 0, 0
		change = False
		count += 1
		if count == maxCount:
			count = 0

		position = player.get_position()
		move = (0,0)

		columns = mapCoords[startX:endX]
		displayArea = [y[startY:endY] for y in columns]

		keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				running = False
			else:
				pass

			# elif event.type == KEYDOWN:
				# if event.key == K_UP:
				# 	move = (0, -1)

				# elif event.key == K_DOWN:
				# 	move = (0, 1)

				# elif event.key == K_LEFT:
				# 	move = (-1, 0)

				# elif event.key == K_RIGHT:
				# 	move = (1, 0)

				# else:
				# 	pass

		if keys[K_SPACE]:
			interact(mainMap, player)

		elif keys[K_UP] or keys[K_w]:
			move = (0, -1)
		elif keys[K_DOWN] or keys[K_s]:
			move = (0, 1)
		elif keys[K_LEFT] or keys[K_a]:
			move = (-1, 0)
		elif keys[K_RIGHT] or keys[K_d]:
			move = (1, 0)

		if move != (0, 0):

			if count == 0 and mainMap.passable(player, move):
				change = True
				offsetX = int(1*BOXSIZE/4) * move[0]
				offsetY = int(1*BOXSIZE/4) * move[1]

			elif count == 1 and mainMap.passable(player, move):
				change = True
				offsetX = int(2*BOXSIZE/4) * move[0]
				offsetY = int(2*BOXSIZE/4) * move[1]

			elif count == 2 and mainMap.passable(player, move):
				change = True
				offsetX = int(3*BOXSIZE/4) * move[0]
				offsetY = int(3*BOXSIZE/4) * move[1]

			elif count == 3 and mainMap.passable(player, move):
				change = True
				startX += move[0]
				endX += move[0]
				startY += move[1]
				endY += move[1]
				offsetX, offsetY = 0, 0
			
				player.update(move)

				mapImages = update_map(mainMap, mapImages, player, move)

			# elif count == 3:
			# 	change = True
			# 	player.turn(move)


		if change:
			draw_mapImages(mapImages, (offsetX, offsetY))
			# draw_map(mainMap, displayArea)
			
			playerSprite.draw(DISPLAYSURF)

			pygame.display.update()

		FPSCLOCK.tick(FPS)



if __name__ == '__main__':
	main()
	pygame.quit()









