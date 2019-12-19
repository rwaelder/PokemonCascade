from pokemonTypes import ground, flying, electric
from attack import Attack, MultiAttack
from statuses import Flinch, TypeResistance, Bound, SemiInvulnerable
from random import randint
from attackKeywords import *

class BoneClub(Attack):
	def __init__(self):
		self.name = 'Bone Club'
		self.type = ground
		self.attackType = [physical, optConditionModifier]
		self.condition = Flinch()
		self.effectAccuracy = 0
		self.description = 'Clubs the foe with a bone. May cause flinching.'

		power = 65
		accuracy = 85
		pp = 20
		super().__init__(pp, power, accuracy)

class BoneRush(MultiAttack):
	def __init__(self):
		self.name = 'Bone Rush'
		self.type = ground
		self.attackType = [physical]
		self.description = 'Strikes the foe with a bone in hand 2 to 5 times.'

		power = 25
		accuracy = 80
		pp = 10
		super().__init__(pp, power, accuracy)

class Bonemerang(MultiAttack):
	def __init__(self):
		self.name = 'Bonemerang'
		self.type = ground
		self.attackType = [physical]
		self.description = 'Throws a bone boomerang that strikes twice.'

		power = 50
		accuracy = 90
		pp = 10
		super().__init__(pp, power, accuracy)

class Dig(Attack):
	def __init__(self):
		self.name = 'Dig'
		self.type = ground
		self.attackType = [physical, selfConditionModifier]
		self.condition = SemiInvulnerable(self.name)
		self.effectAccuracy = 0
		self.turnNumber = 0
		self.description = 'Digs underground on the first turn and strikes the next turn.'

		power = 60
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		if self.turnNumber == 0:
			self.pp -= 1
			

		if not userPokemon.keepUsingAttack:
			userPokemon.keep_using_attack(self)

		damage = 0
		messages = []

		if self.turnNumber == 0:
			mixer.play_attack_sound('%s_part_1' % self.name)
			m = userPokemon.afflict_status(self.condition)
			self.turnNumber += 1
		else:
			messages.append('%s used %s!' % (userPokemon.name, self.name))

			if randint(1,100) < (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
				protected, m = self.check_protect(userPokemon, targetPokemon)
				messages.extend(m)
				if not protected:
					mixer.play_attack_sound('%s_part_2' % self.name)
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
				damage = 0
				messages.append('%s\'s attack missed.' % userPokemon.name)

		

		if self.turnNumber == 1:
			userPokemon.stop_using_attack()
			self.turnNumber = 0

		return damage, messages

class Earthquake(Attack):
	def __init__(self):
		self.name = 'Earthquake'
		self.type = ground
		self.attackType = [physical]
		self.description = 'A powerful quake, but has no effect on flying foes.'

		power = 100
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

class Fissure(Attack):
	def __init__(self):
		self.name = 'Fissure'
		self.type = ground
		self.attackType = [physical]
		self.description = 'A one-hit KO move that drops the foe in a fissure.'

		power = 0
		accuracy = 30
		pp = 5
		super().__init__(pp, power, accuracy)

		def calculate_damage(self, userPokemon, targetPokemon):
			damage = 0
			messages = []
			if flying in targetPokemon.type:
				message.append('Doesn\'t effect %s' % targetPokemon.name)

			else:
				damage = targetPokemon.maxHp
				messages.append('One-hit KO!')

			return damage, messages

class Magnitude(Attack):
	def __init__(self):
		self.name = 'Magnitude'
		self.type = ground
		self.attackType = [physical]
		self.description = 'A ground-shaking attack of random intensity.'

		power = 0
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []

		messages.append('%s used %s!' % (userPokemon.name, self.name))
		self.pp -= 1
		mag = randint(1,100)
		if mag > 95:
			self.power = 150
			self.magnitude = 10
		elif mag > 85:
			self.power = 110
			self.magnitude = 9
		elif mag > 65:
			self.power = 90
			self.magnitude = 8
		elif mag > 35:
			self.power = 70
			self.magnitude = 7
		elif mag > 15:
			self.power = 50
			self.magnitude = 6
		elif mag > 5:
			self.power = 30
			self.magnitude = 5
		else:
			self.power = 10
			self.magnitude = 4

		messages.append('Magnitude %i!' % self.magnitude)

		if randint(1,100) < (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
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
			messages.append('%s\'s attack missed.' % userPokemon.name)

		return damage, messages

class MudShot(Attack):
	def __init__(self):
		self.name = 'Mud Shot'
		self.type = ground
		self.attackType = [physical, optStatModifier]
		self.statsModified = [speed]
		self.stageModifier = -1
		self.effectAccuracy = 0
		self.description = 'Hurls mud at the foe and reduces speed.'

		power = 55
		accuracy = 95
		pp = 15
		super().__init__(pp, power, accuracy)

class MudSport(Attack):
	def __init__(self):
		self.name = 'Mud Sport'
		self.type = ground
		self.attackType = [selfConditionModifier]
		self.condition = TypeResistance(electric)
		self.effectAccuracy = 0
		self.description = 'Covers the user in mud for electrical resistance.'

		power = 0
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class MudSlap(Attack):
	def __init__(self):
		self.name = 'Mud Slap'
		self.type = ground
		self.attackType = [physical, optStatModifier]
		self.statsModified = [accuracyStat]
		self.stageModifier = -1
		self.effectAccuracy = 0
		self.description = 'Hurls mud in the foe\'s face to reduce its accuracy.'

		power = 20
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

class SandTomb(Attack):
	def __init__(self):
		self.name = 'Sand Tomb'
		self.type = ground
		self.attackType = [special, optConditionModifier]
		self.condition = Bound(self.name)
		self.effectAccuracy = 0
		self.description = 'Traps and hurts the foe in quicksand for 2 to 5 turns.'

		power = 15
		accuracy = 70
		pp = 15
		super().__init__(pp, power, accuracy)


class SandAttack(Attack):
	def __init__(self):
		self.name = 'Sand-attack'
		self.type = ground
		self.attackType = [optStatModifier]
		self.statsModified = [accuracyStat]
		self.stageModifier = -1
		self.effectAccuracy = 0
		self.description = 'Reduces the foe\'s accuracy by hurling sand in its face.'

		power = 0
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class Spikes(Attack):
	def __init__(self):
		self.name = 'Spikes'
		self.type = ground
		self.attackType = [areaEffect]
		# self.condition = Bound(self.name)?=
		self.effectAccuracy = 0
		self.description = 'Sets spikes that hurt a foe switching out.'

		power = 0
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)
