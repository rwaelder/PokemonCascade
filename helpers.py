import pygame, sys
from pygame.locals import *

# pygame helpers

# wait_for_click() 
# -> pauses game until mouse is clicked

# make text(text, color, bgcolor, left, top, **kwargs)
# 	returns pygame text surface and rectangle
# 	text = text to be displayed
# 	color = color of text
# 	bgcolor = background color of text surface
# 	left, top = left and top coordinates of text rect
# 	kwargs:
# 		size = font size
# 		style = one of: 'basic', 'bold', 'italic', 'bolditalic'

def quit():
	pygame.quit()
	sys.exit()

def wait_for_click():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				quit()
			elif event.type == MOUSEBUTTONUP:
				return
			else:
				continue

def wait_for_space():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				quit()
			elif event.type == KEYUP and event.key == K_SPACE:
				return
			else:
				continue

def wait_for_sound(mixer):
	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				quit()
			elif event.type == mixer.SOUND_END:
				return
			elif not mixer.get_busy():
				return
			else:
				continue

def make_text(text, color, bgcolor, left, top, size=20, style='basic'):
	# fontName = 'DejaVuSansMono'
	# fontName = 'ArcadeClassic'
	fontName = 'SuperLegendBoy'
	# fontName = 'PressStart'
	if style == 'basic':
		fontName += '.ttf'
	elif style == 'bold':
		fontName += '-Bold.ttf'
	elif style == 'italic':
		fontName += '-Oblique.ttf'
	elif style == 'bolditalic' or style == 'italicbold':
		fontName += '-BoldOblique.ttf'

	font = pygame.font.Font(fontName, size)
	textSurf = font.render(text, True, color, bgcolor)
	textRect = textSurf.get_rect()
	textRect.topleft = (left, top)
	return textSurf, textRect

def load_pokemon_image(pokemon, style='default'):
	pokemonName = pokemon.name.replace(' ', '_')
	if style == 'default':
		imageFile = 'pokemonImages/Default/' + pokemon.image
	elif style == 'redblue':
		imageFile = 'pokemonImages/RedBlue/%s%s_RB.png' % (str(pokemon.number).zfill(3), pokemonName)
	elif style == 'redgreen':
		imageFile = 'pokemonImages/RedGreen/%s%s_RG.png' % (str(pokemon.number).zfill(3), pokemonName)
	elif style == 'official':
		imageFile = 'pokemonImages/Official/%s%s.png' % (str(pokemon.number).zfill(3), pokemonName)

	return pygame.image.load(imageFile).convert_alpha()

def load_pokemon_menu_sprite(pokemon, scale):
	imageFile = 'pokemonImages/Menu Sprites/Ani%sMS.png' % str(pokemon.number).zfill(3)

	image = pygame.image.load(imageFile).convert_alpha()
	width, height = image.get_size()
	image = pygame.transform.scale(image, (width*scale, height*scale))
	
	return image

def load_pokemon_sprite(pokemon, frontBack='front'):

	if frontBack == 'front':
		imageFile = 'pokemonImages/Sprites III/Spr_3f_%s.png' % str(pokemon.number).zfill(3)
	elif frontBack == 'back':
		imageFile = 'pokemonImages/Sprites III/Spr_b_3f_%s.png' % str(pokemon.number).zfill(3)


	if pokemon.class_type() == 'pokemon':
		try:
			image = pygame.image.load(imageFile).convert_alpha()

		except pygame.error:
			pass
			# if pokemon.gender == 'm':
			# 	imageFile = imageFile.replace('.png', '_m.png')
			# elif pokemon.gender == 'f':
			# 	imageFile = imageFile.replace('.png', '_f.png')

		if pokemon.shiny:
			imageFile = imageFile.replace('.png', '_s.png')

		image = pygame.image.load(imageFile).convert_alpha()

	else:
		try:
			image = pygame.image.load(imageFile).convert_alpha()

		except pygame.error:
			imageFile = imageFile.replace('.png', '_m.png')
			# print(imageFile)
			image = pygame.image.load(imageFile).convert_alpha()

	return image

def load_trainer_image(trainer, back=False):

	imageFile = 'trainerImages/Gen V/' + trainer.image

	if back:
		imageFile = imageFile.replace('Spr_', '')
		imageFile = imageFile.replace('.png', '_Back.png')

	image = pygame.image.load(imageFile)
	transColor = image.get_at((0,0))
	image.set_colorkey(transColor)
	return image
	return pygame.image.load(imageFile).convert_alpha()

def load_image(path, scale=1):
	imageFile = path
	if scale == 1:
		return pygame.image.load(imageFile).convert_alpha()

	else:
		image = pygame.image.load(imageFile).convert_alpha()
		width, height = image.get_size()
		image = pygame.transform.scale(image, (width*scale, height*scale))
		return image





