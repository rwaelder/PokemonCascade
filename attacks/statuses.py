from random import randint, choice
from pokemonTypes import *
from colors import *
# non-volitile statuses

class NoStatus():

	def __init__(self):
		self.displayText = ''
		self.displayColor = SILVER
		self.name = 'nostatus'
		self.statusType = 'non-volitile'
		self.battleText = 'healed'

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0

		return skipTurn, messages, damage

class RegPoison():

	def __init__(self):
		self.displayText = 'PSN'
		self.displayColor = PURPLE
		self.battleText = 'poisoned'
		self.sound = 'Poisoned'
		self.name = 'poison'
		self.statusType = 'non-volitile'


	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0
		if not isTurnEnd:
			pass
		else:
			damage = int(affectedPokemon.maxHp / 8)
			mixer.play_attack_sound('Status_%s' % self.sound)
			messages.append('%s is hurt by poison.' % affectedPokemon.name)

		return skipTurn, messages, damage

class BadPoison():

	def __init__(self):
		self.displayText = 'PSN'
		self.displayColor = PURPLE
		self.battleText = 'badly poisoned'
		self.sound = 'Poisoned'
		self.name = 'badpoison'
		self.turns = 1
		self.statusType = 'non-volitile'


	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0
		if not isTurnEnd:
			pass
		else:
			damage = int(self.turns * affectedPokemon.maxHp / 8)
			mixer.play_attack_sound('Status_%s' % self.sound)
			messages.append('%s is hurt by poison.' % affectedPokemon.name)
			self.turns += 1

		return skipTurn, messages, damage

class Burn():

	def __init__(self):
		self.displayText = 'BRN'
		self.displayColor = MAROON
		self.battleText = 'burned'
		self.sound = 'Burned'
		self.name = 'burn'
		self.statusType = 'non-volitile'


	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0
		if not isTurnEnd:
			pass
		else:
			damage = int(affectedPokemon.maxHp / 8)
			mixer.play_attack_sound('Status_%s' % self.sound)
			messages.append('%s is hurt by burn.' % affectedPokemon.name)

		return skipTurn, messages, damage

class Paralysis():

	def __init__(self):
		self.displayText = 'PAR'
		self.displayColor = GOLD
		self.battleText = 'paralyzed'
		self.sound = 'Paralyzed'
		self.name = 'paralysis'
		self.statusType = 'non-volitile'

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0
		if not isTurnEnd:
			messages.append('%s is paralyzed!' % affectedPokemon.name)
			if randint(1,100) < 25:
				skipTurn = True
				mixer.play_attack_sound('Status_%s' % self.sound)
				messages.append('%s is fully paralyzed!' % affectedPokemon.name)
		else:
			pass

		return skipTurn, messages, damage

class Freeze():

	def __init__(self):
		self.displayText = 'FRZ'
		self.displayColor = BLUE
		self.battleText = 'frozen'
		self.sound = 'Frozen'
		self.name = 'freeze'
		self.statusType = 'non-volitile'

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0
		if not isTurnEnd:
			if randint(1,100) < 20:
				skipTurn = False
				messages.append('%s thawed out!' % affectedPokemon.name)
				damage = -1
			else:
				skipTurn = True
				mixer.play_attack_sound('Status_%s' % self.sound)
				messages.append('%s is frozen solid!' % affectedPokemon.name)
		else:
			pass

		return skipTurn, messages, damage

class Sleep():

	def __init__(self, duration=randint(1,5)):
		self.displayText = 'SLP'
		self.displayColor = TEAL
		self.battleText = 'put to sleep'
		self.sound = 'Sleep'
		self.name = 'sleep'
		self.duration = duration
		self.turns = 0
		self.statusType = 'non-volitile'

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0
		if not isTurnEnd:
			if self.turns == self.duration:
				skipTurn = False
				messages.append('%s woke up!' % affectedPokemon.name)
				damage = -1
			else:
				skipTurn = True
				mixer.play_attack_sound('Status_%s' % self.sound)
				messages.append('%s is fast asleep!' % affectedPokemon.name)
				self.turns += 1
		else:
			pass

		return skipTurn, messages, damage


# volitile statuses

class Bound():

	def __init__(self, attackName, duration=randint(2,5)):
		self.attackName = attackName
		self.battleText = 'bound by %s' % self.attackName
		self.sound = '%s turn damage' % self.attackName
		self.name = 'bound'
		self.duration = duration
		self.turns = 0
		self.statusType = 'volitile'

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0

		if not isTurnEnd:
			pass

		elif self.turns == self.duration:
			messages.append('%s is free from %s!' % (affectedPokemon.name, self.attackName))
			damage = -1
		else:
			mixer.play_attack_sound('%s' % self.sound)
			messages.append('%s is hurt by %s!' % (affectedPokemon.name, self.attackName))
			damage = int(affectedPokemon.maxHp / 16)
			self.turns += 1

		return skipTurn, messages, damage

class CantEscape():

	def __init__(self):
		self.battleText = 'trapped'
		self.name = 'cantescape'
		self.statusType = 'volitile'

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0

		return skipTurn, messages, damage

class ConfusionStatus():
	def __init__(self):
		self.battleText = 'confused'
		self.sound = 'Confused'
		self.name = 'confusion'
		self.statusType = 'volitile'

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0

		if not isTurnEnd:
			messages.append('%s is confused.' % affectedPokemon.name)
			mixer.play_attack_sound('Status_%s' % self.sound)
			if 50 < randint(1,100):
				mixer.play_attack_sound('Damage')
				messages.append('%s hurt itself in its confusion.' % affectedPokemon.name)
				damage = int(((((2*affectedPokemon.level/5)+2) * 40 * affectedPokemon.attack/affectedPokemon.defense)/50 + 2))
				skipTurn = True

		return skipTurn, messages, damage

class Cursed():
	def __init__(self):
		self.battleText = 'cursed'
		self.sound = 'Curse'
		self.name = 'cursed'
		self.statusType = 'volitile'


	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0
		if not isTurnEnd:
			pass
		else:
			mixer.play_attack_sound('Status_%s' % self.sound)
			damage = int(affectedPokemon.maxHp / 4)
			messages.append('%s is haunted by curse!.' % affectedPokemon.name)

		return skipTurn, messages, damage

class Infatuation():

	def __init__(self):
		self.battleText = 'infatuated'
		self.sound = 'Charm'
		self.name = 'infatuation'
		self.statusType = 'volitile'

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0

		if not isTurnEnd:
			messages.append('%s is infatuated!' % affectedPokemon.name)
			mixer.play_attack_sound('Status_%s' % self.sound)
			if randint(1,100) < 50:
				skipTurn = True
				messages.append('%s is immobilized by love!' % affectedPokemon.name)

		return skipTurn, messages, damage

class LeechSeedStatus():

	def __init__(self):
		self.battleText = 'seeded'
		self.sound = 'Leech Seed turn damage'
		self.name = 'leechseed'
		self.statusType = 'volitile'

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0

		if not isTurnEnd:
			pass
		else:
			mixer.play_attack_sound('Status_%s' % self.sound)
			damage = int(affectedPokemon.maxHp / 8)
			messages.append('%s is sapped by Leech Seed!' % affectedPokemon.name)

		return skipTurn, messages, damage

class LightScreened():
	def __init__(self):
		self.battleText = 'protected'
		self.name = 'lightscreened'
		self.statusType = 'volitile'
		self.turnNumber = 0
		self.duration = 4

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0

		if not isTurnEnd:
			pass
		else:
			self.turnNumber += 1

			if self.turnNumber == self.duration:
				damage = -1
				messages.append('%s\'s Light Screen wore off!' % affectedPokemon.name)
			

		return skipTurn, messages, damage

class NightmareStatus():

	def __init__(self):
		self.battleText = 'haunted by nightmares'
		self.sound = 'Nightmare'
		self.name = 'nightmare'
		self.statusType = 'volitile'

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0

		if not affectedPokemon.isAsleep():
			damage = -1
			return skipTurn, messages, damage

		if not isTurnEnd:
			pass
		else:
			mixer.play_attack_sound('Status_%s' % self.sound)
			messages.append('%s is haunted by nightmares!' % affectedPokemon.name)
			damage = int(affectedPokemon.maxHp / 4)
			self.turns += 1

		return skipTurn, messages, damage

class ReflectScreened():
	def __init__(self):
		self.battleText = 'protected'
		self.name = 'reflectscreened'
		self.statusType = 'volitile'
		self.turnNumber = 0
		self.duration = 4

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0

		if not isTurnEnd:
			pass
		else:
			self.turnNumber += 1

			if self.turnNumber == self.duration:
				damage = -1
				messages.append('%s\'s Reflect wore off!' % affectedPokemon.name)
			

		return skipTurn, messages, damage

class ReType():

	def __init__(self, targetType=choice(typeList)):
		self.battleText = 'now %s type' % targetType
		self.statusType = 'volitile'
		self.name = 'retype'
		self.targetType = targetType

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0

		if not isTurnEnd:
			affectedPokemon.re_type(self.targetType)
		else:
			pass
		return skipTurn, messages, damage

class TypeResistance():

	def __init__(self, typeResist):
		self.battleText = 'now %s resistant' % typeResist
		self.name = '%sresist' % typeResist
		self.statusType = 'volitile'
		self.typeResist = typeResist
		self.inEffect = False
		if self.typeResist == fire:
			self.resistType = water
		elif self.typeResist == electric:
			self.resistType = ground


	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0

		if not isTurnEnd and not self.inEffect:
			affectedPokemon.type.append(self.resistType)
			self.inEffect = True
		
		return skipTurn, messages, damage


# battle volitile statuses

class BideCondition():

	def __init__(self):
		self.battleText = 'storing energy'
		self.name = 'bide'
		self.turnNumber = 0
		self.totalDamage = 0
		self.turnHP = 0
		self.statusType = 'battle'

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = True
		messages = []
		damage = 0

		if not isTurnEnd and self.turnNumber < 2:
			self.turnHP = affectedPokemon.hp
			messages.append('%s is storing energy!' % affectedPokemon.name)
		elif turnNumber == 2:
			skipTurn = True
			messages.append('%s unleashed energy!' % affectedPokemon.name)
			# affectedPokemon.
		else:
			damage = self.turnHP - affectedPokemon.hp
			self.totalDamage += 2 * damage
			damage = 0
			self.turnNumber += 1

		return skipTurn, messages, damage

class Disabled():
	def __init__(self, attackNumber):
		self.battleText = 'disabled'
		self.name = 'disabled'
		self.statusType = 'battle'
		self.attackNumber = attackNumber
		self.duration = randint(2,5)
		self.turnNumber = 0


	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0

		if not isTurnEnd:
			affectedPokemon.attacks[self.attackNumber].disable()

		else:
			if self.turnNumber == self.duration:
				affectedPokemon.attacks[self.attackNumber].enable()
				self.turnNumber = 0
			else:
				self.turnNumber += 1

		return skipTurn, messages, damage

class EncoreStatus():
	def __init__(self):
		self.battleText = 'encore'
		self.name = 'encore'
		self.statusType = 'battle'
		self.turnHP = 0

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0
		if self.turnHP == 0:
			self.turnHP = affectedPokemon.hp

		if not isTurnEnd:
			self.turnHP = affectedPokemon.hp

		else:
			if self.turnHP > affectedPokemon.hp:
				messages.append(affectedPokemon.modify_battle_stats('attack', 1))

		return skipTurn, messages, damage

class Enraged():
	def __init__(self):
		self.battleText = 'enraged'
		self.sound = 'Stat Rise Up'
		self.name = 'enraged'
		self.statusType = 'battle'
		self.turnHP = 0

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0
		if self.turnHP == 0:
			self.turnHP = affectedPokemon.hp

		if not isTurnEnd:
			self.turnHP = affectedPokemon.hp

		else:
			if self.turnHP > affectedPokemon.hp:
				mixer.play_attack_sound('Status_%s' % self.sound)
				messages.append(affectedPokemon.modify_battle_stats('attack', 1))

		return skipTurn, messages, damage

class Flinch():
	def __init__(self):
		self.battleText = 'flinching'
		self.name = 'flinch'
		self.statusType = 'battle'

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0

		if not isTurnEnd:
			skipTurn = True
			messages.append('%s is flinching!' % affectedPokemon.name)

		else:
			skipTurn = False
			damage = -1
		return skipTurn, messages, damage

class FuryCutterUsed():
	def __init__(self):
		self.battleText = 'building power'
		self.name = 'furycutter'
		self.statusType = 'battle'

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		return False, [], 0

class Ingrained():

	def __init__(self):
		self.battleText = 'rooted'
		self.sound = 'Ingrain turn heal'
		self.name = 'ingrained'
		self.statusType = 'volitile'

	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0

		if not isTurnEnd:
			pass
		else:
			mixer.play_attack_sound('Status_%s' % self.sound)
			affectedPokemon.heal(1/16)
			messages.append('%s is restored by roots!' % affectedPokemon.name)

		return skipTurn, messages, damage

class Protected():

	def __init__(self):
		self.battleText = 'protected'
		self.name = 'protected'
		self.duration = 2
		self.turnNumber = 0
		self.statusType = 'battle'

	def handle(self, mixer, affectedPokemon, isTurnEnd):
	
		skipTurn = False
		messages = []
		damage = 0

		if self.duration == self.turnNumber:
			damage = -1
			skipTurn = False

		elif isTurnEnd:
			self.turnNumber += 1

		return skipTurn, messages, damage

	def check_attack(self, attackName):
		if self.turnNumber == 0:
			return False
		else:
			return True

class Recharge():

	def __init__(self):
		self.battleText = 'recharging'
		self.name = 'recharge'
		self.turnNumber = 0
		self.duration = 1
		self.statusType = 'battle'


	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = True
		messages = []
		damage = 0

		if self.duration == self.turnNumber:
			damage = -1
			skipTurn = False
			self.turnNumber = 0

		elif not isTurnEnd and self.turnNumber < 1:
			skipTurn = True
			messages.append('%s is recharging' % affectedPokemon.name)

		elif isTurnEnd:
			self.turnNumber += 1

		return skipTurn, messages, damage

class SemiInvulnerable():

	def __init__(self, causeAttack):
		self.causeAttack = causeAttack
		if causeAttack == 'Dive':
			self.battleText = 'deep underwater'
		elif causeAttack == 'Dig':
			self.battleText = 'deep underground'
		elif causeAttack in ['Fly', 'Bounce']:
			self.battleText = 'high in the sky'

		self.name = 'semiinvulnerable'
		self.duration = 1
		self.turnNumber = 0
		self.statusType = 'battle'

	def handle(self, mixer, affectedPokemon, isTurnEnd):
	
		skipTurn = True
		messages = []
		damage = 0

		if self.duration == self.turnNumber:
			damage = -1
			skipTurn = False

		elif not isTurnEnd and self.turnNumber < 1:
			skipTurn = True

		elif isTurnEnd:
			self.turnNumber += 1

		return skipTurn, messages, damage

	def check_attack(self, attackName):
		if self.causeAttack == 'Dive':
			if attackName in ['Surf', 'Whirlpool']:
				return True
		elif self.causeAttack == 'Dig':
			if attackName in ['Earthquake', 'Magnitude', 'Fissure']:
				return True
		else:
			if attackName in ['Gust', 'Smack Down', 'Sky Uppercut', 'Thunder', 'Twister', 'Hurricane']:
				return True

		return False

class Taunted():
	def __init__(self):
		self.battleText = 'taunted'
		self.name = 'taunted'
		self.statusType = 'battle'

	def handle(self, affectedPokemon, attack, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0
		if attack == None:
			pass
		elif not isTurnEnd and ('physical' in affectedPokemon.attacks[attack].attackType or 'special' in affectedPokemon.attacks[attack].attackType):
			skipTurn = False
		elif not isTurnEnd:
			skipTurn = True
			messages.append('%s can only attack while taunted.' % affectedPokemon.name)
		else:
			pass

		return skipTurn, messages, damage
		
class Tormented():
	def __init__(self):
		self.battleText = 'tormented'
		self.name = 'tormented'
		self.lastAttack = ''
		self.statusType = 'battle'

	def handle(self, affectedPokemon, attack, isTurnEnd):
		skipTurn = False
		messages = []
		damage = 0
		attackName = affectedPokemon.attacks[attack].name

		if attack == None:
			pass
		elif not isTurnEnd:
			if self.lastAttack != attackName:
				self.lastAttack = attackName
			else:
				skipTurn = True
				messages.append('%s can\'t use move succesively.')
		
		return skipTurn, messages, damage

class Yawning():
	def __init__(self):
		self.battleText = 'drowsy'
		self.sound = 'Status Sleep'
		self.name = 'yawning'
		self.turnNumber = 0
		self.duration = 1
		self.statusType = 'battle'


	def handle(self, mixer, affectedPokemon, isTurnEnd):
		skipTurn = True
		messages = []
		damage = 0

		if self.duration == self.turnNumber and isTurnEnd:
			damage = -1
			skipTurn = False
			affectedPokemon.afflict_status(Sleep())
			mixer.play_attack_sound('Status_%s' % self.sound)
			self.turnNumber = 0
			messages.append('%s fell asleep!' % affectedPokemon.name)


		elif not isTurnEnd and self.turnNumber < 1:
			skipTurn = True
			messages.append('%s is recharging' % affectedPokemon.name)

		elif isTurnEnd:
			self.turnNumber += 1

		return skipTurn, messages, damage

