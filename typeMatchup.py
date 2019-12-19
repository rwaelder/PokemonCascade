from pokemonTypes import *


normalMatchup = {normal : 1, fight : 1, flying : 1, poison : 1, ground : 1,
				rock : 0.5, bug : 1, ghost : 0, steel : 0.5, fire : 1,
				water : 1, grass : 1, electric : 1, psychic : 1,
				ice : 1, dragon : 1, dark : 1, fairy : 1}

fightMatchup  = {normal : 2, fight : 1, flying : 0.5, poison : 0.5, ground : 1,
				rock : 2, bug : 0.5, ghost : 0, steel : 2, fire : 1,
				water : 1, grass : 1, electric : 1, psychic : 0.5,
				ice : 2, dragon : 1, dark : 2, fairy : 0.5}

flyingMatchup = {normal : 1, fight : 2, flying : 1, poison : 1, ground : 1,
				rock : 0.5, bug : 2, ghost : 1, steel : 0.5, fire : 1,
				water : 1, grass : 2, electric : 0.5, psychic : 1,
				ice : 1, dragon : 1, dark : 1, fairy : 1}

poisonMatchup = {normal : 1, fight : 1, flying : 1, poison : 0.5, ground : 0.5,
				rock : 0.5, bug : 1, ghost : 0.5, steel : 0, fire : 1,
				water : 1, grass : 2, electric : 1, psychic : 1,
				ice : 1, dragon : 1, dark : 1, fairy : 2}

groundMatchup = {normal : 1, fight : 1, flying : 0, poison : 2, ground : 1,
				rock : 2, bug : 0.5, ghost : 1, steel : 2, fire : 2,
				water : 1, grass : 0.5, electric : 2, psychic : 1,
				ice : 1, dragon : 1, dark : 1, fairy : 1}

rockMatchup   = {normal : 1, fight : 0.5, flying : 2, poison : 1, ground : 0.5,
				rock : 1, bug : 2, ghost : 1, steel : 0.5, fire : 2,
				water : 1, grass : 1, electric : 1, psychic : 1,
				ice : 2, dragon : 1, dark : 1, fairy : 1}

bugMatchup    = {normal : 1, fight : 0.5, flying : 0.5, poison : 0.5, ground : 1,
				rock : 1, bug : 1, ghost : 0.5, steel : 0.5, fire : 0.5,
				water : 1, grass : 2, electric : 1, psychic : 2,
				ice : 1, dragon : 1, dark : 2, fairy : 0.5}

ghostMatchup  = {normal : 0, fight : 1, flying : 1, poison : 1, ground : 1,
				rock : 1, bug : 1, ghost : 2, steel : 1, fire : 1,
				water : 1, grass : 1, electric : 1, psychic : 2,
				ice : 1, dragon : 1, dark : 0.5, fairy : 1}

steelMatchup  = {normal : 1, fight : 1, flying : 1, poison : 1, ground : 1,
				rock : 2, bug : 1, ghost : 1, steel : 0.5, fire : 0.5,
				water : 0.5, grass : 1, electric : 0.5, psychic : 1,
				ice : 2, dragon : 1, dark : 1, fairy : 2}

fireMatchup   = {normal : 1, fight : 1, flying : 1, poison : 1, ground : 1,
				rock : 0.5, bug : 2, ghost : 1, steel : 2, fire : 0.5,
				water : 0.5, grass : 2, electric : 1, psychic : 1,
				ice : 2, dragon : 0.5, dark : 1, fairy : 1}

waterMatchup  = {normal : 1, fight : 1, flying : 1, poison : 1, ground : 2,
				rock : 2, bug : 1, ghost : 1, steel : 1, fire : 2,
				water : 0.5, grass : 0.5, electric : 1, psychic : 1,
				ice : 1, dragon : 0.5, dark : 1, fairy : 1}	

grassMatchup  = {normal : 1, fight : 1, flying : 0.5, poison : 0.5, ground : 2,
				rock : 2, bug : 0.5, ghost : 1, steel : 0.5, fire : 0.5,
				water : 2, grass : 0.5, electric : 1, psychic : 1,
				ice : 1, dragon : 0.5, dark : 1, fairy : 1}		

electricMatchup={normal : 1, fight : 1, flying : 2, poison : 1, ground : 0,
				rock : 1, bug : 1, ghost : 1, steel : 1, fire : 1,
				water : 2, grass : 0.5, electric : 0.5, psychic : 1,
				ice : 1, dragon : 0.5, dark : 1, fairy : 1}

psychicMatchup= {normal : 1, fight : 2, flying : 1, poison : 2, ground : 1,
				rock : 1, bug : 1, ghost : 1, steel : 0.5, fire : 1,
				water : 1, grass : 1, electric : 1, psychic : 0.5,
				ice : 1, dragon : 1, dark : 0, fairy : 1}

iceMatchup    = {normal : 1, fight : 1, flying : 2, poison : 1, ground : 2,
				rock : 1, bug : 1, ghost : 1, steel : 0.5, fire : 0.5,
				water : 0.5, grass : 2, electric : 1, psychic : 1,
				ice : 0.5, dragon : 2, dark : 1, fairy : 1}


dragonMatchup = {normal : 1, fight : 1, flying : 1, poison : 1, ground : 1,
				rock : 1, bug : 1, ghost : 1, steel : 0.5, fire : 1,
				water : 1, grass : 1, electric : 1, psychic : 1,
				ice : 1, dragon : 2, dark : 1, fairy : 0}

darkMatchup   = {normal : 1, fight : 0.5, flying : 1, poison : 1, ground : 1,
				rock : 1, bug : 1, ghost : 2, steel : 1, fire : 1,
				water : 1, grass : 1, electric : 1, psychic : 2,
				ice : 1, dragon : 1, dark : 0.5, fairy : 0.5}

fairyMatchup  = {normal : 1, fight : 2, flying : 1, poison : 0.5, ground : 1,
				rock : 1, bug : 1, ghost : 1, steel : 0.5, fire : 0.5,
				water : 1, grass : 1, electric : 1, psychic : 1,
				ice : 1, dragon : 2, dark : 2, fairy : 1}


typeMatchup = {normal : normalMatchup, fight : fightMatchup, flying : flyingMatchup,
			  poison : poisonMatchup, ground : groundMatchup, rock : rockMatchup,
			  bug : bugMatchup, ghost : ghostMatchup, steel : steelMatchup,
			  fire : fireMatchup, water : waterMatchup, grass : grassMatchup,
			  electric : electricMatchup, psychic : psychicMatchup,
			  ice : iceMatchup, dragon : dragonMatchup, dark : darkMatchup,
			  fairy : fairyMatchup}

def get_type_modifier(attackType, defendingType):
	modifier = 1
	for pokemonType in defendingType:
		modifier *= typeMatchup[attackType][pokemonType]

	return modifier
