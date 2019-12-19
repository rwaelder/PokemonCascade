from battle import WildBattle, TrainerBattle
from trainer import Trainer, MainPlayer
from pocketMonsters import Pokemon
from creatures1_25 import *
from creatures26_50 import *
from creatures51_75 import *
import pygame
from helpers import wait_for_click, load_image
from setupTestBattle import ChooseParty
from random import randint
from pokemonList import pokemonList
from mixer import Mixer

pygame.init()
displaySurface = pygame.display.set_mode((600,700))
pygame.display.set_caption('Pokémon')
displaySurface.fill(WHITE)
image = load_image('pokemon_logo.png')
image = pygame.transform.scale(image, (400,200))
displaySurface.blit(image, (100, 200))
pygame.display.update()
mixer = Mixer()

mixer.play_song('Opening 1')


# pygame.time.delay(12000)
wait_for_click()

# party = [Pokemon(Charmander(), level=25), Pokemon(Pikachu(), level=25)]
party = ChooseParty(displaySurface, mixer).party
player = MainPlayer(party=party)

optParty = []
for i in range(5):
	optParty.append(Pokemon(pokemonList[randint(1,150)], level=50))



opponent = Trainer(party=optParty, name='Youngster Joey')

TrainerBattle(displaySurface, mixer, player, opponent)