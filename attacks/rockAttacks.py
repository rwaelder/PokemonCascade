from pokemonTypes import rock
from attack import Attack, MultiAttack
from statuses import *
from random import randint
from attackKeywords import *

class Ancientpower(Attack):
	def __init__(self):
		self.name = 'Ancientpower'
		self.type = rock
		self.attackType = [physical, selfStatModifier]
		self.statsModified = ['all']
		self.stageModifier = 1
		self.effectAccuracy = 10
		self.description = 'An attack that may raise all stats.'

		power = 60
		accuracy = 100
		pp = 5
		super().__init__(pp, power, accuracy)

class RockBlast(MultiAttack):
	def __init__(self):
		self.name = 'Rock Blast'
		self.type = rock
		self.attackType = [physical]
		self.description = 'Hurls boulders at the foe 2 to 5 times in a row.'

		power = 25
		accuracy = 80
		pp = 10
		super().__init__(pp, power, accuracy)

class RockSlide(Attack):
	def __init__(self):
		self.name = 'Rock Slide'
		self.type = rock
		self.attackType = [physical, optConditionModifier]
		self.condition = Flinch()
		self.effectAccuracy = 30
		self.description = 'Large boulders are hurled. May cause flinching.'

		power = 75
		accuracy = 90
		pp = 10
		super().__init__(pp, power, accuracy)

class RockThrow(Attack):
	def __init__(self):
		self.name = 'Rock Throw'
		self.type = rock
		self.attackType = [physical]
		self.description = 'Throws small rocks to strike the foe.'

		power = 50
		accuracy = 90
		pp = 15
		super().__init__(pp, power, accuracy)

class RockTomb(Attack):
	def __init__(self):
		self.name = 'Rock Tomb'
		self.type = rock
		self.attackType = [physical, optStatModifier]
		self.statsModified = [speed]
		self.stageModifier = -1
		self.effectAccuracy = 100
		self.description = 'Stops the foe from moving with rocks and cuts speed.'

		power = 50
		accuracy = 80
		pp = 10
		super().__init__(pp, power, accuracy)

class Rollout(Attack):
	def __init__(self):
		self.name = 'Rollout'
		self.type = rock
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
			mixer.play_attack_sound(self.name)
			self.power = 30 * (2**self.turnNumber)
			protected, m = self.check_protect(userPokemon, targetPokemon)
			messages.extend(m)
			if not protected:
				damage, m = self.calculate_damage(userPokemon, targetPokemon)
				if 'Super effective!' in m:
					mixer.play_sound('Super Effective')
				elif 'Not very effective...' in m:
					mixer.play_sound('Not Very Effective')
				elif 'Doesn\'t affect %s.' % targetPokemon.name in m:
					pass
				else:
					mixer.play_sound('Damage')
				messages.extend(m)
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

class Sandstorm(Attack):
	def __init__(self):
		self.name = 'Sandstorm'
		self.type = rock
		self.attackType = [weather]
		# self.weather = Sunny()
		self.description = 'Causes a sandstorm that rages for several turns.'

		power = 0
		accuracy = 0
		pp = 10
		super().__init__(pp, power, accuracy)