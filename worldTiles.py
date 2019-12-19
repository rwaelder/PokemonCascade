import pygame

class Tile():
	def __init__(self, isWalkable, isRunnable, isBikeable, isSurfable):
		self.isWalkable = isWalkable
		self.isRunnable = isRunnable
		self.isBikeable = isBikeable
		self.isSurfable = isSurfable

		self.item = None
		self.decoration = None

		self.isEncounterTile = False
		self.encounterRate = 0
		self.encounters = []

	def draw(self):
		image = pygame.image.load(self.baseTile).convert_alpha()
		if self.decoration != None:
			decoration = pygame.image.load(self.decoration).convert_alpha()
			image.blit(decoration)

		return image
		



