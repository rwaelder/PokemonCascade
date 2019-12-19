from pokemonTypes import ice
from attack import Attack, MultiAttack
from statuses import *
from random import randint
from attackKeywords import *

class AuroraBeam(Attack):
	def __init__(self):
		self.name = 'Aurora Beam'
		self.type = ice
		self.attackType = [special, optStatModifier]
		self.statsModified = [attack]
		self.stageModifier = -1
		self.effectAccuracy = 10
		self.description = 'Fires a rainbow-colored beam that may lower attack.'

		power = 65
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Blizzard(Attack):
	def __init__(self):
		self.name = 'Blizzard'
		self.type = ice
		self.attackType = [special, optConditionModifier]
		self.condition = Freeze()
		self.effectAccuracy = 10
		self.description = 'Hits the foe with an icy storm that may freeze it.'

		power = 120
		accuracy = 70
		pp = 5
		super().__init__(pp, power, accuracy)

class Hail(Attack):
	def __init__(self):
		self.name = 'Hail'
		self.type = ice
		self.attackType = [weather]
		# self.weather = Hailstorm()
		self.description = 'Summons a hailstorm that strikes every turn.'

		power = 0
		accuracy = 0
		pp = 10
		super().__init__(pp, power, accuracy)

class Haze(Attack):
	def __init__(self):
		self.name = 'Haze'
		self.type = ice
		self.attackType = [selfStatModifier, optStatModifier]
		self.statsModified = ['all']
		self.effectAccuracy = 0
		self.description = 'Maximizes attack while sacrificing HP.'

		power = 0
		accuracy = 0
		pp = 30
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		self.pp -= 1

		userPokemon.reset_battle_stats()
		targetPokemon.reset_battle_stats()

		messages.append('All stat changes eliminated.')

		return damage, messages

class IceBall(Attack):
	def __init__(self):
		self.name = 'Ice Ball'
		self.type = ice
		self.attackType = [physical]
		self.duration = 4
		self.turnNumber = 0
		self.description = 'A 5-turn attack that gains power on successive hits.'

		power = 30
		accuracy = 90
		pp = 20
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):			

		if not userPokemon.keepUsingAttack:
			self.turnNumber = 0
			userPokemon.keep_using_attack(self)
			self.pp -= 1

		damage = 0
		messages = []

		messages.append('%s used %s!' % (userPokemon.name, self.name))
		if randint(1,100) < (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
			self.power = 30 * (2**self.turnNumber)
			protected, m = self.check_protect(userPokemon, targetPokemon)
			messages.extend(m)
			if not protected:
				mixer.play_attack_sound(self.name)
				damage, m = self.calculate_damage(userPokemon, targetPokemon)
				if 'Super effective!' in m:
					mixer.play_sound('Super Effective')
				elif 'Not very effective...' in m:
					mixer.play_sound('Not Very Effective')
				elif 'Doesn\'t affect %s.' % targetPokemon.name in m:
					pass
				else:
					mixer.play_sound('Damage')
				messages.append(m)
			else:
				self.turnNumber = self.duration
		else:
			damage = 0
			messages.append('%s\'s attack missed.' % userPokemon.name)
			self.turnNumber = self.duration

		self.turnNumber += 1

		if self.turnNumber == self.duration:
			userPokemon.afflict_status(self.condition)
			userPokemon.stop_using_attack()
			self.turnNumber = 0

		return damage, messages

class IceBeam(Attack):
	def __init__(self):
		self.name = 'Ice Beam'
		self.type = ice
		self.attackType = [special, optConditionModifier]
		self.condition = Freeze()
		self.effectAccuracy = 10
		self.description = 'Blasts the foe with an icy beam that may freeze it.'

		power = 95
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

class IcePunch(Attack):
	def __init__(self):
		self.name = 'Ice Punch'
		self.type = ice
		self.attackType = [physical, optConditionModifier]
		self.condition = Freeze()
		self.effectAccuracy = 10
		self.description = 'A icy punch that may freeze the foe.'

		power = 75
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class IcicleSpear(MultiAttack):
	def __init__(self):
		self.name = 'Icicle Spear'
		self.type = ice
		self.attackType = [physical]
		self.description = 'Attacks the foe by firing 2 to 5 icicles in a row.'

		power = 10
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)

class IcyWind(Attack):
	def __init__(self):
		self.name = 'Icy Wind'
		self.type = ice
		self.attackType = [special, optStatModifier]
		self.statsModified = [speed]
		self.stageModifier = -1
		self.effectAccuracy = 100
		self.description = 'A chilling attack that lowers the foe\'s speed.'

		power = 55
		accuracy = 95
		pp = 15
		super().__init__(pp, power, accuracy)

class Mist(Attack):
	def __init__(self):
		self.name = 'Mist'
		self.type = ice
		self.attackType = [weather]
		# self.weather = Hailstorm()
		self.description = 'Creates a mist that stops reduction of abilities.'

		power = 0
		accuracy = 0
		pp = 30
		super().__init__(pp, power, accuracy)

class PowderSnow(Attack):
	def __init__(self):
		self.name = 'Powder Snow'
		self.type = ice
		self.attackType = [special, optConditionModifier]
		self.condition = Freeze()
		self.effectAccuracy = 10
		self.description = 'Blasts the foe with a snowy gust. May cause freezing.'

		power = 40
		accuracy = 100
		pp = 25
		super().__init__(pp, power, accuracy)

class SheerCold(Attack):
	def __init__(self):
		self.name = 'Sheer Cold'
		self.type = ice
		self.attackType = [special]
		self.description = 'A chilling attack that causes fainting if it hits.'

		power = 0
		accuracy = 30
		pp = 5
		super().__init__(pp, power, accuracy)

		def calculate_damage(self, userPokemon, targetPokemon):			
			messages = []
			damage = targetPokemon.maxHp
			messages.append('One-hit KO!')

			return damage, messages