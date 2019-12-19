import pygame, sys, os
from pygame.locals import *
from os.path import sep
from colors import BLACK, WHITE, YELLOW
from helpers import make_text, wait_for_click, quit
from worldBuildingTiles import *
from saveLoad import save_map_square, load_map_square
import textInput as txt


def left_top_coords_of_box(boxx, boxy, mapArea=True):
	if mapArea:
		left = boxx * (BOXSIZE) + XMARGIN
		top = boxy * (BOXSIZE) + YMARGIN
	else:
		left = (boxx+18) * (2*BOXSIZE) + XMARGIN
		top = boxy * (2*BOXSIZE) + YMARGIN
	return (left, top)

def highlight_square(boxx, boxy, mapArea=True):
	left, top = left_top_coords_of_box(boxx, boxy, mapArea=mapArea)
	pygame.draw.rect(DISPLAYSURF, YELLOW, (left, top, 2*BOXSIZE, 2*BOXSIZE), 4)


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

def get_box_at_pixel(x, y):
	for boxx in range(BOARDWIDTH):
		for boxy in range(BOARDHEIGHT):
			left, top = left_top_coords_of_box(boxx, boxy)
			boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
			if boxRect.collidepoint(x, y):
				return (boxx, boxy)
	return(None, None)

def load_map(mapSquare, scaleImages=True):
	mapSize = len(mapSquare)
	if scaleImages:
		scaleSize = BOXSIZE
	else:
		scaleSize = 48
	mapImages = []
	for x in range(mapSize):
		column = []
		for y in range(mapSize):
			tileImage = mapSquare[x][y].draw(scaleSize)
			
			column.append(tileImage)
		mapImages.append(column)
	return mapImages


def draw_map(mapImages, returnSurface=False):
	mapSize = len(mapImages)
	if returnSurface:
		surface = pygame.Surface((48*mapSize, 48*mapSize))
	
	left, top = left_top_coords_of_box(0, 0)
	pygame.draw.rect(DISPLAYSURF, WHITE, (left, top, BOXSIZE*mapSize, BOXSIZE*mapSize))
	for x in range(mapSize):
		for y in range(mapSize):
			tileImage = mapImages[x][y]
			left, top = left_top_coords_of_box(x, y)
			if returnSurface:
				surface.blit(tileImage, (48*x, 48*y))
			else:
				DISPLAYSURF.blit(tileImage, (left, top))

	if returnSurface:
		return surface


def draw_tileSet(tileSetFolder):
	left, top = left_top_coords_of_box(0, 0, mapArea=False)
	pygame.draw.rect(DISPLAYSURF, BLACK, (left, top, BOXSIZE*32, BOXSIZE*32))
	for x in range(16):
		for y in range(16):
			tileFile = 'tiles' + sep + tileSetFolder + sep + '%i_%i.png' % (x+1, y+1)
			tileImage = pygame.image.load(tileFile).convert_alpha()
			tileImage = pygame.transform.scale(tileImage, (2*BOXSIZE, 2*BOXSIZE))
			left, top = left_top_coords_of_box(x, y, mapArea=False)
			DISPLAYSURF.blit(tileImage, (left, top))

def get_group_name():
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

	return text

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
	try:
		saveSquare.tiles[0][0].isJumpable
	except:
		saveSquare.update()

	saveSquare.set_group(get_group_name())
	save_map_square(saveSquare, text)
	mapImages = load_map(mapSquare, scaleImages=False)
	surface = draw_map(mapImages, returnSurface=True)
	savefile = 'mapSquares' + sep + text + '.png'
	pygame.image.save(surface, savefile)


def set_decoration(mapSquare, area, tileSetFolder, tileCoords):
	yMin, yMax = 0, 15
	xMin, xMax = 36, 51
	squareX, squareY = tileCoords

	xStart, xEnd = squareX-36, squareX+1-36
	yStart, yEnd = squareY, squareY+1

	while True:
		draw_tileSet(tileSetFolder)
		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			if not keys[K_LSHIFT]:
				xStart, xEnd = squareX-36, squareX+1-36
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
					selected = [y[yStart:yEnd] for y in columns]
					sWidth = len(selected)
					sHeight = len(selected[0])

					aWidth = len(area)
					aHeight = len(area[0])

					if (sWidth, sHeight) == (aWidth, aHeight):
						for x in range(sWidth):
							for y in range(sHeight):
								locX, locY = area[x][y]
								tile = mapSquare[locX][locY]
								decFile = 'tiles' + sep + tileSetFolder + sep + '%i_%i.png' % (selected[x][y][0]+1, selected[x][y][1]+1)
								tile.set_decoration(decFile)
								mapSquare[locX][locY] = tile

					elif sWidth == sHeight == 1:
						for x in range(aWidth):
							for y in range(aHeight):
								locX, locY = area[x][y]
								tile = mapSquare[locX][locY]
								decFile = 'tiles' + sep + tileSetFolder + sep + '%i_%i.png' % (selected[x][y][0]+1, selected[x][y][1]+1)
								tile.set_decoration(decFile)
								mapSquare[locX][locY] = tile
					elif sWidth == aWidth:
						for x in range(aWidth):
							sY = 0
							for y in range(aHeight):
								if sY == sHeight:
									sY = 0
								tile = Tile(setParams)
								tileFile = 'tiles' + sep + tileSetFolder + sep + '%i_%i.png' % (selected[x][sY][0]+1, selected[x][sY][1]+1)
								tile.set_base_tile(tileFile)
								locX, locY = area[x][y]
								tile.set_location(locX, locY)
								mapSquare[locX][locY] = tile
								sY += 1

					elif sHeight == aHeight:
						for y in range(aHeight):
							sX = 0
							for x in range(aWidth):
								if sX == sWidth:
									sX = 0
								tile = Tile(setParams)
								tileFile = 'tiles' + sep + tileSetFolder + sep + '%i_%i.png' % (selected[sX][y][0]+1, selected[sX][y][1]+1)
								tile.set_base_tile(tileFile)
								locX, locY = area[x][y]
								tile.set_location(locX, locY)
								mapSquare[locX][locY] = tile
								sX += 1
					else:
						continue
					return mapSquare, (squareX, squareY)

				elif event.key == K_q:
					return mapSquare, (squareX, squareY)
			else:
				continue

		columns = mapCoords[xStart:xEnd]
		selected = [y[yStart:yEnd] for y in columns]
		highlight_area(selected, mapArea=False)
		pygame.display.update()
		FPSCLOCK.tick(FPS)

def set_tiles(mapSquare, area, tileSetFolder, tileCoords):
	yMin, yMax = 0, 15
	xMin, xMax = 36, 51
	squareX, squareY = tileCoords

	xStart, xEnd = squareX-36, squareX+1-36
	yStart, yEnd = squareY, squareY+1

	while True:
		draw_tileSet(tileSetFolder)
		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			if not keys[K_LSHIFT]:
				xStart, xEnd = squareX-36, squareX+1-36
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
					selected = [y[yStart:yEnd] for y in columns]
					sWidth = len(selected)
					sHeight = len(selected[0])

					aWidth = len(area)
					aHeight = len(area[0])

					if (sWidth, sHeight) == (aWidth, aHeight):
						for x in range(sWidth):
							for y in range(sHeight):
								tile = Tile(setParams)
								tileFile = 'tiles' + sep + tileSetFolder + sep + '%i_%i.png' % (selected[x][y][0]+1, selected[x][y][1]+1)
								tile.set_base_tile(tileFile)
								locX, locY = area[x][y]
								tile.set_location(locX, locY)
								mapSquare[locX][locY] = tile

					elif sWidth == sHeight == 1:
						for x in range(aWidth):
							for y in range(aHeight):
								tile = Tile(setParams)
								tileFile = 'tiles' + sep + tileSetFolder + sep + '%i_%i.png' % (selected[0][0][0]+1, selected[0][0][1]+1)
								tile.set_base_tile(tileFile)
								locX, locY = area[x][y]
								tile.set_location(locX, locY)
								mapSquare[locX][locY] = tile
					elif sWidth == aWidth:
						for x in range(aWidth):
							sY = 0
							for y in range(aHeight):
								if sY == sHeight:
									sY = 0
								tile = Tile(setParams)
								tileFile = 'tiles' + sep + tileSetFolder + sep + '%i_%i.png' % (selected[x][sY][0]+1, selected[x][sY][1]+1)
								tile.set_base_tile(tileFile)
								locX, locY = area[x][y]
								tile.set_location(locX, locY)
								mapSquare[locX][locY] = tile
								sY += 1

					elif sHeight == aHeight:
						for y in range(aHeight):
							sX = 0
							for x in range(aWidth):
								if sX == sWidth:
									sX = 0
								tile = Tile(setParams)
								tileFile = 'tiles' + sep + tileSetFolder + sep + '%i_%i.png' % (selected[sX][y][0]+1, selected[sX][y][1]+1)
								tile.set_base_tile(tileFile)
								locX, locY = area[x][y]
								tile.set_location(locX, locY)
								mapSquare[locX][locY] = tile
								sX += 1
					else:
						continue
					return mapSquare, (squareX, squareY)

				elif event.key == K_q:
					return mapSquare, (squareX, squareY)
			else:
				continue

		columns = mapCoords[xStart:xEnd]
		selected = [y[yStart:yEnd] for y in columns]
		highlight_area(selected, mapArea=False)
		pygame.display.update()
		FPSCLOCK.tick(FPS)

def fill_map(tileSetFolder, tileCoords):
	yMin, yMax = 0, 15
	xMin, xMax = 36, 51
	squareX, squareY = tileCoords
	while True:
		draw_tileSet(tileSetFolder)
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
					tiles = []
					for x in range(32):
						column = []
						for y in range(32):
							tile = Tile(setParams)
							tileFile = tileFile = 'tiles' + sep + tileSetFolder + sep + '%i_%i.png' % (squareX+1-36, squareY+1)
							tile.set_base_tile(tileFile)
							tile.set_location(x, y)
							column.append(tile)
						tiles.append(column)
					return tiles, (squareX, squareY)

				elif event.key == K_q:
					return None, (squareX, squareY)
			else:
				continue

		highlight_square(squareX-36, squareY, mapArea=False)
		pygame.display.update()
		FPSCLOCK.tick(FPS)

def edit_tile_params(mapSquare, area):
	return 


def draw_tile_params(mapSquare, area):
	left, top = left_top_coords_of_box(.5, 32.5, mapArea=True)

	if len(area) > 1 or len(area[-1]) > 1:
		pygame.draw.rect(DISPLAYSURF, BLACK, (left, top, BOXSIZE*8, BOXSIZE*5), 4)
	else:
		x, y = area[-1][-1]

		tilePassingParams = mapSquare[x][y].get_passing_params()
		keys = tilePassingParams.keys()
		pygame.draw.rect(DISPLAYSURF, WHITE, (left, top, BOXSIZE*8, BOXSIZE*5), 4)
		for i, key in enumerate(keys):
			left, top = left_top_coords_of_box(1, 33+i, mapArea=True)
			text = '%s: %s' % (key, tilePassingParams[key])
			surf, rect = make_text(text, WHITE, BLACK, left, top, size=FONTSIZE)
			DISPLAYSURF.blit(surf, rect)


def draw_set_params():
	keys = setParams.keys()
	rects = []
	left, top = left_top_coords_of_box(11.75, 16.25, mapArea=False)
	pygame.draw.rect(DISPLAYSURF, WHITE, (left, top, BOXSIZE*9, BOXSIZE*5), 4)
	for i, key in enumerate(keys):
		left, top = left_top_coords_of_box(12, 16.5+(i/2), mapArea=False)
		text = '%s: %s' % (key, setParams[key])
		surf, rect = make_text(text, WHITE, BLACK, left, top, size=FONTSIZE)
		DISPLAYSURF.blit(surf, rect)
		rects.append(rect)

	return rects

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
	pygame.display.set_caption('Map Square Maker')

	global setParams
	setParams = {}
	setParams['isWalkable'] = True
	setParams['isRunnable'] = True
	setParams['isBikeable'] = True
	setParams['isSurfable'] = False
	draw_set_params()


	squareX = squareY = 0
	yMin, yMax = 0, 31
	xMin, xMax = 0, 31
	mouseX = mouseY = 0
	tileCoords = (36, 0)
	xStart, xEnd = squareX, squareX+1
	yStart, yEnd = squareY, squareY+1

	tileSets = [x[1] for x in os.walk('tiles')][0]
	tileSets.sort()
	tileSetNum = 0
	tileSetFolder = tileSets[tileSetNum]
	
	left, top = left_top_coords_of_box(0, 17, mapArea=False)
	surf, prevRect = make_text('Prev', WHITE, BLACK, left, top, size=FONTSIZE)
	DISPLAYSURF.blit(surf, prevRect)

	left, top = left_top_coords_of_box(4, 17, mapArea=False)
	surf, nextRect = make_text('Next', WHITE, BLACK, left, top, size=FONTSIZE)
	DISPLAYSURF.blit(surf, nextRect)

	
	try:
		mapSquare = load_map_square(sys.argv[1]).tiles
	except:
		mapSquare = fill_map(tileSetFolder, tileCoords)[0]

	mapImages = load_map(mapSquare)

	draw_map(mapImages)

	area = []

	global mapCoords
	mapCoords = []
	for x in range(len(mapSquare)):
		column = []
		for y in range(len(mapSquare)):
			column.append((x, y))
		mapCoords.append(column)


	while True:
		DISPLAYSURF.fill(BLACK)

		tileSetFolder = tileSets[tileSetNum]

		left, top = left_top_coords_of_box(2, 17, mapArea=False)
		text = '%s/%i' % (str(tileSetNum+1).zfill(2), len(tileSets))
		surf, rect = make_text(text, WHITE, BLACK, left, top, size=FONTSIZE)
		DISPLAYSURF.blit(surf, rect)

		left, top = left_top_coords_of_box(0, 17, mapArea=False)
		surf, prevRect = make_text('Prev', WHITE, BLACK, left, top, size=FONTSIZE)
		DISPLAYSURF.blit(surf, prevRect)

		left, top = left_top_coords_of_box(4, 17, mapArea=False)
		surf, nextRect = make_text('Next', WHITE, BLACK, left, top, size=FONTSIZE)
		DISPLAYSURF.blit(surf, nextRect)

		left, top = left_top_coords_of_box(12, 34, mapArea=True)
		surf, saveRect = make_text('Save', WHITE, BLACK, left, top, size=FONTSIZE)
		DISPLAYSURF.blit(surf, saveRect)

		
		draw_map(mapImages)
		draw_tileSet(tileSetFolder)

		paramRects = draw_set_params()



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
					mapSquare, tileCoords = set_tiles(mapSquare, area, tileSetFolder, tileCoords)
					mapImages = load_map(mapSquare)

				elif event.key == K_b:
					columns = mapCoords[xStart:xEnd]
					area = [y[yStart:yEnd] for y in columns]
					highlight_area(area)
					mapSquare, tileCoords = set_decoration(mapSquare, area, tileSetFolder, tileCoords)
					mapImages = load_map(mapSquare)

				elif keys[K_LCTRL] and event.key == K_f:
					mapArea, tileCoords = fill_map(tileSetFolder, tileCoords)
					if mapArea != None:
						mapSquare = mapArea
						mapImages = load_map(mapSquare)

				elif keys[K_LCTRL] and event.key == K_e:
					columns = mapCoords[xStart:xEnd]
					area = [y[yStart:yEnd] for y in columns]
					highlight_area(area)
					edit_tile_params(mapSquare, area)

				elif keys[K_LCTRL] and event.key == K_r:
					mapSquare[squareX][squareY].rotate()
					mapImages[squareX][squareY] = mapSquare[squareX][squareY].draw(BOXSIZE)

				elif keys[K_LCTRL] and event.key == K_h:
					mapSquare[squareX][squareY].flip_horizontal()
					mapImages[squareX][squareY] = mapSquare[squareX][squareY].draw(BOXSIZE)

				elif keys[K_LCTRL] and event.key == K_v:
					mapSquare[squareX][squareY].flip_vertical()
					mapImages[squareX][squareY] = mapSquare[squareX][squareY].draw(BOXSIZE)


			elif event.type == MOUSEBUTTONUP:
				mouseX, mouseY = event.pos
				tileCoords = (36, 0)
				if nextRect.collidepoint(mouseX, mouseY):
					tileSetNum += 1
					if tileSetNum == len(tileSets):
						tileSetNum = 0

				elif prevRect.collidepoint(mouseX, mouseY):
					tileSetNum -= 1
					if tileSetNum < 0:
						tileSetNum = len(tileSets)-1

				elif saveRect.collidepoint(mouseX, mouseY):
					save(mapSquare)


				else:
					paramKeys = list(setParams.keys())
					for i in range(len(setParams)):
						if paramRects[i].collidepoint(mouseX, mouseY):
							setParams[paramKeys[i]] = not setParams[paramKeys[i]]

			else:
				continue
		columns = mapCoords[xStart:xEnd]
		area = [y[yStart:yEnd] for y in columns]
		draw_tile_params(mapSquare, area)
		highlight_area(area)
		FPSCLOCK.tick(FPS)

	


if __name__ == '__main__':
	main()