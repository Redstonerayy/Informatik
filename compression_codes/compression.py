from PIL import Image
from itertools import chain

img = [
	[0,0,0,240,240,240],
	[0,0,0,240,240,240],
	[240, 240, 240, 0,0,0],
	[240, 240, 240, 240, 240,0],
	[240, 240, 240, 240, 240,0],
	[240, 240, 240, 240, 240,0],
]

def printimg(img):
	for i in img:
		print(i)

def getmean(img, x, y, xcount, ycount):
	values = []
	for j in range(y, y + ycount):
		try:
			for i in range(x, x + xcount):
				values.append(img[j][i])
		except:
			pass # out of range

	return int(sum(values)/len(values))

def scale(img, scalex, scaley):
	xcomb = round(len(img[0])/scalex)
	ycomb = round(len(img)/scaley)
	newimg = [[0 for i in range(scalex)] for j in range(scaley)]
	for y in range(scaley):
		for x in range(scalex):
			newimg[y][x] = getmean(img, x * xcomb, y * ycomb, xcomb, ycomb)
	return newimg

newi = scale(img, 3, 3)

img1 = Image.new("L", (len(img[0]), len(img)))
img1.putdata(list(chain(*img)))
img1.save("unscaled.png")

img2 = Image.new("L", (len(newi[0]), len(newi)))
img2.putdata(list(chain(*newi)))
img2.save("scaled.png")
