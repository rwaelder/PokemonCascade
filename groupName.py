from saveLoad import load_map_square
from sys import argv

def broken():
	print('Map not found or specified.')
	exit()

if len(argv) < 2:
	broken()

try:
	mm = load_map_square(argv[1])
	print(mm.tiles[0][0].group)

except:
	broken()


