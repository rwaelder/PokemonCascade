

class Trainer():

	def __init__(self, party=[], items=[], name='Trainer'):
		self.party = party
		self.items = items
		self.name = name

		self.image = 'Spr_B2W2_Youngster.png'


	def canBattle(self):
		pokeStatus = []
		for pokemon in self.party:
			pokeStatus.append(pokemon.fainted)

		if False in pokeStatus:
			return True
		else:
			return False

	def computer_choose_next_battler(self):

		for i, pokemon in enumerate(self.party):
			if not pokemon.fainted:
				return i

	def reset_battle_stats(self):
		for pokemon in self.party:
			pokemon.reset_battle_stats()

class MainPlayer(Trainer):

	def __init__(self, party=[], items=[], name='Player'):
		super().__init__(party, items, name)

		self.image = 'Spr_B2W2_Nate.png'

