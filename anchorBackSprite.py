from PIL import Image
from sys import argv

oldImage = Image.open(argv[1])

width, height = oldImage.size

lastPixel = (0, 0, 0, 0)

for y in range(height):
	for x in range(width):
		currentPixel = oldImage.getpixel((x, y))

		if currentPixel != lastPixel:
			row = y
		else:
			continue

		lastPixel = currentPixel

newImage = Image.new(mode='RGBA', size=(width, height), color=(0, 0, 0, 0))

cropped = oldImage.crop((0, 0, width, row))

newImage.paste(cropped, box=(0, height-row))


# newImage.show()
newImage.save(argv[1])