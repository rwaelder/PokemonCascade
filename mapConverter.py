import pygame
import os
from pygame.locals import *
from saveLoad import save_map_square, load_map_square

# Converts filenames in all maps to the new folder structure

def save(mapData, file):
	text = file
	# print(mapData)
	# saveSquare = MainMap(mapData)
	save_map_square(mapData, text)
	# mapImages = load_map(mapSquare, scaleImages=False)
	# surface = saveSquare.draw()
	# text = text.replace('.pickle', '.png')
	# savefile = 'mapSquares/' + text
	# pygame.image.save(surface, savefile)


pygame.init()
display = pygame.display.set_mode((1,1))

mapSquares = [x[2] for x in os.walk('mapSquares')][0]
mapSquares.sort()

for file in mapSquares:
	if 'pickle' in file:
		mapData = load_map_square(file)

		for x in range(32):
			for y in range(32):
				tile = mapData.tiles[x][y]

				for i in range(1, 10):
					oldString = 'tiles/%i_' % i
					if oldString in tile.baseTile:
						newString = 'tiles/0%i_' % i
						tile.baseTile = tile.baseTile.replace(oldString, newString)
					if tile.decoration != None and oldString in tile.decoration:
						newString = 'tiles/0%i_' % i
						tile.decoration = tile.decoration.replace(oldString, newString)

		save(mapData, file)