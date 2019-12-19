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

class Magmar(PocketMonster):

	def __init__(self):
		self.name = 'Magmar'
		baseHp = 65
		baseAttack = 95
		baseDefense = 57
		baseSpAttack = 100
		baseSpDefense = 85
		baseSpeed = 93
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 126
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fire]
		self.weight = 44.5 # kg
		self.height = 1.3 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 167

		self.levelUpAttacks = {1 : Ember(), 7 : Leer(),
							   13 : Smog(), 19 : FirePunch(), 
							   25 : Smokescreen(), 33 : SunnyDay(),
							   41 : Flamethrower(), 49 : ConfuseRay(),
							   57 : FireBlast()}

class Pinsir(PocketMonster):

	def __init__(self):
		self.name = 'Pinsir'
		baseHp = 65
		baseAttack = 125
		baseDefense = 100
		baseSpAttack = 55
		baseSpDefense = 70
		baseSpeed = 85
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 127
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [bug]
		self.weight = 55.0 # kg
		self.height = 1.5 # m
		self.femaleRate = 50 # percent

		self.expGroup = slow
		self.catchRate = 45
		self.baseExpYield = 200

		self.levelUpAttacks = {1 : Vicegrip(), 2 : FocusEnergy(),
							   7 : Bind(), 13 : SeismicToss(), 
							   19 : Harden(), 25 : Revenge(),
							   31 : BrickBreak(), 37 : Guillotine(),
							   43 : Submission(), 49 : SwordsDance()}

class Tauros(PocketMonster):

	def __init__(self):
		self.name = 'Tauros'
		baseHp = 75
		baseAttack = 100
		baseDefense = 95
		baseSpAttack = 40
		baseSpDefense = 70
		baseSpeed = 110
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 128
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 88.4 # kg
		self.height = 1.4 # m
		self.femaleRate = 0 # percent

		self.expGroup = slow
		self.catchRate = 45
		self.baseExpYield = 211

		self.levelUpAttacks = {1 : Tackle(), 2 : TailWhip(),
							   4 : Rage(), 8 : HornAttack(), 
							   13 : ScaryFace(), 19 : Pursuit(),
							   26 : Swagger(), 34 : Rest(),
							   43 : Thrash(), 53 : TakeDown()}		

class Magikarp(PocketMonster):

	def __init__(self):
		self.name = 'Magikarp'
		baseHp = 20
		baseAttack = 10
		baseDefense = 55
		baseSpAttack = 15
		baseSpDefense = 20
		baseSpeed = 80
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 129
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 10.0 # kg
		self.height = 0.9 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 20
		self.expGroup = slow
		self.catchRate = 255
		self.baseExpYield = 20

		self.levelUpAttacks = {1 : Splash(), 15 : Tackle(),
							   30 : Flail()}

	def evolve(self):
		return Gyrados()

class Gyarados(PocketMonster):

	def __init__(self):
		self.name = 'Gyarados'
		baseHp = 95
		baseAttack = 125
		baseDefense = 79
		baseSpAttack = 60
		baseSpDefense = 100
		baseSpeed = 81
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 130
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water, flying]
		self.weight = 235.0 # kg
		self.height = 6.5 # m
		self.femaleRate = 50 # percent

		self.expGroup = slow
		self.catchRate = 45
		self.baseExpYield = 214

		self.levelUpAttacks = {1 : Thrash(), 20 : Bite(),
							   25 : DragonRage(), 30 : Leer(), 
							   35 : Twister(), 40 : HydroPump(),
							   45 : RainDance(), 50 : DragonDance(),
							   55 : HyperBeam()}	

class Lapras(PocketMonster):

	def __init__(self):
		self.name = 'Lapras'
		baseHp = 130
		baseAttack = 85
		baseDefense = 80
		baseSpAttack = 85
		baseSpDefense = 95
		baseSpeed = 60
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 131
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water, ice]
		self.weight = 220.0 # kg
		self.height = 2.5 # m
		self.femaleRate = 50 # percent

		self.expGroup = slow
		self.catchRate = 45
		self.baseExpYield = 219

		self.levelUpAttacks = {1 : WaterGun(), 2 : Growl(),
							   3 : Sing(), 7 : Mist(), 
							   13 : BodySlam(), 19 : ConfuseRay(),
							   25 : PerishSong(), 31 : IceBeam(),
							   37 : RainDance(), 43 : Safeguard(),
							   49 : HydroPump(), 55 : SheerCold()}

class Ditto(PocketMonster):

	def __init__(self):
		self.name = 'Ditto'
		baseHp = 48
		baseAttack = 48
		baseDefense = 48
		baseSpAttack = 48
		baseSpDefense = 48
		baseSpeed = 48
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 132
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 4.0 # kg
		self.height = 0.3 # m
		self.femaleRate = -1 # genderless

		self.expGroup = mFast
		self.catchRate = 35
		self.baseExpYield = 61

		self.levelUpAttacks = {1 : Transform()}	

class Eevee(PocketMonster):

	def __init__(self):
		self.name = 'Eevee'
		baseHp = 55
		baseAttack = 55
		baseDefense = 50
		baseSpAttack = 45
		baseSpDefense = 65
		baseSpeed = 55
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 133
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 6.5 # kg
		self.height = 0.3 # m
		self.femaleRate = 50 # percent

		self.evolvesWith = ['thunderstone', 'firestone', 'waterstone']
		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 92

		self.levelUpAttacks = {1 : Tackle(), 2 : TailWhip(),
							   3 : HelpingHand(), 8 : SandAttack(),
							   16 : Growl(), 23 : QuickAttack(),
							   30 : Bite(), 36 : BatonPass(),
							   42 : TakeDown()}

	def evolve(self, special=''):
		if special == '':
			pass
		elif special == 'waterstone':
			return Vaporeon()
		elif special == 'thunderstone':
			return Jolteon()
		elif special == 'firestone':
			return Flareon()
	
class Vaporeon(PocketMonster):

	def __init__(self):
		self.name = 'Vaporeon'
		baseHp = 130
		baseAttack = 65
		baseDefense = 60
		baseSpAttack = 110
		baseSpDefense = 95
		baseSpeed = 65
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 134
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [water]
		self.weight = 29.0 # kg
		self.height = 1.0 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 196

		self.levelUpAttacks = {1 : Tackle(), 2 : TailWhip(),
							   3 : HelpingHand(), 8 : SandAttack(),
							   16 : WaterGun(), 23 : QuickAttack(),
							   30 : Bite(), 36 : AuroraBeam(),
							   42 : Haze(), 47 : AcidArmor(),
							   52 : HydroPump()}	

class Jolteon(PocketMonster):

	def __init__(self):
		self.name = 'Jolteon'
		baseHp = 65
		baseAttack = 65
		baseDefense = 60
		baseSpAttack = 110
		baseSpDefense = 95
		baseSpeed = 130
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 135
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [electric]
		self.weight = 24.5 # kg
		self.height = 0.8 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 197

		self.levelUpAttacks = {1 : Tackle(), 2 : TailWhip(),
							   3 : HelpingHand(), 8 : SandAttack(),
							   16 : Thundershock(), 23 : QuickAttack(),
							   30 : DoubleKick(), 36 : PinMissile(),
							   42 : ThunderWave(), 47 : Agility(),
							   52 : Thunder()}	

class Flareon(PocketMonster):

	def __init__(self):
		self.name = 'Flareon'
		baseHp = 65
		baseAttack = 130
		baseDefense = 60
		baseSpAttack = 95
		baseSpDefense = 110
		baseSpeed = 65
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 136
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fire]
		self.weight = 25.0 # kg
		self.height = 0.9 # m
		self.femaleRate = 50 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 198

		self.levelUpAttacks = {1 : Tackle(), 2 : TailWhip(),
							   3 : HelpingHand(), 8 : SandAttack(),
							   16 : Ember(), 23 : QuickAttack(),
							   30 : Bite(), 36 : FireSpin(),
							   42 : Smog(), 47 : Leer(),
							   52 : Flamethrower()}

class Porygon(PocketMonster):

	def __init__(self):
		self.name = 'Porygon'
		baseHp = 65
		baseAttack = 60
		baseDefense = 70
		baseSpAttack = 85
		baseSpDefense = 75
		baseSpeed = 40
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 137
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 36.5 # kg
		self.height = 0.8 # m
		self.femaleRate = -1 # genderless

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 130

		self.levelUpAttacks = {1 : Conversion2(), 2 : Tackle(),
							   3 : Conversion(), 9 : Agility(),
							   12 : Psybeam(), 20 : Recover(),
							   24 : Sharpen(), 32 : LockOn(),
							   36 : TriAttack(), 44 : Recycle(),
							   48 : ZapCannon()}

class Omanyte(PocketMonster):

	def __init__(self):
		self.name = 'Omanyte'
		baseHp = 35
		baseAttack = 40
		baseDefense = 100
		baseSpAttack = 90
		baseSpDefense = 55
		baseSpeed = 35
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 138
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [rock, water]
		self.weight = 7.5 # kg
		self.height = 0.4 # m
		self.femaleRate = 13 # percent

		self.evolvesAt = 40
		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 120

		self.levelUpAttacks = {1 : Constrict(), 2 : Withdraw(),
							   13 : Bite(), 19 : WaterGun(),
							   25 : MudShot(), 31 : Leer(),
							   37 : Protect(), 43 : Tickle(),
							   49 : Ancientpower(), 55 : HydroPump()}

	def evolve(self):
		return Omastar()

class Omastar(PocketMonster):

	def __init__(self):
		self.name = 'Omastar'
		baseHp = 70
		baseAttack = 60
		baseDefense = 125
		baseSpAttack = 115
		baseSpDefense = 70
		baseSpeed = 55
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 139
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [rock, water]
		self.weight = 35.0 # kg
		self.height = 1.0 # m
		self.femaleRate = 13 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 199

		self.levelUpAttacks = {1 : Constrict(), 2 : Withdraw(),
							   13 : Bite(), 19 : WaterGun(),
							   25 : MudShot(), 31 : Leer(),
							   37 : Protect(), 40 : SpikeCannon(), 46 : Tickle(),
							   55 : Ancientpower(), 65 : HydroPump()}

class Kabuto(PocketMonster):

	def __init__(self):
		self.name = 'Kabuto'
		baseHp = 30
		baseAttack = 80
		baseDefense = 90
		baseSpAttack = 55
		baseSpDefense = 45
		baseSpeed = 55
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 140
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [rock, water]
		self.weight = 11.5 # kg
		self.height = 0.5 # m
		self.femaleRate = 13 # percent

		self.evolvesAt = 40
		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 119

		self.levelUpAttacks = {1 : Scratch(), 2 : Harden(),
							   13 : Absorb(), 19 : Leer(),
							   25 : MudShot(), 31 : SandAttack(),
							   37 : Endure(), 43 : MetalSound(),
							   49 : MegaDrain(), 55 : Ancientpower()}

	def evolve(self):
		return Kabutops()

class Kabutops(PocketMonster):

	def __init__(self):
		self.name = 'Kabutops'
		baseHp = 60
		baseAttack = 115
		baseDefense = 105
		baseSpAttack = 65
		baseSpDefense = 70
		baseSpeed = 80
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 141
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [rock, water]
		self.weight = 40.5 # kg
		self.height = 1.3 # m
		self.femaleRate = 13 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 201

		self.levelUpAttacks = {1 : Scratch(), 2 : Harden(),
							   13 : Absorb(), 19 : Leer(),
							   25 : MudShot(), 31 : SandAttack(),
							   37 : Endure(), 40 : Slash(), 46 : MetalSound(),
							   55 : MegaDrain(), 65 : Ancientpower()}

class Aerodactyl(PocketMonster):

	def __init__(self):
		self.name = 'Aerodactyl'
		baseHp = 80
		baseAttack = 105
		baseDefense = 65
		baseSpAttack = 60
		baseSpDefense = 75
		baseSpeed = 130
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 142
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [rock, flying]
		self.weight = 59.0 # kg
		self.height = 1.8 # m
		self.femaleRate = 13 # percent

		self.expGroup = mFast
		self.catchRate = 45
		self.baseExpYield = 202

		self.levelUpAttacks = {1 : WingAttack(), 8 : Agility(),
							   15 : Bite(), 22 : Supersonic(),
							   29 : Ancientpower(), 36 : ScaryFace(),
							   43 : TakeDown(), 50 : HyperBeam()}

class Snorlax(PocketMonster):

	def __init__(self):
		self.name = 'Snorlax'
		baseHp = 160
		baseAttack = 110
		baseDefense = 65
		baseSpAttack = 65
		baseSpDefense = 110
		baseSpeed = 30
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 143
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [normal]
		self.weight = 460.0 # kg
		self.height = 2.1 # m
		self.femaleRate = 13 # percent

		self.expGroup = mFast
		self.catchRate = 25
		self.baseExpYield = 154

		self.levelUpAttacks = {1 : Tackle(), 5 : Amnesia(),
							   9 : DefenseCurl(), 13 : BellyDrum(),
							   17 : Headbutt(), 21 : Yawn(),
							   25 : Rest(), 29 : Snore(),
							   33 : BodySlam(), 37 : SleepTalk(),
							   41 : Block(), 45 : Covet(),
							   49 : Rollout(), 53 : HyperBeam()}

class Articuno(PocketMonster):

	def __init__(self):
		self.name = 'Articuno'
		baseHp = 90
		baseAttack = 85
		baseDefense = 100
		baseSpAttack = 95
		baseSpDefense = 125
		baseSpeed = 85
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 144
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [ice, flying]
		self.weight = 55.4 # kg
		self.height = 1.7 # m
		self.femaleRate = -1 # genderless

		self.expGroup = slow
		self.catchRate = 3
		self.baseExpYield = 215

		self.levelUpAttacks = {1 : Gust(), 2 : PowderSnow(),
							   13 : Mist(), 25 : Agility(),
							   37 : MindReader(), 49 : IceBeam(),
							   61 : Reflect(), 73 : Blizzard(),
							   85 : SheerCold()}

class Zapdos(PocketMonster):

	def __init__(self):
		self.name = 'Zapdos'
		baseHp = 90
		baseAttack = 90
		baseDefense = 85
		baseSpAttack = 125
		baseSpDefense = 90
		baseSpeed = 100
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 145
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [electric, flying]
		self.weight = 52.6 # kg
		self.height = 1.6 # m
		self.femaleRate = -1 # genderless

		self.expGroup = slow
		self.catchRate = 3
		self.baseExpYield = 216

		self.levelUpAttacks = {1 : Peck(), 2 : Thundershock(),
							   13 : ThunderWave(), 25 : Agility(),
							   37 : Detect(), 49 : DrillPeck(),
							   61 : Charge(), 73 : LightScreen(),
							   85 : Thunder()}

class Moltres(PocketMonster):

	def __init__(self):
		self.name = 'Moltres'
		baseHp = 90
		baseAttack = 100
		baseDefense = 90
		baseSpAttack = 125
		baseSpDefense = 85
		baseSpeed = 90
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 146
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [fire, flying]
		self.weight = 60.0 # kg
		self.height = 2.0 # m
		self.femaleRate = -1 # genderless

		self.expGroup = slow
		self.catchRate = 3
		self.baseExpYield = 217

		self.levelUpAttacks = {1 : WingAttack(), 2 : Ember(),
							   13 : FireSpin(), 25 : Agility(),
							   37 : Endure(), 49 : Flamethrower(),
							   61 : Safeguard(), 73 : HeatWave(),
							   85 : SkyAttack()}

class Dratini(PocketMonster):

	def __init__(self):
		self.name = 'Dratini'
		baseHp = 41
		baseAttack = 64
		baseDefense = 45
		baseSpAttack = 50
		baseSpDefense = 50
		baseSpeed = 50
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 147
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [dragon]
		self.weight = 3.3 # kg
		self.height = 1.8 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 30
		self.expGroup = slow
		self.catchRate = 45
		self.baseExpYield = 67

		self.levelUpAttacks = {1 : Wrap(), 2 : Leer(),
							   8 : ThunderWave(), 15 : Twister(),
							   22 : DragonRage(), 29 : Slam(),
							   36 : Agility(), 43 : Safeguard(),
							   50 : Outrage(), 57 : HyperBeam()}

	def evolve(self):
		return Dragonair()

class Dragonair(PocketMonster):

	def __init__(self):
		self.name = 'Dragonair'
		baseHp = 61
		baseAttack = 84
		baseDefense = 65
		baseSpAttack = 70
		baseSpDefense = 70
		baseSpeed = 70
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 148
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [dragon]
		self.weight = 16.5 # kg
		self.height = 4.0 # m
		self.femaleRate = 50 # percent

		self.evolvesAt = 55
		self.expGroup = slow
		self.catchRate = 45
		self.baseExpYield = 144

		self.levelUpAttacks = {1 : Wrap(), 2 : Leer(),
							   8 : ThunderWave(), 15 : Twister(),
							   22 : DragonRage(), 29 : Slam(),
							   38 : Agility(), 47 : Safeguard(),
							   56 : Outrage(), 65 : HyperBeam()}

	def evolve(self):
		return Dragonite()

class Dragonite(PocketMonster):

	def __init__(self):
		self.name = 'Dragonite'
		baseHp = 91
		baseAttack = 134
		baseDefense = 95
		baseSpAttack = 100
		baseSpDefense = 100
		baseSpeed = 80
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 149
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [dragon, flying]
		self.weight = 210.0 # kg
		self.height = 2.2 # m
		self.femaleRate = 50 # percent

		self.expGroup = slow
		self.catchRate = 45
		self.baseExpYield = 218

		self.levelUpAttacks = {1 : Wrap(), 2 : Leer(),
							   8 : ThunderWave(), 15 : Twister(),
							   22 : DragonRage(), 29 : Slam(),
							   38 : Agility(), 47 : Safeguard(),
							   55 : WingAttack(), 61 : Outrage(), 
							   75 : HyperBeam()}

class Mewtwo(PocketMonster):

	def __init__(self):
		self.name = 'Mewtwo'
		baseHp = 106
		baseAttack = 110
		baseDefense = 90
		baseSpAttack = 154
		baseSpDefense = 90
		baseSpeed = 130
		super().__init__(baseHp, baseAttack, baseDefense, baseSpAttack, baseSpDefense, baseSpeed)


		self.number = 150
		self.image = '%s-%s.png' % (str(self.number).zfill(3), self.name.lower())

		self.type = [psychic]
		self.weight = 122.0 # kg
		self.height = 2.0 # m
		self.femaleRate = -1 # genderless

		self.expGroup = slow
		self.catchRate = 3
		self.baseExpYield = 220

		self.levelUpAttacks = {1 : Confusion(), 2 : Disable(),
							   11 : Barrier(), 22 : Mist(),
							   33 : Swift(), 44 : Recover(),
							   55 : Safeguard(), 66 : Psychic(),
							   77 : PsychUp(), 88 : FutureSight(), 
							   99 : Amnesia()}
