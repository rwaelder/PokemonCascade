from saveLoad import load_map_square, save_map_square
from worldBuildingTiles import *
from os.path import sep
import pygame

pygame.init()
displaysurface = pygame.display.set_mode((1,1))

# mapDimensions = (24, 16)

# mapData = []

# mapName = 'main_map'

# squaresFolder = 'individualSquares' + sep

mapDimensions = (5, 5)

mapData = []

mapName = 'mini_map'

squaresFolder = 'mini_map' + sep

print('Compiling...')
for x in range(mapDimensions[0]+2):
	column = []
	for y in range(mapDimensions[1]+2):
		if (x == 0 or y == 0) or (x == mapDimensions[0]+1 or y == mapDimensions[1]+1):
			mapSquareName = squaresFolder + 'none'
		else:
			mapSquareName = squaresFolder + '%i_%i' % (x, y)

		try:
			mapSquare = load_map_square(mapSquareName)
		except:
			mapSquareName = squaresFolder + 'none'
			mapSquare = load_map_square(mapSquareName)

		mapSquare.place_on_map_at(x, y)

		column.append(mapSquare)

	mapData.append(column)

print('Saving...')
fullMap = MainMap(mapData)
save_map_square(fullMap, mapName)


print('Drawing...')
surface = fullMap.draw_complete(tileSize=32)
savefile = 'mapSquares' + sep + mapName + '.png'
pygame.image.save(surface, savefile)

print('Drawing overlay...')
surface = fullMap.draw_complete(tileSize=32, overlay=True)
savefile = 'mapSquares' + sep + mapName + '_overlay.png'
pygame.image.save(surface, savefile)

print('Complete!')