from saveLoad import load_map_square, save_map_square
from worldBuildingTiles import *
from os.path import sep
import pygame

pygame.init()
displaysurface = pygame.display.set_mode((1,1))

mapDimensions = (24, 16)

mapData = []


print('Compiling...')
for x in range(mapDimensions[0]+2):
	column = []
	for y in range(mapDimensions[1]+2):
		if (x == 0 or y == 0) or (x == mapDimensions[0]+1 or y == mapDimensions[1]+1):
			mapName = 'none'
		else:
			mapName = '%i_%i' % (x, y)

		try:
			mapSquare = load_map_square(mapName)
		except:
			mapName = 'none'
			mapSquare = load_map_square(mapName)

		mapSquare.place_on_map_at(x, y)

		column.append(mapSquare)

	mapData.append(column)

print('Saving...')
text = 'main_map_full_test'
fullMap = MainMap(mapData)
save_map_square(fullMap, text)


print('Drawing...')
surface = fullMap.draw_complete(tileSize=16)
savefile = 'mapSquares' + sep + text + '.png'
pygame.image.save(surface, savefile)
print('Complete!')