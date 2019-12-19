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
from creatures76_100 import Golem

class Dugtrio(PocketMonster):

	def __init__(self):
		self.name = 'Dugtrio'
		baseHp = 35
		baseAttack = 80
		baseDefense = 50
		baseSpAttack = 50
		baseSpDefense = 70
		baseSpeed = 120
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 51
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [ground]
		self.weight = 33.3 # kg
		self.height = 0.7 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 50
		self.baseExpYield = 153

		self.levelUpAttacks = {1 : SandAttack(), 2 : Scratch(), 3 : TriAttack(),
							   5 : Growl(), 9 : Magnitude(), 
							   17 : Dig(), 21 : FurySwipes(),
							   25 : MudSlap(), 26 : SandTomb(), 38 : Slash(),
							   51 : Earthquake(), 64 : Fissure()}

class Meowth(PocketMonster):

	def __init__(self):
		self.name = 'Meowth'
		baseHp = 40
		baseAttack = 45
		baseDefense = 35
		baseSpAttack = 40
		baseSpDefense = 40
		baseSpeed = 90
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 52
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 4.2 # kg
		self.height = 0.4 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 28
		self.expGroup = mFast
		self.catchRate = 255
		self.baseExpYield = 69

		self.levelUpAttacks = {1 : Scratch(), 2 : Growl(),
							   10 : Bite(), 18 : PayDay(), 
							   25 : FaintAttack(), 31 : Screech(),
							   36 : FurySwipes(), 40 : Slash(),
							   43 : FakeOut(), 45 : Swagger()}

	def evolve(self):
		return Persian()

class Persian(PocketMonster):

	def __init__(self):
		self.name = 'Persian'
		baseHp = 65
		baseAttack = 70
		baseDefense = 60
		baseSpAttack = 65
		baseSpDefense = 65
		baseSpeed = 115
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 53
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 32.0 # kg
		self.height = 1.0 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 90
		self.baseExpYield = 148

		self.levelUpAttacks = {1 : Scratch(), 2 : Growl(),
							   10 : Bite(), 18 : PayDay(), 
							   25 : FaintAttack(), 34 : Screech(),
							   42 : FurySwipes(), 49 : Slash(),
							   55 : FakeOut(), 61 : Swagger()}

class Psyduck(PocketMonster):

	def __init__(self):
		self.name = 'Psyduck'
		baseHp = 50
		baseAttack = 52
		baseDefense = 48
		baseSpAttack = 65
		baseSpDefense = 50
		baseSpeed = 55
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 54
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 19.6 # kg
		self.height = 0.8 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 33
		self.expGroup = mFast
		self.catchRate = 190
		self.baseExpYield = 80

		self.levelUpAttacks = {1 : WaterSport(), 2 : Scratch(),
							   5 : TailWhip(), 10 : Disable(), 
							   16 : Confusion(), 23 : Screech(),
							   31 : PsychUp(), 40 : FurySwipes(),
							   50 : HydroPump()}

	def evolve(self):
		return Golduck()

class Golduck(PocketMonster):

	def __init__(self):
		self.name = 'Golduck'
		baseHp = 80
		baseAttack = 82
		baseDefense = 78
		baseSpAttack = 95
		baseSpDefense = 80
		baseSpeed = 85
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 55
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 76.6 # kg
		self.height = 1.7 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 75
		self.baseExpYield = 174

		self.levelUpAttacks = {1 : WaterSport(), 2 : Scratch(),
							   5 : TailWhip(), 10 : Disable(), 
							   16 : Confusion(), 23 : Screech(),
							   31 : PsychUp(), 44 : FurySwipes(),
							   58 : HydroPump()}

class Mankey(PocketMonster):

	def __init__(self):
		self.name = 'Mankey'
		baseHp = 40
		baseAttack = 80
		baseDefense = 35
		baseSpAttack = 35
		baseSpDefense = 45
		baseSpeed = 70
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 56
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fight]
		self.weight = 28.0 # kg
		self.height = 0.5 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 28
		self.expGroup = mFast
		self.catchRate = 190
		self.baseExpYield = 74

		self.levelUpAttacks = {1 : Scratch(), 2 : Leer(),
							   6 : LowKick(), 11 : KarateChop(), 
							   16 : FurySwipes(), 21 : FocusEnergy(),
							   26 : SeismicToss(), 31 : CrossChop(),
							   36 : Swagger(), 41 : Screech(), 46 : Thrash()}

	def evolve(self):
		return Primeape()

class Primeape(PocketMonster):

	def __init__(self):
		self.name = 'Primeape'
		baseHp = 65
		baseAttack = 105
		baseDefense = 60
		baseSpAttack = 60
		baseSpDefense = 70
		baseSpeed = 95
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 57
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fight]
		self.weight = 32.0 # kg
		self.height = 1.0 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 75
		self.baseExpYield = 149

		self.levelUpAttacks = {1 : Scratch(), 2 : Leer(), 3 : Rage(),
							   6 : LowKick(), 11 : KarateChop(), 
							   16 : FurySwipes(), 21 : FocusEnergy(),
							   26 : SeismicToss(), 28 : Rage(), 35 : CrossChop(),
							   44 : Swagger(), 53 : Screech(), 62 : Thrash()}

class Growlithe(PocketMonster):

	def __init__(self):
		self.name = 'Growlithe'
		baseHp = 55
		baseAttack = 70
		baseDefense = 45
		baseSpAttack = 70
		baseSpDefense = 50
		baseSpeed = 60
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 58
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fire]
		self.weight = 19.0 # kg
		self.height = 0.7 # m
		self.femaleRate = 25 # percent

		self.evolvesWith = 'firestone'
		self.expGroup = slow
		self.catchRate = 190
		self.baseExpYield = 91

		self.levelUpAttacks = {1 : Bite(), 2 : Roar(),
							   7 : Ember(), 13 : Leer(), 
							   19 : OdorSleuth(), 25 : TakeDown(),
							   31 : FlameWheel(), 37 : HelpingHand(),
							   43 : Agility(), 49 : Flamethrower()}

	def evolve(self):
		return Arcanine()

class Arcanine(PocketMonster):

	def __init__(self):
		self.name = 'Arcanine'
		baseHp = 90
		baseAttack = 110
		baseDefense = 80
		baseSpAttack = 100
		baseSpDefense = 80
		baseSpeed = 95
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 59
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fire]
		self.weight = 155.0 # kg
		self.height = 1.9 # m
		self.femaleRate = 25 # percent

		self.expGroup = slow
		self.catchRate = 75
		self.baseExpYield = 213

		self.levelUpAttacks = {1 : Bite(), 2 : Roar(),
							   3 : Ember(), 4 : OdorSleuth(),
							   49 : Extremespeed()}

class Poliwag(PocketMonster):

	def __init__(self):
		self.name = 'Poliwag'
		baseHp = 40
		baseAttack = 50
		baseDefense = 40
		baseSpAttack = 40
		baseSpDefense = 40
		baseSpeed = 90
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 60
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 12.4 # kg
		self.height = 0.6 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 25
		self.expGroup = mSlow
		self.catchRate = 255
		self.baseExpYield = 77

		self.levelUpAttacks = {1 : Bubble(), 7 : Hypnosis(),
							   13 : WaterGun(), 19 : Doubleslap(), 
							   25 : RainDance(), 31 : BodySlam(),
							   37 : BellyDrum(), 43 : HydroPump()}

	def evolve(self):
		return Poliwhirl()

class Poliwhirl(PocketMonster):

	def __init__(self):
		self.name = 'Poliwhirl'
		baseHp = 65
		baseAttack = 65
		baseDefense = 65
		baseSpAttack = 50
		baseSpDefense = 50
		baseSpeed = 90
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 61
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 20.0 # kg
		self.height = 1.0 # m
		self.femaleRate = 50 # percent

		self.evolvesWith = 'waterstone'
		self.expGroup = mSlow
		self.catchRate = 120
		self.baseExpYield = 131

		self.levelUpAttacks = {1 : Bubble(), 7 : Hypnosis(),
							   13 : WaterGun(), 19 : Doubleslap(), 
							   27 : RainDance(), 35 : BodySlam(),
							   43 : BellyDrum(), 51 : HydroPump()}

	def evolve(self):
		return Poliwrath()

class Poliwrath(PocketMonster):

	def __init__(self):
		self.name = 'Poliwrath'
		baseHp = 90
		baseAttack = 85
		baseDefense = 95
		baseSpAttack = 70
		baseSpDefense = 90
		baseSpeed = 70
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 62
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water, fight]
		self.weight = 54.0 # kg
		self.height = 1.3 # m
		self.femaleRate = 50 # percent

		self.expGroup = mSlow
		self.catchRate = 75
		self.baseExpYield = 185

		self.levelUpAttacks = {1 : WaterGun(), 2 : Hypnosis(),
							   3 : Doubleslap(), 4 : Submission(), 
							   35 : Submission(), 51 : MindReader()}		

class Abra(PocketMonster):

	def __init__(self):
		self.name = 'Abra'
		baseHp = 25
		baseAttack = 20
		baseDefense = 15
		baseSpAttack = 105
		baseSpDefense = 55
		baseSpeed = 90
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 63
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [psychic]
		self.weight = 19.5 # kg
		self.height = 0.9 # m
		self.femaleRate = 25 # percent

		self.evolvesAt = 16
		self.expGroup = mSlow
		self.catchRate = 200
		self.baseExpYield = 73

		self.levelUpAttacks = {1 : Teleport()}

	def evolve(self):
		return Kadabra() 

class Kadabra(PocketMonster):

	def __init__(self):
		self.name = 'Kadabra'
		baseHp = 40
		baseAttack = 35
		baseDefense = 30
		baseSpAttack = 120
		baseSpDefense = 70
		baseSpeed = 105
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 64
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [psychic]
		self.weight = 56.5 # kg
		self.height = 1.3 # m
		self.femaleRate = 25 # percent

		self.evolvesWith = 'trade'
		self.expGroup = mSlow
		self.catchRate = 100
		self.baseExpYield = 145

		self.levelUpAttacks = {1 : Teleport(), 2 : Kinesis(),
							   3 : Confusion(), 16 : Confusion(), 
							   18 : Disable(), 21 : Psybeam(),
							   23 : Reflect(), 25 : Recover(),
							   30 : FutureSight(), 33 : RolePlay(),
							   36 : Psychic(), 43 : Trick()}

	def evolve(self):
		return Alakazam()

class Alakazam(PocketMonster):

	def __init__(self):
		self.name = 'Alakazam'
		baseHp = 55
		baseAttack = 50
		baseDefense = 45
		baseSpAttack = 135
		baseSpDefense = 85
		baseSpeed = 120
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 65
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [psychic]
		self.weight = 48.0 # kg
		self.height = 1.5 # m
		self.femaleRate = 25 # percent

		self.expGroup = mSlow
		self.catchRate = 50
		self.baseExpYield = 186

		self.levelUpAttacks = {1 : Teleport(), 2 : Kinesis(),
							   3 : Confusion(), 16 : Confusion(), 
							   18 : Disable(), 21 : Psybeam(),
							   23 : Reflect(), 25 : Recover(),
							   30 : FutureSight(), 33 : RolePlay(),
							   36 : Psychic(), 43 : Trick()}

class Machop(PocketMonster):

	def __init__(self):
		self.name = 'Machop'
		baseHp = 70
		baseAttack = 80
		baseDefense = 50
		baseSpAttack = 35
		baseSpDefense = 35
		baseSpeed = 35
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 66
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fight]
		self.weight = 19.5 # kg
		self.height = 0.8 # m
		self.femaleRate = 25 # percent

		self.evolvesAt = 28
		self.expGroup = mSlow
		self.catchRate = 180
		self.baseExpYield = 88

		self.levelUpAttacks = {1 : LowKick(), 2 : Leer(),
							   7 : FocusEnergy(), 13 : KarateChop(), 
							   19 : SeismicToss(), 22 : Foresight(),
							   25 : Revenge(), 31 : VitalThrow(),
							   37 : Submission(), 40 : CrossChop(),
							   43 : ScaryFace(), 49 : Dynamicpunch()}

	def evolve(self):
		return Machoke() 

class Machoke(PocketMonster):

	def __init__(self):
		self.name = 'Machoke'
		baseHp = 80
		baseAttack = 100
		baseDefense = 70
		baseSpAttack = 50
		baseSpDefense = 60
		baseSpeed = 45
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 67
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fight]
		self.weight = 70.5 # kg
		self.height = 1.5 # m
		self.femaleRate = 25 # percent

		self.evolvesWith = 'trade'
		self.expGroup = mSlow
		self.catchRate = 90
		self.baseExpYield = 146

		self.levelUpAttacks = {1 : LowKick(), 2 : Leer(),
							   7 : FocusEnergy(), 13 : KarateChop(), 
							   19 : SeismicToss(), 22 : Foresight(),
							   25 : Revenge(), 33 : VitalThrow(),
							   41 : Submission(), 46 : CrossChop(),
							   51 : ScaryFace(), 59 : Dynamicpunch()}

	def evolve(self):
		return Machamp() 

class Machamp(PocketMonster):

	def __init__(self):
		self.name = 'Machamp'
		baseHp = 90
		baseAttack = 130
		baseDefense = 80
		baseSpAttack = 65
		baseSpDefense = 85
		baseSpeed = 55
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 68
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fight]
		self.weight = 130.0 # kg
		self.height = 1.6 # m
		self.femaleRate = 25 # percent

		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 193

		self.levelUpAttacks = {1 : LowKick(), 2 : Leer(),
							   7 : FocusEnergy(), 13 : KarateChop(), 
							   19 : SeismicToss(), 22 : Foresight(),
							   25 : Revenge(), 33 : VitalThrow(),
							   41 : Submission(), 46 : CrossChop(),
							   51 : ScaryFace(), 59 : Dynamicpunch()}


class Bellsprout(PocketMonster):

	def __init__(self):
		self.name = 'Bellsprout'
		baseHp = 50
		baseAttack = 75
		baseDefense = 35
		baseSpAttack = 70
		baseSpDefense = 30
		baseSpeed = 40
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 69
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [grass, poison]
		self.weight = 4.0# kg
		self.height = 0.7 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 21
		self.expGroup = mSlow
		self.catchRate = 255
		self.baseExpYield = 84

		self.levelUpAttacks = {1 : VineWhip(), 6 : Growth(),
							   11 : Wrap(), 15 : SleepPowder(), 
							   17 : PoisonPowder(), 19 : StunSpore(), 23 : Acid(),
							   30 : SweetScent(), 37 : RazorLeaf(), 45 : Slam()}

	def evolve(self):
		return Weepinbell()

class Weepinbell(PocketMonster):

	def __init__(self):
		self.name = 'Weepinbell'
		baseHp = 65
		baseAttack = 90
		baseDefense = 50
		baseSpAttack = 85
		baseSpDefense = 45
		baseSpeed = 55
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 70
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [grass, poison]
		self.weight = 6.4 # kg
		self.height = 1.0 # m
		self.femaleRate = 50 # percent

		self.evolvesWith = 'leafstone'
		self.expGroup = mSlow
		self.catchRate = 120
		self.baseExpYield = 151

		self.levelUpAttacks = {1 : VineWhip(), 6 : Growth(),
							   11 : Wrap(), 15 : SleepPowder(), 
							   17 : PoisonPowder(), 19 : StunSpore(), 24 : Acid(),
							   33 : SweetScent(), 42 : RazorLeaf(), 54 : Slam()}

	def evolve(self):
		return Victreebell()

class Victreebel(PocketMonster):

	def __init__(self):
		self.name = 'Victreebel'
		baseHp = 80
		baseAttack = 105
		baseDefense = 65
		baseSpAttack = 100
		baseSpDefense = 60
		baseSpeed = 70
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 71
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [grass, poison]
		self.weight = 15.5 # kg
		self.height = 1.7 # m
		self.femaleRate = 50 # percent

		self.expGroup = mSlow
		self.catchRate = 45
		self.baseExpYield = 191

		self.levelUpAttacks = {1 : Stockpile(), 2 : SpitUp(),
							   3 : Swallow(), 4 : VineWhip(), 
							   5 : SleepPowder(), 6 : SweetScent(), 
							   6 : RazorLeaf()}

class Tentacool(PocketMonster):

	def __init__(self):
		self.name = 'Tentacool'
		baseHp = 40
		baseAttack = 40
		baseDefense = 35
		baseSpAttack = 50
		baseSpDefense = 100
		baseSpeed = 70
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 72
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water, poison]
		self.weight = 45.5 # kg
		self.height = 0.9 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 30
		self.expGroup = slow
		self.catchRate = 190
		self.baseExpYield = 105

		self.levelUpAttacks = {1 : PoisonSting(), 6 : Supersonic(),
							   12 : Constrict(), 19 : Acid(), 
							   25 : Bubblebeam(), 30 : Wrap(), 36 : Barrier(),
							   43 : Screech(), 49 : HydroPump()}

	def evolve(self):
		return Tentacruel()

class Tentacruel(PocketMonster):

	def __init__(self):
		self.name = 'Tentacruel'
		baseHp = 80
		baseAttack = 70
		baseDefense = 65
		baseSpAttack = 80
		baseSpDefense = 120
		baseSpeed = 100
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 73
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water, poison]
		self.weight = 55.0 # kg
		self.height = 1.6 # m
		self.femaleRate = 50 # percent

		self.expGroup = slow
		self.catchRate = 60
		self.baseExpYield = 205

		self.levelUpAttacks = {1 : PoisonSting(), 6 : Supersonic(),
							   12 : Constrict(), 19 : Acid(), 
							   25 : Bubblebeam(), 30 : Wrap(), 38 : Barrier(),
							   47 : Screech(), 55 : HydroPump()}

class Geodude(PocketMonster):

	def __init__(self):
		self.name = 'Geodude'
		baseHp = 40
		baseAttack = 80
		baseDefense = 100
		baseSpAttack = 30
		baseSpDefense = 30
		baseSpeed = 20
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 74
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [rock, ground]
		self.weight = 20.0 # kg
		self.height = 0.8 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 25
		self.expGroup = mSlow
		self.catchRate = 255
		self.baseExpYield = 86

		self.levelUpAttacks = {1 : Tackle(), 2 : DefenseCurl(),
							   6 : MudSport(), 11 : RockThrow(), 
							   16 : Magnitude(), 21 : Selfdestruct(),
							   26 : Rollout(), 31 : RockBlast(),
							   36 : Earthquake(), 41 : Explosion(),
							   46 : DoubleEdge()}

	def evolve(self):
		return Graveler()

class Graveler(PocketMonster):

	def __init__(self):
		self.name = 'Graveler'
		baseHp = 55
		baseAttack = 95
		baseDefense = 115
		baseSpAttack = 45
		baseSpDefense = 45
		baseSpeed = 35
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 75
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [rock, ground]
		self.weight = 105.0 # kg
		self.height = 1.0 # m
		self.femaleRate = 50 # percent

		self.evolvesWith = 'trade'
		self.expGroup = mSlow
		self.catchRate = 120
		self.baseExpYield = 134

		self.levelUpAttacks = {1 : Tackle(), 2 : DefenseCurl(),
							   6 : MudSport(), 11 : RockThrow(), 
							   16 : Magnitude(), 21 : Selfdestruct(),
							   29 : Rollout(), 37 : RockBlast(),
							   45 : Earthquake(), 53 : Explosion(),
							   62 : DoubleEdge()}

	def evolve(self):
		return Golem() 