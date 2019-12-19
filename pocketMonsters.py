from random import randint
from pokemonTypes import *
import sys
sys.path.append('attacks/')


from statuses import NoStatus
from expTable import level_exp, exp_to_next_level
from colors import LIME, YELLOW, RED

class Pokemon():

	def __init__(self, pocketMonster, level=1):

		self.pocketMonster = pocketMonster.__class__()

		self.image = self.pocketMonster.image
		self.name = self.pocketMonster.name
		self.type = self.pocketMonster.type
		self.number = self.pocketMonster.number


		self.hpIV = randint(0,15)
		self.attackIV = randint(0,15)
		self.defenseIV = randint(0,15)
		self.spAttackIV = randint(0,15)
		self.spDefenseIV = randint(0,15)
		self.speedIV = randint(0,15)

		self.hpEV = 0
		self.attackEV = 0
		self.defenseEV = 0
		self.spAttackEV = 0
		self.spDefenseEV = 0
		self.speedEV = 0


		self.attackStage = 0
		self.defenseStage = 0
		self.spAttackStage = 0
		self.spDefenseStage = 0
		self.speedStage = 0
		self.accuracyStage = 0
		self.evasivenessStage = 0
		self.critStage = 0


		self.status = NoStatus()
		self.volitileStatuses = []
		self.battleStatuses = []
		self.keepUsingAttack = False
		self.continueAttackNumber = 0
		self.charge = 1
		self.stockpile = 0
		self.lockedOn = False
		self.uproar = False
		self.enduring = False
		self.transformed = False

		self.level = 1
		self.calculate_stats()
		self.hp = self.maxHp

		
		self.attacks = self.pocketMonster.get_new_attacks([], self.level)
		self.fainted = False

		self.totalExpPoints = 0
		self.set_level(level)

		self.levelUpExp = exp_to_next_level(self.level, self.pocketMonster.expGroup)

		# if randint(0, 4095) == 3114:
		# if randint(0, 255) == 128:
		if randint(0, 15) == 8:
			self.shiny = True
		else:
			self.shiny = False

		self.gender = self.pocketMonster.gender()

	def transform(self, targetPokemon):
		self.originalAttacks = self.attacks
		self.originalForm = self.pocketMonster

		self.pocketMonster = targetPokemon.pocketMonster
		self.attacks = targetPokemon.attacks
		self.image = self.pocketMonster.image
		self.type = self.pocketMonster.type
		self.number = self.pocketMonster.number
		self.transformed = True

	def un_transform(self):
		if self.transformed:
			self.pocketMonster = self.originalForm
			self.attacks = self.originalAttacks
			self.image = self.pocketMonster.image
			self.type = self.pocketMonster.type
			self.number = self.pocketMonster.number
			self.transformed = False

	def endure(self):
		self.enduring = True

	def lock_on(self):
		self.lockedOn = True

	def lock_off(self):
		self.lockedOn = False

	def exp_bar_length(self):
		if self.level == 100:
			return 0
		levelExp = self.totalExpPoints - level_exp(self.level, self.pocketMonster.expGroup)
		levelUpExp = exp_to_next_level(self.level, self.pocketMonster.expGroup)

		return levelExp / levelUpExp

	def hp_bar(self):
		hpPct = self.hp / self.maxHp

		if hpPct > 0.5:
			color = LIME
		elif hpPct > 0.20:
			color = YELLOW
		else:
			color = RED

		return hpPct, color

	def gain_exp(self, exp, evolve=True):
		messages = []
		self.totalExpPoints += exp
		messages.append('%s gained %i exp!' % (self.name, exp))
		while True:
			if self.level == 100:
				break
			elif self.totalExpPoints >= level_exp(self.level, self.pocketMonster.expGroup) + exp_to_next_level(self.level, self.pocketMonster.expGroup):
				messages.append('%s grew to level %i!' % (self.name, self.level))
				self.level_up(evolve=evolve)
			else:
				break

		return messages

	def select(self):
		selected = True
		messages = []

		if self.hp == 0:
			selected = False
			messages.append('%s has no will to fight!' % self.name)

		return selected, messages

	def has_status():
		if self.status.name == 'nostatus':
			return False
		else:
			return True

	def keep_using_attack(self, attack):
		self.keepUsingAttack = True
		for i in range(len(self.attacks)):
			if self.attacks[i].name == attack.name:
				self.continueAttackNumber = i

	def stop_using_attack(self):
		self.keepUsingAttack = False

	def faint(self):
		self.hp = 0
		self.fainted = True
		self.un_transform()

	def isFainted(self):
		return self.fainted

	def re_type(self, targetType):
		self.type = targetType

	def heal(self, healAmount):
		if healAmount <= 1:
			recoveredHp = int(healAmount * self.maxHp)
		else:
			recoveredHp = healAmount

		if self.hp + recoveredHp > self.maxHp:
			self.hp = self.maxHp
		else:
			self.hp += recoveredHp

	def isBurned(self):
		if self.status.name == 'burn':
			return True
		else:
			return False

	def isParalyzed(self):
		if self.status.name == 'paralysis':
			return True
		else:
			return False

	def isAsleep(self):
		if self.status.name == 'sleep':
			return True
		else:
			return False

	def is_light_screened(self):
		for status in self.volitileStatuses:
			if status.name == 'lightscreened':
				return True
		return False

	def is_reflect_screened(self):
		for status in self.volitileStatuses:
			if status.name == 'reflectscreened':
				return True
		return False

	def remove_walls(self):
		messages = []
		if 'reflectscreened' in self.volitile_status_names():
			messages.append('%s\'s Reflect broken!' % self.name)
			self.remove_volitile_status('reflectscreened')
		if 'lightscreened' in self.volitile_status_names():
			messages.append('%s\'s Light Screen broken!' % self.name)
			self.remove_volitile_status('lightscreened')

		return messages


	def afflict_status(self, status):
		if status.statusType == 'volitile':
			return self.afflict_volitile_status(status)
		elif status.statusType == 'battle':
			return self.afflict_battle_status(status)
		else:


			if self.status.name != 'nostatus':
				afflicted = False
			elif status.name == self.status.name:
				afflicted = False
			elif status.name == 'burn' and fire in self.type:
				afflicted = False
			elif 'poison' in status.name and poison in self.type:
				afflicted = False
			elif status.name == 'frozen' and ice in self.type:
				afflicted = False
			elif status.name == 'paralysis' and electric in self.type:
				afflicted = False
			else:
				if status.name == 'sleep' and not self.uproar:
					self.status = status.__class__(status.duration)
				else:
					self.status = status.__class__()
				afflicted = True

		return afflicted

	def afflict_volitile_status(self, status):
		messages = []
		afflicted = True

		if status.name == 'nightmare':
			if not self.isAsleep():
				afflicted = False

		for condition in self.volitileStatuses:
			if status.name == condition.name:
				afflicted = False
				break

		if afflicted:
			if status.name == 'bound':
				self.volitileStatuses.append(status.__class__(status.attackName, duration=status.duration))
			elif status.name == 'retype':
				self.volitileStatuses.append(status.__class__(targetType=status.targetType))
			elif 'resist' in status.name:
				self.volitileStatuses.append(status.__class__(status.typeResist))
			else:
				self.volitileStatuses.append(status.__class__())

		return afflicted

	def afflict_battle_status(self, status):
		messages = []
		afflicted = True

		if status.name == 'protected':
			afflicted = True
		else:
			for condition in self.battleStatuses:
				if status.name == condition.name:
					afflicted = False
					break

		if afflicted:
			if status.name == 'semiinvulnerable':
				self.battleStatuses.append(status.__class__(status.causeAttack))
			elif status.name == 'disabled':
				self.battleStatuses.append(status.__class__(status.attackNumber))
			else:
				self.battleStatuses.append(status.__class__())

		return afflicted

	def status_name(self):
		return self.status.name

	def volitile_status_names(self):
		names = []
		for volitileStatus in self.volitileStatuses:
			names.append(volitileStatus.name)

		return names

	def battle_status_names(self):
		names = []
		for battleStatus in self.battleStatuses:
			names.append(battleStatus.name)

		return names

	def heal_status(self):
		self.status = NoStatus()

	def remove_volitile_status(self, statusName):
		for i in range(len(self.volitileStatuses)):
			if self.volitileStatuses[i].name == statusName:
				self.volitileStatuses.pop(i)
				break

	def remove_battle_status(self, statusName):
		for i in range(len(self.battleStatuses)):
			if self.battleStatuses[i].name == statusName:
				self.battleStatuses.pop(i)
				break

	def handle_status(self, mixer, attack, isTurnEnd):
		skipTurn = []
		messages = []
		totalDamage = 0

		skip, message, damage = self.status.handle(mixer, self, isTurnEnd)
		skipTurn.append(skip)
		messages.extend(message)
		if damage == -1:
			self.heal_status()
			damage = 0
		totalDamage += damage

		if not skip:

			removeStatuses = []
			for volitileStatus in self.volitileStatuses:
				skip, message, damage = volitileStatus.handle(mixer, self, isTurnEnd)
				skipTurn.append(skip)
				messages.extend(message)
				if damage == -1:
					removeStatuses.append(volitileStatus.name)
					damage = 0
				totalDamage += damage

			for statusName in removeStatuses:
				self.remove_volitile_status(statusName)

			removeStatuses = []
			for battleStatus in self.battleStatuses:
				if battleStatus.name in ['taunted', 'tormented']:
					skip, message, damage = battleStatus.handle(self, attack, isTurnEnd)
				else:
					skip, message, damage = battleStatus.handle(self, attack, isTurnEnd)
				skipTurn.append(skip)
				messages.extend(message)
				if damage < 0:
					removeStatuses.append(battleStatus.name)
					damage = 0
				totalDamage += damage

			for statusName in removeStatuses:
				self.remove_battle_status(statusName)


		if True in skipTurn:
			skip = True
		else:
			skip = False

		if skip:
			self.stop_using_attack()

		return skip, messages, totalDamage

	def modify_battle_stats(self, stat, stageModifier):
		message = ''
		if stat == 'attack':
			if self.attackStage == 6:
				message = '%s\'s attack can\'t go higher!' % self.name
			elif self.attackStage == -6:
				message = '%s\'s attack can\'t go lower!' % self.name
			else:
				self.attackStage += stageModifier
				if stageModifier > 0:
					message = '%s\'s attack increased!' % self.name
				else:
					message = '%s\'s attack decreased!' % self.name
		elif stat == 'defense':
			if self.defenseStage == 6:
				message = '%s\'s defense can\'t go higher!' % self.name
			elif self.defenseStage == -6:
				message = '%s\'s defense can\'t go lower!' % self.name
			else:
				self.defenseStage += stageModifier
				if stageModifier > 0:
					message = '%s\'s defense increased!' % self.name
				else:
					message = '%s\'s defense decreased!' % self.name
		elif stat == 'spAttack':
			if self.spAttackStage == 6:
				message = '%s\'s special attack can\'t go higher!' % self.name
			elif self.spAttackStage == -6:
				message = '%s\'s special attack can\'t go lower!' % self.name
			else:
				self.spAttackStage += stageModifier
				if stageModifier > 0:
					message = '%s\'s special attack increased!' % self.name
				else:
					message = '%s\'s special attack decreased!' % self.name	
		elif stat == 'spDefense':
			if self.spDefenseStage == 6:
				message = '%s\'s special defense can\'t go higher!' % self.name
			elif self.spDefenseStage == -6:
				message = '%s\'s special defense can\'t go lower!' % self.name
			else:
				self.spDefenseStage += stageModifier
				if stageModifier > 0:
					message = '%s\'s special defense increased!' % self.name
				else:
					message = '%s\'s special defense decreased!' % self.name
		elif stat == 'speed':
			if self.speedStage == 6:
				message = '%s\'s speed can\'t go higher!' % self.name
			elif self.speedStage == -6:
				message = '%s\'s speed can\'t go lower!' % self.name
			else:
				self.speedStage += stageModifier
				if stageModifier > 0:
					message = '%s\'s speed increased!' % self.name
				else:
					message = '%s\'s speed decreased!' % self.name

		elif stat == 'accuracy':
			if self.accuracyStage == 6:
				message = '%s\'s accuracy can\'t go higher!' % self.name
			elif self.accuracyStage == -6:
				message = '%s\'s accuracy can\'t go lower!' % self.name
			else:
				self.accuracyStage += stageModifier
				if stageModifier > 0:
					message = '%s\'s accuracy increased!' % self.name
				else:
					message = '%s\'s accuracy decreased!' % self.name

		elif stat == 'evasiveness':
			if self.evasivenessStage == 6:
				message = '%s\'s evasiveness can\'t go higher!' % self.name
			elif self.evasivenessStage == -6:
				message = '%s\'s evasiveness can\'t go lower!' % self.name
			else:
				self.evasivenessStage += stageModifier
				if stageModifier > 0:
					message = '%s\'s evasiveness increased!' % self.name
				else:
					message = '%s\'s evasiveness decreased!' % self.name

		elif stat == 'critStage':
			if self.critStage == 6:
				message = '%s\'s focus can\'t go higher!' % self.name
			elif self.critStage == -6:
				message = '%s\'s focus can\'t go lower!' % self.name
			else:
				self.critStage += stageModifier
				if stageModifier > 0:
					message = '%s is tightening its focus!' % self.name
				else:
					message = '%s lost its focus!' % self.name

		if ('increased' in message or 'decreased' in message) and abs(stageModifier) == 2:
			message = message.replace('increased', 'sharply increased')
			message = message.replace('decreased', 'sharply decreased')


		self.calculate_battle_stats()
		return message	


	def get_stat_modifier(self, stage):
		if stage == 0:
			return 1

		elif stage == -6:
			return 0.25
		elif stage == -5:
			return 0.285
		elif stage == -4:
			return 0.33
		elif stage == -3:
			return 0.4
		elif stage == -2:
			return 0.5
		elif stage == -1:
			return 0.6
		elif stage > 0:
			return 1 + 0.5 * stage

	def take_damage(self, damage):
		if damage >= self.hp:
			if self.enduring:
				self.hp = 1
			else:
				self.faint()
		else:
			self.hp -= damage

		if self.enduring:
			self.enduring = False


	def calculate_battle_stats(self):
		self.battleAttack = self.get_stat_modifier(self.attackStage) * self.attack
		self.battleDefense = self.get_stat_modifier(self.defenseStage) * self.defense
		self.battleSpAttack = self.get_stat_modifier(self.spAttackStage) * self.spAttack
		self.battleSpDefense = self.get_stat_modifier(self.spDefenseStage) * self.spDefense
		self.battleSpeed = self.get_stat_modifier(self.speedStage) * self.speed


	def reset_battle_stats(self, inBattle=False):
		self.attackStage = 0
		self.defenseStage = 0
		self.spAttackStage = 0
		self.spDefenseStage = 0
		self.speedStage = 0
		self.accuracyStage = 0
		self.evasivenessStage = 0
		self.critStage = 0

		self.calculate_battle_stats()
		
		if not inBattle:
			self.type = self.pocketMonster.type

			self.volitileStatuses = []
			self.battleStatuses = []
			self.keepUsingAttack = False
			self.charge = 1
			self.stockpile = 0
			self.lockedOn = False
			self.uproar = False
			self.enduring = False
			self.transformed = False



	def evolve(self):
		self.pocketMonster = self.pocketMonster.evolve().__class__()
		formerMaxHp = self.maxHp
		self.calculate_stats()
		self.hp += self.maxHp - formerMaxHp
		self.image = self.pocketMonster.image
		self.name = self.pocketMonster.name
		self.type = self.pocketMonster.type
		self.number = self.pocketMonster.number
		self.attacks = self.pocketMonster.get_new_attacks(self.attacks, self.level)

	def set_level(self, targetLevel):
		self.gain_exp(level_exp(targetLevel, self.pocketMonster.expGroup), evolve=False)

	def level_up(self, evolve=True):
		if self.level == 100:
			pass
		else:
			self.level += 1
			formerMaxHp = self.maxHp
			self.calculate_stats()
			self.hp += self.maxHp - formerMaxHp
			self.attacks = self.pocketMonster.get_new_attacks(self.attacks, self.level)
			if self.level == self.pocketMonster.evolvesAt and evolve:
				self.evolve()


	def calculate_stats(self):
		nature = 1
		
		self.maxHp = int(((self.hpIV + 2*self.pocketMonster.baseHp + (self.hpEV/4))* (self.level/100)) + 10 + self.level)
		self.attack = int((((self.attackIV + 2*self.pocketMonster.baseAttack + (self.attackEV/4))* (self.level/100)) + 5) * nature)
		self.defense = int((((self.defenseIV + 2*self.pocketMonster.baseDefense + (self.defenseEV/4))* (self.level/100)) + 5) * nature)
		self.spAttack = int((((self.spAttackIV + 2*self.pocketMonster.baseSpAttack + (self.spAttackEV/4))* (self.level/100)) + 5) * nature)
		self.spDefense = int((((self.spDefenseIV + 2*self.pocketMonster.baseSpDefense + (self.spDefenseEV/4))* (self.level/100)) + 5) * nature)
		self.speed = int((((self.speedIV + 2*self.pocketMonster.baseSpeed + (self.speedEV/4))* (self.level/100)) + 5) * nature)

	def class_type(self):
		return 'pokemon'

class PocketMonster():
	def __init__(self, hp, attack, defense, spAttack, spDefense, speed):
		self.baseHp = hp
		self.baseAttack = speed
		self.baseDefense = defense
		self.baseSpAttack = spAttack
		self.baseSpDefense = spDefense
		self.baseSpeed = speed

		self.evolvesAt = 102

		self.shiny = False
		self.femaleRate = -1

	def gender(self):
		if self.femaleRate == -1:
			return ''
		else:
			if randint(1,100) < self.femaleRate:
				return 'f'
			else:
				return 'm'

	def import_moves(self, attacks):
		self.attacks = attacks

	def get_new_attacks(self, attacks, level):
		if level in self.levelUpAttacks and len(attacks) < 4:
			attacks.append(self.levelUpAttacks[level].__class__())
		elif level in self.levelUpAttacks:
			attacks[randint(0,3)] = self.levelUpAttacks[level].__class__()
		
		return attacks

	def class_type(self):
		return 'pocketMonster'
