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
from creatures101_125 import Electrode

class Golem(PocketMonster):

	def __init__(self):
		self.name = 'Golem'
		baseHp = 80
		baseAttack = 110
		baseDefense = 130
		baseSpAttack = 55
		baseSpDefense = 65
		baseSpeed = 45
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 76
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [rock, ground]
		self.weight = 300.0 # kg
		self.height = 1.4 # m
		self.femaleRate = 50 # percent

		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 177

		self.levelUpAttacks = {1 : Tackle(), 2 : DefenseCurl(),
							   6 : MudSport(), 11 : RockThrow(), 
							   16 : Magnitude(), 21 : Selfdestruct(),
							   29 : Rollout(), 37 : RockBlast(),
							   45 : Earthquake(), 53 : Explosion(),
							   62 : DoubleEdge()}

class Ponyta(PocketMonster):

	def __init__(self):
		self.name = 'Ponyta'
		baseHp = 50
		baseAttack = 85
		baseDefense = 55
		baseSpAttack = 65
		baseSpDefense = 65
		baseSpeed = 90
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 77
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fire]
		self.weight = 30.0 # kg
		self.height = 1.0 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 40
		self.expGroup = mFast
		self.catchRate = 190
		self.baseExpYield = 152

		self.levelUpAttacks = {1 : QuickAttack(), 5 : Growl(),
							   9 : TailWhip(), 14 : Ember(), 
							   19 : Stomp(), 25 : FireSpin(),
							   31 : TakeDown(), 38 : Agility(),
							   45 : Bounce(), 53 : FireBlast()}

	def evolve(self):
		return Rapidash()

class Rapidash(PocketMonster):

	def __init__(self):
		self.name = 'Rapidash'
		baseHp = 65
		baseAttack = 100
		baseDefense = 70
		baseSpAttack = 80
		baseSpDefense = 80
		baseSpeed = 105
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 78
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fire]
		self.weight = 95.0 # kg
		self.height = 1.7 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 60
		self.baseExpYield = 192

		self.levelUpAttacks = {1 : QuickAttack(), 5 : Growl(),
							   9 : TailWhip(), 14 : Ember(), 
							   19 : Stomp(), 25 : FireSpin(),
							   31 : TakeDown(), 38 : Agility(), 40 : FuryAttack(),
							   50 : Bounce(), 63 : FireBlast()}

class Slowpoke(PocketMonster):

	def __init__(self):
		self.name = 'Slowpoke'
		baseHp = 90
		baseAttack = 65
		baseDefense = 65
		baseSpAttack = 40
		baseSpDefense = 40
		baseSpeed = 15
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 79
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water, psychic]
		self.weight = 36.0 # kg
		self.height = 1.2 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 37
		self.expGroup = mFast
		self.catchRate = 190
		self.baseExpYield = 99

		self.levelUpAttacks = {1 : Curse(), 2 : Yawn(),
							   3 : Tackle(), 6 : Growl(), 
							   13 : WaterGun(), 17 : Confusion(),
							   24 : Disable(), 29 : Headbutt(),
							   36 : Amnesia(), 40 : Psychic(), 47 : PsychUp()}

	def evolve(self):
		return Slowbro()

class Slowbro(PocketMonster):

	def __init__(self):
		self.name = 'Slowbro'
		baseHp = 95
		baseAttack = 75
		baseDefense = 110
		baseSpAttack = 100
		baseSpDefense = 80
		baseSpeed = 30
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 80
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water, psychic]
		self.weight = 78.5 # kg
		self.height = 1.6 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 75
		self.baseExpYield = 164

		self.levelUpAttacks = {1 : Curse(), 2 : Yawn(),
							   3 : Tackle(), 6 : Growl(), 
							   13 : WaterGun(), 17 : Confusion(),
							   24 : Disable(), 29 : Headbutt(), 36 : Amnesia(),
							   37 : Withdraw(), 44 : Psychic(), 55 : PsychUp()}

class Magnemite(PocketMonster):

	def __init__(self):
		self.name = 'Magnemite'
		baseHp = 25
		baseAttack = 35
		baseDefense = 70
		baseSpAttack = 95
		baseSpDefense = 55
		baseSpeed = 45
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 81
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [electric, steel]
		self.weight = 6.0 # kg
		self.height = 0.3 # m
		self.femaleRate = -1 # genderless

		self.evolvesAt = 30
		self.expGroup = mFast
		self.catchRate = 190
		self.baseExpYield = 89

		self.levelUpAttacks = {1 : MetalSound(), 2 : Tackle(),
							   6 : Thundershock(), 11 : Supersonic(), 
							   16 : Sonicboom(), 21 : ThunderWave(),
							   26 : Spark(), 32 : LockOn(),
							   38 : Swift(), 44 : Screech(), 50 : ZapCannon()}

	def evolve(self):
		return Magneton()

class Magneton(PocketMonster):

	def __init__(self):
		self.name = 'Magneton'
		baseHp = 50
		baseAttack = 60
		baseDefense = 95
		baseSpAttack = 120
		baseSpDefense = 70
		baseSpeed = 70
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 82
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [electric, steel]
		self.weight = 60.0 # kg
		self.height = 1.0 # m
		self.femaleRate = -1 # genderless

		self.expGroup = mFast
		self.catchRate = 60
		self.baseExpYield = 161

		self.levelUpAttacks = {1 : MetalSound(), 2 : Tackle(),
							   6 : Thundershock(), 11 : Supersonic(), 
							   16 : Sonicboom(), 21 : ThunderWave(),
							   26 : Spark(), 35 : LockOn(),
							   44 : TriAttack(), 53 : Screech(), 62 : ZapCannon()}

class Farfetchd(PocketMonster):

	def __init__(self):
		self.name = 'Farfetch\'d'
		baseHp = 52
		baseAttack = 65
		baseDefense = 55
		baseSpAttack = 58
		baseSpDefense = 62
		baseSpeed = 30
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 83
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal, flying]
		self.weight = 15.0 # kg
		self.height = 0.8 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 94

		self.levelUpAttacks = {1 : Peck(), 6 : SandAttack(),
							   11 : Leer(), 16 : FuryAttack(), 
							   21 : KnockOff(), 26 : FuryCutter(),
							   31 : SwordsDance(), 36 : Agility(),
							   41 : Slash(), 46 : FalseSwipe()}

class Doduo(PocketMonster):

	def __init__(self):
		self.name = 'Doduo'
		baseHp = 35
		baseAttack = 85
		baseDefense = 45
		baseSpAttack = 35
		baseSpDefense = 35
		baseSpeed = 75
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 84
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal, flying]
		self.weight = 39.2 # kg
		self.height = 1.4 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 31
		self.expGroup = mFast
		self.catchRate = 190
		self.baseExpYield = 96

		self.levelUpAttacks = {1 : Peck(), 2 : Growl(),
							   9 : Pursuit(), 13 : FuryAttack(), 
							   21 : TriAttack(), 25 : Rage(),
							   33 : Uproar(), 37 : DrillPeck(),
							   45 : Agility()}

	def evolve(self):
		return Dodrio()

class Dodrio(PocketMonster):

	def __init__(self):
		self.name = 'Dodrio'
		baseHp = 60
		baseAttack = 110
		baseDefense = 70
		baseSpAttack = 60
		baseSpDefense = 60
		baseSpeed = 100
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 85
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal, flying]
		self.weight = 85.2 # kg
		self.height = 1.8 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 158

		self.levelUpAttacks = {1 : Peck(), 2 : Growl(),
							   9 : Pursuit(), 13 : FuryAttack(), 
							   21 : TriAttack(), 25 : Rage(),
							   38 : Uproar(), 47 : DrillPeck(),
							   60 : Agility()}

class Seel(PocketMonster):

	def __init__(self):
		self.name = 'Seel'
		baseHp = 65
		baseAttack = 45
		baseDefense = 55
		baseSpAttack = 45
		baseSpDefense = 70
		baseSpeed = 45
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 86
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 90.0 # kg
		self.height = 1.1 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 34
		self.expGroup = mFast
		self.catchRate = 190
		self.baseExpYield = 100

		self.levelUpAttacks = {1 : Headbutt(), 9 : Growl(),
							   17 : IcyWind(), 21 : AuroraBeam(), 
							   29 : Rest(), 37 : TakeDown(),
							   41 : IceBeam(), 49 : Safeguard()}

	def evolve(self):
		return Dewgong()

class Dewgong(PocketMonster):

	def __init__(self):
		self.name = 'Dewgong'
		baseHp = 90
		baseAttack = 70
		baseDefense = 80
		baseSpAttack = 70
		baseSpDefense = 95
		baseSpeed = 70
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 87
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water, ice]
		self.weight = 120.0 # kg
		self.height = 1.7 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 75
		self.baseExpYield = 176

		self.levelUpAttacks = {1 : Headbutt(), 2 : SignalBeam(), 9 : Growl(),
							   17 : IcyWind(), 21 : AuroraBeam(), 
							   29 : Rest(), 34 : SheerCold(), 42 : TakeDown(),
							   51 : IceBeam(), 64 : Safeguard()}

class Grimer(PocketMonster):

	def __init__(self):
		self.name = 'Grimer'
		baseHp = 80
		baseAttack = 80
		baseDefense = 50
		baseSpAttack = 40
		baseSpDefense = 50
		baseSpeed = 25
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 88
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [poison]
		self.weight = 30.0 # kg
		self.height = 0.9 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 38
		self.expGroup = mFast
		self.catchRate = 190
		self.baseExpYield = 90

		self.levelUpAttacks = {1 : PoisonGas(), 2 : Pound(),
							   4 : Harden(), 8 : Disable(), 
							   13 : Sludge(), 19 : Minimize(),
							   26 : Screech(), 34 : AcidArmor(),
							   43 : SludgeBomb(), 53 : Memento()}

	def evolve(self):
		return Muk()

class Muk(PocketMonster):

	def __init__(self):
		self.name = 'Muk'
		baseHp = 105
		baseAttack = 105
		baseDefense = 75
		baseSpAttack = 65
		baseSpDefense = 100
		baseSpeed = 50
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 89
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [poison]
		self.weight = 30.0 # kg
		self.height = 1.2 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 75
		self.baseExpYield = 157

		self.levelUpAttacks = {1 : PoisonGas(), 2 : Pound(),
							   4 : Harden(), 8 : Disable(), 
							   13 : Sludge(), 19 : Minimize(),
							   26 : Screech(), 34 : AcidArmor(),
							   47 : SludgeBomb(), 61 : Memento()}

class Shellder(PocketMonster):

	def __init__(self):
		self.name = 'Shellder'
		baseHp = 30
		baseAttack = 65
		baseDefense = 100
		baseSpAttack = 45
		baseSpDefense = 25
		baseSpeed = 40
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 90
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 4.0 # kg
		self.height = 0.3 # m
		self.femaleRate = 50 # percent

		self.evolvesWith = 'waterstone'
		self.expGroup = slow
		self.catchRate = 190
		self.baseExpYield = 97

		self.levelUpAttacks = {1 : Tackle(), 2 : Withdraw(),
							   8 : IcicleSpear(), 15 : Supersonic(), 
							   22 : AuroraBeam(), 29 : Protect(),
							   36 : Leer(), 43 : Clamp(),
							   50 : IceBeam()}

	def evolve(self):
		return Cloyster()

class Cloyster(PocketMonster):

	def __init__(self):
		self.name = 'Cloyster'
		baseHp = 50
		baseAttack = 95
		baseDefense = 180
		baseSpAttack = 85
		baseSpDefense = 45
		baseSpeed = 70
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 91
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water, ice]
		self.weight = 132.5 # kg
		self.height = 1.5 # m
		self.femaleRate = 50 # percent

		self.expGroup = slow
		self.catchRate = 60
		self.baseExpYield = 203

		self.levelUpAttacks = {1 : Withdraw(), 2 : Supersonic(),
							   3 : AuroraBeam(), 4 : Protect(), 
							   33 : Spikes(), 41 : SpikeCannon()}

class Gastly(PocketMonster):

	def __init__(self):
		self.name = 'Gastly'
		baseHp = 30
		baseAttack = 35
		baseDefense = 30
		baseSpAttack = 100
		baseSpDefense = 35
		baseSpeed = 80
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 92
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [ghost, poison]
		self.weight = 0.1 # kg
		self.height = 1.3 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 25
		self.expGroup = mSlow
		self.catchRate = 190
		self.baseExpYield = 95

		self.levelUpAttacks = {1 : Hypnosis(), 2 : Lick(),
							   8 : Spite(), 13 : Curse(), 
							   16 : NightShade(), 21 : ConfuseRay(),
							   28 : DreamEater(), 33 : DestinyBond(),
							   36 : ShadowBall(), 41 : Nightmare(),
							   48 : MeanLook()}

	def evolve(self):
		return Haunter()

class Haunter(PocketMonster):

	def __init__(self):
		self.name = 'Haunter'
		baseHp = 45
		baseAttack = 50
		baseDefense = 45
		baseSpAttack = 115
		baseSpDefense = 55
		baseSpeed = 95
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 93
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [ghost, poison]
		self.weight = 0.1 # kg
		self.height = 1.6 # m
		self.femaleRate = 50 # percent

		self.evolvesWith = 'trade'
		self.expGroup = mSlow
		self.catchRate = 90
		self.baseExpYield = 126

		self.levelUpAttacks = {1 : Hypnosis(), 2 : Lick(),
							   8 : Spite(), 13 : Curse(), 
							   16 : NightShade(), 21 : ConfuseRay(), 25 : ShadowPunch(),
							   31 : DreamEater(), 39 : DestinyBond(),
							   45 : ShadowBall(), 53 : Nightmare(),
							   64 : MeanLook()}

	def evolve(self):
		return Gengar()

class Gengar(PocketMonster):

	def __init__(self):
		self.name = 'Gengar'
		baseHp = 60
		baseAttack = 65
		baseDefense = 60
		baseSpAttack = 130
		baseSpDefense = 75
		baseSpeed = 110
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 94
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [ghost, poison]
		self.weight = 40.5 # kg
		self.height = 1.5 # m
		self.femaleRate = 50 # percent

		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 190

		self.levelUpAttacks = {1 : Hypnosis(), 2 : Lick(),
							   8 : Spite(), 13 : Curse(), 
							   16 : NightShade(), 21 : ConfuseRay(), 25 : ShadowPunch(),
							   31 : DreamEater(), 39 : DestinyBond(),
							   45 : ShadowBall(), 53 : Nightmare(),
							   64 : MeanLook()}

class Onix(PocketMonster):

	def __init__(self):
		self.name = 'Onix'
		baseHp = 35
		baseAttack = 45
		baseDefense = 160
		baseSpAttack = 30
		baseSpDefense = 45
		baseSpeed = 70
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 95
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [rock, ground]
		self.weight = 210.0 # kg
		self.height = 8.8 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 108

		self.levelUpAttacks = {1 : Tackle(), 2 : Screech(),
							   8 : Bind(), 12 : RockThrow(), 
							   19 : Harden(), 23 : Rage(),
							   30 : Dragonbreath(), 34 : Sandstorm(),
							   41 : Slam(), 45 : IronTail(),
							   52 : SandTomb(), 56 : DoubleEdge()}

class Drowzee(PocketMonster):

	def __init__(self):
		self.name = 'Drowzee'
		baseHp = 60
		baseAttack = 48
		baseDefense = 45
		baseSpAttack = 43
		baseSpDefense = 90
		baseSpeed = 42
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 96
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [psychic]
		self.weight = 32.4 # kg
		self.height = 1.0 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 26
		self.expGroup = mFast
		self.catchRate = 190
		self.baseExpYield = 102

		self.levelUpAttacks = {1 : Pound(), 2 : Hypnosis(),
							   7 : Disable(), 11 : Confusion(), 
							   17 : Headbutt(), 21 : PoisonGas(),
							   27 : Meditate(), 31 : Psychic(),
							   37 : PsychUp(), 41 : Swagger(),
							   47 : FutureSight()}

	def evolve(self):
		return Hypno()

class Hypno(PocketMonster):

	def __init__(self):
		self.name = 'Hypno'
		baseHp = 85
		baseAttack = 73
		baseDefense = 70
		baseSpAttack = 73
		baseSpDefense = 115
		baseSpeed = 67
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 97
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [psychic]
		self.weight = 75.6 # kg
		self.height = 1.6 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 75
		self.baseExpYield = 165

		self.levelUpAttacks = {1 : Pound(), 2 : Hypnosis(),
							   7 : Disable(), 11 : Confusion(), 
							   17 : Headbutt(), 21 : PoisonGas(),
							   29 : Meditate(), 35 : Psychic(),
							   43 : PsychUp(), 49 : Swagger(),
							   57 : FutureSight()}

class Krabby(PocketMonster):

	def __init__(self):
		self.name = 'Krabby'
		baseHp = 30
		baseAttack = 105
		baseDefense = 90
		baseSpAttack = 25
		baseSpDefense = 25
		baseSpeed = 50
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 98
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 6.5 # kg
		self.height = 0.4 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 28
		self.expGroup = mFast
		self.catchRate = 225
		self.baseExpYield = 115

		self.levelUpAttacks = {1 : Bubble(), 5 : Leer(),
							   12 : Vicegrip(), 16 : Harden(), 
							   23 : MudShot(), 27 : Stomp(),
							   34 : Guillotine(), 38 : Protect(),
							   45 : Crabhammer(), 49 : Flail()}

	def evolve(self):
		return Kingler()

class Kingler(PocketMonster):

	def __init__(self):
		self.name = 'Kingler'
		baseHp = 55
		baseAttack = 130
		baseDefense = 115
		baseSpAttack = 50
		baseSpDefense = 50
		baseSpeed = 75
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 99
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 60.0 # kg
		self.height = 1.3 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 60
		self.baseExpYield = 206

		self.levelUpAttacks = {1 : Bubble(), 2 : MetalClaw(), 5 : Leer(),
							   12 : Vicegrip(), 16 : Harden(), 
							   23 : MudShot(), 27 : Stomp(),
							   38 : Guillotine(), 42 : Protect(),
							   57 : Crabhammer(), 65 : Flail()}

class Voltorb(PocketMonster):

	def __init__(self):
		self.name = 'Voltorb'
		baseHp = 40
		baseAttack = 30
		baseDefense = 50
		baseSpAttack = 55
		baseSpDefense = 55
		baseSpeed = 100
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 100
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [electric]
		self.weight = 10.4 # kg
		self.height = 0.5 # m
		self.femaleRate = -1 # genderless

		self.evolvesAt = 30
		self.expGroup = mFast
		self.catchRate = 190
		self.baseExpYield = 103

		self.levelUpAttacks = {1 : Charge(), 2 : Tackle(),
							   8 : Screech(), 15 : Sonicboom(), 
							   21 : Spark(), 27 : Selfdestruct(),
							   32 : Rollout(), 37 : LightScreen(),
							   42 : Swift(), 46 : Explosion(), 49 : MirrorCoat()}

	def evolve(self):
		return Electrode()