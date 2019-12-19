import os, pygame
from pygame.locals import *
from random import choice
from saveLoad import load_map_square
from trainer import MainPlayer
from helpers import load_image
from colors import MAGENTA

from mixer import Mixer

from pokemonList import random_pokemon, get_pokemon

from battle3 import WildBattle


class Player(pygame.sprite.Sprite):
	def __init__(self, scale, party=[]):
		pygame.sprite.Sprite.__init__(self)

		self.trainer = MainPlayer(party=party)
		# self.party = party
		self.scale = scale
		self.load_sprites(self.scale)
		# self.image = self.standDown
		# self.image = pygame.transform.scale(self.image, (BOXSIZE, BOXSIZE))
		self.image = self.sprites['walk-down-0']
		self.rect = self.image.get_rect()
		left, top = left_top_coords_of_box(7, 4)
		self.rect.x = left
		self.rect.y = top

		# # old test
		# self.x = 75
		# self.y = 80

		self.x = 48
		self.y = 48

		self.moved = False
		self.lastMove = (0,0)

		self.isWalking = True
		self.isRunning = False
		self.isBiking = False
		self.isSurfing = False
		self.facing = (0, 1)
		self.surfCount = 0

	def toggle_run(self):
		self.isWalking = not self.isWalking
		self.isRunning = not self.isRunning
		self.update_sprite((0, 0))

	def toggle_bike(self):
		if self.isBiking:
			self.isWalking = True
			self.isRunning = False
			self.isBiking = False
			self.rect.x += 8*self.scale
			self.update_sprite((0, 0))

		else:
			self.isWalking = False
			self.isRunning = False
			self.isBiking = True
			self.rect.x -= 8*self.scale
			self.update_sprite((0, 0))

	def toggle_surf(self):
		if self.isSurfing:
			self.isWalking = True
			self.isRunning = False
			self.isBiking = False
			self.isSurfing = False
			self.rect.x += 8*self.scale
			self.update_sprite((0, 0))

		else:
			self.isWalking = False
			self.isRunning = False
			self.isBiking = False
			self.isSurfing = True
			self.rect.x -= 8*self.scale
			self.update_sprite((0, 0))

	def load_sprites(self, scale):
		spriteList = [x[2] for x in os.walk('trainers/Red/')][0]

		self.sprites = {}

		for spriteFile in spriteList:
			image = load_image('trainers/Red/' + spriteFile, scale=scale)
			self.sprites[ spriteFile.replace('.png', '') ] = image


	def update(self, move):
		self.update_sprite(move)
		self.x += move[0]
		self.y += move[1]
		# left, top = left_top_coords_of_box(7, 5)
		# self.rect.x = left
		# self.rect.y = top
		self.lastMove = move

	def sprite_direction(self, move):
		return

	def walk_sprite_update(self, move):
		return

	def surf_sprite_update(self, move):
		spriteName = 'surf-'

		x, y = move

		if move == (0, 0):
			x, y = self.facing

		if y > 0:
			spriteName += 'down-'
		elif y < 0:
			spriteName += 'up-'
		elif x > 0:
			spriteName += 'right-'
		elif x < 0:
			spriteName += 'left-'

		if self.surfCount > 5:
			spriteName += '0'
		else:
			spriteName += '1'

		self.surfCount += 1
		if self.surfCount == 10:
			self.surfCount = 0

		self.image = self.sprites[spriteName]
		return



	def update_sprite(self, move):
		spriteName = ''
		if self.isWalking:
			spriteName += 'walk-'
		elif self.isRunning:
			spriteName += 'run-'
		elif self.isBiking:
			spriteName += 'bike-'
		elif self.isSurfing:
			self.surf_sprite_update(move)
			return

		x, y = move

		if move == (0, 0):
			x, y = self.facing

		if y > 0:
			spriteName += 'down-'
		elif y < 0:
			spriteName += 'up-'
		elif x > 0:
			spriteName += 'right-'
		elif x < 0:
			spriteName += 'left-'

		if move == (0, 0):
			spriteName += '0'
			self.image = self.sprites[spriteName]
			return

		if self.moved:
			spriteName += '1'
		else:
			spriteName += '2'
		self.moved = not self.moved

		self.image = self.sprites[spriteName]

		if move != (0, 0):
			self.facing = move

	def turn(self, move):
		if self.isSurfing:
			return

		if move == (0, 0):
			return
		else:
			self.update_sprite((0,0))

		if move != (0, 0):
			self.facing = move


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



def draw_map(mainMap, displayArea):
	image = mainMap.draw_screen(displayArea, tileSize=BOXSIZE)
	DISPLAYSURF.blit(image, (0,0))

def draw_screen(mapImages, playerSprite, mapDecorations, offset):
	draw_mapImages(mapImages, offset)
	playerSprite.draw(DISPLAYSURF)
	draw_mapDecorations(mapDecorations, offset)

def draw_mapImages(mapImages, offset):
	width = len(mapImages)
	height = len(mapImages[0])

	for x in range(width):
		for y in range(height):
			left, top = left_top_coords_of_box(x-2, y-2)
			DISPLAYSURF.blit(mapImages[x][y], (left-offset[0], top-offset[1]))

def draw_mapDecorations(mapDecorations, offset):
	width = len(mapDecorations)
	height = len(mapDecorations[0])

	for x in range(width):
		for y in range(height):
			if mapDecorations[x][y] == None:
				pass
			else:
				left, top = left_top_coords_of_box(x-2, y-2)
				DISPLAYSURF.blit(mapDecorations[x][y], (left-offset[0], top-offset[1]))

def update_map(mainMap, mapImages, mapDecorations, player, move):
	mapImages, mapDecorations = mainMap.load_relevant_tiles(player, mapImages, mapDecorations, move, tileSize=BOXSIZE)

	return mapImages, mapDecorations

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

def do_move(mapImages, playerSprite, mapDecorations, player, move):
	if player.isWalking:
		maxCount = 10
	elif player.isRunning:
		maxCount = 8
	elif player.isBiking:
		maxCount = 5
	elif player.isSurfing:
		maxCount = 5
	for count in range(1, maxCount+1):
		offsetX = int(count * BOXSIZE / maxCount * move[0])
		offsetY = int(count * BOXSIZE / maxCount * move[1])

		for event in pygame.event.get():
			pass

		if count == maxCount-2:
			player.turn(move)


		draw_screen(mapImages, playerSprite, mapDecorations, (offsetX, offsetY))

		pygame.display.update()
		FPSCLOCK.tick(FPS)

def do_jump(mapImages, playerSprite, mapDecorations, player, move):
	maxCount = 10
	for count in range(1, maxCount+1):
		offsetX = int(count * BOXSIZE / maxCount * move[0])
		offsetY = int(count * BOXSIZE / maxCount * move[1])

		for event in pygame.event.get():
			pass

		if count % 2 == 0:
			player.update_sprite(move)

		draw_screen(mapImages, playerSprite, mapDecorations, (offsetX, offsetY))

		pygame.display.update()
		FPSCLOCK.tick(FPS)


	




def main():
	global DISPLAYSURF, FPSCLOCK, FPS

	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	FPS = 60
	pygame.key.set_repeat(int(1000 / FPS))

	global XMARGIN, YMARGIN, BOXSIZE

	width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

	maxHeight = int(0.8 * height)
	maxWidth = int(1.5 * maxHeight)

	XMARGIN = YMARGIN = 0
	BOXSIZE = 16
	maxBoxSize = int( (maxWidth / 15))
	for scale in range(2, 5):
		if BOXSIZE * scale > maxBoxSize:
			break
	scale -= 1
	scale = 3
	BOXSIZE *= scale


	windowWidth = 15 * BOXSIZE
	windowHeight = 10 * BOXSIZE

	DISPLAYSURF = pygame.display.set_mode((windowWidth, windowHeight))
	pygame.display.set_caption('Map Test')
	DISPLAYSURF.set_colorkey((255, 0, 255))

	mixer = Mixer()

	player = Player(scale, party=[get_pokemon(132, level=50), random_pokemon(level=50), random_pokemon(level=50)])
	# player = Player()

	playerSprite = pygame.sprite.Group()
	playerSprite.add(player)

	startX = player.get_position()[0] - 7
	endX = startX + 15

	startY = player.get_position()[1] - 5
	endY = startY + 11



	mainMap = load_map_square('main_map_full_test')
	mapSquare = mainMap.tiles
	mapImages, mapDecorations = mainMap.new_screen_images_array(player, tileSize=BOXSIZE)

	mixer.play_song(mainMap.tiles[player.x][player.y].group)

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
	change = True	
	while running:
		offsetX, offsetY = 0, 0

		count += 1
		if count == maxCount:
			count = 0

		position = player.get_position()
		move = (0,0)

		columns = mapCoords[startX:endX]
		displayArea = [y[startY:endY] for y in columns]

		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				running = False

			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					interact(mainMap, player)
				elif event.key in [K_UP, K_w]:
					move = (0, -1)

				elif event.key in [K_DOWN, K_s]:
					move = (0, 1)

				elif event.key in [K_LEFT, K_a]:
					move = (-1, 0)

				elif event.key in [K_RIGHT, K_d]:
					move = (1, 0)

			elif event.type == KEYUP:
				if event.key == K_x:
					player.toggle_run()

				elif event.key == K_b:
					player.toggle_bike()
					change = True

				elif event.key == K_v and mainMap.surfable(player):
					player.toggle_surf()
					move = player.facing
					change = True

				else:
					pass

		if move != (0, 0):
			if mainMap.passable(player, move):
				change = True
				player.update(move)
				do_move(mapImages, playerSprite, mapDecorations, player, move)
				mapImages, mapDecorations = update_map(mainMap, mapImages, mapDecorations, player, move)
			elif mainMap.jumpable(player, move):
				change = True
				move = tuple_add(move, move)
				player.update(move)
				do_jump(mapImages, playerSprite, mapDecorations, player, move)
				mapImages, mapDecorations = update_map(mainMap, mapImages, mapDecorations, player, move)
			else:
				change = True
				player.turn(move)

			if mainMap.encounter_tile(player):
				# print('encounter')
				encounterPokemon = random_pokemon(level=50)
				WildBattle(DISPLAYSURF, mixer, player, encounterPokemon)
				# DISPLAYSURF.set_mode((windowWidth, windowHeight))

		# keys = pygame.key.get_pressed()
		# if keys[K_SPACE]:
		# 	interact(mainMap, player)

		# elif keys[K_UP] or keys[K_w]:
		# 	move = (0, -1)
		# elif keys[K_DOWN] or keys[K_s]:
		# 	move = (0, 1)
		# elif keys[K_LEFT] or keys[K_a]:
		# 	move = (-1, 0)
		# elif keys[K_RIGHT] or keys[K_d]:
		# 	move = (1, 0)

		# if move != (0, 0):

		# 	if count == 0 and mainMap.passable(player, move):
		# 		change = True
		# 		offsetX = int(1*BOXSIZE/4) * move[0]
		# 		offsetY = int(1*BOXSIZE/4) * move[1]

		# 	elif count == 1 and mainMap.passable(player, move):
		# 		change = True
		# 		offsetX = int(2*BOXSIZE/4) * move[0]
		# 		offsetY = int(2*BOXSIZE/4) * move[1]

		# 	elif count == 2 and mainMap.passable(player, move):
		# 		change = True
		# 		offsetX = int(3*BOXSIZE/4) * move[0]
		# 		offsetY = int(3*BOXSIZE/4) * move[1]

		# 	elif count == 3 and mainMap.passable(player, move):
		# 		change = True
		# 		startX += move[0]
		# 		endX += move[0]
		# 		startY += move[1]
		# 		endY += move[1]
		# 		offsetX, offsetY = 0, 0
			
		# 		player.update(move)

		# 		mapImages = update_map(mainMap, mapImages, player, move)

		# 	elif count == 3:
		# 		change = True
		# 		player.turn(move)


		if change:
			offsetX, offsetY = 0, 0

			draw_screen(mapImages, playerSprite, mapDecorations, (offsetX, offsetY))

			pygame.display.update()
			change = False

			# print(mainMap.tiles[player.x][player.y].group)
			if player.isBiking:
				mixer.play_song('Cycling')
			elif player.isSurfing:
				mixer.play_song('Surfing')
			else:
				mixer.play_song(mainMap.tiles[player.x][player.y].group)

		FPSCLOCK.tick(FPS)



if __name__ == '__main__':
	main()
	pygame.quit()









