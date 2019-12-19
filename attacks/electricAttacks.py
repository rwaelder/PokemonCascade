from pokemonTypes import electric
from attack import Attack
from statuses import *
from random import randint
from attackKeywords import *

class Charge(Attack):
	def __init__(self):
		self.name = 'Charge'
		self.type = electric
		self.attackType = [selfStatModifier]
		self.description = 'Charges power to boost the electric move used next.'
		
		power = 0
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []

		messages.append('%s used %s!' % userPokemon.name, self.name)
		self.pp -= 1

		if userPokemon.charge == 1:
			mixer.play_attack_sound(self.name)
			userPokemon.charge = 2
			messages.append('%s is building charge!' % userPokemon.name)
		else:
			messages.append('%s is already at full charge!' % userPokemon.name)

		return damage, messages

class ShockWave(Attack):
	def __init__(self):
		self.name = 'Shock Wave'
		self.type = electric
		self.attackType = [special]
		self.description = 'A fast and unavoidable electric attack.'

		power = 60
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)

class Spark(Attack):
	def __init__(self):
		self.name = 'Spark'
		self.type = electric
		self.attackType = [physical, optConditionModifier]
		self.condition = Paralysis()
		self.effectAccuracy = 30
		self.description = 'An electrified tackle that may paralyze the foe.'

		power = 65
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Thunder(Attack):
	def __init__(self):
		self.name = 'Thunder'
		self.type = electric
		self.attackType = [special, optConditionModifier]
		self.condition = Paralysis()
		self.effectAccuracy = 30
		self.description = 'A lightning attack that may cause paralysis.'

		power = 120
		accuracy = 70
		pp = 10
		super().__init__(pp, power, accuracy)

class ThunderWave(Attack):
	def __init__(self):
		self.name = 'Thunder Wave'
		self.type = electric
		self.attackType = [optConditionModifier]
		self.condition = Paralysis()
		self.effectAccuracy = 0
		self.description = 'A weak jolt of electricity that paralyzes the foe.'

		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Thunderbolt(Attack):
	def __init__(self):
		self.name = 'Thunderbolt'
		self.type = electric
		self.attackType = [special, optConditionModifier]
		self.condition = Paralysis()
		self.effectAccuracy = 10
		self.description = 'A strong electrical attack that may paralyze the foe.'

		power = 95
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class Thunderpunch(Attack):
	def __init__(self):
		self.name = 'Thunderpunch'
		self.type = electric
		self.attackType = [physical, optConditionModifier]
		self.condition = Paralysis()
		self.effectAccuracy = 10
		self.description = 'An electrified punch that may paralyze the foe.'

		power = 75
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class Thundershock(Attack):
	def __init__(self):
		self.name = 'Thundershock'
		self.type = electric
		self.attackType = [special, optConditionModifier]
		self.condition = Paralysis()
		self.effectAccuracy = 10
		self.description = 'An electrical attack that may paralyze the foe.'

		power = 40
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)

class VoltTackle(Attack):
	def __init__(self):
		self.name = 'Volt Tackle'
		self.type = electric
		self.attackType = [physical]
		self.description = 'A life-risking tackle that slightly hurts the user.'

		power = 120
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)
		self.recoilModifier = 0.33

class ZapCannon(Attack):
	def __init__(self):
		self.name = 'Zap Cannon'
		self.type = electric
		self.attackType = [special, optConditionModifier]
		self.condition = Paralysis()
		self.effectAccuracy = 0
		self.description = 'Powerful and sure to cause paralysis, but inaccurate.'

		power = 100
		accuracy = 50
		pp = 5
		super().__init__(pp, power, accuracy)