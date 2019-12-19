from pokemonTypes import grass
from attack import Attack, MultiAttack
from statuses import Sleep, LeechSeedStatus, NoStatus, Recharge, Ingrained, Flinch, ConfusionStatus, Paralysis
from random import randint
from attackKeywords import *

class Absorb(Attack):
	def __init__(self):
		self.name = 'Absorb'
		self.type = grass
		self.attackType = [special, heal]
		# heal modifier of 1.x means damage dependent heal
		# heal at 0.x * damage
		self.healModifier = 1.5
		self.effectAccuracy = 0
		self.description = 'An attack that absorbs half the damage inflicted.'

		power = 20
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Aromatherapy(Attack):
	def __init__(self):
		self.name = 'Aromatherapy'
		self.type = grass
		self.attackType = [selfConditionModifier]
		self.condition = NoStatus()
		self.effectAccuracy = 0
		self.description = 'Heals all status problems with a soothing scent.'

		power = 0
		accuracy = 0
		pp = 5
		super().__init__(pp, power, accuracy)

class BulletSeed(MultiAttack):
	def __init__(self):
		self.name = 'Bullet Seed'
		self.type = grass
		self.attackType = [special]
		self.description = 'Shoots 2 to 5 seeds in a row to strike te foe.'

		power = 10
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)

class CottonSpore(Attack):
	def __init__(self):
		self.name = 'Cotton Spore'
		self.type = grass
		self.attackType = [optStatModifier]
		self.statsModified = [speed]
		self.stageModifier = -2
		self.effectAccuracy = 0
		self.description = 'Spores cling to the foe, sharply reducing speed.'

		power = 0
		accuracy = 85
		pp = 40
		super().__init__(pp, power, accuracy)

class FrenzyPlant(Attack):
	def __init__(self):
		self.name = 'Frenzy Plant'
		self.type = grass
		self.attackType = [physical, selfConditionModifier]
		self.condition = Recharge()
		self.effectAccuracy = 0
		self.description = 'Powerful, but leaves the user immobile the next turn.'

		power = 150
		accuracy = 90
		pp = 5
		super().__init__(pp, power, accuracy)

class GigaDrain(Attack):
	def __init__(self):
		self.name = 'Giga Drain'
		self.type = grass
		self.attackType = [special, heal]
		# heal modifier of 1.x means damage dependent heal
		# heal at 0.x * damage
		self.healModifier = 1.5
		self.effectAccuracy = 0
		self.description = 'An attack that steals half the damage inflicted.'

		power = 60
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class GrassWhistle(Attack):
	def __init__(self):
		self.name = 'Grass Whistle'
		self.type = grass
		self.attackType = [optConditionModifier]
		self.condition = Sleep()
		self.effectAccuracy = 0
		self.description = 'Lulls the foe to sleep with a pleasant'

		power = 0
		accuracy = 55
		pp = 15
		super().__init__(pp, power, accuracy)

class Ingrain(Attack):
	def __init__(self):
		self.name = 'Ingrain'
		self.type = grass
		self.attackType = [selfConditionModifier]
		self.condition = Ingrained()
		self.effectAccuracy = 0

		power = 0
		accuracy = 0
		pp =20
		super().__init__(pp, power, accuracy)

class LeafBlade(Attack):
	def __init__(self):
		self.name = 'Leaf Blade'
		self.type = grass
		self.attackType = [physical]
		self.description = 'Slashes with a sharp leaf. High critical-hit ratio.'

		power = 70
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)
		self.critStage = 1

class LeechSeed(Attack):
	def __init__(self):
		self.name = 'Leech Seed'
		self.type = grass
		self.attackType = [optConditionModifier]
		self.condition = LeechSeedStatus()
		self.effectAccuracy = 0
		self.description = 'Plants a seed on the foe to steal HP on every turn.'

		power = 0
		accuracy = 90
		pp = 10
		super().__init__(pp, power, accuracy)

class MagicalLeaf(Attack):
	def __init__(self):
		self.name = 'Magical Leaf'
		self.type = grass
		self.attackType = [special]
		self.description = 'Attacks with a strange leaf that cannot be evaded.'

		power = 60
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)

class MegaDrain(Attack):
	def __init__(self):
		self.name = 'Mega Drain'
		self.type = grass
		self.attackType = [special, heal]
		# heal modifier of 1.x means damage dependent heal
		# heal at 0.x * damage
		self.healModifier = 1.5
		self.effectAccuracy = 0
		self.description = 'An attack that absorbs half the damage inflicted.'

		power = 40
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class NeedleArm(Attack):
	def __init__(self):
		self.name = 'Needle Arm'
		self.type = grass
		self.attackType = [physical, optConditionModifier]
		self.condition = Flinch()
		self.effectAccuracy = 30
		self.description = 'Attacks with a thorny arm. May cause flinching.'

		power = 60
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class PedalDance(Attack):
	def __init__(self):
		self.name = 'Pedal Dance'
		self.type = grass
		self.attackType = [special, selfConditionModifier]
		self.duration = randint(2,3)
		self.turnNumber = 0
		self.condition = ConfusionStatus()
		self.effectAccuracy = 0

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
				messages.extend(m)

		else:
			damage = 0
			messages.append('%s\'s attack missed.' % userPokemon.name)

		self.turnNumber += 1

		if self.turnNumber == self.duration:
			userPokemon.afflict_status(self.condition)
			userPokemon.stop_using_attack()
			self.turnNumber = 0

		return damage, messages

class RazorLeaf(Attack):
	def __init__(self):
		self.name = 'Razor Leaf'
		self.type = grass
		self.attackType = [physical]
		self.description = 'Cuts the enemy with leaves. High critical-hit ratio.'

		power = 55
		accuracy = 95
		pp = 25
		super().__init__(pp, power, accuracy)
		self.critStage = 1

class SleepPowder(Attack):
	def __init__(self):
		self.name = 'Sleep Powder'
		self.type = grass
		self.attackType = [optConditionModifier]
		self.condition = Sleep()
		self.effectAccuracy = 100
		self.description = 'Scatters a powder that may cause the foe to sleep.'

		power = 0
		accuracy = 75
		pp = 15
		super().__init__(pp, power, accuracy)

class Solarbeam(Attack):
	def __init__(self):
		self.name = 'Solar Beam'
		self.type = grass
		self.attackType = [special]
		self.turnNumber = 0
		self.description = 'Absorbs light in one turn, then attacks next turn.'
		power = 120
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
			messages.append('%s is taking in sunlight!' % userPokemon.name)
			
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
					messages.extend(m)

			else:
				damage = 0
				messages.append('%s\'s attack missed.' % userPokemon.name)

		self.turnNumber += 1

		if self.turnNumber == 2:
			userPokemon.stop_using_attack()
			self.turnNumber = 0

		return damage, messages

class Spore(Attack):
	def __init__(self):
		self.name = 'Spore'
		self.type = grass
		self.attackType = [optConditionModifier]
		self.condition = Sleep()
		self.effectAccuracy = 0
		self.description = 'Scatters a cloud of spores that always induce sleep.'

		power = 0
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class StunSpore(Attack):
	def __init__(self):
		self.name = 'Stun Spore'
		self.type = grass
		self.attackType = [optConditionModifier]
		self.condition = Paralysis()
		self.effectAccuracy = 0
		self.description = 'Scatters a powder that may paralyze the foe.'

		power = 0
		accuracy = 75
		pp = 30
		super().__init__(pp, power, accuracy)

class Synthesis(Attack):
	def __init__(self):
		self.name = 'Synthesis'
		self.type = grass
		self.attackType = [heal]
		self.healModifier = 0.5
		self.effectAccuracy = 100
		self.description = 'Restores HP. The amount varies with the weather.'

		power = 0
		accuracy = 75
		pp = 15
		super().__init__(pp, power, accuracy)

class VineWhip(Attack):
	def __init__(self):
		self.name = 'Vine Whip'
		self.type = grass
		self.attackType = [physical]
		self.description = 'Strikes the foe with slender, whiplike vines.'

		power = 35
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)
