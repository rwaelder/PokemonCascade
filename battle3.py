import pygame, sys
sys.path.append('attacks')
from pygame.locals import *
from colors import SILVER, BLACK, LIME, YELLOW, RED, BLUE, GRAY, GOLD
from attack import NoAttack
from random import choice, randint
from helpers import *
from pokemonTypes import typeColorDict

class Battle():

	def __init__(self, displaySurface, mixer):
		self.displaySurface = displaySurface
		self.mixer = mixer

		self.fps = 30
		self.fpsclock = pygame.time.Clock()

		self.boxsize = int (displaySurface.get_height() / 10 )
		self.scale = int(self.boxsize / 16)
		self.textSize = 8 * (self.scale - 1)
		self.smalltextSize = 8 * (self.scale - 2)
		self.linewidth = int(self.boxsize / 8)
		self.halfLinewidth = int(self.linewidth / 2)

		self.runawayAttempts = 0

	def left_top_coords_of_box(self, boxx, boxy):
		left = int(boxx * (self.boxsize))
		top = int(boxy * (self.boxsize))
		return (left, top)

	# Drawing functions

	def battle_fade_animation(self):
		count = 0
		left1 = 0
		left2 = 5*self.boxsize
		left3 = 10*self.boxsize
		for i in range(50):
			pygame.draw.rect(self.displaySurface, BLACK, (left1, int(0+(self.boxsize/10)*4*i), self.boxsize*5, self.boxsize))
			pygame.draw.rect(self.displaySurface, BLACK, (left2, int(10*self.boxsize-(self.boxsize/10)*4*i), self.boxsize*5, self.boxsize))
			pygame.draw.rect(self.displaySurface, BLACK, (left3, int(0+(self.boxsize/10)*4*i), self.boxsize*5, self.boxsize))

			for event in pygame.event.get():
				pass

			pygame.display.update()
			self.fpsclock.tick(self.fps)

	def begin_battle_animation(self):
		size = self.boxsize*4
		playerImage = load_pokemon_sprite(self.playerPokemon, frontBack='back')
		playerImage = pygame.transform.scale(playerImage, (size, size))


		opponentImage = load_pokemon_sprite(self.opposingPokemon)
		opponentImage = pygame.transform.scale(opponentImage, (size, size))

		playerStartLeft, playerTop = self.left_top_coords_of_box(9, 3)
		playerEndLeft = self.left_top_coords_of_box(2, 3)[0]

		optStartLeft, optTop = self.left_top_coords_of_box(2, 0.5)
		optEndLeft = self.left_top_coords_of_box(9, 0.5)[0]

		animationFrames = 30
		moveDist = int( (optEndLeft-optStartLeft) / animationFrames )
		for i in range(animationFrames):
			self.draw_background()

			playerLeft = playerStartLeft - (moveDist*i)
			self.displaySurface.blit(playerImage, (playerLeft, playerTop))

			optLeft = optStartLeft + (moveDist*i)
			self.displaySurface.blit(opponentImage, (optLeft, optTop))

			for event in pygame.event.get():
				pass

			pygame.display.update()
			self.fpsclock.tick(self.fps)

	def draw_messages(self, messages, skipLastClick=False):

		left, top = self.left_top_coords_of_box(0.5, 7)
		messagePosition = (left, top, self.boxsize*14, int(self.boxsize * 2.5))
		pygame.draw.rect(self.displaySurface, SILVER, messagePosition)
		pygame.draw.rect(self.displaySurface, BLACK, messagePosition, self.linewidth)

		for i, message in enumerate(messages):
			self.mixer.play_queue()
			words = message.split(' ')
			left, top = self.left_top_coords_of_box(0.5, 7)
			pygame.draw.rect(self.displaySurface, SILVER, messagePosition)
			pygame.draw.rect(self.displaySurface, BLACK, messagePosition, self.linewidth)
			
			left, top = self.left_top_coords_of_box(1, 7.625)
			surf, rect = make_text(' '.join(words[:2]), BLACK, SILVER, left, top, size=self.textSize)
			self.displaySurface.blit(surf, rect)
			left, top = self.left_top_coords_of_box(1, 8.625)
			surf, rect = make_text(' '.join(words[2:]), BLACK, SILVER, left, top, size=self.textSize)
			self.displaySurface.blit(surf, rect)
			pygame.display.update()

			if self.mixer.get_busy():
				wait_for_sound(self.mixer)
			# if (i+1) != len(messages):
			# 	wait_for_click()
			# elif not skipLastClick:
			# 	wait_for_click()
			# else:
			# 	# wait_for_sound()
			# 	# pass
			wait_for_click()
	
	def draw_battlefield(self):
		battlefield = load_image('images/battlefield-grass.png', scale=self.scale)

		left, top = self.left_top_coords_of_box(8.25, 3)
		self.displaySurface.blit(battlefield, (left, top))


		battlefield = load_image('images/battlefield-grass.png', scale=self.scale+1)

		left, top = self.left_top_coords_of_box(0.5, 6)
		self.displaySurface.blit(battlefield, (left, top))	

	def draw_background(self):
		self.displaySurface.fill(SILVER)
		
		background = load_image('images/background-forest.png', scale=self.scale)
		self.displaySurface.blit(background, (0,0))

		self.draw_battlefield()

		left, top = self.left_top_coords_of_box(0.5, 0.5)
		outlinePosition = (left, top, self.displaySurface.get_width()-int(self.boxsize), self.displaySurface.get_height()-int(self.boxsize))
		
		pygame.draw.rect(self.displaySurface, BLACK, outlinePosition, self.linewidth)
		
		left, top = self.left_top_coords_of_box(0.5, 7)
		messagePosition = (left, top, self.boxsize*14, int(self.boxsize * 2.5))
		pygame.draw.rect(self.displaySurface, SILVER, messagePosition)
		pygame.draw.rect(self.displaySurface, BLACK, messagePosition, self.linewidth)

		left, top = self.left_top_coords_of_box(9, 7)
		commandPosition = (left, top, int(self.boxsize*5.5), int(self.boxsize*2.5))
		pygame.draw.rect(self.displaySurface, BLACK, commandPosition, self.linewidth)

	def draw_main_screen(self):
		self.draw_background()
		self.draw_pokemon()
		self.draw_pokemon_status()
		self.draw_menu()
		self.draw_exp_bar()

	def draw_menu(self):
		
		left, top = self.left_top_coords_of_box(0.5, 7)
		messagePosition = (left, top, self.boxsize*9, int(self.boxsize * 2.5))
		pygame.draw.rect(self.displaySurface, SILVER, messagePosition)
		pygame.draw.rect(self.displaySurface, BLACK, messagePosition, self.linewidth)

		left, top = self.left_top_coords_of_box(9, 7)
		commandPosition = (left, top, int(self.boxsize*5.5), int(self.boxsize*2.5))
		pygame.draw.rect(self.displaySurface, SILVER, commandPosition)
		pygame.draw.rect(self.displaySurface, BLACK, commandPosition, self.linewidth)

		message = 'What will %s do?' % self.playerPokemon.name
		words = message.split(' ')

		left, top = self.left_top_coords_of_box(1, 7.625)
		surf, rect = make_text(' '.join(words[:2]), BLACK, SILVER, left, top, size=self.textSize)
		self.displaySurface.blit(surf, rect)
		left, top = self.left_top_coords_of_box(1, 8.625)
		surf, rect = make_text(' '.join(words[2:]), BLACK, SILVER, left, top, size=self.textSize)
		self.displaySurface.blit(surf, rect)

		left, top = self.left_top_coords_of_box(9.5, 7.625)
		fightSurf, fightRect = make_text('{:5s}'.format('Fight'), BLACK, SILVER, left, top, size=self.textSize)
		self.displaySurface.blit(fightSurf, fightRect)

		left, top = self.left_top_coords_of_box(11.5, 7.625)
		pokeSurf, pokeRect = make_text('{:7s}'.format('Pokémon'), BLACK, SILVER, left, top, size=self.textSize)
		self.displaySurface.blit(pokeSurf, pokeRect)

		left, top = self.left_top_coords_of_box(9.5, 8.625)
		bagSurf, bagRect = make_text('{:5s}'.format('Bag'), BLACK, SILVER, left, top, size=self.textSize)
		self.displaySurface.blit(bagSurf, bagRect)

		left, top = self.left_top_coords_of_box(11.5, 8.625)
		runSurf, runRect = make_text('{:7s}'.format('Run'), BLACK, SILVER, left, top, size=self.textSize)
		self.displaySurface.blit(runSurf, runRect)

		options = [fightRect, bagRect, pokeRect, runRect]

		return options

	def draw_battlers(self):
		self.draw_player()
		self.draw_opponent()

	def draw_player(self):
		playerImage = load_trainer_image(self.player, back=True).convert_alpha()
		# playerImage = pygame.transform.flip(playerImage, True, False)
		self.displaySurface.blit(playerImage, (50,300))

	def draw_opponent(self):
		opponentImage = load_trainer_image(self.opponent).convert_alpha()
		self.displaySurface.blit(opponentImage, (300,50))

	def draw_pokemon(self):
		self.draw_player_pokemon()
		self.draw_opponent_pokemon()	

	def draw_player_pokemon(self):
		left, top = self.left_top_coords_of_box(2, 3)
		size = self.boxsize*4
		# pygame.draw.rect(self.displaySurface, SILVER, (left, top, size, size))
		playerImage = load_pokemon_sprite(self.playerPokemon, frontBack='back')
		playerImage = pygame.transform.scale(playerImage, (size, size))
		# playerImage = pygame.transform.flip(playerImage, True, False)
		self.displaySurface.blit(playerImage, (left, top))

		left, top = self.left_top_coords_of_box(7.75, 4.75)
		pygame.draw.rect(self.displaySurface, SILVER, (left, top, self.boxsize*6.125, self.boxsize*2.5))
		pygame.draw.rect(self.displaySurface, BLACK, (left, top, self.boxsize*6.125, self.boxsize*2.5), self.halfLinewidth)

		left, top = self.left_top_coords_of_box(8, 5)
		playerText = '{:10s}'.format(self.playerPokemon.name)
		textSurf, textRect = make_text(playerText, BLACK, SILVER, left, top, size=8*(self.scale-1))
		self.displaySurface.blit(textSurf, textRect)

		left, top = self.left_top_coords_of_box(11.75, 5)
		playerText = 'lv.{:2d}'.format(self.playerPokemon.level)
		textSurf, textRect = make_text(playerText, BLACK, SILVER, left, top, size=8*(self.scale-1))
		self.displaySurface.blit(textSurf, textRect)
		self.draw_exp_bar()

	def draw_opponent_pokemon(self):
		left, top = self.left_top_coords_of_box(9, 0.5)
		size = self.boxsize*4
		# pygame.draw.rect(self.displaySurface, SILVER, (left, top, size, size))
		opponentImage = load_pokemon_sprite(self.opposingPokemon)
		opponentImage = pygame.transform.scale(opponentImage, (size, size))
		self.displaySurface.blit(opponentImage, (left, top))
		
		left, top = self.left_top_coords_of_box(0.75, 0.75)
		pygame.draw.rect(self.displaySurface, SILVER, (left, top, self.boxsize*6.125, self.boxsize*1.5))
		pygame.draw.rect(self.displaySurface, BLACK, (left, top, self.boxsize*6.125, self.boxsize*1.5), self.halfLinewidth)


		left, top = self.left_top_coords_of_box(1, 1)
		opponentText = '{:10s}'.format(self.opposingPokemon.name)
		textSurf, textRect = make_text(opponentText, BLACK, SILVER, left, top, size=self.textSize)
		self.displaySurface.blit(textSurf, textRect)

		left, top = self.left_top_coords_of_box(4.75, 1)
		opponentText = 'lv.{:2d}'.format(self.opposingPokemon.level)
		textSurf, textRect = make_text(opponentText, BLACK, SILVER, left, top, size=self.textSize)
		self.displaySurface.blit(textSurf, textRect)

	def draw_pokemon_status(self):
		self.draw_player_status()
		self.draw_opponent_status()

	def draw_player_status(self):
		hpPct, color = self.playerPokemon.hp_bar()
		
		left, top = self.left_top_coords_of_box(10, 5.5)

		playerText = self.playerPokemon.status.displayText.center(5)
		if playerText != ''.center(5):		
			textSurf, textRect = make_text(playerText, BLACK, self.playerPokemon.status.displayColor, left, top, size=self.textSize)
			textRect.right = left
			pygame.draw.rect(self.displaySurface, BLACK, (textRect.left, textRect.top, textRect.width, textRect.height), self.halfLinewidth)
			self.displaySurface.blit(textSurf, textRect)
		else:
			textSurf, textRect = make_text('HP', GOLD, BLACK, left, top, size=self.textSize)
			textRect.right = left
			pygame.draw.rect(self.displaySurface, BLACK, (textRect.left, textRect.top, textRect.width, textRect.height), self.halfLinewidth)
			self.displaySurface.blit(textSurf, textRect)

		hpBarLength = int(self.boxsize * 3.5)
		hpBarHeight = textRect.height

		left, top = self.left_top_coords_of_box(10, 5.5)
		
		pygame.draw.rect(self.displaySurface, SILVER, (left, top, hpBarLength, hpBarHeight))
		if hpPct != 0:
			pygame.draw.rect(self.displaySurface, color, (left, top, int(hpBarLength*hpPct), hpBarHeight))
		pygame.draw.rect(self.displaySurface, BLACK, (left, top, hpBarLength, hpBarHeight), self.halfLinewidth)
		

		left, top = self.left_top_coords_of_box(10, 6)
		hpText = '{:3d}/{:3d}'.format(self.playerPokemon.hp, self.playerPokemon.maxHp)
		textSurf, textRect = make_text(hpText, BLACK, SILVER, left, top, size=self.textSize)
		# textRect.right = left
		self.displaySurface.blit(textSurf, textRect)



	def draw_opponent_status(self):
		hpPct, color = self.opposingPokemon.hp_bar()
			
		left, top = self.left_top_coords_of_box(2.5, 1.5)
		
		opponentText = self.opposingPokemon.status.displayText.center(5)
		if opponentText != ''.center(5):
			textSurf, textRect = make_text(opponentText, BLACK, self.opposingPokemon.status.displayColor, left, top, size=self.textSize)
			textRect.right = left
			pygame.draw.rect(self.displaySurface, BLACK, (textRect.left, textRect.top, textRect.width, textRect.height), self.halfLinewidth)
			self.displaySurface.blit(textSurf, textRect)
		else:
			textSurf, textRect = make_text('HP', GOLD, BLACK, left, top, size=self.textSize)
			textRect.right = left
			pygame.draw.rect(self.displaySurface, BLACK, (textRect.left, textRect.top, textRect.width, textRect.height), self.halfLinewidth)
			self.displaySurface.blit(textSurf, textRect)

		hpBarLength = int(self.boxsize * 3.5)
		hpBarHeight = textRect.height

		pygame.draw.rect(self.displaySurface, SILVER, (left, top, hpBarLength, hpBarHeight))
		if hpPct != 0:
			pygame.draw.rect(self.displaySurface, color, (left, top, int(hpBarLength*hpPct), hpBarHeight))
		pygame.draw.rect(self.displaySurface, BLACK, (left, top, hpBarLength, hpBarHeight), self.halfLinewidth)
		

	def draw_exp_bar(self, expPct=0, animate=False):
		if not animate:
			expPct = self.playerPokemon.exp_bar_length()
		
		left, top = self.left_top_coords_of_box(9, 6.5)

		textSurf, textRect = make_text('EXP', GOLD, BLACK, left, top, size=self.textSize)
		textRect.right = left
		pygame.draw.rect(self.displaySurface, BLACK, textRect, self.halfLinewidth)
		
		expBarLength = self.boxsize * 4.5
		expBarHeight = textRect.height
		self.displaySurface.blit(textSurf, textRect)

		
		if expPct != 0:
			pygame.draw.rect(self.displaySurface, BLUE, (left, top, int(expBarLength*expPct), expBarHeight))
		pygame.draw.rect(self.displaySurface, BLACK, (left, top, expBarLength, expBarHeight), self.halfLinewidth)


	def draw_attack_stats(self, attack):
		left, top = self.left_top_coords_of_box(10, 7)
		commandPosition = (left, top, int(self.boxsize*4.5), int(self.boxsize*2.5))
		pygame.draw.rect(self.displaySurface, SILVER, commandPosition)
		pygame.draw.rect(self.displaySurface, BLACK, commandPosition, self.linewidth)
		# pygame.draw.rect(self.displaySurface, SILVER, (350, 575, 200, 90))

		left, top = self.left_top_coords_of_box(10.5, 7.625)
		surf, rect = make_text(attack.type, BLACK, typeColorDict[attack.type], left, top, size=self.textSize)
		self.displaySurface.blit(surf, rect)

		left, top = self.left_top_coords_of_box(10.5, 8.625)
		ppText = 'PP {:2}/{:2}'.format(attack.pp, attack.maxPP)
		surf, rect = make_text(ppText, BLACK, SILVER, left, top, size=self.textSize)
		self.displaySurface.blit(surf, rect)

		pygame.display.update()

	def animate_damage(self, damage, defendingPokemon):
		damageDealt = 0
		while damageDealt < damage:
			defendingPokemon.take_damage(1)
			self.draw_pokemon_status()

			for event in pygame.event.get():
				pass

			damageDealt += 1
			pygame.display.update()
			self.fpsclock.tick(self.fps)

	def animate_exp(self, EXPbar, endEXPbar):

		while EXPbar < endEXPbar:

			self.draw_exp_bar(EXPbar, animate=True)

			for event in pygame.event.get():
				pass

			EXPbar += 0.01
			pygame.display.update()
			self.fpsclock.tick(self.fps)



	def choose_battler_from_party(self):
		self.displaySurface.fill(SILVER)

		background = load_image('images/background-indoor.png', scale=self.scale)
		self.displaySurface.blit(background, (0,0))

		left, top = self.left_top_coords_of_box(0.5, 0.5)
		outlinePosition = (left, top, self.displaySurface.get_width()-int(self.boxsize), self.displaySurface.get_height()-int(self.boxsize))
		pygame.draw.rect(self.displaySurface, BLACK, outlinePosition, self.linewidth)
		
		left, top = self.left_top_coords_of_box(0.5, 8)
		messagePosition = (left, top, self.boxsize*14, int(self.boxsize * 1.5))
		pygame.draw.rect(self.displaySurface, BLACK, messagePosition, self.linewidth)
		
		pygame.display.update()
		


		pokeCoords = [(1, 0.75), (1, 3.125), (1, 5.5), (8, 0.75), (8, 3.125), (8, 5.5)]
		rects = []
		# draw boxes
		for i in range(6):
			x, y = pokeCoords[i]
			left, top = self.left_top_coords_of_box(x, y)
			rect = pygame.draw.rect(self.displaySurface, SILVER, (left, top, self.boxsize*6, self.boxsize*2.25))
			rect = pygame.draw.rect(self.displaySurface, BLACK, (left, top, self.boxsize*6, self.boxsize*2.25), self.halfLinewidth)
			rects.append(rect)
			
		for i, pokemon in enumerate(self.player.party):
			x, y = pokeCoords[i]
			left, top = self.left_top_coords_of_box(x, y)
			# pokemon image
			image = load_pokemon_menu_sprite(pokemon, self.scale)
			self.displaySurface.blit(image, (left, top))
			# pokemon name, status
			left, top = self.left_top_coords_of_box(x+2.25, y+0.5)
			surf, rect = make_text('{:10}'.format(pokemon.name), BLACK, SILVER, left, top, size=self.textSize)
			self.displaySurface.blit(surf, rect)
			left, top = self.left_top_coords_of_box(x+4, y+1)
			surf, rect = make_text('lv.%i' % pokemon.level, BLACK, SILVER, left, top, size=self.textSize)
			self.displaySurface.blit(surf, rect)
			# pokemon hp
			left, top = self.left_top_coords_of_box(x+2.5, y+1.5)
			hpPct, color = pokemon.hp_bar()
			
			if pokemon.hp != 0:
				pygame.draw.rect(self.displaySurface, color, (left, top, int(self.boxsize*3*hpPct), int(self.boxsize/2)))
			pygame.draw.rect(self.displaySurface, BLACK, (left, top, self.boxsize*3, int(self.boxsize/2)), self.halfLinewidth)

			left, top = self.left_top_coords_of_box(x+2.25, y+1)
			statusText = pokemon.status.displayText.center(5)
			surf, rect = make_text(statusText, BLACK, pokemon.status.displayColor, left, top, size=self.textSize)
			self.displaySurface.blit(surf, rect)

			if pokemon.fainted:
				statusText = 'FNT'.center(5)
			pygame.display.update()
		

		selected = False
		
		while not selected:
			messages = []
			

			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()
				elif event.type == KEYUP:
					if event.key == K_q:
						return None
				
				elif event.type == MOUSEBUTTONDOWN:
					mousex, mousey = event.pos
					for i in range(len(self.player.party)):
						if rects[i].collidepoint(mousex, mousey):
							if i == 0:
								messages.append('%s is already in battle!' % self.player.party[0].name)
								break
							pokeNumber = i
							selected, messages = self.player.party[i].select()
							
			if messages:
				self.draw_messages(messages)
				pygame.draw.rect(self.displaySurface, SILVER, (40, 575, 250, 90))
				pygame.display.update()

		return pokeNumber

	# Battle functions

	def calculate_battle_stats(self):
		self.playerPokemon.calculate_battle_stats()
		self.opposingPokemon.calculate_battle_stats()

	def get_faster_pokemon(self):
		fasterPokemon = ''
		if self.playerPokemon.battleSpeed > self.opposingPokemon.battleSpeed:
			fasterPokemon = 'player'
		else:
			fasterPokemon = 'opponent'
		return fasterPokemon

	def check_recoil(self, attackingPokemon, attackNumber, damage):
		recoilDamage = attackingPokemon.attacks[attackNumber].get_recoil(damage)
		if recoilDamage:
			recoilMessage = ['%s is hit with recoil!' % attackingPokemon.name]
			self.draw_messages(recoilMessage)
			attackingPokemon.take_damage(recoilDamage)

	def fight(self):


		left, top = self.left_top_coords_of_box(0.5, 7)
		messagePosition = (left, top, self.boxsize*9.5, int(self.boxsize * 2.5))
		pygame.draw.rect(self.displaySurface, SILVER, messagePosition)
		pygame.draw.rect(self.displaySurface, BLACK, messagePosition, self.linewidth)

		left, top = self.left_top_coords_of_box(10, 7)
		commandPosition = (left, top, int(self.boxsize*4.5), int(self.boxsize*2.5))
		pygame.draw.rect(self.displaySurface, SILVER, commandPosition)
		pygame.draw.rect(self.displaySurface, BLACK, commandPosition, self.linewidth)


		# for event in pygame.event.get():
		# 	pass
		# pygame.display.update()

		attacks = self.playerPokemon.attacks

		while len(attacks) < 4:
			attacks.append(NoAttack())


		attackCoords = [self.left_top_coords_of_box(1, 7.625), self.left_top_coords_of_box(5.5, 7.625), 
		self.left_top_coords_of_box(1, 8.625), self.left_top_coords_of_box(5.5, 8.625)]
		rects = []

		for i in range(4):
			left, top = attackCoords[i]
			surf, atkRect = make_text('{:12}'.format(attacks[i].name), BLACK, SILVER, left, top, size=self.textSize)
			rects.append(atkRect)
			self.displaySurface.blit(surf, atkRect)


		pygame.display.update()
		
		selected = self.playerPokemon.keepUsingAttack
		if selected:
			attackNumber = self.playerPokemon.continueAttackNumber
		
		while not selected:
			messages = []
			

			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()
				elif event.type == KEYUP:
					if event.key == K_q:
						return None
				elif event.type == MOUSEMOTION:
					mousex, mousey = event.pos
					for i in range(4):
						if rects[i].collidepoint(mousex, mousey):
							self.draw_attack_stats(attacks[i])
							break
						else:
							pygame.draw.rect(self.displaySurface, SILVER, (350, 575, 200, 90))
							pygame.display.update()

				elif event.type == MOUSEBUTTONDOWN:
					mousex, mousey = event.pos
					for i in range(4):
						if rects[i].collidepoint(mousex, mousey):
							attackNumber = i
							selected, messages = self.playerPokemon.attacks[i].select()
							
			if messages:
				self.draw_messages(messages)
				pygame.draw.rect(self.displaySurface, SILVER, (40, 575, 250, 90))
				for i in range(4):
					left, top = attackCoords[i]
					surf, atkRect = make_text('{:10}'.format(attacks[i].name), BLACK, SILVER, left, top, size=20)
					rects.append(atkRect)
					self.displaySurface.blit(surf, atkRect)
				pygame.display.update()

		return attackNumber

	def get_turn_order(self):
		firstMove = ''
		if self.action == 'fight':
			playerAttack = self.playerTurn
			if self.opponentAction != 'fight':
				firstMove = 'opponent'
			else:
				opponentAttack = self.opponentTurn
				if self.playerPokemon.attacks[playerAttack].priority == self.opposingPokemon.attacks[opponentAttack].priority:
					firstMove = self.get_faster_pokemon()
				elif self.playerPokemon.attacks[playerAttack].priority > self.opposingPokemon.attacks[opponentAttack].priority:
					firstMove = 'player'
				else:
					firstMove = 'opponent'

		else:
			firstMove = 'player'

		return firstMove

	def status_handle(self, pokemon, attackNumber, otherPokemon):
		attack = pokemon.attacks[attackNumber]
		turnSkip, messages, damage = pokemon.handle_status(self.mixer, attack, self.isTurnEnd)
		if messages:
			self.draw_messages(messages)
		if damage > 0:
			pokemon.take_damage(damage)
			self.draw_pokemon_status()
		for message in messages:
			if 'Seed' in message:
				seedHeal = int(pokemon.maxHp / 8)
				otherPokemon.heal(seedHeal)

		return turnSkip

	def do_fight(self, attackingPokemon, attackNumber, defendingPokemon):
		skip = self.status_handle(attackingPokemon, attackNumber, defendingPokemon)
		if not skip:
			print(attackingPokemon.attacks[attackNumber].name)
			damage, messages = attackingPokemon.attacks[attackNumber].use(self.mixer, attackingPokemon, defendingPokemon)

			self.draw_main_screen()
			self.draw_messages(messages, skipLastClick=True)
			self.animate_damage(damage, defendingPokemon)
			self.draw_pokemon_status()
			self.check_recoil(attackingPokemon, attackNumber, damage)
			self.draw_pokemon_status()


	def do_opponent_turn(self):
		if self.opponentAction == 'fight':
			attackNumber = self.opponentTurn
			self.do_fight(self.opposingPokemon, attackNumber, self.playerPokemon)
		elif self.opponentAction == 'bag':
			itemNumber = self.opponentTurn
			self.do_use_item(itemNumber)
		elif self.opponentAction == 'changePoke':
			pokeNumber = self.opponentTurn
			self.do_switch_pokemon(self.opposingTrainer, pokeNumber)
			self.opposingPokemon = self.opposingTrainer.party[0]
			messages = ['%s sent out %s!' % (self.opposingTrainer.name, self.opposingPokemon.name)]
			self.draw_messages(messages)
			self.draw_main_screen()
			self.calculate_battle_stats()
			pygame.display.update()

	def do_switch_pokemon(self, trainer, pokeNumber):
		messages = []
		messages.append('%s, come back!' % trainer.party[0].name)
		self.draw_messages(messages)
		pokemonSwitchIn = trainer.party[pokeNumber]
		trainer.party[pokeNumber] = trainer.party[0]
		trainer.party[0] = pokemonSwitchIn
		self.mixer.play_cry_sound(pokemonSwitchIn)

	def handle_turn(self):
		self.isTurnEnd = False
		firstMove = self.get_turn_order()

		if self.action == 'fight':
			playerAttack = self.playerTurn
			
			if firstMove == 'player':
				self.do_fight(self.playerPokemon, playerAttack, self.opposingPokemon)
				if self.opposingPokemon.fainted:
					return
				self.do_opponent_turn()

			else:
				self.do_opponent_turn()
				if self.playerPokemon.fainted:
					return
				self.do_fight(self.playerPokemon, playerAttack, self.opposingPokemon)
				
		elif self.action == 'bag':
			playerAttack = None

		elif self.action == 'changePoke':
			playerAttack = None
			pokeNumber = self.playerTurn

			self.do_switch_pokemon(self.player, pokeNumber)
			self.playerPokemon = self.player.party[0]
			messages = ['Go, %s!' % self.playerPokemon.name]
			self.draw_messages(messages)
			self.draw_main_screen()
			self.calculate_battle_stats()
			pygame.display.update()

			self.do_opponent_turn()


		elif self.action == 'run':
			playerAttack = None
			runAway, messages = self.run()

			self.draw_messages(messages)

			if self.battleType == 'trainer':
				return

			elif runAway:
				return runAway

			else:
				self.do_opponent_turn()


		self.isTurnEnd = True
		self.status_handle(self.playerPokemon, 0, self.opposingPokemon)
		self.status_handle(self.opposingPokemon, 0, self.playerPokemon)

	def calculate_exp(self):
		if self.battleType == 'wild':
			a = 1
		else:
			a = 1.5

		b = self.opposingPokemon.pocketMonster.baseExpYield
		# lucky egg
		# e = 1.5 if hold item is lucky egg
		# TODO: items
		e = 1
		# affection
		# f = affection modifier
		f = 1
		L = self.opposingPokemon.level
		p = 1
		# s = number of pokemon participated in battle
		s = 1
		t = 1 # traded or original trainer
		v = 1

		exp = int(a * t * b * e * L * p * f * v / 7 / s)
		return exp

	def post_battle(self):
		messages = []
		if not self.player.canBattle:
			messages.append('%s has no more Pokémon!' % self.player.name)
			messages.append('%s whited out!' % self.player.name)
			messages.append('Game over!')
		else:
			if self.battleType == 'wild':
				self.mixer.play_song('Wild Victory')
			else:
				self.mixer.play_song('Trainer Victory')
			startEXPbar = self.playerPokemon.exp_bar_length()
			exp = self.calculate_exp()
			m = self.playerPokemon.gain_exp(exp)
			messages.extend(m)
			endEXPbar = self.playerPokemon.exp_bar_length()

		self.draw_messages(messages)
		self.animate_exp(startEXPbar, endEXPbar)

	def run(self):
		runAway = False
		messages = []
		self.runawayAttempts += 1

		if self.battleType == 'trainer':
			messages.append('There\'s no running from a trainer battle!')
			runAway = False

		else:
			flee = int((self.playerPokemon.speed * 28) / self.opposingPokemon.speed + 30 * self.runawayAttempts)
			f = randint(0, 255)
			print(f, flee)
			if f < flee:
				messages.append('Got away safely!')
				runAway = True
			else:
				messages.append('Can\'t escape!')
				runAway = False

		return runAway, messages


class WildBattle(Battle):

	def __init__(self, displaySurface, mixer, player, wildPokemon):
		super().__init__(displaySurface, mixer)

		self.player = player.trainer
		self.playerPokemon = self.player.party[0]
		self.opposingPokemon = wildPokemon
		self.battleType = 'wild'

		self.main()

	def get_opponent_turn(self):
		if self.opposingPokemon.keepUsingAttack:
			self.opponentTurn = self.opposingPokemon.continueAttackNumber
		else:
			self.opponentTurn = choice(list(range(len(self.opposingPokemon.attacks))))
		self.opponentAction = 'fight'


	def main(self):
		

		self.mixer.play_song('Wild Battle')

		self.battle_fade_animation()
		self.begin_battle_animation()

		mousex = mousey = 0
		self.draw_main_screen()
		pygame.display.update()
		
		self.calculate_battle_stats()

		while True:
			self.draw_pokemon_status()
			
			
			self.action = ''

			if self.playerPokemon.fainted:
				pokeNumber = self.choose_battler_from_party()
				self.do_switch_pokemon(self.player, pokeNumber)
				self.playerPokemon = self.player.party[0]
				messages = ['Go, %s!' % self.playerPokemon.name]
				self.draw_messages(messages)
				self.draw_main_screen()

			if self.opposingPokemon.fainted:
				break

			self.calculate_battle_stats()
			while not self.action:
				options = self.draw_menu()

				for event in pygame.event.get():
					if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
						pygame.quit()
						sys.exit()

					elif event.type == MOUSEBUTTONDOWN:
						mousex, mousey = event.pos
						if options[0].collidepoint(mousex, mousey):
							attackNumber = self.fight()
							if attackNumber != None:
								self.action = 'fight'
								self.playerTurn = attackNumber

						elif options[1].collidepoint(mousex, mousey):
							self.action = 'bag'
							self.playerTurn = None

						elif options[2].collidepoint(mousex, mousey):
							pokeNumber = self.choose_battler_from_party()
							print(pokeNumber)
							self.draw_main_screen()
							if pokeNumber != None:
								self.action = 'changePoke'
								self.playerTurn = pokeNumber

						elif options[3].collidepoint(mousex, mousey):
							self.action = 'run'
							self.playerTurn = None

				self.mixer.play_queue()
				pygame.display.update()
				self.fpsclock.tick(self.fps)



			self.get_opponent_turn()
			runAway = self.handle_turn()
			pygame.display.update()
			self.fpsclock.tick(self.fps)

			if runAway:
				break

		if runAway:
			wait_for_click()
		else:
			self.post_battle()
			self.draw_exp_bar()
			pygame.display.update()
			wait_for_click()

		self.playerPokemon.reset_battle_stats()
		self.opposingPokemon.reset_battle_stats()


class TrainerBattle(Battle):

	def __init__(self, displaySurface, mixer, player, opponent):
		super().__init__(displaySurface, mixer)

		self.player = player.trainer
		self.playerPokemon = self.player.party[0]
		self.opponent = opponent
		self.opposingPokemon = self.opponent.party[0]
		self.batleType = 'trainer'

		self.main()

	def get_opponent_turn(self):
		if self.opposingPokemon.keepUsingAttack:
			self.opponentTurn = self.opposingPokemon.continueAttackNumber
		else:
			self.opponentTurn = choice(list(range(len(self.opposingPokemon.attacks))))
		self.opponentAction = 'fight'


	def main(self):
		

		mousex = mousey = 0

		self.displaySurface.fill(SILVER)
		pygame.draw.rect(self.displaySurface, BLACK, (25, 25, 550, 650), 5)
		pygame.draw.rect(self.displaySurface, BLACK, (25, 555, 550, 120), 5)
		pygame.draw.rect(self.displaySurface, BLACK, (340, 555, 235, 120), 5)
		self.draw_battlers()
		pygame.display.update()

		self.mixer.play_song('Trainer Battle')

		messages = ['%s wants to fight!' % self.opponent.name]
		self.draw_messages(messages)

		messages = ['%s sent out %s!' % (self.opponent.name, self.opposingPokemon.name)]
		self.draw_messages(messages)
		self.draw_opponent_pokemon()
		self.draw_opponent_status()
		pygame.display.update()
		self.mixer.play_cry_sound(self.opposingPokemon)

		messages = ['Go %s!' % self.playerPokemon.name]
		self.draw_messages(messages)
		self.draw_player_pokemon()
		self.draw_player_status()
		self.draw_exp_bar()
		pygame.display.update()
		self.mixer.play_cry_sound(self.playerPokemon)
		
		self.calculate_battle_stats()

		while self.player.canBattle() and self.opponent.canBattle():
			while not self.playerPokemon.fainted and not self.opposingPokemon.fainted:
				self.draw_pokemon_status()
				self.calculate_battle_stats()
				self.action = ''

				
				while not self.action:
					options = self.draw_menu()

					for event in pygame.event.get():
						if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
							pygame.quit()
							sys.exit()

						elif event.type == MOUSEBUTTONDOWN:
							mousex, mousey = event.pos
							if options[0].collidepoint(mousex, mousey):
								attackNumber = self.fight()
								if attackNumber != None:
									self.action = 'fight'
									self.playerTurn = attackNumber

							elif options[1].collidepoint(mousex, mousey):
								self.action = 'bag'
								self.playerTurn = None

							elif options[2].collidepoint(mousex, mousey):
								pokeNumber = self.choose_battler_from_party()
								self.draw_main_screen()
								if pokeNumber != None:
									self.action = 'changePoke'
									self.playerTurn = pokeNumber

							elif options[3].collidepoint(mousex, mousey):
								self.action = 'run'
								self.playerTurn = None


					self.mixer.play_queue()
					pygame.display.update()
					self.fpsclock.tick(self.fps)



				self.get_opponent_turn()
				self.handle_turn()
				pygame.display.update()
				self.fpsclock.tick(self.fps)

			self.post_battle()
			self.draw_exp_bar()
			pygame.display.update()

			if self.playerPokemon.fainted and self.player.canBattle():
				messages = ['%s fainted!' % self.playerPokemon.name]
				self.draw_messages(messages)
				pokeNumber = self.choose_battler_from_party()
				self.do_switch_pokemon(self.player, pokeNumber)
				self.playerPokemon = self.player.party[0]
				messages = ['Go, %s!' % self.playerPokemon.name]
				self.draw_messages(messages)
				self.draw_main_screen()

			if self.opposingPokemon.fainted and self.opponent.canBattle():
				messages = ['Foe %s fainted!' % self.opposingPokemon.name]
				self.draw_messages(messages)
				pokeNumber = self.opponent.computer_choose_next_battler()
				self.do_switch_pokemon(self.opponent, pokeNumber)
				self.opposingPokemon = self.opponent.party[0]
				messages = ['%s sent out %s!' % (self.opponent.name, self.opposingPokemon.name)]
				self.draw_messages(messages)
				self.draw_main_screen()

		

		messages = ['%s defeated %s!' % (self.player.name, self.opponent.name)]
		self.draw_messages(messages)
		self.player.reset_battle_stats()
		self.opponent.reset_battle_stats()
		wait_for_click()
		

