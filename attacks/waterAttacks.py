from pokemonTypes import water, fire
from attack import Attack
from statuses import ConfusionStatus, SemiInvulnerable, Recharge, Bound, TypeResistance
from attackKeywords import *

class Bubble(Attack):
	def __init__(self):
		self.name = 'Bubble'
		self.type = water
		self.attackType = [special, optStatModifier]
		self.statsModified = [speed]
		self.stageModifier = -1
		self.effectAccuracy = 10
		self.description = 'An attack using bubbles. May lower foe\'s speed.'

		power = 20
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)

class Bubblebeam(Attack):
	def __init__(self):
		self.name = 'Bubblebeam'
		self.type = water
		self.attackType = [special, optStatModifier]
		self.statsModified = [speed]
		self.stageModifier = -1
		self.effectAccuracy = 10
		self.description = 'Forcefully sprays bubbles that may lower speed.'

		power = 65
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Clamp(Attack):
	def __init__(self):
		self.name = 'Clamp'
		self.type = water
		self.attackType = [physical, optConditionModifier]
		self.condition = Bound(self.name)
		self.effectAccuracy = 0
		self.description = 'Traps and squeezes the foe 2 to 5 turns.'

		power = 35
		accuracy = 75
		pp = 10
		super().__init__(pp, power, accuracy)

class Crabhammer(Attack):
	def __init__(self):
		self.name = 'Crabhammer'
		self.type = water
		self.attackType = [physical]
		self.description = 'Hammers with a pincer. Has a high critical-hit ratio.'

		power = 90
		accuracy = 85
		pp = 10
		super().__init__(pp, power, accuracy)
		self.critStage = 1

class Dive(Attack):
	def __init__(self):
		self.name = 'Dive'
		self.type = water
		self.attackType = [physical, selfConditionModifier]
		self.condition = SemiInvulnerable(self.name)
		self.effectAccuracy = 0
		self.description = 'Dives underwater the first turn and strikes next turn.'

		power = 60
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

class HydroCannon(Attack):
	def __init__(self):
		self.name = 'Hydro Cannon'
		self.type = water
		self.attackType = [physical, selfConditionModifier]
		self.condition = Recharge()
		self.effectAccuracy = 0
		self.description = 'Powerful, but leaves user immobile the next turn.'

		power = 150
		accuracy = 90
		pp = 5
		super().__init__(pp, power, accuracy)

class HydroPump(Attack):
	def __init__(self):
		self.name = 'Hydro Pump'
		self.type = water
		self.attackType = [special]
		self.description = 'Blasts water at high power to strike the foe.'

		power = 120
		accuracy = 80
		pp = 5
		super().__init__(pp, power, accuracy)

class MuddyWater(Attack):
	def __init__(self):
		self.name = 'Muddy Water'
		self.type = water
		self.attackType = [special, optStatModifier]
		self.statsModified = [accuracy]
		self.stageModifier = -1
		self.effectAccuracy = 30
		self.description = 'Attacks with muddy water. May lower accuracy.'

		power = 95
		accuracy = 85
		pp = 10
		super().__init__(pp, power, accuracy)

class Octazooka(Attack):
	def __init__(self):
		self.name = 'Octazooka'
		self.type = water
		self.attackType = [special, optStatModifier]
		self.statsModified = [accuracy]
		self.stageModifier = -1
		self.effectAccuracy = 50
		self.description = 'Fires a lump of ink to damage and cut accuracy.'

		power = 65
		accuracy = 85
		pp = 10
		super().__init__(pp, power, accuracy)

class RainDance(Attack):
	def __init__(self):
		self.name = 'Rain Dance'
		self.type = water
		self.attackType = [weather]
		# self.weatherEffect = 'rain'
		self.description = 'Boosts power of water type moves for 5 turns.'

		power = 0
		accuracy = 0
		pp = 5
		super().__init__(pp, power, accuracy)

class WaterGun(Attack):
	def __init__(self):
		self.name = 'Water Gun'
		self.type = water
		self.attackType = [special]
		self.description = 'Squirts water to attack the foe.'

		power = 40
		accuracy = 100
		pp = 25
		super().__init__(pp, power, accuracy)

class WaterPulse(Attack):
	def __init__(self):
		self.name = 'Water Pulse'
		self.type = water
		self.attackType = [special, optConditionModifier]
		self.condition = ConfusionStatus()
		self.effectAccuracy = 20
		self.description = 'Attacks with ultrasonic waves. May confuse the foe.'

		power = 60
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class WaterSport(Attack):
	def __init__(self):
		self.name = 'Water Sport'
		self.type = water
		self.attackType = [selfConditionModifier]
		self.condition = TypeResistance(fire)
		self.effectAccuracy = 0
		self.description = 'The user becomes soaked to raise fire resistance.'

		power = 0
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class WaterSpout(Attack):
	def __init__(self):
		self.name = 'Water Spout'
		self.type = water
		self.attackType = [special]
		self.description = 'Inflicts more damage if the user\'s HP is high.'

		power = 150
		accuracy = 100
		pp = 5
		super().__init__(pp, power, accuracy)

	def calculate_damage(self, userPokemon, targetPokemon):
		messages = []

		power = int( (userPokemon.hp * self.power






			) / userPokemon.maxHp )

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
			


		modifier = typeModifier * stab * burnModifier * crit * (randint(85,100)/100)

		damage = ((((2*userPokemon.level/5)+2) * power * userAttack/targetDefense)/50 + 2) * modifier

		return damage, messages

class Waterfall(Attack):
	def __init__(self):
		self.name = 'Waterfall'
		self.type = water
		self.attackType = [physical]
		self.description = 'Charges the foe with speed to climb waterfalls.'

		power = 80
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class Whirlpool(Attack):
	def __init__(self):
		self.name = 'Whirlpool'
		self.type = water
		self.attackType = [special, optConditionModifier]
		self.condition = Bound(self.name)
		self.effectAccuracy = 0
		self.description = 'Traps and hurts the foe in a whirlpool for 2 to 5 turns.'

		power = 15
		accuracy = 70
		pp = 15
		super().__init__(pp, power, accuracy)

class Withdraw(Attack):
	def __init__(self):
		self.name = 'Withdraw'
		self.type = water
		self.attackType = [selfStatModifier]
		self.statsModified = [defense]
		self.stageModifier = 1
		self.effectAccuracy = 0
		self.description = 'Withdraws the body into its hard shell to raise defense.'

		power = 0
		accuracy = 0
		pp = 40
		super().__init__(pp, power, accuracy)
