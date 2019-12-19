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

class Electrode(PocketMonster):

	def __init__(self):
		self.name = 'Electrode'
		baseHp = 60
		baseAttack = 50
		baseDefense = 70
		baseSpAttack = 80
		baseSpDefense = 80
		baseSpeed = 140
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 101
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [electric]
		self.weight = 66.6 # kg
		self.height = 1.2 # m
		self.femaleRate = -1 # genderless

		self.expGroup = mFast
		self.catchRate = 60
		self.baseExpYield = 150

		self.levelUpAttacks = {1 : Charge(), 2 : Tackle(),
							   8 : Screech(), 15 : Sonicboom(), 
							   21 : Spark(), 27 : Selfdestruct(),
							   34 : Rollout(), 41 : LightScreen(),
							   48 : Swift(), 54 : Explosion(), 59 : MirrorCoat()}

class Exeggcute(PocketMonster):

	def __init__(self):
		self.name = 'Exeggcute'
		baseHp = 60
		baseAttack = 40
		baseDefense = 80
		baseSpAttack = 60
		baseSpDefense = 45
		baseSpeed = 40
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 102
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [grass, psychic]
		self.weight = 2.5 # kg
		self.height = 0.4 # m
		self.femaleRate = 50 # percent

		self.evolvesWith = 'leafstone'
		self.expGroup = slow
		self.catchRate = 90
		self.baseExpYield = 98

		self.levelUpAttacks = {1 : Barrage(), 2 : Uproar(),
							   3 : Hypnosis(), 13 : LeechSeed(), 
							   19 : Confusion(), 25 : StunSpore(),
							   31 : PoisonPowder(), 37 : SleepPowder(),
							   43 : Solarbeam()}

	def evolve(self):
		return Exeggutor()

class Exeggutor(PocketMonster):

	def __init__(self):
		self.name = 'Exeggutor'
		baseHp = 95
		baseAttack = 95
		baseDefense = 85
		baseSpAttack = 125
		baseSpDefense = 65
		baseSpeed = 55
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 103
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [grass, psychic]
		self.weight = 120.0 # kg
		self.height = 2.0 # m
		self.femaleRate = 50 # percent

		self.expGroup = slow
		self.catchRate = 45
		self.baseExpYield = 212

		self.levelUpAttacks = {1 : Barrage(), 2 : Hypnosis(),
							   3 : Confusion(), 19 : Stomp(), 
							   31 : EggBomb()}

class Cubone(PocketMonster):

	def __init__(self):
		self.name = 'Cubone'
		baseHp = 50
		baseAttack = 50
		baseDefense = 95
		baseSpAttack = 40
		baseSpDefense = 50
		baseSpeed = 35
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 104
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [ground]
		self.weight = 6.5 # kg
		self.height = 0.4 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 28
		self.expGroup = mFast
		self.catchRate = 190
		self.baseExpYield = 87

		self.levelUpAttacks = {1 : Growl(), 5 : TailWhip(),
							   9 : BoneClub(), 13 : Headbutt(), 
							   17 : Leer(), 21 : FocusEnergy(),
							   25 : Bonemerang(), 29 : Rage(),
							   33 : FalseSwipe(), 37 : Thrash(),
							   41 : BoneRush(), 45 : DoubleEdge()}

	def evolve(self):
		return Marowak()

class Marowak(PocketMonster):

	def __init__(self):
		self.name = 'Marowak'
		baseHp = 60
		baseAttack = 80
		baseDefense = 110
		baseSpAttack = 50
		baseSpDefense = 80
		baseSpeed = 45
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 105
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [ground]
		self.weight = 45.0 # kg
		self.height = 1.0 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 75
		self.baseExpYield = 124

		self.levelUpAttacks = {1 : Growl(), 5 : TailWhip(),
							   9 : BoneClub(), 13 : Headbutt(), 
							   17 : Leer(), 21 : FocusEnergy(),
							   25 : Bonemerang(), 32 : Rage(),
							   39 : FalseSwipe(), 46 : Thrash(),
							   53 : BoneRush(), 61 : DoubleEdge()}

class Hitmonlee(PocketMonster):

	def __init__(self):
		self.name = 'Hitmonlee'
		baseHp = 50
		baseAttack = 120
		baseDefense = 53
		baseSpAttack = 35
		baseSpDefense = 110
		baseSpeed = 87
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 106
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fight]
		self.weight = 49.8 # kg
		self.height = 1.5 # m
		self.femaleRate = 0 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 139

		self.levelUpAttacks = {1 : Revenge(), 2 : DoubleKick(),
							   6 : Meditate(), 11 : RollingKick(), 
							   16 : JumpKick(), 20 : BrickBreak(),
							   21 : FocusEnergy(), 26 : HiJumpKick(),
							   31 : MindReader(), 36 : Foresight(),
							   41 : Endure(), 46 : MegaKick(),
							   51 : Reversal()}

class Hitmonchan(PocketMonster):

	def __init__(self):
		self.name = 'Hitmonchan'
		baseHp = 50
		baseAttack = 105
		baseDefense = 79
		baseSpAttack = 35
		baseSpDefense = 110
		baseSpeed = 76
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 107
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fight]
		self.weight = 50.2 # kg
		self.height = 1.4 # m
		self.femaleRate = 0 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 140

		self.levelUpAttacks = {1 : Revenge(), 2 : CometPunch(),
							   7 : Agility(), 13 : Pursuit(), 
							   20 : MachPunch(), 25 : Thunderpunch(),
							   26 : IcePunch(), 27 : FirePunch(),
							   32 : SkyUppercut(), 38 : MegaPunch(),
							   44 : Detect(), 50 : Counter()}

class Lickitung(PocketMonster):

	def __init__(self):
		self.name = 'Lickitung'
		baseHp = 90
		baseAttack = 55
		baseDefense = 75
		baseSpAttack = 60
		baseSpDefense = 75
		baseSpeed = 30
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 108
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 65.5 # kg
		self.height = 1.2 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 127

		self.levelUpAttacks = {1 : Lick(), 7 : Supersonic(),
							   12 : DefenseCurl(), 18 : KnockOff(), 
							   23 : Stomp(), 29 : Wrap(),
							   34 : Disable(), 40 : Slam(),
							   45 : Screech(), 51 : Refresh()}

class Koffing(PocketMonster):

	def __init__(self):
		self.name = 'Koffing'
		baseHp = 40
		baseAttack = 65
		baseDefense = 95
		baseSpAttack = 60
		baseSpDefense = 45
		baseSpeed = 35
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 109
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 1.0 # kg
		self.height = 0.6 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 35
		self.expGroup = mFast
		self.catchRate = 190
		self.baseExpYield = 114

		self.levelUpAttacks = {1 : PoisonGas(), 2 : Tackle(),
							   9 : Smog(), 17 : Selfdestruct(), 
							   21 : Sludge(), 25 : Smokescreen(),
							   33 : Haze(), 41 : Explosion(),
							   45 : DestinyBond(), 49 : Memento()}

	def evolve(self):
		return Weezing()

class Weezing(PocketMonster):

	def __init__(self):
		self.name = 'Weezing'
		baseHp = 65
		baseAttack = 90
		baseDefense = 120
		baseSpAttack = 85
		baseSpDefense = 70
		baseSpeed = 60
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 110
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 9.5 # kg
		self.height = 1.2 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 60
		self.baseExpYield = 173

		self.levelUpAttacks = {1 : PoisonGas(), 2 : Tackle(),
							   9 : Smog(), 17 : Selfdestruct(), 
							   21 : Sludge(), 25 : Smokescreen(),
							   33 : Haze(), 44 : Explosion(),
							   51 : DestinyBond(), 58 : Memento()}

class Rhyhorn(PocketMonster):

	def __init__(self):
		self.name = 'Rhyhorn'
		baseHp = 80
		baseAttack = 85
		baseDefense = 95
		baseSpAttack = 30
		baseSpDefense = 30
		baseSpeed = 25
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 111
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [ground, rock]
		self.weight = 115.0 # kg
		self.height = 1.0 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 42
		self.expGroup = slow
		self.catchRate = 120
		self.baseExpYield = 135

		self.levelUpAttacks = {1 : HornAttack(), 2 : TailWhip(),
							   10 : Stomp(), 15 : FuryAttack(), 
							   24 : ScaryFace(), 29 : RockBlast(),
							   38 : HornDrill(), 43 : TakeDown(),
							   52 : Earthquake(), 57 : Megahorn()}

	def evolve(self):
		return Rhydon()

class Rhydon(PocketMonster):

	def __init__(self):
		self.name = 'Rhydon'
		baseHp = 105
		baseAttack = 130
		baseDefense = 120
		baseSpAttack = 45
		baseSpDefense = 45
		baseSpeed = 40
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 112
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [ground, rock]
		self.weight = 120.0 # kg
		self.height = 1.9 # m
		self.femaleRate = 50 # percent

		self.expGroup = slow
		self.catchRate = 60
		self.baseExpYield = 204

		self.levelUpAttacks = {1 : HornAttack(), 2 : TailWhip(),
							   10 : Stomp(), 15 : FuryAttack(), 
							   24 : ScaryFace(), 29 : RockBlast(),
							   38 : HornDrill(), 46 : TakeDown(),
							   58 : Earthquake(), 66 : Megahorn()}

class Chansey(PocketMonster):

	def __init__(self):
		self.name = 'Chansey'
		baseHp = 250
		baseAttack = 5
		baseDefense = 5
		baseSpAttack = 35
		baseSpDefense = 105
		baseSpeed = 50
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 113
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 34.6 # kg
		self.height = 1.1 # m
		self.femaleRate = 100 # percent

		self.expGroup = fast
		self.catchRate = 30
		self.baseExpYield = 255

		self.levelUpAttacks = {1 : Pound(), 2 : Growl(),
							   5 : TailWhip(), 9 : Refresh(), 
							   13 : Softboiled(), 17 : Doubleslap(),
							   23 : Minimize(), 29 : Sing(),
							   35 : EggBomb(), 41 : DefenseCurl(),
							   49 : LightScreen(), 57 : DoubleEdge()}

class Tangela(PocketMonster):

	def __init__(self):
		self.name = 'Tangela'
		baseHp = 65
		baseAttack = 55
		baseDefense = 115
		baseSpAttack = 100
		baseSpDefense = 40
		baseSpeed = 60
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 114
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [grass]
		self.weight = 35.0 # kg
		self.height = 1.0 # m
		self.femaleRate = 50 # percent

		self.expGroup = fast
		self.catchRate = 45
		self.baseExpYield = 166

		self.levelUpAttacks = {1 : Ingrain(), 2 : Constrict(),
							   4 : SleepPowder(), 10 : Absorb(), 
							   13 : Growth(), 19 : PoisonPowder(),
							   22 : VineWhip(), 28 : Bind(),
							   31 : MegaDrain(), 37 : StunSpore(),
							   40 : Slam(), 46 : Tickle()}

class Kangaskhan(PocketMonster):

	def __init__(self):
		self.name = 'Kangaskhan'
		baseHp = 105
		baseAttack = 95
		baseDefense = 80
		baseSpAttack = 40
		baseSpDefense = 80
		baseSpeed = 90
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 115
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 80.0 # kg
		self.height = 2.2 # m
		self.femaleRate = 100 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 175

		self.levelUpAttacks = {1 : CometPunch(), 2 : Leer(),
							   7 : Bite(), 13 : TailWhip(), 
							   19 : FakeOut(), 25 : MegaPunch(),
							   31 : Rage(), 37 : Endure(),
							   43 : DizzyPunch(), 49 : Reversal()}

class Horsea(PocketMonster):

	def __init__(self):
		self.name = 'Horsea'
		baseHp = 30
		baseAttack = 40
		baseDefense = 70
		baseSpAttack = 70
		baseSpDefense = 25
		baseSpeed = 60
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 116
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 8.0 # kg
		self.height = 0.4 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 32
		self.expGroup = mFast
		self.catchRate = 225
		self.baseExpYield = 83

		self.levelUpAttacks = {1 : Bubble(), 8 : Smokescreen(),
							   15 : Leer(), 22 : WaterGun(), 
							   29 : Twister(), 36 : Agility(),
							   43 : HydroPump(), 50 : DragonDance()}

	def evolve(self):
		return Seadra()

class Seadra(PocketMonster):

	def __init__(self):
		self.name = 'Seadra'
		baseHp = 55
		baseAttack = 65
		baseDefense = 95
		baseSpAttack = 95
		baseSpDefense = 45
		baseSpeed = 85
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 117
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 25.0 # kg
		self.height = 1.2 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 75
		self.baseExpYield = 155

		self.levelUpAttacks = {1 : Bubble(), 8 : Smokescreen(),
							   15 : Leer(), 22 : WaterGun(), 
							   29 : Twister(), 40 : Agility(),
							   51 : HydroPump(), 62 : DragonDance()}

class Goldeen(PocketMonster):

	def __init__(self):
		self.name = 'Goldeen'
		baseHp = 45
		baseAttack = 67
		baseDefense = 60
		baseSpAttack = 35
		baseSpDefense = 50
		baseSpeed = 63
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 118
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 15.0 # kg
		self.height = 0.6 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 33
		self.expGroup = mFast
		self.catchRate = 225
		self.baseExpYield = 111

		self.levelUpAttacks = {1 : Peck(), 2 : TailWhip(),
							   3 : WaterSport(), 10 : Supersonic(), 
							   15 : HornAttack(), 24 : Flail(),
							   29 : FuryAttack(), 38 : Waterfall(),
							   43 : HornDrill(), 52 : Agility(),
							   57 : Megahorn()}

	def evolve(self):
		return Seaking()

class Seaking(PocketMonster):

	def __init__(self):
		self.name = 'Seaking'
		baseHp = 80
		baseAttack = 92
		baseDefense = 65
		baseSpAttack = 65
		baseSpDefense = 80
		baseSpeed = 68
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 119
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 39.0 # kg
		self.height = 1.3 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 60
		self.baseExpYield = 170

		self.levelUpAttacks = {1 : Peck(), 2 : TailWhip(),
							   3 : WaterSport(), 10 : Supersonic(), 
							   15 : HornAttack(), 24 : Flail(),
							   29 : FuryAttack(), 41 : Waterfall(),
							   49 : HornDrill(), 61 : Agility(),
							   69 : Megahorn()}

class Staryu(PocketMonster):

	def __init__(self):
		self.name = 'Staryu'
		baseHp = 30
		baseAttack = 45
		baseDefense = 55
		baseSpAttack = 70
		baseSpDefense = 55
		baseSpeed = 85
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 120
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 34.5 # kg
		self.height = 0.8 # m
		self.femaleRate = -1 # genderless

		self.evolvesWith = 'waterstone'
		self.expGroup = slow
		self.catchRate = 225
		self.baseExpYield = 106

		self.levelUpAttacks = {1 : Tackle(), 2 : Harden(),
							   6 : WaterGun(), 10 : RapidSpin(), 
							   15 : Recover(), 19 : Camouflage(),
							   24 : Swift(), 28 : Bubblebeam(),
							   33 : Minimize(), 37 : LightScreen(),
							   42 : CosmicPower(), 46 : HydroPump()}

	def evolve(self):
		return Starmie()

class Starmie(PocketMonster):

	def __init__(self):
		self.name = 'Starmie'
		baseHp = 60
		baseAttack = 75
		baseDefense = 85
		baseSpAttack = 100
		baseSpDefense = 85
		baseSpeed = 115
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 121
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water, psychic]
		self.weight = 80.0 # kg
		self.height = 1.1 # m
		self.femaleRate = -1 # genderless

		self.expGroup = slow
		self.catchRate = 60
		self.baseExpYield = 207

		self.levelUpAttacks = {1 : WaterGun(), 2 : RapidSpin(), 
							   3 : Recover(), 4 : Swift(), 
							   33 : ConfuseRay()}

class MrMime(PocketMonster):

	def __init__(self):
		self.name = 'Mr. Mime'
		baseHp = 40
		baseAttack = 45
		baseDefense = 65
		baseSpAttack = 100
		baseSpDefense = 120
		baseSpeed = 90
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 122
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [psychic]
		self.weight = 54.5 # kg
		self.height = 1.3 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 136

		self.levelUpAttacks = {1 : Barrier(), 5 : Confusion(),
							   8 : Substitute(), 12 : Meditate(), 
							   15 : Doubleslap(), 18 : LightScreen(),
							   19 : Reflect(), 22 : MagicalLeaf(),
							   26 : Encore(), 29 : Psybeam(),
							   33 : Recycle(), 36 : Trick(),
							   40 : RolePlay(), 43 : Psychic(),
							   47 : BatonPass(), 50 : Safeguard()}

class Scyther(PocketMonster):

	def __init__(self):
		self.name = 'Scyther'
		baseHp = 70
		baseAttack = 110
		baseDefense = 80
		baseSpAttack = 55
		baseSpDefense = 80
		baseSpeed = 105
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 123
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [bug, flying]
		self.weight = 56.0 # kg
		self.height = 1.5 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 187

		self.levelUpAttacks = {1 : QuickAttack(), 2 : Leer(),
							   6 : FocusEnergy(), 11 : Pursuit(), 
							   16 : FalseSwipe(), 21 : Agility(),
							   26 : WingAttack(), 31 : Slash(),
							   36 : SwordsDance(), 41 : DoubleTeam(),
							   46 : FuryCutter()}

class Jynx(PocketMonster):

	def __init__(self):
		self.name = 'Jynx'
		baseHp = 65
		baseAttack = 50
		baseDefense = 35
		baseSpAttack = 115
		baseSpDefense = 95
		baseSpeed = 95
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 124
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [ice, psychic]
		self.weight = 40.6 # kg
		self.height = 1.4 # m
		self.femaleRate = 100 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 137

		self.levelUpAttacks = {1 : Pound(), 2 : Lick(),
							   9 : LovelyKiss(), 13 : PowderSnow(), 
							   21 : Doubleslap(), 25 : IcePunch(),
							   35 : MeanLook(), 41 : FakeTears(),
							   51 : BodySlam(), 57 : PerishSong(),
							   67 : Blizzard()}

class Electabuzz(PocketMonster):

	def __init__(self):
		self.name = 'Electabuzz'
		baseHp = 65
		baseAttack = 83
		baseDefense = 57
		baseSpAttack = 95
		baseSpDefense = 85
		baseSpeed = 105
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 125
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [electric]
		self.weight = 30.0 # kg
		self.height = 1.1 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 156

		self.levelUpAttacks = {1 : QuickAttack(), 2 : Leer(),
							   9 : Thunderpunch(), 17 : LightScreen(), 
							   25 : Swift(), 36 : Screech(),
							   47 : Thunderbolt(), 58 : Thunder()}
