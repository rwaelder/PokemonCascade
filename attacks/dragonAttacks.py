from pokemonTypes import dragon
from attack import Attack
from typeMatchup import get_type_modifier
from statuses import ConfusionStatus
from attackKeywords import *
from random import randint

class DracoMeteor(Attack):
	def __init__(self):
		self.name = 'Draco Meteor'
		self.type = dragon
		self.attackType = [special, selfStatModifier]
		self.statsModified = [spAttack]
		self.stageModifier = -2
		self.effectAccuracy = 0
		self.description = 'Allows a full-power attack, but sharply reduces special attack.'

		power = 140
		accuracy = 90
		pp = 5
		super().__init__(pp, power, accuracy)

class DragonClaw(Attack):
	def __init__(self):
		self.name = 'Dragon Claw'
		self.type = dragon
		self.attackType = [physical]
		self.description = 'Slashes the foe with sharp claws.'

		power = 80
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class DragonDance(Attack):
	def __init__(self):
		self.name = 'Dragon Dance'
		self.type = dragon
		self.attackType = [selfStatModifier]
		self.description = 'A mystical dance that ups attack and speed.'

		power = 0
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		messages.append('%s used %s!' % (userPokemon.name, self.name))

		self.pp -= 1
		mixer.play_attack_sound(self.name)
		messages.append(userPokemon.modify_battle_stats(attack, 1))
		messages.append(userPokemon.modify_battle_stats(speed, 1))
		mixer.play_attack_sound('Stat Rise Up')

		return damage, messages

class DragonRage(Attack):
	def __init__(self):
		self.name = 'Dragon Rage'
		self.type = dragon
		self.attackType = [special]
		self.description = 'Launches shock waves that always inflicts 40 damage.'

		power = 0
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)
	
	def calculate_damage(self, userPokemon, targetPokemon):
		damage = 40
		messages = []

		typeModifier = get_type_modifier(self.type, targetPokemon.type)
		if typeModifier == 2 or typeModifier == 4:
			messages.append('Super effective!')
		elif typeModifier == 0.5 or typeModifier == 0.25:
			messages.append('Not very effective...')
		elif typeModifier == 0:
			messages.append('Does not affect %s.' % targetPokemon.name)

		return damage, messages

class Dragonbreath(Attack):
	def __init__(self):
		self.name = 'Dragonbreath'
		self.type = dragon
		self.attackType = [special]
		self.description = 'Strikes the foe with an incredible blast of breath.'

		power = 60
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Outrage(Attack):
	def __init__(self):
		self.name = 'Outrage'
		self.type = dragon
		self.attackType = [special, selfConditionModifier]
		self.duration = randint(2,3)
		self.turnNumber = 0
		self.condition = ConfusionStatus()
		self.effectAccuracy = 0
		self.description = 'A rampage of 2 to 3 turns that confuses the user.'

		power = 70
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		if self.turnNumber == 0:
			self.pp -= 1
			self.duration = randint(2,3)

		if not userPokemon.keepUsingAttack:
			userPokemon.keep_using_attack(self)

		damage = 0
		messages = []

		messages.append('%s used %s!' % (userPokemon.name, self.name))
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
			damage = 0
			messages.append('%s\'s attack missed.' % userPokemon.name)

		self.turnNumber += 1

		if self.turnNumber == self.duration:
			userPokemon.afflict_status(self.condition)
			userPokemon.stop_using_attack()
			self.turnNumber = 0

		return damage, messages

class Twister(Attack):
	def __init__(self):
		self.name = 'Twister'
		self.type = dragon
		self.attackType = [special]
		self.description = 'Whips up a twister to tear at the foe.'

		power = 40
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)