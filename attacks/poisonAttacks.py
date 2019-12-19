from pokemonTypes import poison
from attack import Attack
from statuses import RegPoison, BadPoison
from attackKeywords import *

class Acid(Attack):
	def __init__(self):
		self.name = 'Acid'
		self.type = poison
		self.attackType = [special, optStatModifier]
		self.statsModified = [defense]
		self.stageModifier = -1
		self.effectAccuracy = 10
		self.description = 'Sprays a hide-melting acid. May reduce defense.'

		power = 0
		accuracy = 75
		pp = 30
		super().__init__(pp, power, accuracy)

class AcidArmor(Attack):
	def __init__(self):
		self.name = 'Acid Armor'
		self.type = poison
		self.attackType = [selfStatModifier]
		self.statsModified = [defense]
		self.stageModifier = 2
		self.effectAccuracy = 100
		self.description = 'Liquifies the user\'s body to sharply raise defense.'

		power = 0
		accuracy = 0
		pp = 40
		super().__init__(pp, power, accuracy)

class PoisonFang(Attack):
	def __init__(self):
		self.name = 'Poison Fang'
		self.type = poison
		self.attackType = [physical, optConditionModifier]
		self.condition = BadPoison()
		self.effectAccuracy = 30
		self.description = 'A sharp-fanged attack. May badly poison the foe.'

		power = 50
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class PoisonGas(Attack):
	def __init__(self):
		self.name = 'Poison Gas'
		self.type = poison
		self.attackType = [optConditionModifier]
		self.condition = RegPoison()
		self.effectAccuracy = 100
		self.description = 'Envelops the foe in a toxic gas that may poison.'

		power = 0
		accuracy = 55
		pp = 40
		super().__init__(pp, power, accuracy)

class PoisonSting(Attack):
	def __init__(self):
		self.name = 'Poison Sting'
		self.type = poison
		self.attackType = [physical,optConditionModifier]
		self.condition = RegPoison()
		self.effectAccuracy = 10
		self.description = 'A toxic attack with barbs, etc., that may poison.'

		power = 15
		accuracy = 100
		pp = 35
		super().__init__(pp, power, accuracy)

class PoisonTail(Attack):
	def __init__(self):
		self.name = 'Poison Tail'
		self.type = poison
		self.attackType = [physical,optConditionModifier]
		self.condition = RegPoison()
		self.effectAccuracy = 10
		self.description = 'Has a high critical-hit ratio. May also poison.'

		power = 50
		accuracy = 100
		pp = 25
		super().__init__(pp, power, accuracy)

		self.critStage = 1

class PoisonPowder(Attack):
	def __init__(self):
		self.name = 'Poisonpowder'
		self.type = poison
		self.attackType = [optConditionModifier]
		self.condition = RegPoison()
		self.effectAccuracy = 100
		self.description = 'Scatters a cloud of spores that always induce poison.'

		power = 0
		accuracy = 75
		pp = 35
		super().__init__(pp, power, accuracy)

class Sludge(Attack):
	def __init__(self):
		self.name = 'Sludge'
		self.type = poison
		self.attackType = [special,optConditionModifier]
		self.condition = RegPoison()
		self.effectAccuracy = 30
		self.description = 'Sludge is hurled to inflict damage. May also poison.'

		power = 65
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class SludgeBomb(Attack):
	def __init__(self):
		self.name = 'Sludge Bomb'
		self.type = poison
		self.attackType = [special,optConditionModifier]
		self.condition = RegPoison()
		self.effectAccuracy = 30
		self.description = 'Sludge is hurled to inflict damage. May also poison.'

		power = 90
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

class Smog(Attack):
	def __init__(self):
		self.name = 'Smog'
		self.type = poison
		self.attackType = [special,optConditionModifier]
		self.condition = RegPoison()
		self.effectAccuracy = 40
		self.description = 'An exhaust-gas attack that may also poison.'

		power = 20
		accuracy = 70
		pp = 20
		super().__init__(pp, power, accuracy)

class Toxic(Attack):
	def __init__(self):
		self.name = 'Toxic'
		self.type = poison
		self.attackType = [optConditionModifier]
		self.condition = BadPoison()
		self.effectAccuracy = 100
		self.description = 'Poisons the foe with an intensifying toxin.'

		power = 0
		accuracy = 85
		pp = 10
		super().__init__(pp, power, accuracy)

	def use(self, mixer, userPokemon, targetPokemon):
		messages = []

		messages.append('%s used %s!' % (userPokemon.name, self.name))
		self.pp -= 1

		if poison in userPokemon.type:
			accuracy = 100
		else:
			accuracy = self.accuracy

		if self.accuracy == 0 or randint(0,100) > (self.accuracy * self.accuracy_evasion_modifier(userPokemon.accuracyStage-targetPokemon.evasivenessStage)):
			mixer.play_attack_sound(self.name)
			protected, m = self.check_protect(userPokemon, targetPokemon)
			messages.extend(m)
			if not protected:

				afflicted = targetPokemon.afflict_status(self.condition)
				if afflicted:
					messages.append('%s is %s!' % (targetPokemon.name, self.condition.battleText))
				else:
					messages.append('%s cannot be %s!' % (targetPokemon.name, self.condition.battleText))
			
		return 0, messages