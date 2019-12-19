from pokemonTypes import fire
from attack import Attack
from statuses import Burn, Recharge, Bound
from attackKeywords import *

class BlastBurn(Attack):
	def __init__(self):
		self.name = 'Blast Burn'
		self.type = fire
		self.attackType = [special, selfConditionModifier]
		self.description = 'Powerful, but leaves the user immobile the next turn.'
		self.condition = Recharge()
		power = 150
		accuracy = 90
		pp = 5
		super().__init__(pp, power, accuracy)

class BlazeKick(Attack):
	def __init__(self):
		self.name = 'Blaze Kick'
		self.type = fire
		self.attackType = [physical, optConditionModifier]
		self.condition = Burn()
		self.effectAccuracy = 10
		self.description = 'A kick with a high critical- hit ratio. May cause a burn.'

		power = 85
		accuracy = 90
		pp = 10
		super().__init__(pp, power, accuracy)
		self.critStage = 1

class Ember(Attack):
	def __init__(self):
		self.name = 'Ember'
		self.type = fire
		self.attackType = [special, optConditionModifier]
		self.condition = Burn()
		self.effectAccuracy = 10
		self.description = 'A weak fire attack that may inflict a burn.'

		power = 40
		accuracy = 100
		pp = 25
		super().__init__(pp, power, accuracy)

class Eruption(Attack):
	def __init__(self):
		self.name = 'Eruption'
		self.type = fire
		self.attackType = [special]
		self.condition = Burn()
		self.effectAccuracy = 10
		self.description = 'The higher the user\'s HP, the more damage caused.'

		power = 150
		accuracy = 100
		pp = 5
		super().__init__(pp, power, accuracy)

	def calculate_damage(self, userPokemon, targetPokemon):
		messages = []

		power = int( (userPokemon.hp * self.power) / userPokemon.maxHp )

		userAttack = userPokemon.battleSpAttack
		targetDefense = targetPokemon.battleSpDefense

		if self.type in userPokemon.type:
			stab = 1.5
		else:
			stab = 1

		critStage = self.critStage + userPokemon.critStage
		
		if critStage == 0 and randint(0,15) == 15:
			crit = 2
		elif critStage == 1 and randint(0,7) == 7:
			crit = 2
		elif critStage == 2 and randint(0,3) == 3:
			crit = 2
		elif critStage == 3 and randint(0,2) == 2:
			crit = 2
		elif critStage >=4 and randint(0,1) == 1:
			crit = 2
		else:
			crit = 1

		if crit == 2:
			messages.append('Critical hit!')

		typeModifier = get_type_modifier(self.type, targetPokemon.type)
		if typeModifier == 2 or typeModifier == 4:
			messages.append('Super effective!')
		elif typeModifier == 0.5 or typeModifier == 0.25:
			messages.append('Not very effective...')
		elif typeModifier == 0:
			messages.append('Does not affect %s.' % targetPokemon.name)
			


		modifier = typeModifier * stab * crit * (randint(85,100)/100)

		damage = ((((2*userPokemon.level/5)+2) * power * userAttack/targetDefense)/50 + 2) * modifier
		damage *= self.screen_damage_modifier(targetPokemon)
		damage = int(damage)
		
		return damage, messages

class FireBlast(Attack):
	def __init__(self):
		self.name = 'Fire Blast'
		self.type = fire
		self.attackType = [special, optConditionModifier]
		self.condition = Burn()
		self.effectAccuracy = 10
		self.description = 'A fiery blast that scorches all. May cause a burn.'

		power = 120
		accuracy = 85
		pp = 5
		super().__init__(pp, power, accuracy)

class FirePunch(Attack):
	def __init__(self):
		self.name = 'Fire Punch'
		self.type = fire
		self.attackType = [physical, optConditionModifier]
		self.condition = Burn()
		self.effectAccuracy = 10
		self.description = 'A fiery punch that may burn the foe.'

		power = 75
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class FireSpin(Attack):
	def __init__(self):
		self.name = 'Fire Spin'
		self.type = fire
		self.attackType = [special, optConditionModifier]
		self.condition = Bound(self.name)
		self.effectAccuracy = 0
		self.description = 'Traps the foe in a ring of fire for 2 to 5 turns.'

		power = 15
		accuracy = 70
		pp = 15
		super().__init__(pp, power, accuracy)

class FlameWheel(Attack):
	def __init__(self):
		self.name = 'Flame Wheel'
		self.type = fire
		self.attackType = [physical,optConditionModifier]
		self.condition = Burn()
		self.effectAccuracy = 10
		self.description = 'A fiery charge attack that may inflict a burn.'

		power = 60
		accuracy = 100
		pp = 25
		super().__init__(pp, power, accuracy)

class Flamethrower(Attack):
	def __init__(self):
		self.name = 'Flamethrower'
		self.type = fire
		self.attackType = [special,optConditionModifier]
		self.condition = Burn()
		self.effectAccuracy = 10
		self.description = 'A powerful fire attack that may inflict a burn.'

		power = 95
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class HeatWave(Attack):
	def __init__(self):
		self.name = 'Heat Wave'
		self.type = fire
		self.attackType = [special,optConditionModifier]
		self.condition = Burn()
		self.effectAccuracy = 10
		self.description = 'Exhales a hot breath on the foe. May inflict a burn.'

		power = 100
		accuracy = 90
		pp = 10
		super().__init__(pp, power, accuracy)

class Overheat(Attack):
	def __init__(self):
		self.name = 'Overheat'
		self.type = fire
		self.attackType = [special,selfStatModifier]
		self.statsModified = [spAttack]
		self.stageModifier = -2
		self.effectAccuracy = 10
		self.description = 'Allows a full-power attack, but sharply lowers special attack.'

		power = 140
		accuracy = 90
		pp = 5
		super().__init__(pp, power, accuracy)

class SacredFire(Attack):
	def __init__(self):
		self.name = 'Sacred Fire'
		self.type = fire
		self.attackType = [special,optConditionModifier]
		self.condition = Burn()
		self.effectAccuracy = 50
		self.description = 'A mystical fire attack that may inflict a burn.'

		power = 100
		accuracy = 95
		pp = 5
		super().__init__(pp, power, accuracy)

class SunnyDay(Attack):
	def __init__(self):
		self.name = 'Sunny Day'
		self.type = fire
		self.attackType = [weather]
		# self.weather = Sunny()
		self.description = 'Boosts the power of fire type moves for 5 turns.'

		power = 0
		accuracy = 0
		pp = 5
		super().__init__(pp, power, accuracy)

class WillOWisp(Attack):
	def __init__(self):
		self.name = 'Will-o-wisp'
		self.type = fire
		self.attackType = [optConditionModifier]
		self.condition = Burn()
		self.effectAccuracy = 100
		self.description = 'Inflicts a burn on the foe with intense fire.'

		power = 0
		accuracy = 75
		pp = 15
		super().__init__(pp, power, accuracy)
