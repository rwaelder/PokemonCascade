from pokemonTypes import steel
from attack import Attack
from attackKeywords import *

class IronDefense(Attack):
	def __init__(self):
		self.name = 'Iron Defense'
		self.type = steel
		self.attackType = [selfStatModifier]
		self.statsModified = [defense]
		self.stageModifier = 2
		self.effectAccuracy = 0
		self.description = 'Hardens the body\'s surface to sharply raise defense.'

		power = 0
		accuracy = 100
		pp = 40
		super().__init__(pp, power, accuracy)

class IronTail(Attack):
	def __init__(self):
		self.name = 'Iron Tail'
		self.type = steel
		self.attackType = [physical, optStatModifier]
		self.statsModified = [defense]
		self.stageModifier = -1
		self.effectAccuracy = 30
		self.description = 'Attacks with a rock-hard tail. May lower defense.'

		power = 100
		accuracy = 75
		pp = 15
		super().__init__(pp, power, accuracy)

class MetalClaw(Attack):
	def __init__(self):
		self.name = 'Metal Claw'
		self.type = steel
		self.attackType = [physical, selfStatModifier]
		self.statsModified = [attack]
		self.stageModifier = 1
		self.effectAccuracy = 10
		self.description = 'A claw attack that may raise the user\'s attack.'

		power = 50
		accuracy = 95
		pp = 35
		super().__init__(pp, power, accuracy)

class MetalSound(Attack):
	def __init__(self):
		self.name = 'Metal Sound'
		self.type = steel
		self.attackType = [optStatModifier]
		self.statsModified = [defense]
		self.stageModifier = -2
		self.effectAccuracy = 0
		self.description = 'Emits a horrible screech that sharply lowers special defense.'

		power = 0
		accuracy = 85
		pp = 40
		super().__init__(pp, power, accuracy)

class MeteorMash(Attack):
	def __init__(self):
		self.name = 'Meteor Mash'
		self.type = steel
		self.attackType = [physical, selfStatModifier]
		self.statsModified = [attack]
		self.stageModifier = 1
		self.effectAccuracy = 20
		self.description = 'Fires a meteor-like punch. May raise attack.'

		power = 100
		accuracy = 85
		pp = 10
		super().__init__(pp, power, accuracy)

class SteelWing(Attack):
	def __init__(self):
		self.name = 'Steel Wing'
		self.type = steel
		self.attackType = [physical]
		self.description = 'Strikes the foe with hard wings spread wide.'

		power = 70
		accuracy = 90
		pp = 25
		super().__init__(pp, power, accuracy)