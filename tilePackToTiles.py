from PIL import Image
from sys import argv


tilePack = Image.open(argv[1])
tilePack = tilePack.resize((768, 768))
tileSize = 48
folder = argv[1].split('.')[0] + '/'

for x in range(16):
	for y in range(16):
		saveTile = tilePack.crop((x*tileSize, y*tileSize, (x+1)*tileSize, (y+1)*tileSize))
		saveFile = folder + '%i_%i.png' % (x+1, y+1)
		saveTile.save(saveFile)