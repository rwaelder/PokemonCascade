from pokemonTypes import fight
from attack import Attack, MultiAttack
from statuses import *
from random import randint
from attackKeywords import *


class ArmThrust(MultiAttack):
	def __init__(self):
		self.name = 'Arm Thrust'
		self.type = fight
		self.attackType = [physical]
		self.description = 'Straight-arm punches that strike the foe 2 to 5 times.'
		
		power = 15
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class BrickBreak(Attack):
	def __init__(self):
		self.name = 'Brick Break'
		self.type = fight
		self.attackType = [physical]
		self.description = 'Destroys barriers such as Reflect and causes damage.'
		
		power = 75
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		messages = []
		damage = 0
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		self.pp -= 1


		if self.accuracy == 0 or randint(0,100) > (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
			protected, m = self.check_protect(userPokemon, targetPokemon)
			messages.extend(m)
			if not protected:
				mixer.play_attack_sound(self.name)
				m = targetPokemon.remove_walls()
				messages.extend(m)
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
			messages.append('%s\'s attack missed.' % userPokemon.name)

		return damage, messages

class BulkUp(Attack):
	def __init__(self):
		self.name = 'Bulk Up'
		self.type = fight
		self.attackType = [selfStatModifier]
		self.statsModified = [attack, defense]
		self.stageModifier = 1
		self.effectAccuracy = 0
		self.description = 'Bulks up the body to boost both attack and defense.'
		
		power = 0
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)

class Counter(Attack):
	def __init__(self):
		self.name = 'Counter'
		self.type = fight
		self.attackType = [selfConditionModifier, optConditionModifier]
		self.description = 'Retaliates any physical hit with double the power.'

		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)
		self.priority = -1

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('This move not yet implemented.')

		return damage, messages

class CrossChop(Attack):
	def __init__(self):
		self.name = 'Cross Chop'
		self.type = fight
		self.attackType = [physical]
		self.description = 'A double-chopping attack. High critical-hit ratio.'

		power = 100
		accuracy = 80
		pp = 5
		super().__init__(pp, power, accuracy)
		self.critStage = 1

class Detect(Attack):
	def __init__(self):
		self.name = 'Detect'
		self.type = normal
		self.attackType = [selfConditionModifier]
		self.condition = Protected()
		self.effectAccuracy = 100
		self.description = 'Evades attack, but may fail if used in succession.'

		power = 0
		accuracy = 0
		pp = 5
		super().__init__(pp, power, accuracy)
		self.priority = 1

	def use(self, mixer, userPokemon, targetPokemon):
		messages = []
		damage = 0
		messages.append('%s used Detect!' % userPokemon.name)
		self.pp -= 1

		if 'protected' in userPokemon.battle_status_names():

			self.effectAccuracy = int(self.effectAccuracy / 2)
		else:
			self.effectAccuracy = 100

		if randint(1,99) < self.effectAccuracy:
			afflicted = userPokemon.afflict_status(self.condition)
			if afflicted:
				mixer.play_attack_sound(self.name)
				messages.append('%s is %s!' % (userPokemon.name, self.condition.battleText))
		else:
			messages.append('But it failed.')


		return damage, messages

class DoubleKick(MultiAttack):
	def __init__(self):
		self.name = 'Double Kick'
		self.type = fight
		self.attackType = [physical]
		self.description = 'A double-kicking attack that strikes the foe twice.'
		
		power = 30
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)

class Dynamicpunch(Attack):
	def __init__(self):
		self.name = 'Dynamicpunch'
		self.type = fight
		self.attackType = [physical, selfConditionModifier]
		self.condition = ConfusionStatus()
		self.effectAccuracy = 0
		self.description = 'Powerful and sure to cause confusion, but inaccurate.'

		power = 100
		accuracy = 50
		pp = 5
		super().__init__(pp, power, accuracy)

class FocusPunch(Attack):
	def __init__(self):
		self.name = 'Focus Punch'
		self.type = fight
		self.attackType = [physical]
		self.turnNumber = 0
		self.description = 'A powerful loyalty attack. The user flinches if hit.'

		power = 100
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)
		self.priority = -3

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('This move not yet implemented.')

		return damage, messages

class HiJumpKick(Attack):
	def __init__(self):
		self.name = 'Hi Jump Kick'
		self.type = fight
		self.attackType = [physical]
		self.description = 'A jumping knee kick. If it misses, the user is hurt.'
		
		power = 85
		accuracy = 90
		pp = 20
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		messages = []
		damage = 0
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		self.pp -= 1


		if self.accuracy == 0 or randint(0,100) > (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
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
			messages.append('%s\' kept going and crashed!.' % userPokemon.name)
			userDamage = int(userPokemon.maxHp / 8)
			userPokemon.take_damage(userDamage)

		return damage, messages

class JumpKick(Attack):
	def __init__(self):
		self.name = 'Jump Kick'
		self.type = fight
		self.attackType = [physical]
		self.description = 'A strong jumping kick. May miss and hurt the kicker.'
		
		power = 70
		accuracy = 95
		pp = 25
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		messages = []
		damage = 0
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		self.pp -= 1


		if self.accuracy == 0 or randint(0,100) > (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
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
			messages.append('%s\' kept going and crashed!.' % userPokemon.name)
			userDamage = int(userPokemon.maxHp / 8)
			userPokemon.take_damage(userDamage)

		return damage, messages

class KarateChop(Attack):
	def __init__(self):
		self.name = 'Karate Chop'
		self.type = fight
		self.attackType = [physical]
		self.description = 'A chopping attack with a high critical-hit ratio.'

		power = 50
		accuracy = 100
		pp = 25
		super().__init__(pp, power, accuracy)
		self.critStage = 1

class LowKick(Attack):
	def __init__(self):
		self.name = 'Low Kick'
		self.type = fight
		self.attackType = [physical]
		self.description = 'A kick that inflicts more damage on heavier foes.'

		power = 0
		accuracy = 80
		pp = 20
		super().__init__(pp, power, accuracy)


	def calculate_damage(self, userPokemon, targetPokemon):
		
		userAttack = userPokemon.battleAttack
		targetDefense = targetPokemon.battleDefense


		if targetPokemon.weight >= 200:
			power = 120
		elif targetPokemon.weight >= 100:
			power = 100
		elif targetPokemon.weight >= 50:
			power = 80
		elif targetPokemon.weight >= 25:
			power = 60
		elif targetPokemon.weight >= 10:
			power = 40
		else:
			power = 20

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
			

		if userPokemon.isBurned() and physical in self.attackType:
			burnModifier = 0.5
		else:
			burnModifier = 1


		modifier = typeModifier * stab * burnModifier * crit * (randint(85,100)/100)

		damage = ((((2*userPokemon.level/5)+2) * power * userAttack/targetDefense)/50 + 2) * modifier
		damage *= self.screen_damage_modifier(targetPokemon)
		damage = int(damage)

		return damage, messages

class MachPunch(Attack):
	def __init__(self):
		self.name = 'Mach Punch'
		self.type = fight
		self.attackType = [physical]
		self.description = 'A punch is thrown at wicked speed to strike first.'

		power = 40
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)
		self.priority = 1

class Revenge(Attack):
	def __init__(self):
		self.name = 'Revenge'
		self.type = fight
		self.attackType = [physical]
		self.description = 'An attack that gains power if injured by the foe.'

		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)
		self.priority = -1

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('This move not yet implemented.')

		return damage, messages

class Reversal(Attack):
	def __init__(self):
		self.name = 'Reversal'
		self.type = fight
		self.attackType = [physical]
		self.description = 'Inflicts more damage when the user\'s HP is down.'

		power = 0
		accuracy = 80
		pp = 20
		super().__init__(pp, power, accuracy)


	def calculate_damage(self, userPokemon, targetPokemon):
		
		userAttack = userPokemon.battleAttack
		targetDefense = targetPokemon.battleDefense

		hpPct = userPokemon.hp / userPokemon.maxHp * 100

		if hpPct >= 68.75:
			power = 20
		elif hpPct >= 35.42:
			power = 40
		elif hpPct >= 20.83:
			power = 80
		elif hpPct >= 10.42:
			power = 100
		elif hpPct >= 4.17:
			power = 150
		else:
			power = 200

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
			

		if userPokemon.isBurned() and physical in self.attackType:
			burnModifier = 0.5
		else:
			burnModifier = 1


		modifier = typeModifier * stab * burnModifier * crit * (randint(85,100)/100)

		damage = ((((2*userPokemon.level/5)+2) * power * userAttack/targetDefense)/50 + 2) * modifier
		damage *= self.screen_damage_modifier(targetPokemon)
		damage = int(damage)

		return damage, messages

class RockSmash(Attack):
	def __init__(self):
		self.name = 'Rock Smash'
		self.type = fight
		self.attackType = [physical, optStatModifier]
		self.statsModified = [defense]
		self.stageModifier = -1
		self.effectAccuracy = 50
		self.description = 'A rock-crushing attack that may lower defense.'

		power = 20
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class RollingKick(Attack):
	def __init__(self):
		self.name = 'Rolling Kick'
		self.type = fight
		self.attackType = [physical, optConditionModifier]
		self.condition = Flinch()
		self.effectAccuracy = 30
		self.description = 'A fast kick delivered from a rapid spin.'

		power = 60
		accuracy = 85
		pp = 15
		super().__init__(pp, power, accuracy)

class SeismicToss(Attack):
	def __init__(self):
		self.name = 'Seismic Toss'
		self.type = fight
		self.attackType = [physical]
		self.description = 'Inflicts damage identical to the user\'s level.'
		
		power = 0
		accuracy = 100
		pp = 20
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

class SkyUppercut(Attack):
	def __init__(self):
		self.name = 'Sky Uppercut'
		self.type = fight
		self.attackType = [physical]
		self.description = 'An uppercut thrown as if leaping into the sky.'
		
		power = 85
		accuracy = 90
		pp = 15
		super().__init__(pp, power, accuracy)

class Submission(Attack):
	def __init__(self):
		self.name = 'Submission'
		self.type = fight
		self.attackType = [physical]
		self.description = 'A reckless body slam that also hurts the user.'

		power = 80
		accuracy = 80
		pp = 25
		super().__init__(pp, power, accuracy)
		self.recoilModifier = 0.25

class Superpower(Attack):
	def __init__(self):
		self.name = 'Superpower'
		self.type = fight
		self.attackType = [physical, selfStatModifier]
		self.statsModified = [attack, defense]
		self.stageModifier = -1
		self.effectAccuracy = 0
		self.description = 'Boosts strength sharply, but lowers abilities.'
		
		power = 120
		accuracy = 100
		pp = 5
		super().__init__(pp, power, accuracy)

class TripleKick(MultiAttack):
	def __init__(self):
		self.name = 'Triple Kick'
		self.type = fight
		self.attackType = [physical]
		self.description = 'Kicks the foe 3 times in a row with rising intensity.'
		
		power = 10
		accuracy = 100
		pp = 5
		super().__init__(pp, power, accuracy)

	def use(self, userPokemon, targetPokemon):
		
		numberOfHits = 3
		totalDamage = 0
		messages = []
		messages.append('%s used %s!' % (userPokemon.name, self.name))

		
		for i in range(numberOfHits):
			if randint(1,100) < (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
				self.power = 10 * i
				protected, m = self.check_protect(userPokemon, targetPokemon)
				messages.extend(m)
				if not protected:
					mixer.play_attack_sound('_1hit' % self.name)
					damage, m = self.calculate_damage(userPokemon, targetPokemon)
					if 'Super effective!' in m:
						mixer.play_sound('Super Effective')
					elif 'Not very effective...' in m:
						mixer.play_sound('Not Very Effective')
					elif 'Doesn\'t affect %s.' % targetPokemon.name in m:
						pass
					else:
						mixer.play_sound('Damage')
					totalDamage += damage
					messages.extend(m)
				
			else:
				messages.append('%s\'s attack missed.' % userPokemon.name)
				break

		messages.append('Hit %i times!' % i)
		return totalDamage, messages

class VitalThrow(Attack):
	def __init__(self):
		self.name = 'Vital Throw'
		self.type = fight
		self.attackType = [physical]
		self.description = 'Makes the user\'s move last, but it never misses.'

		power = 70
		accuracy = 0
		pp = 10
		super().__init__(pp, power, accuracy)
		self.priority = -3