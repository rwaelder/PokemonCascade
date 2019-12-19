from pokemonTypes import normal, ghost
from attack import Attack, MultiAttack
from statuses import *
from random import randint, choice
from typeMatchup import get_type_modifier
from attackKeywords import *


# DOUBLE BATTLE MOVE
# class Assist(Attack):
# 	def __init__(self):
# 		self.name = 'Assist'
# 		self.type = normal
# 		self.attackType = [other]
# 		self.

class Attract(Attack):
	def __init__(self):
		self.name = 'Attract'
		self.type = normal
		self.attackType = [conditionModifier]
		self.condition = Infatuation()
		self.effectAccuracy = 0
		self.description = 'Makes the opponent less likely to attack.'
		
		power = 0
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class Barrage(MultiAttack):
	def __init__(self):
		self.name = 'Barrage'
		self.type = normal
		self.attackType = [special]
		self.description = 'Hurls round objects at the foe 2 to 5 times.'

		power = 15
		accuracy = 85
		pp = 20
		super().__init__(pp, power, accuracy)

class BatonPass(Attack):
	def __init__(self):
		self.name = 'Baton Pass'
		self.type = normal
		self.attackType = [partyEffect]
		self.description = 'Switches out the user while keeping effects in play.'

		power = 0
		accuracy = 0
		pp = 40
		super().__init__(pp, power, accuracy)

		# TODO: define use function

class BellyDrum(Attack):
	def __init__(self):
		self.name = 'Belly Drum'
		self.type = normal
		self.attackType = [selfStatModifier]
		self.statsModified = [attack]
		self.description = 'Maximizes attack while sacrificing HP.'

		power = 0
		accuracy = 0
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		self.pp -= 1

		damage = int(userPokemon.maxHp / 2)
		userPokemon.hp -= damage
		damage = 0
		messages = []
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		mixer.play_attack_sound(self.name)
		userPokemon.attackStage = 6
		messages.append('%s\'s attack is maxed out!' % userPokemon.name)
		mixer.play_attack_sound('Stat Rise Up')

		return damage, messages

class Bide(Attack):
	def __init__(self):
		self.name = 'Bide'
		self.type = normal
		self.attackType = [physical]


		power = 1
		accuracy = 100
		pp = 10

		super().__init__(pp, power, accuracy)


	def use(self, mixer, userPokemon, targetPokemon):
		if self.turnNumber == 0:
			self.pp -= 1
			messages.append('%s used %s!' % (userPokemon.name, self.name))

		if not userPokemon.keepUsingAttack:
			userPokemon.keep_using_attack(self)

		damage = 0
		messages = []

		if self.turnNumber == 0:
			m = userPokemon.afflict_status(self.condition)
			mixer.play_attack_sound(self.name)
			self.turnNumber += 1
			self.startHP = userPokemon.hp
					

		if self.turnNumber == 2:
			userPokemon.stop_using_attack()
			if userPokemon.lockedOn or randint(1,100) < (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
				mixer.play_attack_sound(self.name)
				protected, m = self.check_protect(userPokemon, targetPokemon)
				if 'Super effective!' in m:
					mixer.play_sound('Super Effective')
				elif 'Not very effective...' in m:
					mixer.play_sound('Not Very Effective')
				elif 'Doesn\'t affect %s.' % targetPokemon.name in m:
					pass
				else:
					mixer.play_sound('Damage')
				messages.extend(m)
				if not protected:
					damage = 2 * (self.startHP - userPokemon.hp)

			else:
				damage = 0
				messages.append('%s\'s attack missed.' % userPokemon.name)
			self.turnNumber = 0

			if userPokemon.lockedOn:
				userPokemon.lock_off()

		return damage, messages

class Bind(Attack):
	def __init__(self):
		self.name = 'Bind'
		self.type = normal
		self.attackType = [physical, selfConditionModifier]
		self.condition = Bound(self.name)
		self.description = 'Binds and squeezed the foe for 2 to 5 turns.'

		power = 15
		accuracy = 75
		pp = 20
		super().__init__(pp, power, accuracy)

class Block(Attack):
	def __init__(self):
		self.name = 'Block'
		self.type = normal
		self.attackType = [optConditionModifier]
		self.condition = CantEscape()
		self.effectAccuracy = 0
		self.description = 'Blocks the foe\'s way to prevent escape.'

		power = 0
		accuracy = 100
		pp = 5
		super().__init__(pp, power, accuracy)

class BodySlam(Attack):
	def __init__(self):
		self.name = 'Body Slam'
		self.type = normal
		self.attackType = [physical, optConditionModifier]
		self.condition = Paralysis()
		self.effectAccuracy = 30
		self.description = 'A full-body slam that may cause paralysis.'

		power = 85
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class Camouflage(Attack):
	def __init__(self):
		self.name = 'Camouflage'
		self.type = normal
		self.attackType = [selfConditionModifier]
		self.condition = ReType()
		self.effectAccuracy = 0
		self.description = 'Changes user\'s type depending on location.'

		power = 0
		accuracy = 100
		pp =20
		super().__init__(pp, power, accuracy)

class Charm(Attack):
	def __init__(self):
		self.name = 'Charm'
		self.type = normal
		self.attackType = [optStatModifier]
		self.statsModified = [attack]
		self.stageModifier = -2
		self.effectAccuracy = 0
		self.description = 'Charms the for to sharply reduce attack.'

		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class CometPunch(MultiAttack):
	def __init__(self):
		self.name = 'Comet Punch'
		self.type = normal
		self.attackType = [physical]
		self.description = 'Repeatedly punches the foe 2 to 5 times.'

		power = 18
		accuracy = 85
		pp = 15
		super().__init__(pp, power, accuracy)

class Constrict(Attack):
	def __init__(self):
		self.name = 'Constrict'
		self.type = normal
		self.attackType = [physical, optStatModifier]
		self.statsModified = [speed]
		self.stageModifier = -1
		self.effectAccuracy = 10
		self.description = 'Constricts to inflict pain. May reduce speed.'

		power = 10
		accuracy = 100
		pp = 35
		super().__init__(pp, power, accuracy)

class Conversion(Attack):
	def __init__(self):
		self.name = 'Conversion'
		self.type = normal
		self.attackType = [selfConditionModifier]
		self.condition = ReType()
		self.effectAccuracy = 0
		self.description = 'Changes the user\'s type into an own move\'s type.'

		power = 0
		accuracy = 0
		pp = 30
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		self.pp -= 1
		attackTypes = []
		for attack in userPokemon.attacks:
			attackTypes.append(attack.type)

		mixer.play_attack_sound(self.name)
		becomeType = choice(attackTypes)
		messages.append('%s became %s type!' % (userPokemon.type, becomeType))
		userPokemon.afflict_status(ReType(targetType=becomeType))

		return damage, messages

class Conversion2(Attack):
	def __init__(self):
		self.name = 'Conversion 2'
		self.type = normal
		self.attackType = [selfConditionModifier]
		self.condition = ReType()
		self.effectAccuracy = 0
		self.description = 'Makes the user resistant to the last attack\'s type.'

		power = 0
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)

	# def use(self, userPokemon, targetPokemon):
	# 	damage = 0
	# 	messages = []
	# 	messages.append('%s used %s!' % (userPokemon.name, self.name))
	# 	self.pp -= 1
	# 	attackTypes = []
	# 	for attack in userPokemon.attacks:
	# 		attackTypes.append(attack.type)

	# 	becomeType = choice(attackTypes)
	# 	messages.append('%s became %s type!' % (userPokemon.type, becomeType))
	# 	userPokemon.afflict_status(ReType(targetType=becomeType))

	# 	return damage, messages
	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('This move not yet implemented.')

		return damage, messages

class Covet(Attack):
	def __init__(self):
		self.name = 'Covet'
		self.type = normal
		self.attackType = [physical, item]
		self.effectAccuracy = 100
		self.description = 'Cutely begs to obtain an item held by the foe.'

		power = 40
		accuracy = 100
		pp = 40
		super().__init__(pp, power, accuracy)

class CrushClaw(Attack):
	def __init__(self):
		self.name = 'Crush Claw'
		self.type = normal
		self.attackType = [physical, optStatModifier]
		self.statsModified = [defense]
		self.stageModifier = -1
		self.effectAccuracy = 50

		self.description = 'Tears at the foe with sharp claws. May lower defense.'

		power = 75
		accuracy = 95
		pp = 10
		super().__init__(pp, power, accuracy)

class Cut(Attack):
	def __init__(self):
		self.name = 'Cut'
		self.type = normal
		self.attackType = [physical]
		self.description = 'Cuts the foe with sharp scythes, claws, etc.'

		power = 50
		accuracy = 95
		pp = 30
		super().__init__(pp, power, accuracy)

class DefenseCurl(Attack):

	def __init__(self):
		self.name = 'Defense Curl'
		self.type = normal
		self.attackType = [selfStatModifier]
		self.statsModified = [defense]
		self.stageModifier = 1
		self.effectAccuracy = 100
		self.description = 'Curls up to conceal weak spots and raise defense.'
		power = 0
		accuracy = 100
		pp = 40
		super().__init__(pp, power, accuracy)

class Disable(Attack):
	def __init__(self):
		self.name = 'Disable'
		self.type = ghost
		self.attackType = [optConditionModifier]
		self.description = 'Psychically disables one of the foe\'s moves.'

		power = 0
		accuracy = 0
		pp = 5
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		i = randint(0,3)
		attack = targetPokemon.attacks[i]
		targetPokemon.afflict_status(Disabled(i))
		mixer.play_attack_sound(self.name)
		messages.append('%s is disabled!' % attack.name)

		return damage, messages

class DizzyPunch(Attack):
	def __init__(self):
		self.name = 'Dizzy Punch'
		self.type = normal
		self.attackType = [physical, optConditionModifier]
		self.condition = ConfusionStatus()
		self.effectAccuracy = 20
		self.description = 'A rhythmic punch that may confuse the foe.'

		power = 70
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

class DoubleTeam(Attack):

	def __init__(self):
		self.name = 'Double Team'
		self.type = normal
		self.attackType = [selfStatModifier]
		self.statsModified = [evasiveness]
		self.stageModifier = 1
		self.effectAccuracy = 0
		self.description = 'Creates illusory copies to raise evasiveness.'
		power = 0
		accuracy = 0
		pp = 15
		super().__init__(pp, power, accuracy)

class DoubleEdge(Attack):
	def __init__(self):
		self.name = 'Double-edge'
		self.type = normal
		self.attackType = [physical]
		self.description = 'A life-risking tackle that also hurts the user.'

		power = 120
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)
		self.recoilModifier = 0.33

class Doubleslap(MultiAttack):
	def __init__(self):
		self.name = 'Double Slap'
		self.type = normal
		self.attackType = [physical]
		self.description = 'Repeatedly slaps the foe 2 to 5 times.'

		power = 15
		accuracy = 85
		pp = 10
		super().__init__(pp, power, accuracy)

class EggBomb(Attack):

	def __init__(self):
		self.name = 'Egg Bomb'
		self.type = normal
		self.attackType = [special]
		self.description = 'An egg is forcibly hurled at the foe.'
		power = 100
		accuracy = 75
		pp = 10
		super().__init__(pp, power, accuracy)

class Encore(Attack):
	def __init__(self):
		self.name = 'Encore'
		self.type = normal
		self.attackType = [optConditionModifier]
		self.condition = EncoreStatus()
		self.description = 'Makes the foe repeat its last move over 2 to 6 turns.'

		power = 0
		accuracy = 100
		pp = 5
		super().__init__(pp, power, accuracy)

class Endeavor(Attack):
	def __init__(self):
		self.name = 'Endeavor'
		self.type = normal
		self.attackType = [physical]
		self.description = 'Gains power if the user\'s HP is lower than the foe\'s HP.'

		power = 0
		accuracy = 100
		pp = 5
		super().__init__(pp, power, accuracy)

	def calculate_damage(self, userPokemon, targetPokemon):
		damage = 0
		messages = []

		if targetPokemon.type == ghost:
			messages.append('Doesn\'t effect %s' % targetPokemon.name)

		elif targetPokemon.hp > userPokemon.hp:
			damage = targetPokemon.hp - userPokemon.hp
		else:
			damage = 0

		return damage, messages

class Endure(Attack):
	def __init__(self):
		self.name = 'Endure'
		self.type = normal
		self.attackType = [selfConditionModifier]
		self.description = 'Endures any attack for 1 turn, leaving at least 1HP.'

		power = 0
		accuracy = 0
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		messages = []
		damage = 0
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		self.pp -= 1
		mixer.play_attack_sound(self.name)
		userPokemon.endure()

		messages.append('%s braced itself!' % userPokemon.name)

		return damage, messages

class Explosion(Attack):

	def __init__(self):
		self.name = 'Explosion'
		self.type = normal
		self.attackType = [special, suicide]
		self.description = 'Inflicts severe damage but makes the user faint.'
		power = 250
		accuracy = 100
		pp = 5
		super().__init__(pp, power, accuracy)

class Extremespeed(Attack):

	def __init__(self):
		self.name = 'Fake Out'
		self.type = normal
		self.attackType = [physical]
		self.description = 'An extremely fast and powerful attack.'

		power = 80
		accuracy = 100
		pp = 5
		super().__init__(pp, power, accuracy)
		self.priority = 2

class FakeOut(Attack):

	def __init__(self):
		self.name = 'Fake Out'
		self.type = normal
		self.attackType = [physical, optConditionModifier]
		self.condition = Flinch()
		self.effectAccuracy = 0
		self.description = 'A 1st-turn, 1st-strike move that causes flinching.'

		power = 40
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)
		self.priority = 2

class FalseSwipe(Attack):
	def __init__(self):
		self.name = 'False Swipe'
		self.type = normal
		self.attackType = [physical]
		self.description = 'An attack that leaves the foe with at least 1 HP.'

		power = 0
		accuracy = 90
		pp = 20
		super().__init__(pp, power, accuracy)
	
	def calculate_damage(self, userPokemon, targetPokemon):
		damage, messages = super().calculate_damage(userPokemon, targetPokemon)

		if damage > targetPokemon.hp:
			damage = targetPokemon.hp - 1

		return damage, messages

class Flail(Attack):
	def __init__(self):
		self.name = 'Flail'
		self.type = normal
		self.attackType = [physical]
		self.description = 'Inflicts more damage when the user\'s HP is down.'

		power = 0
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)
	
	def use(self, mixer, userPokemon, targetPokemon):
		hpPct = userPokemon.hp_bar()[0]

		if hpPct >= 68.75:
			self.power = 20
		elif hpPct >= 35.42:
			self.power = 40
		elif hpPct >= 20.83:
			self.power = 80
		elif hpPct >= 10.42:
			self.power = 100
		elif hpPct >= 4.17:
			self.power = 150
		else:
			self.power = 200

		damage, m = super().use(mixer, userPokemon, targetPokemon)
		if 'Super effective!' in m:
			mixer.play_sound('Super Effective')
		elif 'Not very effective...' in m:
			mixer.play_sound('Not Very Effective')
		elif 'Doesn\'t affect %s.' % targetPokemon.name in m:
			pass
		else:
					mixer.play_sound('Damage')

		messages = m
		return damage, messages

class FocusEnergy(Attack):

	def __init__(self):
		self.name = 'Focus Energy'
		self.type = normal
		self.attackType = [selfStatModifier]
		self.statsModified = [critStage]
		self.stageModifier = 1
		self.effectAccuracy = 0
		self.description = 'Focuses power to raise the critical-hit ratio.'
		power = 0
		accuracy = 0
		pp = 30
		super().__init__(pp, power, accuracy)

class FollowMe(Attack):
	def __init__(self):
		self.name = 'Follow Me'
		self.type = normal
		self.attackType = [partyEffect]
		self.effectAccuracy = 0
		self.description = 'Draws attention to make foes attack only the user.'

		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Foresight(Attack):

	def __init__(self):
		self.name = 'Foresight'
		self.type = normal
		self.attackType = [optStatModifier]
		self.statsModified = [evasiveness]
		self.stageModifier = 0
		self.effectAccuracy = 0
		self.description = 'Negates the foe\'s efforts to heighten evasiveness.'
		power = 0
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		messages = []
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		damage = 0
		self.pp -= 1	

		if self.accuracy == 0 or randint(1,100) < (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):			
			protected, m = self.check_protect(userPokemon, targetPokemon)
			messages.extend(m)
			if not protected:
				mixer.play_attack_sound(self.name)
				targetPokemon.evasivenessStage = 0
				messages.append('%s was identified!' % targetPokemon.name)

		else:
			
			messages.append('%s\'s attack missed.' % userPokemon.name)
		
		return damage, messages

class FuryAttack(MultiAttack):
	def __init__(self):
		self.name = 'Fury Attack'
		self.type = normal
		self.attackType = [physical]
		self.description = 'Jabs the foe 2 to 5 times with sharp horns, etc.'

		power = 15
		accuracy = 85
		pp = 20
		super().__init__(pp, power, accuracy)

class FurySwipes(MultiAttack):
	def __init__(self):
		self.name = 'Fury Swipes'
		self.type = normal
		self.attackType = [physical]
		self.description = 'Rakes the foe with sharp claws, etc., 2 to 5 times.'

		power = 18
		accuracy = 80
		pp = 15
		super().__init__(pp, power, accuracy)

class Glare(Attack):
	def __init__(self):
		self.name = 'Glare'
		self.type = normal
		self.attackType = [optConditionModifier]
		self.condition = Paralysis()
		self.effectAccuracy = 0
		self.description = 'Intimidates and frightens the foe into paralysis.'

		power = 0
		accuracy = 75
		pp = 30
		super().__init__(pp, power, accuracy)

class Growl(Attack):
	def __init__(self):
		self.name = 'Growl'
		self.type = normal
		self.attackType = [optStatModifier]
		self.statsModified = [attack]
		self.stageModifier = -1
		self.effectAccuracy = 100
		self.description = 'Growls cutely to reduce the foe\'s attack.'

		power = 0
		accuracy = 100
		pp = 40
		super().__init__(pp, power, accuracy)

class Growth(Attack):

	def __init__(self):
		self.name = 'Growth'
		self.type = normal
		self.attackType = [selfStatModifier]
		self.statsModified = [spAttack]
		self.stageModifier = 1
		self.effectAccuracy = 100
		self.description = 'Forces the body to grow and heightens special attack.'
		power = 0
		accuracy = 0
		pp = 40
		super().__init__(pp, power, accuracy)

class Guillotine(Attack):
	def __init__(self):
		self.name = 'Guillotine'
		self.type = normal
		self.attackType = [physical]
		self.description = 'A powerful pincer attack that may cause fainting.'

		power = 0
		accuracy = 30
		pp = 5
		super().__init__(pp, power, accuracy)

		def calculate_damage(self, userPokemon, targetPokemon):
			damage = 0
			messages = []
			if ghost in targetPokemon.type:
				message.append('Doesn\'t effect %s' % targetPokemon.name)

			else:
				damage = targetPokemon.maxHp
				messages.append('One-hit KO!')

			return damage, messages

class Harden(Attack):

	def __init__(self):
		self.name = 'Harden'
		self.type = normal
		self.attackType = [selfStatModifier]
		self.statsModified = [defense]
		self.stageModifier = 1
		self.effectAccuracy = 100
		self.description = 'Tightens the muscles to raise defense.'
		power = 0
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)

class Headbutt(Attack):

	def __init__(self):
		self.name = 'Headbutt'
		self.type = normal
		self.attackType = [physical, optConditionModifier]
		self.condition = Flinch()
		self.effectAccuracy = 30
		self.description = 'A ramming attack that may cause flinching.'

		power = 70
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class HelpingHand(Attack):
	def __init__(self):
		self.name = 'Helping Hand'
		self.type = normal
		self.attackType = [partyEffect]
		self.effectAccuracy = 0
		self.description = 'Boosts the power of the recipient\'s moves.'

		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class HornAttack(Attack):
	def __init__(self):
		self.name = 'Horn Attack'
		self.type = normal
		self.attackType = [physical]
		self.description = 'Jabs the foe with sharp horns.'

		power = 65
		accuracy = 100
		pp = 25
		super().__init__(pp, power, accuracy)

class HornDrill(Attack):
	def __init__(self):
		self.name = 'Horn Drill'
		self.type = normal
		self.attackType = [physical]
		self.description = 'A one-hit KO attack that uses a horn like a drill.'

		power = 0
		accuracy = 30
		pp = 5
		super().__init__(pp, power, accuracy)

		def calculate_damage(self, userPokemon, targetPokemon):
			damage = 0
			messages = []
			if ghost in targetPokemon.type:
				message.append('Doesn\'t effect %s' % targetPokemon.name)

			else:
				damage = targetPokemon.maxHp
				messages.append('One-hit KO!')

			return damage, messages

class HyperBeam(Attack):
	def __init__(self):
		self.name = 'Hyper Beam'
		self.type = normal
		self.attackType = [special, selfConditionModifier]
		self.description = 'Powerful, but leaves the user immobile the next turn.'
		self.condition = Recharge()
		power = 150
		accuracy = 90
		pp = 5
		super().__init__(pp, power, accuracy)

class HyperFang(Attack):
	def __init__(self):
		self.name = 'Hyper Fang'
		self.type = normal
		self.attackType = [physical, optConditionModifier]
		self.condition = Flinch()
		self.effectAccuracy = 10
		self.description = 'Attacks with sharp fangs. May cause flinching.'

		power = 80
		accuracy = 90
		pp = 15
		super().__init__(pp, power, accuracy)

class HyperVoice(Attack):
	def __init__(self):
		self.name = 'Hyper Voice'
		self.type = normal
		self.attackType = [special]
		self.description = 'A loud attack that uses sound waves to injure.'

		power = 90
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

class Leer(Attack):

	def __init__(self):
		self.name = 'Leer'
		self.type = normal
		self.attackType = [optStatModifier]
		self.statsModified = [defense]
		self.stageModifier = -1
		self.effectAccuracy = 100
		self.description = 'Frightens the foe with a leer to lower defense.'
		power = 0
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)

class LockOn(Attack):
	def __init__(self):
		self.name = 'Lock-on'
		self.type = normal
		self.attackType = [selfStatModifier]
		self.statsModified = ['accuracyStat']
		self.effectAccuracy = 0
		self.description = 'Locks on to the foe to ensure the next move hits.'

		power = 0
		accuracy = 0
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		messages = []
		damage = 0
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		self.pp -= 1

		userPokemon.lock_on()
		mixer.play_attack_sound(self.name)
		messages.append('%s took aim!' % userPokemon.name)

		return damage, messages

class LovelyKiss(Attack):
	def __init__(self):
		self.name = 'Lovely Kiss'
		self.type = normal
		self.attackType = [optConditionModifier]
		self.condition = Sleep()
		self.effectAccuracy = 0
		self.description = 'Demands a kiss with a scary face that induces sleep.'

		power = 0
		accuracy = 75
		pp = 10
		super().__init__(pp, power, accuracy)

class MeanLook(Attack):
	def __init__(self):
		self.name = 'Mean Look'
		self.type = normal
		self.attackType = [optConditionModifier]
		self.condition = CantEscape()
		self.effectAccuracy = 0
		self.description = 'Fixes the foe with a mean look that prevents escape.'

		power = 0
		accuracy = 100
		pp = 5
		super().__init__(pp, power, accuracy)
		self.priority = 1

class MegaKick(Attack):

	def __init__(self):
		self.name = 'Mega Kick'
		self.type = normal
		self.attackType = [physical]
		self.description = 'An extremely powerful kick with intense force.'

		power = 120
		accuracy = 75
		pp = 5
		super().__init__(pp, power, accuracy)

class MegaPunch(Attack):

	def __init__(self):
		self.name = 'Mega Punch'
		self.type = normal
		self.attackType = [physical]
		self.description = 'A strong punch thrown with incredible power.'

		power = 80
		accuracy = 85
		pp = 20
		super().__init__(pp, power, accuracy)

class Metronome(Attack):
	def __init__(self):
		self.name = 'Metronome'
		self.type = normal
		self.attackType = []
		self.description = 'Waggles a finger to use any POKéMON move at random.'

		power = 0
		accuracy = 0
		pp = 10
		super().__init__(pp, power, accuracy)

class Mimic(Attack):
	def __init__(self):
		self.name = 'Mimic'
		self.type = normal
		self.attackType = [special]
		self.description = 'Copies a move used by the foe during one battle.'
		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage, messages = choice(targetPokemon.attacks).use(mixer, userPokemon, targetPokemon)
		return damage, messages

class MindReader(Attack):
	def __init__(self):
		self.name = 'Mind Reader'
		self.type = normal
		self.attackType = [partyEffect]
		self.description = 'Senses the foe\'s action to ensure the next move\'s hit.'
		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)



class Minimize(Attack):
	def __init__(self):
		self.name = 'Minimize'
		self.type = normal
		self.attackType = [selfStatModifier]
		self.statsModified = [evasiveness]
		self.stageModifier = 1
		self.effectAccuracy = 0
		self.description = 'Minimizes the user\'s size to raise evasiveness.'
		power = 0
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)

class Moonlight(Attack):
	def __init__(self):
		self.name = 'Moonlight'
		self.type = normal
		self.attackType = [heal, weather]
		self.healModifier = 0.5
		self.effectAccuracy = 0
		self.description = 'Restores HP. The amount varies with the weather.'
		power = 0
		accuracy = 0
		pp = 5
		super().__init__(pp, power, accuracy)

class OdorSleuth(Attack):

	def __init__(self):
		self.name = 'Odor Sleuth'
		self.type = normal
		self.attackType = [optStatModifier]
		self.statsModified = [evasiveness]
		self.stageModifier = 0
		self.effectAccuracy = 0
		self.description = 'Negates the foe\'s efforts to heighten evasiveness.'
		power = 0
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		messages = []
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		damage = 0
		self.pp -= 1	

		if userPokemon.lockedOn or self.accuracy == 0 or randint(1,100) < (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):			
			protected, m = self.check_protect(userPokemon, targetPokemon)
			messages.extend(m)
			if not protected:
				mixer.play_attack_sound(self.name)
				targetPokemon.evasivenessStage = 0
				messages.append('%s was identified!' % targetPokemon.name)

		else:
			
			messages.append('%s\'s attack missed.' % userPokemon.name)
		
		if userPokemon.lockedOn:
			userPokemon.lock_off()

		return damage, messages

class PayDay(Attack):
	def __init__(self):
		self.name = 'Pay Day'
		self.type = normal
		self.attackType = [special]
		self.description = 'Throws coins at the foe. Money is recovered after.'

		power = 40
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage, messages = super().use(mixer, userPokemon, targetPokemon)

		messages.insert(1, 'Coins scattered everywhere!')
		messages.insert(2, 'Money not yet implemented.')
		return damage, messages

class PerishSong(Attack):
	def __init__(self):
		self.name = 'Perish Song'
		self.type = normal
		self.attackType = [selfConditionModifier, optConditionModifier]
		# self.condition = PerishStatus()
		self.effectAccuracy = 0
		self.description = 'Any pokémon hearing this song faints in 3 turns.'

		power = 0
		accuracy = 0
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('This move not yet implemented.')

		return damage, messages

class Pound(Attack):
	def __init__(self):
		self.name = 'Pound'
		self.type = normal
		self.attackType = [physical]
		self.description = 'Pounds the foe with forelegs or tail.'

		power = 40
		accuracy = 100
		pp = 35
		super().__init__(pp, power, accuracy)

class Protect(Attack):
	def __init__(self):
		self.name = 'Protect'
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
		messages.append('%s used Protect!' % userPokemon.name)
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

class PsychUp(Attack):
	def __init__(self):
		self.name = 'Psych Up'
		self.type = normal
		self.attackType = [selfStatModifier]
		self.statsModified = ['all']
		self.effectAccuracy = 0
		self.description = 'Copies the foe\'s effect(s) and gives to the user.'

		power = 0
		accuracy = 0
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		messages = []
		damage = 0
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		self.pp -= 1
		mixer.play_attack_sound(self.name)
		userPokemon.attackStage = targetPokemon.attackStage
		userPokemon.defenseStage = targetPokemon.defenseStage
		userPokemon.spAttackStage = targetPokemon.spAttackStage
		userPokemon.spDefenseStage = targetPokemon.spDefenseStage
		userPokemon.speedStage = targetPokemon.speedStage
		userPokemon.accuracyStage = targetPokemon.accuracyStage
		userPokemon.evasivenessStage = targetPokemon.evasivenessStage
		mixer.play_attack_sound('Stat Rise Up')
		messages.append('%s copied %s\'s stat changes!' % (userPokemon.name, targetPokemon.name))

		return damage, messages

class QuickAttack(Attack):

	def __init__(self):
		self.name = 'Quick Attack'
		self.type = normal
		self.attackType = [physical]
		self.description = 'An extremely fast attack that always strikes first.'
		power = 40
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)
		self.priority = 1

class Rage(Attack):
	def __init__(self):
		self.name = 'Rage'
		self.type = normal
		self.attackType = [physical, selfConditionModifier]
		self.condition = Enraged()
		self.effectAccuracy = 0
		self.description = 'Raises the users attack every time it is hit.'

		power = 20
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class RapidSpin(Attack):
	def __init__(self):
		self.name = 'Rapid Spin'
		self.type = normal
		self.attackType = [physical, selfConditionModifier]
		self.effectAccuracy = 0
		self.description = 'Spins the body at high speed to strike the foe.'

		power = 20
		accuracy = 100
		pp = 40
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		messages = []
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		damage = 0
		self.pp -= 1	

		if userPokemon.lockedOn or self.accuracy == 0 or randint(1,100) < (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):			
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

			for i in range(len(userPokemon.volitileStatuses)):
				status = userPokemon.volitileStatuses[i]
				if status.name in ['bound', 'leechseed']:
					userPokemon.remove_volitile_status(i)
					messages.append('%s is free from binding!' % userPokemon.name)
		else:
			
			messages.append('%s\'s attack missed.' % userPokemon.name)
		
		if userPokemon.lockedOn:
			userPokemon.lock_off()

		return damage, messages

class Recover(Attack):
	def __init__(self):
		self.name = 'Recover'
		self.type = normal
		self.attackType = [heal]
		self.healModifier = 0.5
		self.effectAccuracy = 0
		self.description = 'Recovers up to half the user\'s maximum HP.'
		power = 0
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)

class Recycle(Attack):
	def __init__(self):
		self.name = 'Recycle'
		self.type = normal
		self.attackType = [item]
		self.effectAccuracy = 0
		self.description = 'Recycles a used item for one more use.'

		power = 0
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

class Refresh(Attack):
	def __init__(self):
		self.name = 'Refresh'
		self.type = normal
		self.attackType = [heal]
		self.description = 'Heals poisoning, paralysis, or a burn.'
		power = 0
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		self.pp -= 1
		mixer.play_attack_sound(self.name)
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		userPokemon.heal_status()
		messages.append('%s is refreshed!' % userPokemon.name)

		return damage, messages

class Roar(Attack):
	def __init__(self):
		self.name = 'Roar'
		self.type = normal
		self.attackType = [partyEffect]
		# self.effect = SwitchOut()
		self.effectAccuracy = 0
		self.description = 'Makes the foe flee to end the battle.'

		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)


class Safeguard(Attack):
	def __init__(self):
		self.name = 'Safeguard'
		self.type = normal
		self.attackType = [partyEffect]
		# self.effect = SwitchOut()
		self.effectAccuracy = 0
		self.description = 'Guards the party against status changes for 5 turns.'

		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class ScaryFace(Attack):

	def __init__(self):
		self.name = 'Scary Face'
		self.type = normal
		self.attackType = [optStatModifier]
		self.statsModified = [speed]
		self.stageModifier = -2
		self.effectAccuracy = 0
		self.description = 'Frightens with a scary face to sharply reduce speed.'
		power = 0
		accuracy = 90
		pp = 10
		super().__init__(pp, power, accuracy)


class Scratch(Attack):

	def __init__(self):
		self.name = 'Scratch'
		self.type = normal
		self.attackType = [physical]
		self.description = 'Scratches the foe with sharp claws.'
		power = 40
		accuracy = 100
		pp = 35
		super().__init__(pp, power, accuracy)

class Screech(Attack):

	def __init__(self):
		self.name = 'Screech'
		self.type = normal
		self.attackType = [optStatModifier]
		self.statsModified = [defense]
		self.stageModifier = -2
		self.effectAccuracy = 0
		self.description = 'Emits a screech to sharply reduce the foe\'s defense.'
		
		power = 0
		accuracy = 85
		pp = 40
		super().__init__(pp, power, accuracy)

class Selfdestruct(Attack):

	def __init__(self):
		self.name = 'Selfdestruct'
		self.type = normal
		self.attackType = [special, suicide]
		self.description = 'Inflicts severe damage but makes the user faint.'
		power = 200
		accuracy = 100
		pp = 5
		super().__init__(pp, power, accuracy)

class Sharpen(Attack):
	def __init__(self):
		self.name = 'Sharpen'
		self.type = normal
		self.attackType = [selfStatModifier]
		self.statsModified = [attack]
		self.stageModifier = 1
		self.effectAccuracy = 0
		self.description = 'Reduces the polygon count and raises attack.'

		power = 0
		accuracy = 0
		pp = 30
		super().__init__(pp, power, accuracy)

class Sing(Attack):
	def __init__(self):
		self.name = 'Sing'
		self.type = normal
		self.attackType = [optConditionModifier]
		self.condition = Sleep()
		self.effectAccuracy = 100
		self.description = 'A soothing song lulls the foe into a deep slumber.'

		power = 0
		accuracy = 55
		pp = 15
		super().__init__(pp, power, accuracy)

class SkullBash(Attack):
	def __init__(self):
		self.name = 'Skull Bash'
		self.type = normal
		self.attackType = [physical]
		self.turnNumber = 0
		self.description = 'Tucks in the head, then attacks on the next turn.'

		power = 100
		accuracy = 100
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
			messages.append('%s tucked in its head!' % userPokemon.name)
			mixer.play_attack_sound('%s_part_1' % self.name)
			
		else:
			messages.append('%s used %s!' % (userPokemon.name, self.name))
			
			if userPokemon.lockedOn or randint(1,100) < (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
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
			userPokemon.lock_off()

		return damage, messages

class Slam(Attack):

	def __init__(self):
		self.name = 'Slam'
		self.type = normal
		self.attackType = [physical]
		self.description = 'Slams the foe with a long tail, vine, etc.'
		power = 80
		accuracy = 75
		pp = 20
		# pp = 1
		super().__init__(pp, power, accuracy)

class Slash(Attack):

	def __init__(self):
		self.name = 'Slash'
		self.type = normal
		self.attackType = [physical]
		self.description = 'Slashes with claws, etc. Has a high critical-hit ratio.'
		power = 70
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)
		self.critStage = 1

class SleepTalk(Attack):
	def __init__(self):
		self.name = 'Sleep Talk'
		self.type = normal
		self.attackType = [special]
		self.description = 'Uses an own move randomly while asleep.'

		power = 0
		accuracy = 0
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('This move not yet implemented.')

		return damage, messages

class Smokescreen(Attack):

	def __init__(self):
		self.name = 'Smokescreen'
		self.type = normal
		self.attackType = [optStatModifier]
		self.statsModified = [accuracyStat]
		self.stageModifier = -1
		self.effectAccuracy = 0
		self.description = 'Lowers the foe\'s accuracy using smoke, ink, etc.'
		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Snore(Attack):
	def __init__(self):
		self.name = 'Substitute'
		self.type = normal
		self.attackType = [special]
		self.description = 'A loud attack that can be used only while asleep.'

		power = 40
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('This move not yet implemented.')

		return damage, messages

class Softboiled(Attack):
	def __init__(self):
		self.name = 'Softboiled'
		self.type = normal
		self.attackType = [heal]
		self.healModifier = 0.5
		self.effectAccuracy = 0
		self.description = 'Recovers up to half the user\'s maximum HP.'
		power = 0
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

class Sonicboom(Attack):
	def __init__(self):
		self.name = 'Sonicboom'
		self.type = normal
		self.attackType = [special]
		self.description = 'Launches shock waves that always inflict 20 HP damage.'

		power = 0
		accuracy = 90
		pp = 20
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

class SpikeCannon(MultiAttack):
	def __init__(self):
		self.name = 'Spike Cannon'
		self.type = normal
		self.attackType = [special]
		self.description = 'Launches sharp spikes that strike 2 to 5 times.'

		power = 20
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class SpitUp(Attack):
	def __init__(self):
		self.name = 'Spit Up'
		self.type = normal
		self.attackType = [special]
		self.description = 'Releases stockpiled power (the more the better).'

		power = 100
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

	def calculate_damage(self, userPokemon, targetPokemon):
		messages = []

		if userPokemon.stockpile == 0:
			messages.append('But it failed.')
			damage = 0
		else:
			power = userPokemon.stockpile * self.power

			userAttack = userPokemon.battleSpAttack
			targetDefense = targetPokemon.battleSpDefense

			if self.type in userPokemon.type:
				stab = 1.5
			else:
				stab = 1

			crit = 1

			typeModifier = get_type_modifier(self.type, targetPokemon.type)
			if typeModifier == 2 or typeModifier == 4:
				messages.append('Super effective!')
			elif typeModifier == 0.5 or typeModifier == 0.25:
				messages.append('Not very effective...')
			elif typeModifier == 0:
				messages.append('Does not affect %s.' % targetPokemon.name)
				


			modifier = typeModifier * stab

			damage = ((((2*userPokemon.level/5)+2) * power * userAttack/targetDefense)/50 + 2) * modifier
			damage *= self.screen_damage_modifier(targetPokemon)
			damage = int(damage)

			userPokemon.stockpile = 0
		
		return damage, messages

class Splash(Attack):
	def __init__(self):
		self.name = 'Splash'
		self.type = normal
		self.attackType = [special]
		# self.condition = PerishStatus()
		self.description = 'It\'s just a splash... Has no effect whatsoever.'

		power = 0
		accuracy = 0
		pp = 40
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		self.pp -= 1
		mixer.play_attack_sound(self.name)
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		messages.append('It has no effect...!')

		return damage, messages

class Stockpile(Attack):
	def __init__(self):
		self.name = 'Stockpile'
		self.type = normal
		self.attackType = [selfStatModifier]
		self.effectAccuracy = 0
		self.description = 'Charges up power for up to 3 turns.'

		power = 0
		accuracy = 0
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []

		messages.append('%s used %s!' % (userPokemon.name, self.name))
		self.pp -= 1

		if userPokemon.stockpile < 3:
			mixer.play_attack_sound(self.name)
			userPokemon.stockpile += 1
			messages.append('%s is stockpiling %i' % (userPokemon.name, userPokemon.stockpile))

		else:
			messages.append('But it failed.')

		return damage, messages

class Stomp(Attack):

	def __init__(self):
		self.name = 'Stomp'
		self.type = normal
		self.attackType = [physical, optConditionModifier]
		self.condition = Flinch()
		self.effectAccuracy = 30
		self.description = 'Stomps the enemy with a big foot. May cause flinching.'

		power = 65
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Substitute(Attack):
	def __init__(self):
		self.name = 'Substitute'
		self.type = normal
		self.attackType = [selfConditionModifier]
		# self.condition = SubstituteStatus()
		self.effectAccuracy = 0
		self.description = 'Creates a decoy using 1/4 of the user\'s maximum HP.'

		power = 0
		accuracy = 0
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		mixer.play_attack_sound(self.name)
		messages.append('This move not yet implemented.')

		return damage, messages

class Supersonic(Attack):
	def __init__(self):
		self.name = 'Supersonic'
		self.type = normal
		self.attackType = [optConditionModifier]
		self.condition = ConfusionStatus()
		self.effectAccuracy = 0
		self.description = 'Emits bizarre sound waves that may confuse the foe.'

		power = 0
		accuracy = 55
		pp = 20
		super().__init__(pp, power, accuracy)

class SuperFang(Attack):
	def __init__(self):
		self.name = 'Super Fang'
		self.type = normal
		self.attackType = [physical]
		self.description = 'Attacks with sharp fangs and cuts half the foe\'s HP.'

		power = 0
		accuracy = 90
		pp = 10
		super().__init__(pp, power, accuracy)

	def calculate_damage(self, userPokemon, targetPokemon):
		messages = []

		typeModifier = get_type_modifier(self.type, targetPokemon.type)
		if typeModifier == 2 or typeModifier == 4:
			messages.append('Super effective!')
		elif typeModifier == 0.5 or typeModifier == 0.25:
			messages.append('Not very effective...')
		elif typeModifier == 0:
			messages.append('Does not affect %s.' % targetPokemon.name)
			
		if typeModifier == 0:
			damage = 0
		else:
			damage = int(targetPokemon.hp / 2)
		
		return damage, messages

class Swagger(Attack):
	def __init__(self):
		self.name = 'Swagger'
		self.type = normal
		self.attackType = [optStatModifier, optConditionModifier]
		self.statsModified = [attack]
		self.stageModifier = 2
		self.condition = ConfusionStatus()
		self.effectAccuracy = 0
		self.description = 'Confuses the foe, but also sharply raises attack.'

		power = 0
		accuracy = 90
		pp = 15
		super().__init__(pp, power, accuracy)

class Swallow(Attack):
	def __init__(self):
		self.name = 'Swallow'
		self.type = normal
		self.attackType = [heal]
		self.description = 'Absorbs stockpiled power and restores HP.'

		power = 0
		accuracy = 0
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		messages = []
		damage = 0

		messages.append('%s used %s!' % (userPokemon.name, self.name))
		self.pp -= 1

		if userPokemon.stockpile == 0:
			messages.append('But it failed.')
		else:
			mixer.play_attack_sound(self.name)
			if userPokemon.stockpile == 1:
				healModifier = 0.25
			elif userPokemon.stockpile == 2:
				healModifier = 0.5
			elif userPokemon.stockpile == 3:
				healModifier = 1

			messages.append('%s recovered HP!' % userPokemon.name)
			userPokemon.heal(healModifier)
			mixer.play_attack_sound('Healing Attack')
			userPokemon.stockpile = 0
		
		return damage, messages

class SweetScent(Attack):

	def __init__(self):
		self.name = 'Sweet Scent'
		self.type = normal
		self.attackType = [optStatModifier]
		self.statsModified = [evasiveness]
		self.stageModifier = -1
		self.effectAccuracy = 0
		self.description = 'Allures the foe to reduce evasiveness.'
		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Swift(Attack):
	def __init__(self):
		self.name = 'Swift'
		self.type = normal
		self.attackType = [special]
		self.description = 'Sprays star-shaped rays that never miss.'

		power = 60
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)

class SwordsDance(Attack):

	def __init__(self):
		self.name = 'Swords Dance'
		self.type = normal
		self.attackType = [selfStatModifier]
		self.statsModified = [attack]
		self.stageModifier = 2
		self.effectAccuracy = 0
		self.description = 'A fighting dance that sharply raises attack.'
		power = 0
		accuracy = 0
		pp = 30
		super().__init__(pp, power, accuracy)

class Tackle(Attack):

	def __init__(self):
		self.name = 'Tackle'
		self.type = normal
		self.attackType = [physical]
		self.description = 'Charges the foe with a full-body tackle.'
		power = 35
		accuracy = 95
		pp = 35
		# pp = 1
		super().__init__(pp, power, accuracy)

class TailWhip(Attack):

	def __init__(self):
		self.name = 'Tail Whip'
		self.type = normal
		self.attackType = [optStatModifier]
		self.statsModified = [defense]
		self.stageModifier = -1
		self.effectAccuracy = 100
		self.description = 'Wags the tail to lower the foe\'s defense.'
		power = 0
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)

class TakeDown(Attack):
	def __init__(self):
		self.name = 'Take Down'
		self.type = normal
		self.attackType = [physical]
		self.description = 'A reckless charge attack that also hurts the user.'

		power = 90
		accuracy = 85
		pp = 20
		super().__init__(pp, power, accuracy)
		self.recoilModifier = 0.25

class Thrash(Attack):
	def __init__(self):
		self.name = 'Thrash'
		self.type = normal
		self.attackType = [physical, selfConditionModifier]
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
		if userPokemon.lockedOn or randint(1,100) < (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
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
			userPokemon.lock_off()
			self.turnNumber = 0

		return damage, messages

class Tickle(Attack):

	def __init__(self):
		self.name = 'Tickle'
		self.type = normal
		self.attackType = [optStatModifier]
		self.statsModified = [attack, defense]
		self.stageModifier = -1
		self.effectAccuracy = 0
		self.description = 'Makes the foe laugh to lower attack and defense.'
		
		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Transform(Attack):
	def __init__(self):
		self.name = 'Transform'
		self.type = normal
		self.attackType = [selfConditionModifier]
		# self.condition = PerishStatus()
		self.effectAccuracy = 0
		self.description = 'Alters the user\'s cells to become a copy of the foe.'

		power = 0
		accuracy = 0
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		self.pp -= 1
		mixer.play_attack_sound(self.name)
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		userPokemon.transform(targetPokemon)
		messages.append('%s transformed into %s!' % (userPokemon.name, targetPokemon.name))

		return damage, messages

class TriAttack(Attack):
	def __init__(self):
		self.name = 'Tri Attack'
		self.type = normal
		self.attackType = [special, optConditionModifier]
		self.condition = [Burn(), Freeze(), Paralysis()]
		self.effectAccuracy = 10
		self.description = 'Fires three types of beams at the same time.'

		power = 80
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		messages = []
		damage = 0
		messages.append('%s used %s!' % (userPokemon.name, self.name))
		self.pp -= 1
		condition = choice(self.condition)
		
		protected, m = self.check_protect(userPokemon, targetPokemon)
		messages.extend(m)

		if userPokemon.lockedOn or self.accuracy == 0 or randint(1,100) < (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
			
			if not protected and (physical in self.attackType or special in self.attackType):
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
			
			if not protected and optConditionModifier in self.attackType:
				if self.effectAccuracy == 0 or randint(1,100) < self.effectAccuracy:
					afflicted = targetPokemon.afflict_status(condition)
					if afflicted:
						messages.append('%s is %s!' % (targetPokemon.name, self.condition.battleText))
					else:
						messages.append('%s cannot be %s!' % (targetPokemon.name, self.condition.battleText))
				else:
					pass
		else:
			damage = 0
			messages.append('%s\'s attack missed.' % userPokemon.name)

		if userPokemon.lockedOn:
			userPokemon.lock_off()
			
		return damage, messages

class Uproar(Attack):
	def __init__(self):
		self.name = 'Uproar'
		self.type = normal
		self.attackType = [physical, selfConditionModifier]
		self.duration = randint(2,3)
		self.turnNumber = 0
		self.condition = ConfusionStatus()
		self.effectAccuracy = 0
		self.description = 'Causes an uproar for 2 to 5 turns and prevents sleep.'

		power = 70
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		damage = 0
		messages = []
		if self.turnNumber == 0:
			self.pp -= 1
			self.duration = randint(2,5)
		
		messages.append('%s used %s!' % (userPokemon.name, self.name))

		if not userPokemon.keepUsingAttack:
			userPokemon.keep_using_attack(self)
			userPokemon.uproar = True

		
		if userPokemon.lockedOn or randint(1,100) < (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
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
				messages.append('%s is causing an uproar!' % userPokemon.name)

		else:
			damage = 0
			messages.append('%s\'s attack missed.' % userPokemon.name)

		self.turnNumber += 1

		if self.turnNumber == self.duration:
			userPokemon.afflict_status(self.condition)
			userPokemon.stop_using_attack()
			userPokemon.lock_off()
			self.turnNumber = 0
			self.uproar = False

		return damage, messages

class Vicegrip(Attack):
	def __init__(self):
		self.name = 'Vicegrip'
		self.type = normal
		self.attackType = [physical]
		self.description = 'Grips the foe with large and powerful pincers.'

		power = 55
		accuracy = 100
		pp = 30
		super().__init__(pp, power, accuracy)

class Whirlwind(Attack):
	def __init__(self):
		self.name = 'Whirlwind'
		self.type = normal
		self.attackType = [partyEffect]
		# self.effect = SwitchOut()
		self.effectAccuracy = 0
		self.description = 'Blows away the foe with wind and ends the battle.'

		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Wrap(Attack):
	def __init__(self):
		self.name = 'Wrap'
		self.type = normal
		self.attackType = [physical, optConditionModifier]
		self.condition = Bound(self.name)
		self.effectAccuracy = 0
		self.description = 'Wraps and squeezes the foe 2 to 5 times with vines, etc.'

		power = 15
		accuracy = 85
		pp = 20
		super().__init__(pp, power, accuracy)

class Yawn(Attack):
	def __init__(self):
		self.name = 'Yawn'
		self.type = normal
		self.attackType = [optConditionModifier]
		self.condition = Yawning()
		self.effectAccuracy = 0
		self.description = 'ulls the foe into yawning, then sleeping next turn.'

		power = 0
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)