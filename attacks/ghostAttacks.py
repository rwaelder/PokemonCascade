from pokemonTypes import ghost
from attack import Attack, MultiAttack
from statuses import *
from random import randint
from attackKeywords import *

class Astonish(Attack):
	def __init__(self):
		self.name = 'Astonish'
		self.type = ghost
		self.attackType = [physical, optConditionModifier]
		self.condition = Flinch()
		self.effectAccuracy = 30
		self.description = 'An attack that may shock the foe into flinching.'

		power = 30
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class ConfuseRay(Attack):
	def __init__(self):
		self.name = 'Confuse Ray'
		self.type = ghost
		self.attackType = [optConditionModifier]
		self.condition = ConfusionStatus()
		self.effectAccuracy = 0
		self.description = 'Emits bizarre sound waves that may confuse the foe.'

		power = 0
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

class Curse(Attack):
	def __init__(self):
		self.name = 'Curse'
		self.type = ghost
		self.attackType = [selfStatModifier, optConditionModifier]
		self.condition = Cursed()
		self.effectAccuracy = 0
		self.description = 'A move that functions differently for ghosts.'

		power = 0
		accuracy = 0
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		messages = []
		damage = 0
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		self.pp -= 1


		
		protected, m = self.check_protect(userPokemon, targetPokemon)
		messages.extend(m)

		if self.accuracy == 0 or randint(1,100) < (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
			
			if not protected and ghost in userPokemon.type:
				mixer.play_attack_sound(self.name)
				damage = int(userPokemon.maxHp / 2)
				userPokemon.take_damage(damage)
				targetPokemon.afflict_status(self.condition)
				messages.append('%s lowered its HP...' % userPokemon.name)
				messages.append('to curse %s!' % targetPokemon.name)
				
			
			elif ghost not in userPokemon.type:
				mixer.play_attack_sound('Stat Rise Up')
				m = userPokemon.modify_battle_stats(attack, 1)
				messages.append(m)
				m = userPokemon.modify_battle_stats(defense, 1)
				messages.append(m)
				m = userPokemon.modify_battle_stats(speed, -1)
				mixer.play_attack_sound('Stat Fall Down')
			else:
				pass
		else:
			damage = 0
			messages.append('%s\'s attack missed.' % userPokemon.name)

			
			
		return damage, messages

class DestinyBond(Attack):
	def __init__(self):
		self.name = 'Destiny Bond'
		self.type = ghost
		self.attackType = [selfConditionModifier, optConditionModifier]
		self.description = 'If the user faints, the foe is also made to faint.'

		power = 0
		accuracy = 0
		pp = 5
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('This move not yet implemented.')

		return damage, messages

class Grudge(Attack):
	def __init__(self):
		self.name = 'Grudge'
		self.type = ghost
		self.attackType = [selfConditionModifier, optConditionModifier]
		self.description = 'If the user faints, deletes the PP of the final move.'

		power = 0
		accuracy = 0
		pp = 5
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('This move not yet implemented.')

		return damage, messages

class Lick(Attack):
	def __init__(self):
		self.name = 'Lick'
		self.type = ghost
		self.attackType = [physical, optConditionModifier]
		self.condition = Paralysis()
		self.effectAccuracy = 30
		self.description = 'Licks with a long tongue to injure. May also paralyze.'

		power = 20
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)

class NightShade(Attack):
	def __init__(self):
		self.name = 'Night Shade'
		self.type = ghost
		self.attackType = [speed]
		self.description = 'Inflicts damage identical to the user\'s level.'
		
		power = 0
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

	def calculate_damage(self, userPokemon, targetPokemon):
		damage = userPokemon.level
		messages = []

		typeModifier = get_type_modifier(self.type, targetPokemon.type)
		if typeModifier == 2 or typeModifier == 4:
			messages.append('Super effective!')
		elif typeModifier == 0.5 or typeModifier == 0.25:
			messages.append('Not very effective...')
		elif typeModifier == 0:
			messages.append('Does not affect %s.' % targetPokemon.name)

		return damage, messages

class Nightmare(Attack):
	def __init__(self):
		self.name = 'Nightmare'
		self.type = ghost
		self.attackType = [optConditionModifier]
		self.condition = NightmareStatus()
		self.effectAccuracy = 0
		self.description = 'Inflicts 1/4 damage on a sleeping foe every turn.'

		power = 0
		accuracy = 100
		pp = 5
		super().__init__(pp, power, accuracy)

class ShadowBall(Attack):
	def __init__(self):
		self.name = 'Shadow Ball'
		self.type = ghost
		self.attackType = [special, optStatModifier]
		self.statsModified = [spDefense]
		self.stageModifier = -1
		self.effectAccuracy = 20
		self.description = 'Hurls a black blob that may lower special defense.'

		power = 80
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class ShadowPunch(Attack):
	def __init__(self):
		self.name = 'Shadow Punch'
		self.type = ghost
		self.attackType = [physical]
		self.description = 'An unavoidable punch that is thrown from shadows.'

		power = 60
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)

class Spite(Attack):
	def __init__(self):
		self.name = 'Spite'
		self.type = ghost
		self.attackType = [selfConditionModifier, optConditionModifier]
		self.description = 'Spitefully cuts the PP of the foe\'s last move.'

		power = 0
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('This move not yet implemented.')

		return damage, messages
