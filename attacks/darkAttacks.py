from pokemonTypes import dark
from attack import Attack
from statuses import Flinch, ConfusionStatus, Taunted, Tormented
from attackKeywords import *

class BeatUp(Attack):
	def __init__(self):
		self.name = 'Beat Up'
		self.type = dark
		self.attackType = [physical]
		self.description = 'Summons party Pokémon to join in the attack.'


		power = 10
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

class Bite(Attack):
	def __init__(self):
		self.name = 'Bite'
		self.type = dark
		self.attackType = [physical, optConditionModifier]
		self.condition = Flinch()
		self.effectAccuracy = 30
		self.description = 'Bites with vicious fangs. May cause flinching.'

		power = 60
		accuracy = 100
		pp = 25
		super().__init__(pp, power, accuracy)

class Crunch(Attack):
	def __init__(self):
		self.name = 'Crunch'
		self.type = dark
		self.attackType = [physical, optStatModifier]
		self.statsModified = [spDefense]
		self.stageModifier = -1
		self.effectAccuracy = 30
		self.description = 'Crunches with sharp fangs. May lower special defense.'

		power = 80
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class FaintAttack(Attack):
	def __init__(self):
		self.name = 'Faint Attack'
		self.type = dark
		self.attackType = [physical]
		self.description = 'Draws the foe close, then strikes without fail.'

		power = 60
		accuracy = 0
		pp = 20
		super().__init__(pp, power, accuracy)

class FakeTears(Attack):
	def __init__(self):
		self.name = 'Fake Tears'
		self.type = dark
		self.attackType = [optStatModifier]
		self.statsModified = [spDefense]
		self.stageModifier = -2
		self.effectAccuracy = 0
		self.description = 'Feigns crying to sharply lower the foe\'s special defense.'

		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Flatter(Attack):
	def __init__(self):
		self.name = 'Flatter'
		self.type = dark
		self.attackType = [optConditionModifier, optStatModifier]
		self.statsModified = [spAttack]
		self.stageModifier = 2
		self.condition = ConfusionStatus()
		self.effectAccuracy = 0
		self.description = 'Confuses the foe, but raises its special attack.'

		power = 0
		accuracy = 100
		pp = 15
		super().__init__(pp, power, accuracy)

class KnockOff(Attack):
	def __init__(self):
		self.name = 'Knock Off'
		self.type = dark
		self.attackType = [physical, item]
		self.description = 'Knocks down the foe\'s held item to prevent its use.'

		power = 20
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Memento(Attack):
	def __init__(self):
		self.name = 'Memento'
		self.type = dark
		self.attackType = [optStatModifier, suicide]
		self.statsModified = ['all']
		self.stageModifier = -1
		self.effectAccuracy = 0
		self.description = 'The user faints and lowers the foe\'s abilities.'

		power = 0
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

class Pursuit(Attack):
	def __init__(self):
		self.name = 'Pursuit'
		self.type = dark
		self.attackType = [physical]
		self.description = 'Inflicts bad damage if used on a foe switching out.'

		power = 40
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Snatch(Attack):
	def __init__(self):
		self.name = 'Snatch'
		self.type = dark
		self.attackType = [physical]
		self.description = 'Steals the effects of the next move the foe uses.'

		power = 0
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

class Taunt(Attack):
	def __init__(self):
		self.name = 'Taunt'
		self.type = dark
		self.attackType = [optConditionModifier]
		self.condition = Taunted()
		self.effectAccuracy = 0
		self.description = 'Taunts the foe into only using attack moves.'

		power = 0
		accuracy = 100
		pp = 20
		super().__init__(pp, power, accuracy)

class Thief(Attack):
	def __init__(self):
		self.name = 'Thief'
		self.type = dark
		self.attackType = [physical, item]
		self.description = 'While attacking, it may steal the foe\'s held item.'

		power = 40
		accuracy = 100
		pp = 10
		super().__init__(pp, power, accuracy)

class Torment(Attack):
	def __init__(self):
		self.name = 'Torment'
		self.type = dark
		self.attackType = [optConditionModifier]
		self.condition = Tormented()
		self.effectAccuracy = 0
		self.description = 'Torments the foe and stops succesive use of a move.'

		power = 0
		accuracy = 100
		pp = 15

		super().__init__(pp, power, accuracy)