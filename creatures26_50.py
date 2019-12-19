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
from expTable import erratic, fast, mFast, mSlow, slow, fluctuating
from creatures51_75 import Dugtrio

class Raichu(PocketMonster):

	def __init__(self):
		self.name = 'Raichu'
		baseHp = 35
		baseAttack = 55
		baseDefense = 30
		baseSpAttack = 50
		baseSpDefense = 40
		baseSpeed = 90
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 26
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [electric]
		self.weight = 30.0 # kg
		self.height = 0.8 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 75
		self.baseExpYield = 122

		self.levelUpAttacks = {1 : Thundershock(), 2 : TailWhip(),
							   3 : QuickAttack(), 4 : Thunderbolt()}

class Sandshrew(PocketMonster):

	def __init__(self):
		self.name = 'Sandshrew'
		baseHp = 50
		baseAttack = 75
		baseDefense = 85
		baseSpAttack = 20
		baseSpDefense = 30
		baseSpeed = 40
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 27
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [ground]
		self.weight = 12.0 # kg
		self.height = 0.6 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 22
		self.expGroup = mFast
		self.catchRate = 255
		self.baseExpYield = 93

		self.levelUpAttacks = {1 : Scratch(), 6 : DefenseCurl(), 11 : SandAttack(),
							   17 : PoisonSting(), 23 : Slash(), 
							   30 : Swift(), 37 : FurySwipes(),
							   45 : SandTomb(), 53 : Sandstorm()}


	def evolve(self):
		return Sandslash()

class Sandslash(PocketMonster):

	def __init__(self):
		self.name = 'Sandslash'
		baseHp = 75
		baseAttack = 100
		baseDefense = 110
		baseSpAttack = 45
		baseSpDefense = 55
		baseSpeed = 65
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 28
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [ground]
		self.weight = 29.5 # kg
		self.height = 1.0 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 90
		self.baseExpYield = 163

		self.levelUpAttacks = {1 : Scratch(), 6 : DefenseCurl(), 11 : SandAttack(),
							   17 : PoisonSting(), 24 : Slash(), 
							   33 : Swift(), 42 : FurySwipes(),
							   52 : SandTomb(), 62 : Sandstorm()}

class NidoranF(PocketMonster):

	def __init__(self):
		self.name = 'Nidoran'
		baseHp = 55
		baseAttack = 47
		baseDefense = 52
		baseSpAttack = 40
		baseSpDefense = 40
		baseSpeed = 41
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 29
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [poison]
		self.weight = 7.0 # kg
		self.height = 0.4 # m
		self.femaleRate = 100 # percent

		self.evolvesAt = 16
		self.expGroup = mSlow
		self.catchRate = 235
		self.baseExpYield = 59

		self.levelUpAttacks = {1 : Scratch(), 2 : Growl(), 8 : TailWhip(),
							   12 : DoubleKick(), 17 : PoisonSting(), 
							   20 : Bite(), 23 : HelpingHand(),
							   30 : FurySwipes(), 38 : Flatter(),
							   47 : Crunch() }

	def evolve(self):
		return Nidorina()

class Nidorina(PocketMonster):

	def __init__(self):
		self.name = 'Nidorina'
		baseHp = 70
		baseAttack = 62
		baseDefense = 67
		baseSpAttack = 55
		baseSpDefense = 55
		baseSpeed = 56
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 30
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [poison]
		self.weight = 20.0 # kg
		self.height = 0.8 # m
		self.femaleRate = 100 # percent

		self.evolvesWith = 'moonstone'
		self.expGroup = mSlow
		self.catchRate = 120
		self.baseExpYield = 117

		self.levelUpAttacks = {1 : Scratch(), 2 : Growl(), 8 : TailWhip(),
							   12 : DoubleKick(), 18 : PoisonSting(), 
							   22 : Bite(), 26 : HelpingHand(),
							   34 : FurySwipes(), 43 : Flatter(),
							   53 : Crunch() }

	def evolve(self):
		return Nidoqueen()

class Nidoqueen(PocketMonster):

	def __init__(self):
		self.name = 'Nidoqueen'
		baseHp = 90
		baseAttack = 82
		baseDefense = 87
		baseSpAttack = 75
		baseSpDefense = 85
		baseSpeed = 76
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 31
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [poison, ground]
		self.weight = 60.0 # kg
		self.height = 1.3 # m
		self.femaleRate = 100 # percent

		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 194

		self.levelUpAttacks = {1 : Scratch(), 2 : Growl(), 8 : TailWhip(),
							   12 : DoubleKick(), 18 : PoisonSting(), 
							   22 : BodySlam(), 43 : Superpower()}

class NidoranM(PocketMonster):

	def __init__(self):
		self.name = 'Nidoran'
		baseHp = 46
		baseAttack = 57
		baseDefense = 40
		baseSpAttack = 40
		baseSpDefense = 40
		baseSpeed = 50
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 32
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [poison]
		self.weight = 9.0 # kg
		self.height = 0.5 # m
		self.femaleRate = 0 # percent

		self.evolvesAt = 16
		self.expGroup = mSlow
		self.catchRate = 235
		self.baseExpYield = 60

		self.levelUpAttacks = {1 : Peck(), 2 : Leer(), 8 : FocusEnergy(),
							   12 : DoubleKick(), 17 : PoisonSting(), 
							   20 : HornAttack(), 23 : HelpingHand(),
							   30 : FuryAttack(), 38 : Flatter(),
							   47 : HornDrill() }

	def evolve(self):
		return Nidorino()

class Nidorino(PocketMonster):

	def __init__(self):
		self.name = 'Nidorino'
		baseHp = 61
		baseAttack = 72
		baseDefense = 57
		baseSpAttack = 55
		baseSpDefense = 55
		baseSpeed = 65
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 33
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [poison]
		self.weight = 19.5 # kg
		self.height = 0.9 # m
		self.femaleRate = 0 # percent

		self.evolvesWith = 'moonstone'
		self.expGroup = mSlow
		self.catchRate = 120
		self.baseExpYield = 118

		self.levelUpAttacks = {1 : Peck(), 2 : Leer(), 8 : FocusEnergy(),
							   12 : DoubleKick(), 17 : PoisonSting(), 
							   22 : HornAttack(), 26 : HelpingHand(),
							   34 : FuryAttack(), 43 : Flatter(),
							   53 : HornDrill() }

	def evolve(self):
		return Nidoking()

class Nidoking(PocketMonster):

	def __init__(self):
		self.name = 'Nidoking'
		baseHp = 81
		baseAttack = 92
		baseDefense = 77
		baseSpAttack = 85
		baseSpDefense = 75
		baseSpeed = 85
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 34
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [poison, ground]
		self.weight = 62.0 # kg
		self.height = 1.4 # m
		self.femaleRate = 0 # percent

		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 195

		self.levelUpAttacks = {1 : Peck(), 2 : Leer(), 8 : FocusEnergy(),
							   12 : DoubleKick(), 17 : PoisonSting(), 
							   23 : Thrash() }

class Clefairy(PocketMonster):

	def __init__(self):
		self.name = 'Clefairy'
		baseHp = 70
		baseAttack = 45
		baseDefense = 48
		baseSpAttack = 60
		baseSpDefense = 65
		baseSpeed = 35
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 35
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 7.5 # kg
		self.height = 0.6 # m
		self.femaleRate = 75 # percent

		self.evolvesWith = 'moonstone'
		self.expGroup = fast
		self.catchRate = 150
		self.baseExpYield = 68

		self.levelUpAttacks = {1 : Pound(), 2 : Growl(), 5 : Encore(),
							   9 : Sing(), 13 : Doubleslap(), 
							   17 : FollowMe(), 21 : Minimize(),
							   25 : DefenseCurl(), 29 : Metronome(),
							   33 : CosmicPower(), 37 : Moonlight(),
							   41 : LightScreen(), 45 : MeteorMash() }

	def evolve(self):
		return Clefable()

class Clefable(PocketMonster):

	def __init__(self):
		self.name = 'Clefable'
		baseHp = 95
		baseAttack = 70
		baseDefense = 73
		baseSpAttack = 85
		baseSpDefense = 90
		baseSpeed = 60
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 36
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 40.0 # kg
		self.height = 1.3 # m
		self.femaleRate = 75 # percent

		self.evolvesWith = 'moonstone'
		self.expGroup = fast
		self.catchRate = 25
		self.baseExpYield = 129

		self.levelUpAttacks = {1 : Sing(), 2 : Doubleslap(), 3 : Minimize(),
							   4 : Metronome()}

class Vulpix(PocketMonster):

	def __init__(self):
		self.name = 'Vulpix'
		baseHp = 38
		baseAttack = 41
		baseDefense = 40
		baseSpAttack = 50
		baseSpDefense = 65
		baseSpeed = 65
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 37
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fire]
		self.weight = 9.9 # kg
		self.height = 0.6 # m
		self.femaleRate = 75 # percent

		self.evolvesWith = 'firestone'
		self.expGroup = mFast
		self.catchRate = 190
		self.baseExpYield = 63

		self.levelUpAttacks = {1 : Ember(), 5 : TailWhip(), 9 : Roar(),
							   13 : QuickAttack(), 17 : WillOWisp(), 
							   21 : ConfuseRay(), 25 : Imprison(),
							   29 : Flamethrower(), 33 : Safeguard(),
							   37 : Grudge(), 41 : FireSpin()}

	def evolve(self):
		return Ninetails()

class Ninetales(PocketMonster):

	def __init__(self):
		self.name = 'Ninetales'
		baseHp = 73
		baseAttack = 76
		baseDefense = 75
		baseSpAttack = 81
		baseSpDefense = 100
		baseSpeed = 100
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 38
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fire]
		self.weight = 19.9 # kg
		self.height = 1.1 # m
		self.femaleRate = 75 # percent

		self.expGroup = mFast
		self.catchRate = 75
		self.baseExpYield = 178

		self.levelUpAttacks = {1 : Ember(), 2 : QuickAttack(), 3 : ConfuseRay(),
							   4 : Safeguard(), 45 : FireSpin()}

class Jigglypuff(PocketMonster):

	def __init__(self):
		self.name = 'Jigglypuff'
		baseHp = 115
		baseAttack = 45
		baseDefense = 20
		baseSpAttack = 45
		baseSpDefense = 25
		baseSpeed = 20
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 39
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 5.5 # kg
		self.height = 0.5 # m
		self.femaleRate = 75 # percent

		self.evolvesWith = 'moonstone'
		self.expGroup = fast
		self.catchRate = 170
		self.baseExpYield = 76

		self.levelUpAttacks = {1 : Sing(), 4 : DefenseCurl(), 9 : Pound(),
							   14 : Disable(), 19 : Rollout(), 
							   24 : Doubleslap(), 29 : Rest(),
							   34 : BodySlam(), 39 : Mimic(),
							   44 : HyperVoice(), 49 : DoubleEdge()}

	def evolve(self):
		return Wigglytuff()

class Wigglytuff(PocketMonster):

	def __init__(self):
		self.name = 'Wigglytuff'
		baseHp = 140
		baseAttack = 70
		baseDefense = 45
		baseSpAttack = 75
		baseSpDefense = 50
		baseSpeed = 45
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 40
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 12.0 # kg
		self.height = 1.0 # m
		self.femaleRate = 75 # percent

		self.expGroup = fast
		self.catchRate = 50
		self.baseExpYield = 109

		self.levelUpAttacks = {1 : Sing(), 2 : Disable(), 3 : DefenseCurl(),
							   4 : Doubleslap()}

class Zubat(PocketMonster):

	def __init__(self):
		self.name = 'Zubat'
		baseHp = 40
		baseAttack = 45
		baseDefense = 35
		baseSpAttack = 30
		baseSpDefense = 40
		baseSpeed = 55
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 41
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [poison, flying]
		self.weight = 7.5 # kg
		self.height = 0.8 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 22
		self.expGroup = mFast
		self.catchRate = 255
		self.baseExpYield = 54

		self.levelUpAttacks = {1 : LeechLife(), 6 : Astonish(),
							   11 : Supersonic(), 16 : Bite(), 
							   21 : WingAttack(), 26 : ConfuseRay(),
							   31 : AirCutter(), 36 : MeanLook(),
							   41 : PoisonFang(), 46 : Haze()}

	def evolve(self):
		return Golbat()

class Golbat(PocketMonster):

	def __init__(self):
		self.name = 'Golbat'
		baseHp = 75
		baseAttack = 80
		baseDefense = 70
		baseSpAttack = 65
		baseSpDefense = 75
		baseSpeed = 90
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 42
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [poison, flying]
		self.weight = 55.0 # kg
		self.height = 1.6 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 90
		self.baseExpYield = 171

		self.levelUpAttacks = {1 : LeechLife(), 2 : Screech(), 6 : Astonish(),
							   11 : Supersonic(), 16 : Bite(), 
							   21 : WingAttack(), 28 : ConfuseRay(),
							   35 : AirCutter(), 42 : MeanLook(),
							   49 : PoisonFang(), 56 : Haze()}

class Oddish(PocketMonster):

	def __init__(self):
		self.name = 'Oddish'
		baseHp = 45
		baseAttack = 50
		baseDefense = 55
		baseSpAttack = 75
		baseSpDefense = 65
		baseSpeed = 30
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 43
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [grass, poison]
		self.weight = 5.4 # kg
		self.height = 0.5 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 21
		self.expGroup = mSlow
		self.catchRate = 255
		self.baseExpYield = 78

		self.levelUpAttacks = {1 : Absorb(), 7 : SweetScent(),
							   14 : PoisonPowder(), 16 : StunSpore(), 
							   18 : SleepPowder(), 23 : Acid(),
							   32 : Moonlight(), 39 : PedalDance()}

	def evolve(self):
		return Gloom()

class Gloom(PocketMonster):

	def __init__(self):
		self.name = 'Gloom'
		baseHp = 60
		baseAttack = 65
		baseDefense = 70
		baseSpAttack = 85
		baseSpDefense = 75
		baseSpeed = 40
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 44
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [grass, poison]
		self.weight = 8.6 # kg
		self.height = 0.8 # m
		self.femaleRate = 50 # percent

		self.evolvesWith = 'leafstone'
		self.expGroup = mSlow
		self.catchRate = 120
		self.baseExpYield = 132

		self.levelUpAttacks = {1 : Absorb(), 7 : SweetScent(),
							   14 : PoisonPowder(), 16 : StunSpore(), 
							   18 : SleepPowder(), 24 : Acid(),
							   35 : Moonlight(), 44 : PedalDance()}

	def evolve(self):
		return Vileplume()

class Vileplume(PocketMonster):

	def __init__(self):
		self.name = 'Vileplume'
		baseHp = 75
		baseAttack = 80
		baseDefense = 85
		baseSpAttack = 100
		baseSpDefense = 90
		baseSpeed = 50
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 45
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [grass, poison]
		self.weight = 18.6 # kg
		self.height = 1.2 # m
		self.femaleRate = 50 # percent

		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 184

		self.levelUpAttacks = {1 : Absorb(), 2 : Aromatherapy(),
							   3 : StunSpore(), 4 : MegaDrain(),
							   44 : PedalDance()}

class Paras(PocketMonster):

	def __init__(self):
		self.name = 'Paras'
		baseHp = 35
		baseAttack = 70
		baseDefense = 55
		baseSpAttack = 45
		baseSpDefense = 55
		baseSpeed = 25
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 46
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [bug, grass]
		self.weight = 5.4 # kg
		self.height = 0.3 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 24
		self.expGroup = mFast
		self.catchRate = 190
		self.baseExpYield = 70

		self.levelUpAttacks = {1 : Scratch(), 7 : StunSpore(),
							   13 : PoisonPowder(), 19 : LeechLife(), 
							   25 : Spore(), 31 : Slash(),
							   37 : Growth(), 43 : GigaDrain(),
							   49 : Aromatherapy()}

	def evolve(self):
		return Parasect()

class Parasect(PocketMonster):

	def __init__(self):
		self.name = 'Parasect'
		baseHp = 60
		baseAttack = 95
		baseDefense = 80
		baseSpAttack = 60
		baseSpDefense = 80
		baseSpeed = 30
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 47
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [bug, grass]
		self.weight = 29.5 # kg
		self.height = 1.0 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 75
		self.baseExpYield = 128

		self.levelUpAttacks = {1 : Scratch(), 7 : StunSpore(),
							   13 : PoisonPowder(), 19 : LeechLife(), 
							   27 : Spore(), 35 : Slash(),
							   43 : Growth(), 51 : GigaDrain(),
							   59 : Aromatherapy()}


class Venonat(PocketMonster):

	def __init__(self):
		self.name = 'Venonat'
		baseHp = 60
		baseAttack = 55
		baseDefense = 50
		baseSpAttack = 40
		baseSpDefense = 55
		baseSpeed = 45
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 48
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [bug, poison]
		self.weight = 30.0 # kg
		self.height = 1.0 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 31
		self.expGroup = mFast
		self.catchRate = 190
		self.baseExpYield = 75

		self.levelUpAttacks = {1 : Tackle(), 2 : Disable(),
							   3 : Foresight(), 9 : Supersonic(), 
							   17 : Confusion(), 20 : PoisonPowder(),
							   25 : LeechLife(), 28 : StunSpore(),
							   33 : Psybeam(), 36 : SleepPowder(),
							   41 : Psychic()}

	def evolve(self):
		return Venomoth()

class Venomoth(PocketMonster):

	def __init__(self):
		self.name = 'Venomoth'
		baseHp = 70
		baseAttack = 65
		baseDefense = 60
		baseSpAttack = 90
		baseSpDefense = 75
		baseSpeed = 90
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 49
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [bug, poison]
		self.weight = 12.5 # kg
		self.height = 1.5 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 75
		self.baseExpYield = 138

		self.levelUpAttacks = {1 : Tackle(), 2 : Disable(),
							   3 : Foresight(), 9 : Supersonic(), 
							   17 : Confusion(), 20 : PoisonPowder(),
							   25 : LeechLife(), 28 : StunSpore(),
							   36 : Psybeam(), 42 : SleepPowder(),
							   52 : Psychic()}

class Diglett(PocketMonster):

	def __init__(self):
		self.name = 'Diglett'
		baseHp = 10
		baseAttack = 55
		baseDefense = 25
		baseSpAttack = 35
		baseSpDefense = 45
		baseSpeed = 95
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 50
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [ground]
		self.weight = 0.8 # kg
		self.height = 0.2 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 26
		self.expGroup = mFast
		self.catchRate = 255
		self.baseExpYield = 81

		self.levelUpAttacks = {1 : SandAttack(), 2 : Scratch(),
							   5 : Growl(), 9 : Magnitude(), 
							   17 : Dig(), 21 : FurySwipes(),
							   25 : MudSlap(), 33 : Slash(),
							   41 : Earthquake(), 49 : Fissure()}

	def evolve(self):
		return Dugtrio()

