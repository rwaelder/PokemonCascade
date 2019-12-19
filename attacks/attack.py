from random import randint
from pokemonTypes import *
from typeMatchup import get_type_modifier
from attackKeywords import *



class Attack():

	def __init__(self, pp, power, accuracy):
		self.power = power
		self.accuracy = accuracy
		self.maxPP = pp
		self.pp = pp
		self.critStage = 0
		self.recoilModifier = 0
		self.priority = 0
		self.disabled = False


	def get_recoil(self, damage):
		return int(damage * self.recoilModifier)

	def disable(self):
		self.disabled = True

	def enable(self):
		self.disabled = False

	def accuracy_evasion_modifier(self, stage):
			if stage == -6:
				return 0.33
			elif stage == -5:
				return 0.375
			elif stage == -4:
				return 0.428
			elif stage == -3:
				return 0.5
			elif stage == -2:
				return 0.6
			elif stage == -1:
				return 0.75
			elif stage >= 0:
				return 1 + 0.33333 * stage


	def screen_damage_modifier(self, targetPokemon):
		damageModifier = 1
		if physical in self.attackType and targetPokemon.is_reflect_screened():
			damageModifier = 0.5
		elif special in self.attackType and targetPokemon.is_light_screened():
			damageModifier = 0.5

		return damageModifier
		


	def calculate_damage(self, userPokemon, targetPokemon):
		messages = []

		if physical in self.attackType:
			userAttack = userPokemon.battleAttack
			targetDefense = targetPokemon.battleDefense
		elif special in self.attackType:
			userAttack = userPokemon.battleSpAttack
			targetDefense = targetPokemon.battleSpDefense

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

		if self.type == electric:
			chargeModifier = userPokemon.charge
			if chargeModifier == 2:
				userPokemon.charge = 1
		else:
			chargeModifier = 1

		modifier = chargeModifier * typeModifier * stab * burnModifier * crit * (randint(85,100)/100)

		damage = ((((2*userPokemon.level/5)+2) * self.power * userAttack/targetDefense)/50 + 2) * modifier
		damage *= self.screen_damage_modifier(targetPokemon)
		damage = int(damage)

		return damage, messages

	def check_protect(self, userPokemon, targetPokemon):
		messages = []
		protected = False
		if 'semiinvulnerable' in targetPokemon.battle_status_names() or 'protected' in targetPokemon.battle_status_names():
			protectStatus = []
			for status in targetPokemon.battleStatuses:
				if status.name in ['semiinvulnerable', 'protected']:
					protectStatus.append(status.check_attack(self.name))


			if False in protectStatus:
				messages.append('%s can\'t hit %s!' % (userPokemon.name, targetPokemon.name))
				protected = True

		return protected, messages

	def use(self, mixer, userPokemon, targetPokemon):
		messages = []
		damage = 0
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		self.pp -= 1
		
		
		protected, m = self.check_protect(userPokemon, targetPokemon)
		messages.extend(m)

		if userPokemon.lockedOn or self.accuracy == 0 or randint(1,100) < (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
			mixer.play_attack_sound(self.name)
			
			if not protected and (physical in self.attackType or special in self.attackType):
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
			if not protected and optStatModifier in self.attackType:
				if self.effectAccuracy == 0 or randint(1,100) < self.effectAccuracy:
					if self.stageModifier > 0:
						mixer.play_attack_sound('Stat Rise Up')
					else:
						mixer.play_attack_sound('Stat Fall Down')
					if 'all' in self.statsModified:
						messages.append(targetPokemon.modify_battle_stats(attack, self.stageModifier))
						messages.append(targetPokemon.modify_battle_stats(defense, self.stageModifier))
						messages.append(targetPokemon.modify_battle_stats(spAttack, self.stageModifier))
						messages.append(targetPokemon.modify_battle_stats(spDefense, self.stageModifier))
						messages.append(targetPokemon.modify_battle_stats(speed, self.stageModifier))
					else:
						for stat in self.statsModified:
							m = targetPokemon.modify_battle_stats(stat, self.stageModifier)
							messages.append(m)
				else:
					pass
			if selfStatModifier in self.attackType:
				if self.effectAccuracy == 0 or  randint(1,100) < self.effectAccuracy:
					if self.stageModifier > 0:
						mixer.play_attack_sound('Stat Rise Up')
					else:
						mixer.play_attack_sound('Stat Fall Down')
					if 'all' in self.statsModified:
						messages.append(userPokemon.modify_battle_stats(attack, self.stageModifier))
						messages.append(userPokemon.modify_battle_stats(defense, self.stageModifier))
						messages.append(userPokemon.modify_battle_stats(spAttack, self.stageModifier))
						messages.append(userPokemon.modify_battle_stats(spDefense, self.stageModifier))
						messages.append(userPokemon.modify_battle_stats(speed, self.stageModifier))
					else:
						for stat in self.statsModified:
							m = userPokemon.modify_battle_stats(stat, self.stageModifier)
							messages.append(m)
				else:
					pass
			if not protected and optConditionModifier in self.attackType:
				if self.effectAccuracy == 0 or randint(1,100) < self.effectAccuracy:
					afflicted = targetPokemon.afflict_status(self.condition)
					if afflicted:
						messages.append('%s is %s!' % (targetPokemon.name, self.condition.battleText))
						if self.condition.name in ['burn', 'confusion', 'freeze', 'paralysis', 'poison', 'badpoison', 'sleep']:
							mixer.play_attack_sound('Status_%s' % self.condition.sound)
					else:
						messages.append('%s cannot be %s!' % (targetPokemon.name, self.condition.battleText))
				else:
					pass
			if selfConditionModifier in self.attackType:
				if self.effectAccuracy == 0 or randint(1,100) < self.effectAccuracy:
					afflicted = userPokemon.afflict_status(self.condition)
					if afflicted:
						messages.append('%s is %s!' % (userPokemon.name, self.condition.battleText))
						if self.condition.name in ['burn', 'confusion', 'freeze', 'paralysis', 'poison', 'badpoison', 'sleep']:
							mixer.play_attack_sound('Status_%s' % self.condition.battleText.title())
					else:
						messages.append('%s cannot be %s' % (userPokemon.name, self.condition.battleText))
			if heal in self.attackType:
				if self.effectAccuracy == 0 or randint(1,100) < self.effectAccuracy:
					if self.healModifier > 1:
						healModifier = int((self.healModifier-1) * damage)
						mixer.play_attack_sound('Healing Attack')
					else:
						healModifier = self.healModifier
					userPokemon.heal(healModifier)
					messages.append('%s regained health!' % userPokemon.name)
			if suicide in self.attackType:
				userPokemon.faint()
				messages.append('%s fainted.' % userPokemon.name)

			if weather in self.attackType:
				messages.append('Weather not yet implemented.')

			if item in self.attackType:
				messages.append('Hold items not yet implemented.')
		
			if areaEffect in self.attackType:
				messages.append('Area attacks not yet implemented.')

			if partyEffect in self.attackType:
				messages.append('Party effects not yet implemented.')
		else:
			damage = 0
			messages.append('%s\'s attack missed.' % userPokemon.name)

			
		if userPokemon.lockedOn:
			userPokemon.lock_off()
			


		return damage, messages

	def select(self):
		selected = False
		messages = []
		if self.pp == 0:
			selected = False
			messages.append('No PP for this move!')
		elif self.disabled:
			selected = False
			messages.append('Disabled!')
		else:
			selected = True

		return selected, messages



class MultiAttack(Attack):

	def use(self, mixer, userPokemon, targetPokemon):
		if self.name in ['Twineedle', 'Bonemerang', 'Double Kick']:
			numberOfHits = 2
		else:
			numberOfHits = randint(2,5)
		totalDamage = 0
		messages = []
		messages.append('%s used %s!' % (userPokemon.name, self.name))

		

		if userPokemon.lockedOn or randint(1,100) < (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
			protected, m = self.check_protect(userPokemon, targetPokemon)
			messages.extend(m)
			if not protected:
				for i in range(numberOfHits):
					mixer.play_attack_sound('%s_1hit' % self.name)
					damage, m = self.calculate_damage(userPokemon, targetPokemon)
					totalDamage += damage
				messages.extend(m)
				messages.append('Hit %i times!' % numberOfHits)

		else:
			messages.append('%s\'s attack missed.' % userPokemon.name)

		if userPokemon.lockedOn:
			userPokemon.lock_off()

		return totalDamage, messages

class NoAttack(Attack):

	def __init__(self):
		self.name = '-'
		self.type = '-'
		pp = '-'
		super().__init__(pp, 0, 0)

	def use(self, mixer, userPokemon, targetPokemon):
		return 0, []

	def select(self):
		return False, []



