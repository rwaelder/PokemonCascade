import pickle
from os.path import sep

def save(pokemon):
	pickling_on = open('poke.pickle', 'wb')
	pickle.dump(pokemon, pickling_on)
	pickling_on.close()

def load():
	pickling_off = open('poke.pickle', 'rb')
	pokemon = pickle.load(pickling_off)
	return pokemon

def save_map_square(mapSquare, mapName):
	savefile = 'mapSquares' + sep + mapName + '.pickle'
	pickling_on = open(savefile, 'wb')
	pickle.dump(mapSquare, pickling_on)
	pickling_on.close()

def load_map_square(mapName):
	if '.pickle' not in mapName:
		mapName += '.pickle'

	if 'mapSquares' not in mapName:
		mapName = 'mapSquares' + sep + mapName

	pickling_off = open(mapName, 'rb')
	mapSquare = pickle.load(pickling_off)
	return mapSquare