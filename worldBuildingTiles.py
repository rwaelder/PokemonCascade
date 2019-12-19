import pygame
import re
from random import randint

class Tile():
	def __init__(self, setParams):
		self.isWalkable = setParams['isWalkable']
		self.isRunnable = setParams['isRunnable']
		self.isBikeable = setParams['isBikeable']
		self.isSurfable = setParams['isSurfable']
		self.isJumpable = False
		self.jumpDirection = None

		self.item = None
		self.decoration = None

		self.isEncounterTile = False
		self.encounterRate = 0
		# self.encounters = []
		self.rotation = 0
		self.hFlip = False
		self.vFlip = False

		self.group = None

	# def __init__(self):
	# 	self.item = None
	# 	self.decoration = None

	def set_group(self, group):
		self.group = group

	def is_decorated(self):
		if self.decoration != None:
			return True
		else:
			return False

	def rotate(self):
		self.rotation += 90
		if self.rotation == 360:
			self.rotation = 0

	def flip_horizontal(self):
		self.hFlip = not self.hFlip

	def flip_vertical(self):
		self.vFlip = not self.vFlip

	def get_location(self):
		return self.x, self.y

	def set_all_params(self, params):
		self.isWalkable = params['Walkable']
		self.isRunnable = params['Runnable']
		self.isBikeable = params['Bikeable']
		self.isSurfable = params['Surfable']
		self.isJumpable = params['Jumpable']
		self.jumpDirection = params['Jump Direction']

		self.isEncounterTile = params['Encounter Tile']
		self.encounterRate = params['Encounter Rate']


	def get_all_params(self):
		params = {}
		params.update(self.get_passing_params())
		params.update(self.get_encounter_params())
		params.update(self.get_item_params())
		params.update(self.get_decoration_params())

		return params

	def get_passing_params(self):
		params = {}
		params['Walkable'] = self.isWalkable
		params['Runnable'] = self.isRunnable
		params['Bikeable'] = self.isBikeable
		params['Surfable'] = self.isSurfable
		params['Jumpable'] = self.isJumpable
		params['Jump Direction'] = self.jumpDirection
		return params

	def get_encounter_params(self):
		params = {}
		params['Encounter Tile'] = self.isEncounterTile
		params['Encounter Rate'] = self.encounterRate
		params['Encounters'] = self.encounters
		return params

	def get_item_params(self):
		params = {}
		params['Item'] = self.item
		return params

	def get_decoration_params(self):
		params = {}
		params['Decoration'] = self.decoration
		return params

	def set_location(self, x, y):
		self.x = x
		self.y = y

	def offset_location(self, X, Y):
		self.x += 32 * X
		self.y += 32 * Y

	def set_base_tile(self, image):
		self.baseTile = image

	def set_decoration(self, image):
		self.decoration = image

	def set_hidden_item(self, item):
		self.item = item

	def collect_item(self):
		if self.item != None:
			item = self.item
			self.item = None
			if self.decoration:
				self.decoration = None
			return item
		else:
			return None

	def set_item(self, item):
		self.item = item
		self.decoration = 'Hideout/12_6.png'
		self.set_unpassable()

	def set_encounter_rate(self, encounterRate=20):
		self.encounterTile = True
		self.encounterRate = encounterRate

	def set_unpassable(self):
		self.isWalkable = False
		self.isRunnable = False
		self.isBikeable = False
		self.isSurfable = False

	def set_passable(self, walkSurf):
		if walkSurf == 'walk':
			self.isWalkable = True
			self.isRunnable = True
			self.isBikeable = True
		elif walkSurf == 'surf':
			self.isSurfable = True

	def change_passable(self):
		self.isWalkable = not self.isWalkable

	def change_runnable(self):
		self.isRunnable = not self.isRunnable

	def change_bikeable(self):
		self.isBikeable = not self.isBikeable

	def change_surfable(self):
		self.isSurfable = not self.isSurfable

	def draw(self, size):
		image = self.draw_base(size)
		if self.decoration != None:
			image.blit(self.draw_decoration(size), (0,0))

		return image

	def draw_base(self, size):
		image = pygame.image.load(self.baseTile).convert_alpha()
		image = pygame.transform.rotate(image, self.rotation)
		image = pygame.transform.flip(image, self.hFlip, self.vFlip)

		image = pygame.transform.scale(image, (size, size))

		return image
		
	def draw_decoration(self, size):
		if self.decoration == None:
			image = None
		else:
			image = pygame.image.load(self.decoration).convert_alpha()
			image = pygame.transform.scale(image, (size, size))

		return image

class MapSquare():

	def __init__(self, tiles):
		if tiles == None:
			self.tiles = []
			for x in range(32):
				column = []
				for y in range(32):
					column.append(None)
				self.tiles.append(column)

		else:
			self.tiles = tiles

	def set_group(self, group):
		for x in range(32):
			for y in range(32):
				self.tiles[x][y].set_group(group)

	def place_on_map_at(self, x, y):
		for i in range(32):
			for j in range(32):
				self.tiles[i][j].offset_location(x, y)

	def draw(self, size):
		image = pygame.Surface((size, size))
		tileSize = int(size/32)
		for i in range(32):
			for j in range(32):
				tile = self.tiles[i][j].draw(tileSize)
				image.blit(tile, (i*tileSize, j*tileSize))

		return image

	def update(self):
		for i in range(32):
			for j in range(32):
				self.tiles[i][j].isJumpable = False
				self.tiles[i][j].jumpDirection = None

class MainMap():
	def __init__(self, squaresArray):
		self.tiles = []
		width = len(squaresArray)
		height = len(squaresArray[0])
		self.tiles = []
		for i in range(width):
			for ii in range(32):
				column = []
				for j in range(height):
					for jj in range(32):
						tiles = squaresArray[i][j].tiles
						tile = tiles[ii][jj]
						
						if tile.baseTile == 'tiles/01_1/6_2.png' and not tile.isEncounterTile:
							tile.isEncounterTile = True
							tile.encounterRate = 30
						column.append(tile)
				self.tiles.append(column)

		self.width = len(self.tiles)
		self.height = len(self.tiles[0])

	def draw_complete(self, tileSize=48):
		image = pygame.Surface((tileSize*self.width, tileSize*self.height))
		for i in range(self.width):
			for j in range(self.height):
				if self.tiles[i][j] == None:
					tile = pygame.Surface((tileSize, tileSize))
					tile.fill((0, 0, 0))
					image.blit(tile, (i*tileSize, j*tileSize))
				else:
					tile = self.tiles[i][j].draw(tileSize)
					image.blit(tile, (i*tileSize, j*tileSize))

		return image

	def draw_screen(self, displayArea, tileSize=48):
		width = len(displayArea)
		height = len(displayArea[0])

		image = pygame.Surface((tileSize*width, tileSize*height))
		for i in range(width):
			for j in range(height):
				x, y = displayArea[i][j]
				tile = self.tiles[x][y].draw(tileSize)
				image.blit(tile, (i*tileSize, j*tileSize))

		return image

	def new_screen_images_array(self, player, tileSize=48):
		startX, startY = player.get_position()
		startX -= 9
		startY -= 7
		endX = startX + 20
		endY = startY + 15

		images = []
		decorations = []
		for x in range(startX, endX):
			column1 = []
			column2 = []
			for y in range(startY, endY):
				column1.append(self.tiles[x][y].draw_base(tileSize))
				column2.append(self.tiles[x][y].draw_decoration(tileSize))

			images.append(column1)
			decorations.append(column2)

		return images, decorations

	def load_relevant_tiles(self, player, imageArray, decorationArray, move, tileSize=48):
		if move == (0, 0):
			pass

		elif abs(move[0]) == 2 or abs(move[1]) == 2:
			imageArray, decorationArray = self.load_relevant_tiles(player, imageArray, decorationArray, (int(move[0]/2), int(move[1]/2)), tileSize=tileSize)
			imageArray, decorationArray = self.load_relevant_tiles(player, imageArray, decorationArray, (int(move[0]/2), int(move[1]/2)), tileSize=tileSize)
		
		else:
			startX, startY = player.get_position()
			startX -= 9
			startY -= 7
			endX = startX + 20
			endY = startY + 15
			x = range(startX, endX)
			y = range(startY, endY)

			if move == (0, -1):
				for i in range(len(imageArray)):
					imageArray[i].pop(-1)
					image = self.tiles[x[i]][startY].draw_base(tileSize)
					imageArray[i].insert(0, image)

					decorationArray[i].pop(-1)
					decoration = self.tiles[x[i]][startY].draw_decoration(tileSize)
					decorationArray[i].insert(0, decoration)

			elif move == (0, 1):
				for i in range(len(imageArray)):
					imageArray[i].pop(0)
					image = self.tiles[x[i]][endY-1].draw_base(tileSize)
					imageArray[i].append(image)

					decorationArray[i].pop(0)
					decoration = self.tiles[x[i]][endY-1].draw_decoration(tileSize)
					decorationArray[i].append(decoration)

			elif move == (-1, 0):
				imageArray.pop(-1)
				decorationArray.pop(-1)
				column1 = []
				column2 = []
				for i in range(len(imageArray[0])):
					image = self.tiles[startX][y[i]].draw_base(tileSize)
					column1.append(image)

					decoration = self.tiles[startX][y[i]].draw_decoration(tileSize)
					column2.append(decoration)

				imageArray.insert(0, column1)
				decorationArray.insert(0, column2)

			elif move == (1, 0):
				imageArray.pop(0)
				decorationArray.pop(0)
				column1 = []
				column2 = []
				for i in range(len(imageArray[0])):
					image = self.tiles[endX-1][y[i]].draw_base(tileSize)
					column1.append(image)

					decoration = self.tiles[endX-1][y[i]].draw_decoration(tileSize)
					column2.append(decoration)

				imageArray.append(column1)
				decorationArray.append(column2)

		return imageArray, decorationArray



	def jumpable(self, player, move):
		playerX, playerY = player.get_position()
		destinationX, destinationY = playerX + move[0], playerY + move[1]

		if self.tiles[destinationX][destinationY].jumpDirection == None:
			return False
		

		if move == (0, 0):
			return False
		elif move == (0, 1):
			jump = 'down'
		elif move == (0, -1):
			jump = 'up'
		elif move == (1, 0):
			jump = 'right'
		elif move == (-1, 0):
			jump = 'left'

		if self.tiles[destinationX][destinationY].jumpDirection == jump:
			return True

		return False

	def surfable(self, player):
		playerX, playerY = player.get_position()
		move = player.facing
		destinationX, destinationY = playerX + move[0], playerY + move[1]

		if self.tiles[destinationX][destinationY].isSurfable:
			return True

		return False

	def passable(self, player, move):
		playerX, playerY = player.get_position()
		destinationX, destinationY = playerX + move[0], playerY + move[1]

		if player.isWalking:
			if self.tiles[destinationX][destinationY].isWalkable:
				return True
			else:
				return False

		elif player.isRunning:
			if self.tiles[destinationX][destinationY].isRunnable:
				return True
			else:
				return False

		elif player.isBiking:
			if self.tiles[destinationX][destinationY].isBikeable:
				return True
			else:
				return False

		elif player.isSurfing:
			if self.tiles[destinationX][destinationY].isSurfable:
				return True
			else:
				return False

	def interact(self, player):
		playerX, playerY = player.get_position()
		destinationX, destinationY = playerX + player.facing[0], playerY + player.facing[1]
		interaction = {}

		if self.tiles[destinationX][destinationY].item != None:
			item = self.tiles[destinationX][destinationY].collect_item()
			interaction['item'] = item

		elif self.tiles[destinationX][destinationY].hasSign:
			text = self.tiles[destinationX][destinationY].signText
			interaction['sign'] = text

		return interaction

	def encounter_tile(self, player):
		playerX, playerY = player.get_position()

		if self.tiles[playerX][playerY].isEncounterTile and randint(1, 100) < self.tiles[playerX][playerY].encounterRate:
			return True
		else:
			return False

