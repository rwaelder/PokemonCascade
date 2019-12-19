from pokemonTypes import *
import sys
sys.path.append('attacks/')
from normalAttacks import *
from fightAttacks import *
from flyingAttacks import *
from poisonAttacks import *
from groundAttacks import *
from rockAttacks import *
from bugAttacks import *
from ghostAttacks import *
from steelAttacks import *
from fireAttacks import *
from waterAttacks import *
from grassAttacks import *
from electricAttacks import *
from psychicAttacks import *
from iceAttacks import *
from dragonAttacks import *
from darkAttacks import *
# from fairyAttacks import *


from pocketMonsters import PocketMonster
from creatures26_50 import Raichu
from expTable import erratic, fast, mFast, mSlow, slow, fluctuating

class Bulbasaur(PocketMonster):

	def __init__(self):
		self.name = 'Bulbasaur'
		baseHp = 45
		baseAttack = 49
		baseDefense = 49
		baseSpAttack = 65
		baseSpDefense = 65
		baseSpeed = 45
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)



		self.number = 1
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [grass, poison]
		self.weight = 6.9 # kg
		self.height = 0.7 # m
		self.femaleRate = 13 # percent

		self.evolvesAt = 16
		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 64
		
		self.levelUpAttacks = {1 : Tackle(), 4 : Growl(), 7 : LeechSeed(),
							  10 : VineWhip(), 14 : PoisonPowder(), 15 : SleepPowder(),
							  20 : RazorLeaf(), 25 : SweetScent(), 32 : Growth(),
							  39 : Synthesis(), 46 : Solarbeam()}


	def evolve(self):
		
		return Ivysaur()


class Ivysaur(PocketMonster):

	def __init__(self):
		self.name = 'Ivysaur'
		baseHp = 45
		baseAttack = 49
		baseDefense = 49
		baseSpAttack = 65
		baseSpDefense = 65
		baseSpeed = 45
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)

		self.number = 2
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [grass, poison]
		self.weight = 13.0 # kg
		self.height = 1.0 # m
		self.femaleRate = 13 # percent

		self.evolvesAt = 32
		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 141

		self.levelUpAttacks = {1 : Tackle(), 4 : Growl(), 7 : LeechSeed(),
							  10 : VineWhip(), 14 : PoisonPowder(), 15 : SleepPowder(),
							  22 : RazorLeaf(), 29 : SweetScent(), 38 : Growth(),
							  47 : Synthesis(), 56 : Solarbeam()}

	def evolve(self):
		return Venusaur()

class Venusaur(PocketMonster):

	def __init__(self):
		self.name = 'Venusaur'
		baseHp = 80
		baseAttack = 82
		baseDefense = 83
		baseSpAttack = 100
		baseSpDefense = 100
		baseSpeed = 80
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)

		self.number = 3
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [grass, poison]
		self.weight = 100.0 # kg
		self.height = 2.0 # m
		self.femaleRate = 13 # percent

		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 208

		self.levelUpAttacks = {1 : Tackle(), 4 : Growl(), 7 : LeechSeed(),
							  10 : VineWhip(), 14 : PoisonPowder(), 15 : SleepPowder(),
							  22 : RazorLeaf(), 29 : SweetScent(), 41 : Growth(),
							  53 : Synthesis(), 65 : Solarbeam()}

class Charmander(PocketMonster):

	def __init__(self):
		self.name = 'Charmander'
		baseHp = 39
		baseAttack = 52
		baseDefense = 43
		baseSpAttack = 60
		baseSpDefense = 50
		baseSpeed = 65
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 4
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fire]
		self.weight = 8.5 # kg
		self.height = 0.6 # m
		self.femaleRate = 13 # percent

		self.evolvesAt = 16
		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 65

		self.levelUpAttacks = {1 : Scratch(), 3 : Growl(), 7 : Ember(),
							  13 : MetalClaw(), 19 : Smokescreen(), 25 : ScaryFace(),
							  31 : Flamethrower(), 37 : Slash(), 43 : DragonRage(),
							  49 : FireSpin()}

	def evolve(self):
		return Charmeleon()

class Charmeleon(PocketMonster):

	def __init__(self):
		self.name = 'Charmeleon'
		baseHp = 58
		baseAttack = 64
		baseDefense = 58
		baseSpAttack = 80
		baseSpDefense = 65
		baseSpeed = 80
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 5
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fire]
		self.weight = 19.0 # kg
		self.height = 1.1 # m
		self.femaleRate = 13 # percent

		self.evolvesAt = 36
		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 142

		self.levelUpAttacks = {1 : Scratch(), 3 : Growl(), 7 : Ember(),
							  13 : MetalClaw(), 20 : Smokescreen(), 27 : ScaryFace(),
							  34 : Flamethrower(), 41 : Slash(), 48 : DragonRage(),
							  55 : FireSpin()}

		

	def evolve(self):
		return Charizard()

class Charizard(PocketMonster):

	def __init__(self):
		self.name = 'Charizard'
		baseHp = 78
		baseAttack = 84
		baseDefense = 78
		baseSpAttack = 109
		baseSpDefense = 85
		baseSpeed = 100
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 6
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fire, flying]
		self.weight = 90.5 # kg
		self.height = 1.7 # m
		self.femaleRate = 13 # percent

		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 209

		self.levelUpAttacks = {1 : Scratch(), 3 : Growl(), 7 : Ember(),
							  13 : MetalClaw(), 19 : Smokescreen(), 25 : ScaryFace(),
							  31 : Flamethrower(), 36 : WingAttack(), 44 : Slash(), 
							  54 : DragonRage(), 64 : FireSpin()}

		
class Squirtle(PocketMonster):

	def __init__(self):
		self.name = 'Squirtle'
		baseHp = 44
		baseAttack = 48
		baseDefense = 65
		baseSpAttack = 50
		baseSpDefense = 64
		baseSpeed = 43
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 7
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 9.0 # kg
		self.height = 0.5 # m
		self.femaleRate = 13 # percent

		self.evolvesAt = 16
		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 66

		self.levelUpAttacks = {1 : Tackle(), 4 : TailWhip(), 7 : Bubble(),
							  10 : Withdraw(), 13 : WaterGun(), 18 : Bite(),
							  23 : RapidSpin(), 28 : Protect(), 33 : RainDance(),
							  40 : SkullBash(), 47 : HydroPump()}

	def evolve(self):
		return Wartortle()

class Wartortle(PocketMonster):

	def __init__(self):
		self.name = 'Wartortle'
		baseHp = 59
		baseAttack = 63
		baseDefense = 80
		baseSpAttack = 65
		baseSpDefense = 80
		baseSpeed = 58
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 8
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 22.5 # kg
		self.height = 1.0 # m
		self.femaleRate = 13 # percent

		self.evolvesAt = 36
		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 143

		self.levelUpAttacks = {1 : Tackle(), 4 : TailWhip(), 7 : Bubble(),
							  10 : Withdraw(), 13 : WaterGun(), 19 : Bite(),
							  25 : RapidSpin(), 31 : Protect(), 37 : RainDance(),
							  45 : SkullBash(), 53 : HydroPump()}

	def evolve(self):
		return Blastoise()


class Blastoise(PocketMonster):

	def __init__(self):
		self.name = 'Blastoise'
		baseHp = 79
		baseAttack = 83
		baseDefense = 100
		baseSpAttack = 85
		baseSpDefense = 105
		baseSpeed = 78
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 9
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 85.5 # kg
		self.height = 1.6 # m
		self.femaleRate = 13 # percent

		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 210

		self.levelUpAttacks = {1 : Tackle(), 4 : TailWhip(), 7 : Bubble(),
							  10 : Withdraw(), 13 : WaterGun(), 19 : Bite(),
							  25 : RapidSpin(), 31 : Protect(), 42 : RainDance(),
							  55 : SkullBash(), 68 : HydroPump()}

class Caterpie(PocketMonster):

	def __init__(self):
		self.name = 'Caterpie'
		baseHp = 45
		baseAttack = 30
		baseDefense = 35
		baseSpAttack = 20
		baseSpDefense = 20
		baseSpeed = 45
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 10
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [bug]
		self.weight = 2.9 # kg
		self.height = 0.3 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 7
		self.expGroup = mFast
		self.catchRate = 255
		self.baseExpYield = 53

		self.levelUpAttacks = {1 : Tackle(), 2 : StringShot()}

	def evolve(self):
		return Metapod()

class Metapod(PocketMonster):

	def __init__(self):
		self.name = 'Metapod'
		baseHp = 50
		baseAttack = 20
		baseDefense = 55
		baseSpAttack = 25
		baseSpDefense = 25
		baseSpeed = 30
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 11
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [bug]
		self.weight = 9.9 # kg
		self.height = 0.7 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 10
		self.expGroup = mFast
		self.catchRate = 120
		self.baseExpYield = 72

		self.levelUpAttacks = {1 : Tackle(), 2 : StringShot(), 7 : Harden()}

	def evolve(self):
		return Butterfree()

class Butterfree(PocketMonster):

	def __init__(self):
		self.name = 'Butterfree'
		baseHp = 60
		baseAttack = 45
		baseDefense = 50
		baseSpAttack = 80
		baseSpDefense = 80
		baseSpeed = 70
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 12
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [bug, flying]
		self.weight = 32.0 # kg
		self.height = 1.1 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 160

		self.levelUpAttacks = {10 : Confusion(), 13 : PoisonPowder(), 14 : StunSpore(),
							   15 : SleepPowder(), 18 : Supersonic(), 23 : Whirlwind(),
							   28 : Gust(), 34 : Psybeam(), 40 : Safeguard(),
							   47 : SilverWind()}

class Weedle(PocketMonster):

	def __init__(self):
		self.name = 'Weedle'
		baseHp = 40
		baseAttack = 35
		baseDefense = 30
		baseSpAttack = 20
		baseSpDefense = 20
		baseSpeed = 50
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 13
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [bug, poison]
		self.weight = 3.2 # kg
		self.height = 0.3 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 7
		self.expGroup = mFast
		self.catchRate = 255
		self.baseExpYield = 52

		self.levelUpAttacks = {1 : PoisonSting(), 2 : StringShot()}

	def evolve(self):
		return Kakuna()

class Kakuna(PocketMonster):

	def __init__(self):
		self.name = 'Kakuna'
		baseHp = 45
		baseAttack = 25
		baseDefense = 50
		baseSpAttack = 25
		baseSpDefense = 25
		baseSpeed = 35
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 14
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [bug, poison]
		self.weight = 10.0 # kg
		self.height = 0.0 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 10
		self.expGroup = mFast
		self.catchRate = 120
		self.baseExpYield = 71

		self.levelUpAttacks = {1 : PoisonSting(), 2 : StringShot(), 7 : Harden()}

	def evolve(self):
		return Beedrill()

class Beedrill(PocketMonster):

	def __init__(self):
		self.name = 'Beedrill'
		baseHp = 65
		baseAttack = 80
		baseDefense = 40
		baseSpAttack = 45
		baseSpDefense = 80
		baseSpeed = 75
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 15
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [bug, poison]
		self.weight = 29.5 # kg
		self.height = 1.0 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 159

		self.levelUpAttacks = {10 : FuryAttack(), 15 : FocusEnergy(), 20 : Twineedle(),
							   25 : Rage(), 30 : Pursuit(), 35 : PinMissile(),
							   40 : Agility(), 45 : Endeavor()}

	def evolve(self):
		return Beedrill()

class Pidgey(PocketMonster):

	def __init__(self):
		self.name = 'Pidgey'
		baseHp = 40
		baseAttack = 45
		baseDefense = 40
		baseSpAttack = 35
		baseSpDefense = 35
		baseSpeed = 56
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 16
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal, flying]
		self.weight = 1.8 # kg
		self.height = 0.3 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 18
		self.expGroup = mSlow
		self.catchRate = 255
		self.baseExpYield = 55

		self.levelUpAttacks = {1 : Tackle(), 5 : SandAttack(), 9 : Gust(),
							   13 : QuickAttack(), 19 : Whirlwind(), 
							   25 : WingAttack(), 31 : Featherdance(),
							   39 : Agility(), 47 : MirrorMove()}

	def evolve(self):
		return Pidgeotto()

class Pidgeotto(PocketMonster):

	def __init__(self):
		self.name = 'Pidgeotto'
		baseHp = 63
		baseAttack = 60
		baseDefense = 55
		baseSpAttack = 50
		baseSpDefense = 50
		baseSpeed = 71
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 17
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal, flying]
		self.weight = 30.0 # kg
		self.height = 1.1 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 36
		self.expGroup = mSlow
		self.catchRate = 120
		self.baseExpYield = 113

		self.levelUpAttacks = {1 : Tackle(), 5 : SandAttack(), 9 : Gust(),
							   13 : QuickAttack(), 20 : Whirlwind(), 
							   27 : WingAttack(), 34 : Featherdance(),
							   43 : Agility(), 52 : MirrorMove()}

	def evolve(self):
		return Pidgeot()

class Pidgeot(PocketMonster):

	def __init__(self):
		self.name = 'Pidgeot'
		baseHp = 83
		baseAttack = 80
		baseDefense = 75
		baseSpAttack = 70
		baseSpDefense = 70
		baseSpeed = 91
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 18
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal, flying]
		self.weight = 39.5 # kg
		self.height = 1.5 # m
		self.femaleRate = 50 # percent

		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 172

		self.levelUpAttacks = {1 : Tackle(), 5 : SandAttack(), 9 : Gust(),
							   13 : QuickAttack(), 20 : Whirlwind(), 
							   27 : WingAttack(), 34 : Featherdance(),
							   48 : Agility(), 62 : MirrorMove()}

class Rattata(PocketMonster):

	def __init__(self):
		self.name = 'Rattata'
		baseHp = 30
		baseAttack = 56
		baseDefense = 35
		baseSpAttack = 25
		baseSpDefense = 35
		baseSpeed = 72
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 19
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 3.5 # kg
		self.height = 0.3 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 20
		self.expGroup = mFast
		self.catchRate = 255
		self.baseExpYield = 57

		self.levelUpAttacks = {1 : Tackle(), 2 : TailWhip(), 7 : QuickAttack(),
							   13 : HyperFang(), 20 : FocusEnergy(), 
							   27 : Pursuit(), 34 : SuperFang(),
							   41 : Endeavor()}

	def evolve(self):
		return Raticate()

class Raticate(PocketMonster):

	def __init__(self):
		self.name = 'Raticate'
		baseHp = 55
		baseAttack = 81
		baseDefense = 60
		baseSpAttack = 50
		baseSpDefense = 70
		baseSpeed = 97
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 20
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 18.5 # kg
		self.height = 0.7 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 127
		self.baseExpYield = 116

		self.levelUpAttacks = {1 : Tackle(), 2 : TailWhip(), 7 : QuickAttack(),
							   13 : HyperFang(), 20 : ScaryFace(), 
							   30 : Pursuit(), 40 : SuperFang(),
							   50 : Endeavor()}


class Spearow(PocketMonster):

	def __init__(self):
		self.name = 'Spearow'
		baseHp = 40
		baseAttack = 60
		baseDefense = 30
		baseSpAttack = 31
		baseSpDefense = 31
		baseSpeed = 70
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 21
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal, flying]
		self.weight = 2.0 # kg
		self.height = 0.3 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 20
		self.expGroup = mFast
		self.catchRate = 255
		self.baseExpYield = 58

		self.levelUpAttacks = {1 : Peck(), 2 : Growl(), 7 : Leer(),
							   13 : FuryAttack(), 19 : Pursuit(), 
							   25 : AerialAce(), 31 : MirrorMove(),
							   37 : DrillPeck(), 43 : Agility()}

	def evolve(self):
		return Fearow()

class Fearow(PocketMonster):

	def __init__(self):
		self.name = 'Fearow'
		baseHp = 65
		baseAttack = 90
		baseDefense = 65
		baseSpAttack = 61
		baseSpDefense = 61
		baseSpeed = 100
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 22
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal, flying]
		self.weight = 38.0 # kg
		self.height = 1.2 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 90
		self.baseExpYield = 162

		self.levelUpAttacks = {1 : Peck(), 2 : Growl(), 7 : Leer(),
							   13 : FuryAttack(), 26 : Pursuit(), 
							   32 : MirrorMove(),
							   40 : DrillPeck(), 47 : Agility()}

class Ekans(PocketMonster):

	def __init__(self):
		self.name = 'Ekans'
		baseHp = 35
		baseAttack = 60
		baseDefense = 44
		baseSpAttack = 40
		baseSpDefense = 54
		baseSpeed = 55
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 23
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [poison]
		self.weight = 6.9 # kg
		self.height = 2.0 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 22
		self.expGroup = mFast
		self.catchRate = 255
		self.baseExpYield = 62

		self.levelUpAttacks = {1 : Wrap(), 2 : Leer(), 8 : PoisonSting(),
							   13 : Bite(), 20 : Glare(), 
							   25 : Screech(), 32 : Acid(),
							   37 : Stockpile(), 38 : Swallow(),
							   39 : SpitUp(), 44 : Haze()}

	def evolve(self):
		return Arbok()

class Arbok(PocketMonster):

	def __init__(self):
		self.name = 'Arbok'
		baseHp = 60
		baseAttack = 85
		baseDefense = 69
		baseSpAttack = 65
		baseSpDefense = 79
		baseSpeed = 80
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 24
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [poison]
		self.weight = 65.0 # kg
		self.height = 3.5 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 90
		self.baseExpYield = 147

		self.levelUpAttacks = {1 : Wrap(), 2 : Leer(), 8 : PoisonSting(),
							   13 : Bite(), 20 : Glare(), 
							   28 : Screech(), 38 : Acid(),
							   46 : Stockpile(), 47 : Swallow(),
							   48 : SpitUp(), 56 : Haze()}

class Pikachu(PocketMonster):

	def __init__(self):
		self.name = 'Pikachu'
		baseHp = 35
		baseAttack = 55
		baseDefense = 30
		baseSpAttack = 50
		baseSpDefense = 40
		baseSpeed = 90
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 25
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [electric]
		self.weight = 6.0 # kg
		self.height = 0.4 # m
		self.femaleRate = 50 # percent

		self.evolvesWith = 'thunderstone'
		self.expGroup = mFast
		self.catchRate = 190
		self.baseExpYield = 82

		self.levelUpAttacks = {1 : Thundershock(), 2 : Growl(), 6 : TailWhip(),
							   11 : QuickAttack(), 15 : DoubleTeam(), 
							   20 : Slam(), 26 : Thunderbolt(),
							   33 : Agility(), 41 : Thunder(),
							   50 : LightScreen()}

	def evolve(self):
		return Raichu()