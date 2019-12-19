import pygame, sys
from pygame.locals import *
from colors import WHITE, BLACK, LIME, YELLOW, RED, BLUE
sys.path.append('attacks')
from attack import NoAttack
from random import choice
from pocketMonsters import Pokemon
from creatures1_25 import *
from creatures26_50 import *
from saveLoad import save, load


def wait_for_click():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONUP:
				return
			else:
				continue

def make_text(text, color, bgcolor, left, top, size=20, style='basic'):
	if style == 'basic':
		font = pygame.font.Font('DejaVuSansMono.ttf', size)
	elif style == 'bold':
		font = pygame.font.Font('DejaVuSansMono-Bold.ttf', size)
	elif style == 'italic':
		font = pygame.font.Font('DejaVuSansMono-Oblique.ttf', size)
	elif style == 'bolditalic' or style == 'italicbold':
		font = pygame.font.Font('DejaVuSansMono-BoldOblique.ttf', size)
	
	textSurf = font.render(text, True, color, bgcolor)
	textRect = textSurf.get_rect()
	textRect.topleft = (left, top)
	return textSurf, textRect

def load_pokemon_image(pokemon):

	imageFile = 'pokemonIcons/' + pokemon.image

	return pygame.image.load(imageFile)

def redraw_screen(displaySurface, playerPokemon, opponentPokemon):
	displaySurface.fill(WHITE)
	pygame.draw.rect(displaySurface, BLACK, (25, 25, 550, 650), 5)
	pygame.draw.rect(displaySurface, BLACK, (25, 555, 550, 120), 5)
	pygame.draw.rect(displaySurface, BLACK, (340, 555, 235, 120), 5)
	draw_pokemon(displaySurface, playerPokemon, opponentPokemon)
	draw_player_pokemon_hp(displaySurface, playerPokemon)
	draw_opponent_pokemon_hp(displaySurface, opponentPokemon)

def draw_pokemon(displaySurface, playerPokemon, opponentPokemon):

	playerImage = load_pokemon_image(playerPokemon).convert()
	opponentImage = load_pokemon_image(opponentPokemon).convert()
	playerImage = pygame.transform.flip(playerImage, True, False)
	# playerImage.set_colorkey(MAGENTA)
	# opponentImage.set_colorkey(MAGENTA)
	displaySurface.blit(playerImage, (50,300))
	displaySurface.blit(opponentImage, (300,50))

	
	playerText = '{:11s}'.format(playerPokemon.name)
	textSurf, textRect = make_text(playerText, BLACK, WHITE, 350, 420, style='bold')
	displaySurface.blit(textSurf, textRect)
	playerText = 'lv.{:2d}'.format(playerPokemon.level)
	textSurf, textRect = make_text(playerText, BLACK, WHITE, 350, 445, size=18)
	displaySurface.blit(textSurf, textRect)

	expPct = playerPokemon.exp_bar_length()

	textSurf, textRect = make_text('EXP', BLACK, WHITE, 350, 527, size=18)
	displaySurface.blit(textSurf, textRect)
	pygame.draw.rect(displaySurface, BLACK, (390, 530, 160, 15), 4)
	pygame.draw.rect(displaySurface, WHITE, (392, 532, 156, 11))
	if expPct != 0:
		pygame.draw.rect(displaySurface, BLUE, (392, 532, int(156*expPct), 11))


	opponentText = '{:11s}'.format(opponentPokemon.name)
	textSurf, textRect = make_text(opponentText, BLACK, WHITE, 50, 45, style='bold')
	displaySurface.blit(textSurf, textRect)
	opponentText = 'lv.{:2d}'.format(opponentPokemon.level)
	textSurf, textRect = make_text(opponentText, BLACK, WHITE, 50, 70, size=18)
	displaySurface.blit(textSurf, textRect)

def draw_player_pokemon_hp(displaySurface, playerPokemon):

	hpPct, color = playerPokemon.hp_bar()

	
	pygame.draw.rect(displaySurface, BLACK, (350, 470, 200, 30), 4)
	pygame.draw.rect(displaySurface, WHITE, (352, 472, 196, 26))
	if playerPokemon.hp != 0:
		pygame.draw.rect(displaySurface, color, (352, 472, int(196*hpPct), 26))
	hpText = 'HP:{:3}/{:}'.format(playerPokemon.hp, playerPokemon.maxHp)
	textSurf, textRect = make_text(hpText, BLACK, WHITE, 350, 505, size=18)
	displaySurface.blit(textSurf, textRect)

	playerText = playerPokemon.status.displayText.center(5)
	textSurf, textRect = make_text(playerText, BLACK, playerPokemon.status.displayColor, 475, 425)
	displaySurface.blit(textSurf, textRect)


def draw_opponent_pokemon_hp(displaySurface, opponentPokemon):

	hpPct, color = opponentPokemon.hp_bar()


	pygame.draw.rect(displaySurface, BLACK, (50, 95, 200, 30), 4)
	pygame.draw.rect(displaySurface, WHITE, (52, 97, 196, 26))
	if opponentPokemon.hp != 0:
		pygame.draw.rect(displaySurface, color, (52, 97, int(196*hpPct), 26))

	opponentText = opponentPokemon.status.displayText.center(5)
	textSurf, textRect = make_text(opponentText, BLACK, opponentPokemon.status.displayColor, 175, 50)
	displaySurface.blit(textSurf, textRect)


def draw_menu(displaySurface, playerPokemon):
	pygame.draw.rect(displaySurface, WHITE, (350, 575, 200, 90))

	message = 'What will %s do?' % playerPokemon.name
	words = message.split(' ')
	pygame.draw.rect(displaySurface, WHITE, (40, 575, 297, 90))
	surf, rect = make_text(' '.join(words[:2]), BLACK, WHITE, 45, 575, size=20)
	displaySurface.blit(surf, rect)
	surf, rect = make_text(' '.join(words[2:]), BLACK, WHITE, 45, 625, size=20)
	displaySurface.blit(surf, rect)

	fightSurf, fightRect = make_text('{:8s}'.format('Fight'), BLACK, WHITE, 350, 575, size=24)
	displaySurface.blit(fightSurf, fightRect)

	pokeSurf, pokeRect = make_text('{:8s}'.format('Pokémon'), BLACK, WHITE, 450, 575, size=24)
	displaySurface.blit(pokeSurf, pokeRect)

	bagSurf, bagRect = make_text('{:8s}'.format('Bag'), BLACK, WHITE, 350, 625, size=24)
	displaySurface.blit(bagSurf, bagRect)

	runSurf, runRect = make_text('{:8s}'.format('Run'), BLACK, WHITE, 450, 625, size=24)
	displaySurface.blit(runSurf, runRect)

	options = [fightRect, bagRect, pokeRect, runRect]

	return options

def draw_attack_stats(displaySurface, attack):
	pygame.draw.rect(displaySurface, WHITE, (350, 575, 200, 90))

	surf, rect = make_text(attack.type, BLACK, WHITE, 350, 575, size=20)
	displaySurface.blit(surf, rect)

	ppText = 'PP {:2}/{:2}'.format(attack.pp, attack.maxPP)
	surf, rect = make_text(ppText, BLACK, WHITE, 350, 625, size=20)
	displaySurface.blit(surf, rect)

	pygame.display.update()

def draw_messages(displaySurface, messages):
	pygame.draw.rect(displaySurface, WHITE, (40, 575, 297, 90))
	pygame.draw.rect(displaySurface, WHITE, (350, 575, 200, 90))

	for message in messages:
		words = message.split(' ')
		pygame.draw.rect(displaySurface, WHITE, (40, 575, 297, 90))
		surf, rect = make_text(' '.join(words[:2]), BLACK, WHITE, 45, 575, size=20)
		displaySurface.blit(surf, rect)
		surf, rect = make_text(' '.join(words[2:]), BLACK, WHITE, 45, 625, size=20)
		displaySurface.blit(surf, rect)
		pygame.display.update()
		wait_for_click()
		
	# pygame.draw.rect(displaySurface, WHITE, (50, 575, 250, 90))
	


def take_damage(displaySurface, pokemon, damage, isOpponent=False):
	finalHP = pokemon.hp - damage
	if finalHP < 0:
		finalHP = 0

	while pokemon.hp > finalHP:
		
		pokemon.take_damage(1)
		if isOpponent:
			draw_opponent_pokemon_hp(displaySurface, pokemon)
		else:
			draw_player_pokemon_hp(displaySurface, pokemon)
		pygame.display.update()
		# FPSCLOCK.tick(FPS)


def get_opponent_turn(opponentPokemon):
	if opponentPokemon.keepUsingAttack:
		attackNumber = opponentPokemon.continueAttackNumber
	else:
		attackNumber = choice(list(range(len(opponentPokemon.attacks))))
	
	return attackNumber

def fight(displaySurface, playerPokemon, opponentPokemon):
	pygame.draw.rect(displaySurface, WHITE, (40, 575, 280, 90))
	pygame.draw.rect(displaySurface, WHITE, (350, 575, 200, 90))


	attacks = playerPokemon.attacks

	while len(attacks) < 4:
		attacks.append(NoAttack())


	attackCoords = [(40, 575), (194, 575), (40, 625), (194, 625)]
	rects = []

	for i in range(4):
		left, top = attackCoords[i]
		surf, atkRect = make_text('{:12}'.format(attacks[i].name), BLACK, WHITE, left, top, size=20)
		rects.append(atkRect)
		displaySurface.blit(surf, atkRect)


	pygame.display.update()
	
	selected = playerPokemon.keepUsingAttack
	if selected:
		attackNumber = playerPokemon.continueAttackNumber
	
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
						draw_attack_stats(displaySurface, attacks[i])
						break
					else:
						pygame.draw.rect(displaySurface, WHITE, (350, 575, 200, 90))
						pygame.display.update()

			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				for i in range(4):
					if rects[i].collidepoint(mousex, mousey):
						attackNumber = i
						selected, messages = playerPokemon.attacks[i].select()
						
		if messages:
			draw_messages(displaySurface, messages)
			pygame.draw.rect(displaySurface, WHITE, (40, 575, 250, 90))
			for i in range(4):
				left, top = attackCoords[i]
				surf, atkRect = make_text('{:10}'.format(attacks[i].name), BLACK, WHITE, left, top, size=20)
				rects.append(atkRect)
				displaySurface.blit(surf, atkRect)
			pygame.display.update()

	return attackNumber

def check_recoil(displaySurface, pokemon, damage, attackNumber):
	recoilDamage = pokemon.attacks[attackNumber].get_recoil(damage)
	if recoilDamage:
		recoilMessage = ['%s is hit with recoil!' % pokemon.name]
		draw_messages(displaySurface, recoilMessage)
		take_damage(displaySurface, pokemon, recoilDamage)

def get_faster_pokemon(playerPokemon, opponentPokemon):
	fasterPokemon = ''
	if playerPokemon.battleSpeed > opponentPokemon.battleSpeed:
		fasterPokemon = 'player'
	else:
		fasterPokemon = 'opponent'
	return fasterPokemon

def get_turn_order(playerPokemon, action, playerTurn, opponentPokemon, opponentAttack):
	firstMove = ''
	if action == 'fight':
		playerAttack = playerTurn
		if playerPokemon.attacks[playerAttack].priority == opponentPokemon.attacks[opponentAttack].priority:
			firstMove = get_faster_pokemon(playerPokemon, opponentPokemon)
		elif playerPokemon.attacks[playerAttack].priority > opponentPokemon.attacks[opponentAttack].priority:
			firstMove = 'player'
		else:
			firstMove = 'opponent'

	else:
		firstMove = 'player'

	return firstMove


def do_opponent_fight(displaySurface, playerPokemon, opponentPokemon, attackNumber):
	damage, messages = opponentPokemon.attacks[attackNumber].use(opponentPokemon, playerPokemon)
	draw_messages(displaySurface, messages)
	draw_player_pokemon_hp(displaySurface, playerPokemon)
	take_damage(displaySurface, playerPokemon, damage)
	check_recoil(displaySurface, opponentPokemon, damage, attackNumber)

def do_player_fight(displaySurface, playerPokemon, opponentPokemon, attackNumber):
	damage, messages = playerPokemon.attacks[attackNumber].use(playerPokemon, opponentPokemon)
	draw_messages(displaySurface, messages)
	draw_opponent_pokemon_hp(displaySurface, opponentPokemon)
	take_damage(displaySurface, opponentPokemon, damage, isOpponent=True)
	check_recoil(displaySurface, playerPokemon, damage, attackNumber)

def status_handle(displaySurface, pokemon, attack, isTurnEnd, isOpponent=False):
	specialHandling = {}
	turnSkip, messages, damage = pokemon.handle_status(attack, isTurnEnd)
	if messages:
		draw_messages(displaySurface, messages)
	if damage > 0:
		take_damage(displaySurface, pokemon, damage, isOpponent)
	for message in messages:
		if 'Seed' in message:
			seedHeal = int(pokemon.maxHp / 8)
			specialHandling['seed'] = seedHeal
		if 'unleashed energy' in messages:
			specialHandling['bide'] = damage * -1

	return turnSkip, specialHandling

def handle_turn(displaySurface, playerPokemon, playerParty, opponentPokemon, action, playerTurn, opponentTurn):
	opponentAttack = opponentTurn

	firstMove = get_turn_order(playerPokemon, action, playerTurn, opponentPokemon, opponentAttack)
	if action == 'fight':
		playerAttack = playerTurn
		

		if firstMove == 'player':
			isTurnEnd = False
			skip, specialHandling = status_handle(displaySurface, playerPokemon, playerAttack, isTurnEnd)
			if skip:
				pass
			elif specialHandling.get('bide'):
				take_damage(displaySurface, opponentPokemon, specialHandling['bide'], isOpponent=True)

			else:
				do_player_fight(displaySurface, playerPokemon, opponentPokemon, playerAttack)

			skip, specialHandling = status_handle(displaySurface, opponentPokemon, opponentAttack, isTurnEnd, isOpponent=True)
			if skip:
				pass
			elif specialHandling.get('bide'):
				take_damage(displaySurface, playerPokemon, specialHandling['bide'])
				
			else:
				do_opponent_fight(displaySurface, playerPokemon, opponentPokemon, opponentAttack)
		else:
			isTurnEnd = False
			skip, specialHandling = status_handle(displaySurface, opponentPokemon, opponentAttack, isTurnEnd, isOpponent=True)
			if skip:
				pass
			elif specialHandling.get('bide'):
				take_damage(displaySurface, playerPokemon, specialHandling['bide'])
				
			else:
				do_opponent_fight(displaySurface, playerPokemon, opponentPokemon, opponentAttack)

			skip, specialHandling = status_handle(displaySurface, playerPokemon, playerAttack, isTurnEnd)
			if skip:
				pass
			elif specialHandling.get('bide'):
				take_damage(displaySurface, opponentPokemon, specialHandling['bide'], isOpponent=True)
				
			else:
				do_player_fight(displaySurface, playerPokemon, opponentPokemon, playerAttack)
			
	elif action == 'bag':
		playerAttack = None

	elif action == 'changePoke':
		playerAttack = None
		pokeNumber = playerTurn

		playerParty = switch_battler(displaySurface, playerPokemon, playerParty, pokeNumber)
		playerPokemon = playerParty[0]
		messages = ['Go, %s!' % playerPokemon.name]
		draw_messages(displaySurface, messages)
		redraw_screen(displaySurface, playerPokemon, opponentPokemon)
		playerPokemon.calculate_battle_stats()
		pygame.display.update()

		isTurnEnd = False
		skip, specialHandling = status_handle(displaySurface, opponentPokemon, opponentAttack, isTurnEnd, isOpponent=True)
		if skip:
			pass
		elif specialHandling.get('bide'):
			take_damage(displaySurface, playerPokemon, specialHandling['bide'])
			
		else:
			do_opponent_fight(displaySurface, playerPokemon, opponentPokemon, opponentAttack)


	elif action == 'run':
		playerAttack = None

	isTurnEnd = True
	skip, specialHandling = status_handle(displaySurface, playerPokemon, playerAttack, isTurnEnd)
	if specialHandling.get('seed'):
		opponentPokemon.heal(specialHandling['seed'])
		draw_opponent_pokemon_hp(displaySurface, opponentPokemon)
	
	skip, specialHandling = status_handle(displaySurface, opponentPokemon, opponentAttack, isTurnEnd, isOpponent=True)
	if specialHandling.get('seed'):
		playerPokemon.heal(specialHandling['seed'])
		draw_player_pokemon_hp(displaySurface, playerPokemon)
	
	return playerPokemon, opponentPokemon, playerParty

def switch_battler(displaySurface, playerPokemon, playerParty, pokeNumber):
	messages = []
	messages.append('%s, come back!' % playerPokemon.name)
	draw_messages(displaySurface, messages)
	pokemonSwitchIn = playerParty[pokeNumber]
	playerParty[pokeNumber] = playerParty[0]
	playerParty[0] = pokemonSwitchIn

	return playerParty

def change_pokemon(displaySurface, playerPokemon, playerParty):
	displaySurface.fill(WHITE)
	pygame.draw.rect(displaySurface, BLACK, (25, 25, 550, 650), 5)
	pygame.display.update()
	


	pokeCoords = [(40, 250), (300, 50), (300, 160), (300, 270), (300, 380), (300, 490)]
	rects = []
	# draw boxes
	for i in range(6):
		left, top = pokeCoords[i]
		rect = pygame.draw.rect(displaySurface, BLACK, (left, top, 250, 105), 4)
		rects.append(rect)
		
	for i in range(len(playerParty)):
		left, top = pokeCoords[i]
		# pokemon image
		image = load_pokemon_image(playerParty[i]).convert()
		image = pygame.transform.scale(image, (100, 100))
		displaySurface.blit(image, (left+4, top+3))
		# pokemon name, status
		surf, rect = make_text('{:12}'.format(playerParty[i].name), BLACK, WHITE, left+115, top+6, size=18)
		displaySurface.blit(surf, rect)
		surf, rect = make_text('lv. %i' % playerParty[i].level, BLACK, WHITE, left+115, top+24, size=16)
		displaySurface.blit(surf, rect)
		# pokemon hp
		hpPct, color = playerParty[i].hp_bar()
		pygame.draw.rect(displaySurface, BLACK, (left+115, top+45, 130, 20), 2)
		pygame.draw.rect(displaySurface, color, (left+117, top+47, 127*hpPct, 17))

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
			
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
				for i in range(len(playerParty)):
					if rects[i].collidepoint(mousex, mousey):
						pokeNumber = i
						selected, messages = playerParty[i].select()
						
		if messages:
			draw_messages(displaySurface, messages)
			pygame.draw.rect(displaySurface, WHITE, (40, 575, 250, 90))
			for i in range(4):
				left, top = attackCoords[i]
				surf, atkRect = make_text('{:10}'.format(attacks[i].name), BLACK, WHITE, left, top, size=20)
				rects.append(atkRect)
				displaySurface.blit(surf, atkRect)
			pygame.display.update()

	return pokeNumber

def calculate_exp(playerPokemon, opponentPokemon):
	# wild battle
	# a = 1.5 if opponent is trainer pokemon
	a = 1
	b = opponentPokemon.pocketMonster.baseExpYield
	# lucky egg
	# e = 1.5 if hold item is lucky egg
	# TODO: items
	e = 1
	# affection
	# f = affection modifier
	f = 1
	L = opponentPokemon.level
	p = 1
	# s = number of pokemon participated in battle
	s = 1
	t = 1 # traded or original trainer
	v = 1

	exp = int(a * t * b * e * L * p * f * v / 7 / s)
	return exp

def post_battle(displaySurface, playerPokemon, opponentPokemon):
	messages = []
	if playerPokemon.hp == 0:
		messages.append('%s fainted!' % playerPokemon.name)
		messages.append('Party not yet implemented.')
		messages.append('Game over!')
	else:
		messages.append('Foe %s fainted!' % opponentPokemon.name)
		exp = calculate_exp(playerPokemon, opponentPokemon)
		m = playerPokemon.gain_exp(exp)
		messages.extend(m)
	draw_messages(displaySurface, messages)


def main():
	pygame.init()

	
	global FPS, FPSCLOCK
	FPS = 30
	FPSCLOCK = pygame.time.Clock()

	displaySurface = pygame.display.set_mode((600,700))
	displaySurface.fill(WHITE)
	pygame.draw.rect(displaySurface, BLACK, (25, 25, 550, 650), 5)
	pygame.draw.rect(displaySurface, BLACK, (25, 555, 550, 120), 5)
	pygame.draw.rect(displaySurface, BLACK, (340, 555, 235, 120), 5)
	pygame.display.set_caption('Pokémon Battle')


	playerParty = []
	playerParty.append(Pokemon(Bulbasaur(), level=25))
	playerParty.append(Pokemon(Pikachu(), level=25))
	playerParty.append(Pokemon(Charmander(), level=25))
	playerParty.append(Pokemon(Ekans(), level=25))
	playerParty.append(Pokemon(Sandshrew(), level=25))
	# playerParty = load()

	playerPokemon = playerParty[0]

	opponentPokemon = Pokemon(Pidgey())
	opponentPokemon.set_level(25)
	

	mousex = mousey = 0

	draw_pokemon(displaySurface, playerPokemon, opponentPokemon)
	draw_player_pokemon_hp(displaySurface, playerPokemon)
	draw_opponent_pokemon_hp(displaySurface, opponentPokemon)
	playerPokemon.calculate_battle_stats()
	opponentPokemon.calculate_battle_stats()

	while playerPokemon.hp > 0 and opponentPokemon.hp > 0:
		draw_player_pokemon_hp(displaySurface, playerPokemon)
		draw_opponent_pokemon_hp(displaySurface, opponentPokemon)

		action = ''

		while not action:
			options = draw_menu(displaySurface, playerPokemon)

			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()

				elif event.type == MOUSEBUTTONUP:
					mousex, mousey = event.pos
					if options[0].collidepoint(mousex, mousey):
						attackNumber = fight(displaySurface, playerPokemon, opponentPokemon)
						if attackNumber != None:
							action = 'fight'
							playerTurn = attackNumber
					elif options[1].collidepoint(mousex, mousey):
						action = 'bag'
						playerTurn = None
					elif options[2].collidepoint(mousex, mousey):
						pokeNumber = change_pokemon(displaySurface, playerPokemon, playerParty)
						redraw_screen(displaySurface, playerPokemon, opponentPokemon)
						if pokeNumber != None:
							action = 'changePoke'
							playerTurn = pokeNumber
					elif options[3].collidepoint(mousex, mousey):
						action = 'run'
						playerTurn = None

			pygame.display.update()
			FPSCLOCK.tick(FPS)



		opponentTurn = get_opponent_turn(opponentPokemon)

		playerPokemon, opponentPokemon, playerParty = handle_turn(displaySurface, playerPokemon, playerParty, opponentPokemon, action, playerTurn, opponentTurn)
		pygame.display.update()
		FPSCLOCK.tick(FPS)

	post_battle(displaySurface, playerPokemon, opponentPokemon)
	draw_pokemon(displaySurface, playerPokemon, opponentPokemon)
	pygame.display.update()
	wait_for_click()
	playerPokemon.reset_battle_stats()
	opponentPokemon.reset_battle_stats()

	save(playerParty)


if __name__ == '__main__':
	main()