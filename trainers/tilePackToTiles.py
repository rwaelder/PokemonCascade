from PIL import Image
from sys import argv


tilePack = Image.open(argv[1])
# tilePack = tilePack.resize((768, 768))
# tileSize = 48
folder = argv[1].split('.')[0] + '/'

xRange = 12
yRange = 8

width, height = tilePack.size

height = int(height / yRange)
width = int(width / xRange)

yOffset = 32
# tileSize = 16

for x in range(12):
	for y in range(8):
		saveTile = tilePack.crop((x*width+4, y*height+yOffset, (x+1)*width-4, (y+1)*height))
		saveFile = folder + '%i_%i.png' % (x+1, y+1)
		saveTile.save(saveFile)