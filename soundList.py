
def get_sound(soundName):
	if soundName in soundLibrary:
		return soundLibrary[soundName]
	else:
		return None

def get_attack_sound(attackName):
	name = attackName.replace(' ', '_')
	fileName = 'sounds/attacks/%s.wav' % name
	# print(fileName)
	return fileName

def get_pokemon_cry(pokemon):
	cry = '%s - %s.wav' % (str(pokemon.number).zfill(3), pokemon.name)
	fileName = 'sounds/cries/%s' % cry
	return fileName

soundLibrary = {}
soundLibrary['Super Effective']    = 'sounds/attacks/Hit_Super_Effective.wav'
soundLibrary['Damage']             = 'sounds/attacks/Hit_Normal_Damage.wav'
soundLibrary['Not Very Effective'] = 'sounds/attacks/Hit_Weak_Not_Very_Effective.wav'

