import pygame, sys
from pygame.locals import *
from colors import BLACK, WHITE, MAROON, GOLD
from helpers import make_text, wait_for_click
from musicList import musicLibrary
from mixer import Mixer
from pocketMonsters import Pokemon
from creatures1_25 import Venusaur

mixer = Mixer()
pygame.init()

displaySurface = pygame.display.set_mode((600,700))
pygame.display.set_caption('Pokémon Soundboard')



def draw_page(keys, pageNum):
	displaySurface.fill(MAROON)
	pygame.draw.rect(displaySurface, BLACK, (25, 25, 550, 650), 5)

	pokeCoords = [(49, 50), (49, 75), (49,100), (49, 125), (49, 150), (49, 175), (49, 200), (49, 225), (49, 250), (49, 275)]
	pokeCoords.extend([(49, 300), (49, 325), (49,350), (49, 375), (49, 400), (49, 425), (49, 450), (49, 475)])
	pokeCoords.extend([(218, 50), (218, 75), (218,100), (218, 125), (218, 150), (218, 175), (218, 200), (218, 225), (218, 250), (218, 275)])
	pokeCoords.extend([(218, 300), (218, 325), (218,350), (218, 375), (218, 400), (218, 425), (218, 450), (218, 475)])
	pokeCoords.extend([(387, 50), (387, 75), (387,100), (387, 125), (387, 150), (387, 175), (387, 200), (387, 225), (387, 250), (387, 275)])
	pokeCoords.extend([(387, 300), (387, 325), (387,350), (387, 375), (387, 400), (387, 425), (387, 450), (387, 475)])
	rects = []
	# draw boxes
	for i in range(len(pokeCoords)):
		if (pageNum*len(pokeCoords)) + (i) >= len(keys):
			break
		left, top = pokeCoords[i]
		rect = pygame.draw.rect(displaySurface, BLACK, (left, top, 169, 25), 4)
		rects.append(rect)
		
		# pokemon image
		key = keys[(pageNum*len(pokeCoords)) + (i)]

		surf, rect = make_text(key.center(15), BLACK, GOLD, left+2, top+2, size=18, style='bold')
		displaySurface.blit(surf, rect)

	return rects


def main(displaySurface, mixer):
	FPS = 30
	FPSCLOCK = pygame.time.Clock()

	
	
	keys = list(musicLibrary.keys())
	mousex, mousey = (0, 0)
	pageNum = 0

	while True:
		
		pageRects = draw_page(keys, pageNum)

		prevPage = pygame.draw.rect(displaySurface, BLACK, (40, 535, 50, 28), 4)
		surf, rect = make_text('Prev', BLACK, GOLD, 44, 538, size=18)
		displaySurface.blit(surf, rect)

		nextPage = pygame.draw.rect(displaySurface, BLACK, (100, 535, 50, 28), 4)
		surf, rect = make_text('Next', BLACK, GOLD, 104, 538, size=18)
		displaySurface.blit(surf, rect)

		attackSound = pygame.draw.rect(displaySurface, BLACK, (160, 535, 50, 28), 4)
		surf, rect = make_text('Surf', BLACK, GOLD, 164, 538, size=18)
		displaySurface.blit(surf, rect)

		crySound = pygame.draw.rect(displaySurface, BLACK, (220, 535, 95, 28), 4)
		surf, rect = make_text('Venusaur', BLACK, GOLD, 224, 538, size=18)
		displaySurface.blit(surf, rect)

		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == KEYUP:
				if event.key == K_q:
					return None
			
			elif event.type == MOUSEBUTTONDOWN:
				mousex, mousey = event.pos
				for i in range(len(pageRects)):
					if pageRects[i].collidepoint(mousex, mousey):
						location = keys[(pageNum*54) + (i)]
						mixer.play_song(location)


				if prevPage.collidepoint(mousex, mousey) and pageNum != 0:
					pageNum -= 1
				if nextPage.collidepoint(mousex, mousey) and pageNum != 3:
					pageNum += 1
				if attackSound.collidepoint(mousex, mousey):
					mixer.play_attack_sound('Surf')
				if crySound.collidepoint(mousex, mousey):
					mixer.play_cry_sound(Pokemon(Venusaur()))
						
		pygame.display.update()
		FPSCLOCK.tick(FPS)


main(displaySurface, mixer)
