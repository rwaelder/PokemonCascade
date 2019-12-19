from pokemonTypes import bug
from attack import Attack, MultiAttack
from statuses import FuryCutterUsed, ConfusionStatus, CantEscape
from attackKeywords import *

class FuryCutter(Attack):
	def __init__(self):
		self.name = 'Fury Cutter'
		self.type = bug
		self.attackType = [physical, selfConditionModifier]
		self.condition = FuryCutterUsed()
		self.effectAccuracy = 0
		self.description = 'Attack that increases in power each time it hits.'

		power = 10
		accuracy = 95
		pp = 20
		super().__init__(pp, power, accuracy)
		self.basePower = 10

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		messages.append('%s used %s!' % (userPokemon.name, self.name))

		statuses = ''.join(userPokemon.battle_status_names())

		powerMultiplier = statuses.count('furycutter')

		self.power = self.basePower * powerMultiplier

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
				userPokemon.afflict_status(self.condition)

		else:
			damage = 0
			messages.append('%s\'s attack missed.' % userPokemon.name)

		return damage, messages

class LeechLife(Attack):
	def __init__(self):
		self.name = 'Leech Life'
		self.type = bug
		self.attackType = [physical, heal]
		# heal modifier of 1.x means damage dependent heal
		# heal at 0.x * damage
		self.healModifier = 1.5
		self.effectAccuracy = 0
		self.description = 'An attack that steals half the damage inflicted.'

		power = 20
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)	

class Megahorn(Attack):
	def __init__(self):
		self.name = 'Megahorn'
		self.type = bug
		self.attackType = [physical]
		self.description = 'A brutal ramming attack using out-thrust horns.'

		power = 120
		accuracy = 85
		pp = 10
		super().__init__(pp, power, accuracy)

class PinMissile(MultiAttack):
	def __init__(self):
		self.name = 'Pin Missile'
		self.type = bug
		self.attackType = [physical]
		self.description = 'Sharp pins are fired to strike 2 to 5 times.'

		power = 14
		accuracy = 85
		pp = 20
		super().__init__(pp, power, accuracy)

class SignalBeam(Attack):
	def __init__(self):
		self.name = 'Signal Beam'
		self.type = bug
		self.attackType = [special, optConditionModifier]
		self.condition = ConfusionStatus()
		self.effectAccuracy = 10
		self.description = 'A strange beam attack that may confuse the foe.'

		power = 75
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class SilverWind(Attack):
	def __init__(self):
		self.name = 'Silver Wind'
		self.type = bug
		self.attackType = [special, selfStatModifier]
		self.statsModified = ['all']
		self.stageModifier = 1
		self.effectAccuracy = 10
		self.description = 'A powdery attack that may raise abilities.'

		power = 60
		accuracy = 100
		pp = 5
		super().__init__(pp, power, accuracy)

class SpiderWeb(Attack):
	def __init__(self):
		self.name = 'Spider Web'
		self.type = bug
		self.attackType = [optConditionModifier]
		self.condition = CantEscape()
		self.effectAccuracy = 0
		self.description = 'Ensnares the foe to stop it from fleeing or switching.'

		power = 0
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

class StringShot(Attack):
	def __init__(self):
		self.name = 'String Shot'
		self.type = bug
		self.attackType = [optStatModifier]
		self.statsModified = [speed]
		self.stageModifier = -1
		self.effectAccuracy = 0
		self.description = 'Binds the foe with string to reduce speed.'

		power = 0
		accuracy = 95
		pp = 40
		super().__init__(pp, power, accuracy)

class TailGlow(Attack):
	def __init__(self):
		self.name = 'Tail Glow'
		self.type = bug
		self.attackType = [selfStatModifier]
		self.statsModified = [spAttack]
		self.stageModifier = 2
		self.effectAccuracy = 0
		self.description = 'Flashes a light that sharply raises special attack.'

		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Twineedle(MultiAttack):
	def __init__(self):
		self.name = 'Twineedle'
		self.type = bug
		self.attackType = [physical]
		self.description = 'Stingers on the forelegs jab the foe twice.'

		power = 25
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)