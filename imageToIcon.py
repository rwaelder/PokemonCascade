from PIL import Image
import sys

characteristicSize = 250


def shrink(img):
    width = img.size[0]
    height = img.size[1]

    if width > height:
        w = characteristicSize
        h = int((w/width)*height)
        size = w,h
    elif height > width:
        h = characteristicSize
        w = int((h/height)*width)
        size = w,h
    elif width == height:
        w = characteristicSize
        h = characteristicSize
        size = w,h
    return img.resize(size)



file = sys.argv[1]

inImage = Image.open(file)

inImage = shrink(inImage)

size = (characteristicSize, characteristicSize)

outImage = Image.new('RGB', size, color=(255,255,255))



outImage.paste(inImage, (int((size[0] - inImage.size[0]) / 2), int((size[1] - inImage.size[1]) / 2)))

outpath = 'trainerIcons/' + file.split('/')[1]
outpath = outpath.replace('.jpg', '.png')
outpath = outpath.replace('.jpeg', '.png')
# print(outpath)
outImage.save(outpath, "png")