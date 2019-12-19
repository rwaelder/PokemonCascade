import pygame, sys
from pygame.locals import *
from colors import BLACK, WHITE
from pocketMonsters import Pokemon
from helpers import make_text, load_pokemon_image, load_pokemon_sprite
# from creatures1_25 import *
# from creatures26_50 import *
# from creatures51_75
from pokemonList import pokemonList
from pokemonTypes import typeColorDict

class ChooseParty():

	def __init__(self, displaySurface, mixer):
		self.displaySurface = displaySurface
		self.mixer = mixer
		self.party = []

		# self.mixer.music.load('sounds/03 To Bill\'s Origin ~ From Cerulean.mp3')
		# self.mixer.music.play(loops=-1)
		
		self.main()

	def draw_page(self, pageNum):
		pokeCoords = [(40, 50), (40, 145), (40,240), (40, 335), (40, 430), (300, 50), (300, 145), (300, 240), (300, 335), (300, 430)]
		rects = []
		typeCoords = [(115, 46), (115, 67)]
		# draw boxes
		for i in range(10):
			left, top = pokeCoords[i]
			rect = pygame.draw.rect(self.displaySurface, BLACK, (left, top, 250, 90), 4)
			rects.append(rect)
			
			# pokemon image
			pokemonNumber = (pageNum*10) + (i+1)
			
			pygame.draw.rect(self.displaySurface, WHITE, (left+4, top+3, 85, 85))
			pokemon = pokemonList[pokemonNumber]
			# image = load_pokemon_image(pokemon, style='official')
			image = load_pokemon_sprite(pokemon)
			image = pygame.transform.scale(image, (85, 85))
			self.displaySurface.blit(image, (left+4, top+3))
			# pokemon name, status
			surf, rect = make_text('{:12}'.format(pokemon.name), BLACK, WHITE, left+115, top+6, size=18)
			self.displaySurface.blit(surf, rect)
			surf, rect = make_text('No. %s' % str(pokemonNumber).zfill(3), BLACK, WHITE, left+115, top+27, size=16)
			self.displaySurface.blit(surf, rect)

			pygame.draw.rect(self.displaySurface, WHITE, (left+115, top+46, 80, 40))
			for i, pokemonType in enumerate(pokemon.type):
				offLeft, offTop = typeCoords[i]
				surf, rect = make_text(pokemonType.center(8, ' '), BLACK, typeColorDict[pokemonType], left+offLeft, top+offTop, size=16)
				self.displaySurface.blit(surf, rect)


		return rects

	def draw_party(self):
		partyCoords = [(30, 580), (121, 580), (212, 580), (303, 580), (394, 580), (485, 580)]

		rects = []
		for i in range(6):
			left, top = partyCoords[i]
			pygame.draw.rect(self.displaySurface, WHITE, (left, top, 85, 85))
			rect = pygame.draw.rect(self.displaySurface, BLACK, (left, top, 85, 85), 2)
			rects.append(rect)

		for i, pokemon in enumerate(self.party):
			left, top = partyCoords[i]
			image = load_pokemon_sprite(pokemon)
			image = pygame.transform.scale(image, (81, 81))
			self.displaySurface.blit(image, (left+2, top+2))

		return rects

	def main(self):
		FPS = 30
		FPSCLOCK = pygame.time.Clock()

		self.displaySurface.fill(WHITE)
		pygame.draw.rect(self.displaySurface, BLACK, (25, 25, 550, 650), 5)

		self.mixer.play_song('Opening 2')

		prevPage = pygame.draw.rect(self.displaySurface, BLACK, (40, 535, 50, 28), 4)
		surf, rect = make_text('Prev', BLACK, WHITE, 44, 538, size=18)
		self.displaySurface.blit(surf, rect)

		nextPage = pygame.draw.rect(self.displaySurface, BLACK, (100, 535, 50, 28), 4)
		surf, rect = make_text('Next', BLACK, WHITE, 104, 538, size=18)
		self.displaySurface.blit(surf, rect)
		
		doneButton = pygame.draw.rect(self.displaySurface, BLACK, (500, 535, 50, 28), 4)
		surf, rect = make_text('Done', BLACK, WHITE, 504, 538, size=18)
		self.displaySurface.blit(surf, rect)

		pygame.display.update()
		

		done = False
		mousex, mousey = (0, 0)
		pageNum = 0

		while not done:
			
			pageRects = self.draw_page(pageNum)
			partyRects = self.draw_party()

			

			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()
				elif event.type == KEYUP:
					if event.key == K_q:
						return None
				
				elif event.type == MOUSEBUTTONDOWN:
					mousex, mousey = event.pos
					for i in range(10):
						if pageRects[i].collidepoint(mousex, mousey) and len(self.party) < 6:
							pokemonNumber = (pageNum*10) + (i+1)
							pokemon = Pokemon(pokemonList[pokemonNumber], level=50)
							self.party.append(pokemon)
							self.mixer.play_cry_sound(pokemon)

					for i in range(len(self.party)):
						if partyRects[i].collidepoint(mousex, mousey):
							self.party.pop(i)

					if prevPage.collidepoint(mousex, mousey) and pageNum != 0:
						pageNum -= 1
					if nextPage.collidepoint(mousex, mousey) and pageNum != 14:
						pageNum += 1

					if doneButton.collidepoint(mousex, mousey) and len(self.party) > 0:
						done = True
							
			pygame.display.update()
			FPSCLOCK.tick(FPS)

		return self.party
