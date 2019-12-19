from pokemonTypes import psychic
from attack import Attack, MultiAttack
from statuses import *
from random import randint
from attackKeywords import *


class Agility(Attack):
	def __init__(self):
		self.name = 'Agility'
		self.type = psychic
		self.attackType = [selfStatModifier]
		self.statsModified = [speed]
		self.stageModifier = 2
		self.effectAccuracy = 0
		self.description = 'Relaxes the body to sharply boost speed.'

		power = 0
		accuracy = 0
		pp = 30
		super().__init__(pp, power, accuracy)

class Amnesia(Attack):
	def __init__(self):
		self.name = 'Amnesia'
		self.type = psychic
		self.attackType = [selfStatModifier]
		self.statsModified = [spDefense]
		self.stageModifier = 2
		self.effectAccuracy = 0
		self.description = 'Forgets about something and sharply raises special defense.'

		power = 0
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)

class Barrier(Attack):
	def __init__(self):
		self.name = 'Barrier'
		self.type = psychic
		self.attackType = [selfStatModifier]
		self.statsModified = [defense]
		self.stageModifier = 2
		self.effectAccuracy = 0
		self.description = 'Creates a barrier that sharply raises defense.'

		power = 0
		accuracy = 0
		pp = 30
		super().__init__(pp, power, accuracy)

class CalmMind(Attack):
	def __init__(self):
		self.name = 'Calm Mind'
		self.type = psychic
		self.attackType = [selfStatModifier]
		self.statsModified = [spAttack, spDefense]
		self.stageModifier = 1
		self.effectAccuracy = 0
		self.description = 'Raises special attack and special defense by focusing the mind.'

		power = 0
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)


class Confusion(Attack):
	def __init__(self):
		self.name = 'Confusion'
		self.type = psychic
		self.attackType = [special, optConditionModifier]
		self.condition = ConfusionStatus()
		self.effectAccuracy = 10
		self.description = 'A psychic attack that may cause confusion.'

		power = 50
		accuracy = 100
		pp = 25
		super().__init__(pp, power, accuracy)

class CosmicPower(Attack):
	def __init__(self):
		self.name = 'Cosmic Power'
		self.type = psychic
		self.attackType = [selfStatModifier]
		self.statsModified = [defense, spDefense]
		self.stageModifier = 1
		self.effectAccuracy = 0
		self.description = 'Raises defense and special defense with a mystic power.'

		power = 0
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)

class DreamEater(Attack):
	def __init__(self):
		self.name = 'Dream Eater'
		self.type = psychic
		self.attackType = [special, heal]
		# heal modifier of 1.x means damage dependent heal
		# heal at 0.x * damage
		self.healModifier = 1.5
		self.effectAccuracy = 0
		self.description = 'Takes half the damage inflicted on a sleeping foe.'

		power = 100
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		self.pp -= 1
		messages.append('%s used %s!' % (userPokemon.name, self.name))

		if targetPokemon.isAsleep():
			if randint(1,100) < (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
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
				messages.extend(m)

				healModifier = int((self.healModifier-1) * damage)
				userPokemon.heal(healModifier)
				mixer.play_attack_sound('Healing Attack')
				messages.append('%s regained health!' % userPokemon.name)
			else:
				messages.append('%s\'s attack missed.' % userPokemon.name)
		else:
			messages.append('Target must be asleep!')

		return damage, messages

class Extrasensory(Attack):
	def __init__(self):
		self.name = 'Extrasensory'
		self.type = psychic
		self.attackType = [special, optConditionModifier]
		self.condition = Flinch()
		self.effectAccuracy = 10
		self.description = 'Bites with vicious fangs. May cause flinching.'

		power = 80
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)

class FutureSight(Attack):
	def __init__(self):
		self.name = 'Future Sight'
		self.type = psychic
		self.attackType = [special]
		self.description = 'Heightens inner power to strike 2 turns later.'

		power = 80
		accuracy = 0
		pp = 30
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('This move not yet implemented.')

		return damage, messages

class Hypnosis(Attack):
	def __init__(self):
		self.name = 'Hypnosis'
		self.type = psychic
		self.attackType = [optConditionModifier]
		self.condition = Sleep()
		self.effectAccuracy = 0
		self.description = 'A hypnotizing move that may induce sleep.'

		power = 0
		accuracy = 60
		pp = 20
		super().__init__(pp, power, accuracy)

class Imprison(Attack):
	def __init__(self):
		self.name = 'Imprison'
		self.type = psychic
		self.attackType = [optConditionModifier]
		self.description = 'Prevents the foe from using moves known by the user.'

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

class Kinesis(Attack):
	def __init__(self):
		self.name = 'Kinesis'
		self.type = normal
		self.attackType = [optStatModifier]
		self.statsModified = [accuracyStat]
		self.stageModifier = -1
		self.effectAccuracy = 0
		self.description = 'Distracts the foe. May lower accuracy.'

		power = 0
		accuracy = 80
		pp = 15
		super().__init__(pp, power, accuracy)

class LightScreen(Attack):
	def __init__(self):
		self.name = 'Light Screen'
		self.type = psychic
		self.attackType = [selfConditionModifier]
		self.condition = LightScreened()
		self.effectAccuracy = 0
		self.description = 'Creates a wall of light that lowers special attack damage.'

		power = 0
		accuracy = 0
		pp = 30
		super().__init__(pp, power, accuracy)

class LusterPurge(Attack):
	def __init__(self):
		self.name = 'Luster Purge'
		self.type = psychic
		self.attackType = [special, optStatModifier]
		self.statsModified = [spDefense]
		self.stageModifier = -1
		self.effectAccuracy = 50
		self.description = 'Attacks with a burst of light. May lower special defense.'

		power = 70
		accuracy = 100
		pp = 5
		super().__init__(pp, power, accuracy)

class MagicCoat(Attack):
	def __init__(self):
		self.name = 'Magic Coat'
		self.type = psychic
		self.attackType = [selfConditionModifier, optConditionModifier]
		self.description = 'Reflects special effects back to the attacker.'

		power = 0
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('This move not yet implemented.')

		return damage, messages

class Meditate(Attack):
	def __init__(self):
		self.name = 'Meditate'
		self.type = psychic
		self.attackType = [selfStatModifier]
		self.statsModified = [attack]
		self.stageModifier = 1
		self.effectAccuracy = 0
		self.description = 'Meditates in a peaceful fashion to raise attack.'

		power = 0
		accuracy = 0
		pp = 40
		super().__init__(pp, power, accuracy)

class MirrorCoat(Attack):
	def __init__(self):
		self.name = 'Mirror Coat'
		self.type = psychic
		self.attackType = [selfConditionModifier, optConditionModifier]
		self.description = 'Counters the foe\'s special attack at double the power.'

		power = 0
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)
		self.priority = -1

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('This move not yet implemented.')

		return damage, messages

class MistBall(Attack):
	def __init__(self):
		self.name = 'Mist Ball'
		self.type = psychic
		self.attackType = [special, optStatModifier]
		self.statsModified = [spAttack]
		self.stageModifier = -1
		self.effectAccuracy = 50
		self.description = 'Attacks with a flurry of down. May lower special attack.'

		power = 70
		accuracy = 100
		pp = 40
		super().__init__(pp, power, accuracy)

class Psybeam(Attack):
	def __init__(self):
		self.name = 'Psybeam'
		self.type = psychic
		self.attackType = [special, optConditionModifier]
		self.condition = ConfusionStatus()
		self.effectAccuracy = 10
		self.description = 'Fires a peculiar ray that may confuse the foe.'

		power = 65
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Psychic(Attack):
	def __init__(self):
		self.name = 'Psychic'
		self.type = psychic
		self.attackType = [special, optStatModifier]
		self.statsModified = [spDefense]
		self.stageModifier = -1
		self.effectAccuracy = 10
		self.description = 'A powerful psychic attack that may lower special defense.'

		power = 90
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

class PsychoBoost(Attack):
	def __init__(self):
		self.name = 'Psycho Boost'
		self.type = psychic
		self.attackType = [special, selfStatModifier]
		self.statsModified = [spAttack]
		self.stageModifier = -2
		self.effectAccuracy = 0
		self.description = 'Allows a full-power attack, but sharply lowers special attack.'

		power = 140
		accuracy = 90
		pp = 5
		super().__init__(pp, power, accuracy)

class Psywave(Attack):
	def __init__(self):
		self.name = 'Psywave'
		self.type = psychic
		self.attackType = [special]
		self.description = 'Attacks with a psychic wave of varying intensity.'

		power = 0
		accuracy = 80
		pp = 15
		super().__init__(pp, power, accuracy)

	def calculate_damage(self, userPokemon, targetPokemon):
		
		damage = userPokemon.level * (randint(0,10) * 10 + 50) / 100
		damage *= self.screen_damage_modifier(targetPokemon)
		damage = int(damage)
		if damage == 0:
			damage = 1
		messages = []

		typeModifier = get_type_modifier(self.type, targetPokemon.type)
		if typeModifier == 2 or typeModifier == 4:
			messages.append('Super effective!')
		elif typeModifier == 0.5 or typeModifier == 0.25:
			messages.append('Not very effective...')
		elif typeModifier == 0:
			messages.append('Does not affect %s.' % targetPokemon.name)



		return damage, messages

class Reflect(Attack):
	def __init__(self):
		self.name = 'Reflect'
		self.type = psychic
		self.attackType = [selfConditionModifier]
		self.condition = ReflectScreened()
		self.effectAccuracy = 0
		self.description = 'Creates a wall of light that lowers attack damage.'

		power = 0
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)

class Rest(Attack):
	def __init__(self):
		self.name = 'Rest'
		self.type = psychic
		self.attackType = [selfConditionModifier]
		self.condition = Sleep(duration=2)
		self.description = 'The user sleeps 2 turns, restoring HP and status.'

		power = 0
		accuracy = 0
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		self.pp -= 1

		messages.append('%s used %s!' % (userPokemon.name, self.name))
		mixer.play_attack_sound(self.name)

		userPokemon.heal_status()
		userPokemon.afflict_status(self.condition)
		userPokemon.heal(1)
		mixer.play_attack_sound('Healing Attack')

		messages.append('%s recovered HP!' % userPokemon.name)

		return damage, messages

class RolePlay(Attack):
	def __init__(self):
		self.name = 'Role Play'
		self.type = psychic
		self.attackType = [selfConditionModifier]
		self.description = 'Mimics the target and copies its special ability.'

		power = 0
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('Abilities not yet implemented.')

		return damage, messages

class SkillSwap(Attack):
	def __init__(self):
		self.name = 'Skill Swap'
		self.type = psychic
		self.attackType = [selfConditionModifier, optConditionModifier]
		self.description = 'The user swaps special abilities with the target.'

		power = 0
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('Abilities not yet implemented.')

		return damage, messages

class Teleport(Attack):
	def __init__(self):
		self.name = 'Teleport'
		self.type = psychic
		self.attackType = [partyEffect]
		self.description = 'A psychic move for fleeing from battle instantly.'

		power = 0
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)

class Trick(Attack):
	def __init__(self):
		self.name = 'Trick'
		self.type = psychic
		self.attackType = [item]
		self.description = 'Tricks the foe into trading held items.'

		power = 0
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)
