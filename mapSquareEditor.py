import pygame, sys, os
from pygame.locals import *
from os.path import sep
from math import ceil
from colors import BLACK, WHITE, YELLOW
from helpers import make_text, wait_for_click, quit, load_image
from worldBuildingTiles import *
from saveLoad import save_map_square, load_map_square
import textInput as txt


def left_top_coords_of_box(boxx, boxy, mapArea=True):
	if mapArea:
		left = boxx * (BOXSIZE) + XMARGIN
		top = boxy * (BOXSIZE) + YMARGIN
	else:
		left = (boxx+9) * (4*BOXSIZE) + XMARGIN
		top = boxy * (4*BOXSIZE) + YMARGIN
	return (left, top)

def highlight_square(boxx, boxy, mapArea=True):
	left, top = left_top_coords_of_box(boxx, boxy, mapArea=mapArea)
	pygame.draw.rect(DISPLAYSURF, YELLOW, (left, top, 4*BOXSIZE, 4*BOXSIZE), 4)


def highlight_area(area, mapArea=True):
	width = len(area)
	height = len(area[0])
	for x in range(width):
		for y in range(height):
			boxx, boxy = area[x][y]
			if mapArea:
				left, top = left_top_coords_of_box(boxx, boxy, mapArea=mapArea)
				pygame.draw.rect(DISPLAYSURF, YELLOW, (left, top, BOXSIZE, BOXSIZE), 2)
			else:
				# boxx -= 36
				left, top = left_top_coords_of_box(boxx, boxy, mapArea=mapArea)
				pygame.draw.rect(DISPLAYSURF, YELLOW, (left, top, 2*BOXSIZE, 2*BOXSIZE), 4)

	pygame.display.update()

def draw_map(mainMapImages, returnSurface=False):
	width = len(mainMapImages)
	height = len(mainMapImages[0])

	for x in range(width):
		for y in range(height):
			if mainMapImages[x][y] != None:
				left, top = left_top_coords_of_box(x, y, mapArea=True)
				tile = mainMapImages[x][y].draw(BOXSIZE)
				tile = pygame.transform.scale(tile, (BOXSIZE, BOXSIZE))
				DISPLAYSURF.blit(tile, (left, top))


def draw_mapSquares(mapImages):
	width = 8
	height = ceil(len(mapImages) / width)

	for x in range(width):
		for y in range(height):
			imageNumber = x + 8*y
			if imageNumber >= len(mapImages):
				pass
			else:
				image = mapImages[imageNumber]
				image = pygame.transform.scale(image, (4*BOXSIZE, 4*BOXSIZE))
				left, top = left_top_coords_of_box(x, y, mapArea=False)
				# print(top, left)
				DISPLAYSURF.blit(image, (left, top))

def mapSquare_at(x, y):
	return x + 8*y


def choose_map(mapData, mapImages, tileCoords=(36,0)):
	yMin, yMax = 0, 8
	xMin, xMax = 36, 43
	squareX, squareY = tileCoords

	

	while True:
		x = squareX-xMin
		y = squareY
		draw_mapSquares(mapImages)
		for event in pygame.event.get():

			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				quit()
			elif event.type == KEYDOWN:

				if event.key in [K_UP, K_w]: 
					if squareY != yMin:
						squareY -= 1
					else:
						squareY = yMax


				elif event.key in [K_LEFT, K_a]:
					if squareX != xMin:
						squareX -= 1
					else:
						squareX = xMax


				elif event.key in [K_RIGHT, K_d]:
					if squareX != xMax:
						squareX += 1
					else:
						squareX = xMin


				elif event.key in [K_DOWN, K_s]:
					if squareY != yMax:
						squareY += 1
					else:
						squareY = yMin


				elif event.key == K_SPACE:
					mapSquareID = mapSquare_at(x, y)
					return mapSquareID


				elif event.key == K_q:
					return None

				else:
					continue


				
			else:
				continue


		highlight_square(x, y, mapArea=False)
		pygame.display.update()
		FPSCLOCK.tick(FPS)

def draw_tile_params(mapSquareTiles, squareX, squareY):
	# return

	tile = mapSquareTiles[squareX][squareY]
	tileParams = tile.get_all_params()

	buttons = []
	for i, key in enumerate(tileParams):

		text = '%s : %s' % (key, str(tileParams[key]))
		left, top = left_top_coords_of_box(38, 4+i)
		surf, rect = make_text(text, WHITE, BLACK, left, top)
		DISPLAYSURF.blit(surf, rect)
		buttons.append(rect)

	return buttons



def save(mapSquare):
	textIn = txt.TextInput()
	text = ''
	while text == '':
		events = pygame.event.get()
		for event in events:
			if event.type == KEYUP and event.key == K_RETURN:
				text = textIn.get_text()

		textIn.update(events)
		textSurf = textIn.get_surface()
		textRect = textSurf.get_size()
		left, top = left_top_coords_of_box(15, 33)
		pygame.draw.rect(DISPLAYSURF, BLACK, (left, top, textRect[0], textRect[1]))
		DISPLAYSURF.blit(textSurf, (left, top))
		pygame.display.update()

		FPSCLOCK.tick(FPS)

	saveSquare = MapSquare(mapSquare)
	save_map_square(saveSquare, text)
	# mapImages = load_map_square(mapSquare, scaleImages=False)
	# surface = draw_map(mapImages, returnSurface=True)
	# savefile = 'mapSquares' + sep + text + '.png'
	# pygame.image.save(surface, savefile)


# XMARGIN = 24
# YMARGIN = 24
# BOXSIZE = 24

# WINDOWWIDTH = 2*XMARGIN + 32*BOXSIZE + 18*2*BOXSIZE + 2*BOXSIZE  # 1728
# WINDOWHEIGHT = 2*YMARGIN + 32*BOXSIZE + 4*BOXSIZE  # 912

def main():
	global DISPLAYSURF, FPSCLOCK, FPS
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	FPS = 15

	global XMARGIN, YMARGIN, BOXSIZE, FONTSIZE
	width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
	
	windowHeight = int(0.8 * height)
	windowWidth = int(1.9 * windowHeight)

	XMARGIN = YMARGIN = int(windowHeight/40)
	BOXSIZE = int( (windowHeight - 2*YMARGIN) / 36)
	FONTSIZE = int(0.8 * BOXSIZE)



	DISPLAYSURF = pygame.display.set_mode((windowWidth, windowHeight))
	pygame.display.set_caption('Map Maker')


	squareX = squareY = 0
	yMin, yMax = 0, 32
	xMin, xMax = 0, 32
	mouseX = mouseY = 0
	tileCoords = (36, 0)

	mapSquares = [x[2] for x in os.walk('mapSquares')][0]
	mapSquares.sort()

	
	# left, top = left_top_coords_of_box(0, 17, mapArea=False)
	# surf, prevRect = make_text('Prev', WHITE, BLACK, left, top, size=FONTSIZE)
	# DISPLAYSURF.blit(surf, prevRect)

	# left, top = left_top_coords_of_box(4, 17, mapArea=False)
	# surf, nextRect = make_text('Next', WHITE, BLACK, left, top, size=FONTSIZE)
	# DISPLAYSURF.blit(surf, nextRect)

	mapImages = []
	mapData = []

	for file in mapSquares:
		filename = 'mapSquares' + sep + file
		if 'main_map' in file:
			pass 
		elif 'png' in file:
			mapImages.append(load_image(filename))
		elif 'pickle' in file:
			mapData.append(load_map_square(filename))

	# print(mapData)
	

	mapSquareID = choose_map(mapData, mapImages)
	mapSquareData = mapData[mapSquareID]
	mapSquareTiles = mapSquareData.tiles

	area = []

	global mapCoords
	mapCoords = []
	for x in range(xMax):
		column = []
		for y in range(yMax):
			column.append((x, y))
		mapCoords.append(column)
	
	squareParams = mapSquareTiles[squareX][squareY].get_passing_params()
	squareParams.update(mapSquareTiles[squareX][squareY].get_encounter_params())
	squareParams.update(mapSquareTiles[squareX][squareY].get_item_params())


	while True:
		DISPLAYSURF.fill(BLACK)


		# left, top = left_top_coords_of_box(2, 17, mapArea=False)
		# text = '%s/%i' % (str(tileSetNum+1).zfill(2), len(tileSets))
		# surf, rect = make_text(text, WHITE, BLACK, left, top, size=FONTSIZE)
		# DISPLAYSURF.blit(surf, rect)

		# left, top = left_top_coords_of_box(0, 17, mapArea=False)
		# surf, prevRect = make_text('Prev', WHITE, BLACK, left, top, size=FONTSIZE)
		# DISPLAYSURF.blit(surf, prevRect)

		# left, top = left_top_coords_of_box(4, 17, mapArea=False)
		# surf, nextRect = make_text('Next', WHITE, BLACK, left, top, size=FONTSIZE)
		# DISPLAYSURF.blit(surf, nextRect)

		left, top = left_top_coords_of_box(12, 34, mapArea=True)
		surf, saveRect = make_text('Save', WHITE, BLACK, left, top, size=FONTSIZE)
		DISPLAYSURF.blit(surf, saveRect)

		
		draw_map(mapSquareTiles)
		buttons = draw_tile_params(mapSquareTiles, squareX, squareY)

		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			if not keys[K_LSHIFT]:
				xStart, xEnd = squareX, squareX+1
				yStart, yEnd = squareY, squareY+1
				
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				quit()
			elif event.type == KEYDOWN:
				if event.key in [K_UP, K_w]: 
					if squareY != yMin:
						squareY -= 1
					else:
						squareY = yMax
					if keys[K_LSHIFT]:

						yStart -= 1

				elif event.key in [K_LEFT, K_a]:
					if squareX != xMin:
						squareX -= 1
					else:
						squareX = xMax
					if keys[K_LSHIFT]:
						xStart -= 1


				elif event.key in [K_RIGHT, K_d]:
					if squareX != xMax:
						squareX += 1
					else:
						squareX = xMin
					if keys[K_LSHIFT]:
						xEnd += 1

				elif event.key in [K_DOWN, K_s]:
					if squareY != yMax:
						squareY += 1
					else:
						squareY = yMin
					if keys[K_LSHIFT]:
						yEnd += 1

				elif event.key == K_SPACE:
					columns = mapCoords[xStart:xEnd]
					area = [y[yStart:yEnd] for y in columns]
					highlight_area(area)
					mainMapData, mainMapImages, tileCoords = set_tiles(mainMapData, mainMapImages, area, mapData, mapImages, tileCoords)


			elif event.type == MOUSEBUTTONUP:
				mouseX, mouseY = event.pos

				if saveRect.collidepoint(mouseX, mouseY):
					# print(mainMapData)
					# print('\n\n')
					# print(mainMapImages)
					save(mapSquareTiles)
					
				else:
					for i, button in enumerate(buttons):
						if button.collidepoint(mouseX, mouseY):
							tile = mapSquareTiles[squareX][squareY]

							tileParams = tile.get_all_params()

							keys = list(tileParams.keys())

							key = keys[i]

							if key == 'Jump Direction':
								if tileParams[key] == None:
									tileParams[key] = 'down'
								elif tileParams[key] == 'down':
									tileParams[key] = 'left'
								elif tileParams[key] == 'left':
									tileParams[key] = 'up'
								elif tileParams[key] == 'up':
									tileParams[key] = 'right'
								elif tileParams[key] == 'right':
									tileParams[key] = 'down'

								tileParams['Jumpable'] = True

							elif key == 'Jumpable':
								tileParams[key] = not tileParams[key]
								if tileParams[key] == False:
									tileParams['Jump Direction'] = None

							elif key == 'Encounter Rate':
								tileParams[key] += 10

								if tileParams[key] > 100:
									tileParams[key] = 0

								if tileParams[key] == 0:
									tileParams['Encounter Tile'] = False
								else:
									tileParams['Encounter Tile'] = True

							elif key == 'Encounter Tile':
								tileParams[key] = not tileParams[key]

								if tileParams[key] == True:
									tileParams['Encounter Rate'] = 30
								else:
									tileParams['Encounter Rate'] = 0

							else:
								tileParams[key] = not tileParams[key]

							mapSquareData.tiles[squareX][squareY].set_all_params(tileParams)

			else:
				continue

		columns = mapCoords[xStart:xEnd]
		area = [y[yStart:yEnd] for y in columns]
		highlight_area(area)
		FPSCLOCK.tick(FPS)

	


if __name__ == '__main__':
	main()