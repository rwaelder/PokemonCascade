from pokemonTypes import flying
from attack import Attack
from statuses import SemiInvulnerable, Paralysis
from attackKeywords import *

class AerialAce(Attack):
	def __init__(self):
		self.name = 'Aerial Ace'
		self.type = flying
		self.attackType = [physical]
		self.description = 'An extremely speedy and unavoidable attack.'

		power = 60
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)

class Aeroblast(Attack):
	def __init__(self):
		self.name = 'Aeroblast'
		self.type = flying
		self.attackType = [special]
		self.description = 'Launches a vacuumed blast. High critical-hit ratio.'

		power = 100
		accuracy = 95
		pp = 5
		super().__init__(pp, power, accuracy)
		self.critStage = 1

class AirCutter(Attack):
	def __init__(self):
		self.name = 'Air Cutter'
		self.type = flying
		self.attackType = [special]
		self.description = 'Hacks with razorlike wind. High critical-hit ratio.'

		power = 55
		accuracy = 95
		pp = 25
		super().__init__(pp, power, accuracy)
		self.critStage = 1

class Bounce(Attack):
	def __init__(self):
		self.name = 'Bounce'
		self.type = flying
		self.attackType = [physical, selfConditionModifier]
		self.condition = SemiInvulnerable(self.name)
		self.secondCondition = Paralysis()
		self.effectAccuracy = 0
		self.paralyzeAccuracy = 30
		self.turnNumber = 0
		self.description = 'Bounces up, then down the next turn. May paralyze.'

		power = 85
		accuracy = 85
		pp = 5
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		if self.turnNumber == 0:
			self.pp -= 1
			

		if not userPokemon.keepUsingAttack:
			userPokemon.keep_using_attack(self)

		damage = 0
		messages = []

		if self.turnNumber == 0:
			mixer.play_attack_sound(self.name)
			m = userPokemon.afflict_status(self.condition)
			
		else:
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

					if randint(1,100) < self.paralyzeAccuracy:
						afflicted = targetPokemon.afflict_status(self.secondCondition)
						if afflicted:
							messages.append('%s is %s!' % (targetPokemon.name, self.secondCondition.battleText))
						else:
							messages.append('%s cannot be %s!' % (targetPokemon.name, self.secondCondition.battleText))

			else:
				damage = 0
				messages.append('%s\'s attack missed.' % userPokemon.name)

		self.turnNumber += 1

		if self.turnNumber == 2:
			userPokemon.stop_using_attack()
			self.turnNumber = 0

		return damage, messages

class DrillPeck(Attack):
	def __init__(self):
		self.name = 'Drill Peck'
		self.type = flying
		self.attackType = [physical]
		self.description = 'A corkscrewing attack with the beak acting as a drill.'

		power = 80
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Featherdance(Attack):
	def __init__(self):
		self.name = 'Featherdance'
		self.type = flying
		self.attackType = [optStatModifier]
		self.statsModified = [attack]
		self.stageModifier = -2
		self.effectAccuracy = 0
		self.description = 'Envelops the foe with down to sharply reduce attack.'

		power = 0
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class Fly(Attack):
	def __init__(self):
		self.name = 'Fly'
		self.type = flying
		self.attackType = [physical, selfConditionModifier]
		self.condition = SemiInvulnerable(self.name)
		self.effectAccuracy = 0
		self.turnNumber = 0
		self.description = 'Flies up on the first turn, then strikes the next turn.'

		power = 70
		accuracy = 95
		pp = 15
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

		self.turnNumber += 1

		if self.turnNumber == 2:
			userPokemon.stop_using_attack()
			self.turnNumber = 0

		return damage, messages

class Gust(Attack):
	def __init__(self):
		self.name = 'Gust'
		self.type = flying
		self.attackType = [special]
		self.description = 'Strikes the foe with a gust of wind whipped up by wings.'

		power = 40
		accuracy = 100
		pp = 35
		super().__init__(pp, power, accuracy)

class MirrorMove(Attack):
	def __init__(self):
		self.name = 'Mirror Move'
		self.type = flying
		self.attackType = [special]
		self.description = 'Counters the foe\'s attack with the same move.'

		power = 0
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('This move not yet implemented.')

		return damage, messages

class Peck(Attack):
	def __init__(self):
		self.name = 'Peck'
		self.type = flying
		self.attackType = [physical]
		self.description = 'Attacks the foe with a jabbing beak, etc.'

		power = 35
		accuracy = 100
		pp = 35
		super().__init__(pp, power, accuracy)

class SkyAttack(Attack):
	def __init__(self):
		self.name = 'Sky Attack'
		self.type = flying
		self.attackType = [physical]
		self.description = 'Searches out weak spots, then strikes the next turn.'

		power = 140
		accuracy = 90
		pp = 5
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
			messages.append('%s is looking for weak spots!' % userPokemon.name)
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

class WingAttack(Attack):
	def __init__(self):
		self.name = 'Wing Attack'
		self.type = flying
		self.attackType = [physical]
		self.description = 'Strikes the foe with wings spread wide.'

		power = 60
		accuracy = 100
		pp = 35
		super().__init__(pp, power, accuracy)
