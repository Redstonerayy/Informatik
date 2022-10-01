from tabnanny import check
from PIL import Image

def imagediff(img1, img2):
	diff = []
	
	for i in range(len(img1)):
		temp = []
		for j in range(len(img1[0])):
			if (img1[i][j] != img2[i][j]):
				temp.append(1)
			else:
				temp.append(0)
			
		diff.append(temp[:])

	return diff

def printimg(img):
	for row in img:
		print(row)
	
def makeimg(img, filename):
	data = []
	for i in range(len(img)):
		for j in range(len(img[0])):
			if img[i][j]:
				data.append(255)
			else:
				data.append(0)

	img = Image.new('L', (len(img[0]), len(img)))
	img.putdata(data)
	img.save(filename)

	return data

def imgfromdata(data, x, y):
	img = Image.new('L', (x, y))
	img.putdata(data)
	img.save("joined.png")

def checksize(img):
	for y in range(len(img)):
		for x in range(len(img[y])):
			lcount, lchecks = checkpixel(img, x, y)
			if img[y][x]:
				print(y, x)
				print(lcount, lchecks)
			else:
				if lchecks == 9 and lcount == 0: # dark square 3x3
					print(y, x)
					print(lcount, lchecks)


def checkpixel(img, x, y):
	count = 0
	checks = 0
	ystart = y - 1 if y - 1 > -1 else 0
	yend = y + 2 if y + 2 < len(img) else len(img)
	xstart = x - 1 if x - 1 > -1 else 0
	xend = x + 2 if x + 2 < len(img[y]) else len(img[y])
	for y in range(ystart, yend):
		for x in range(xstart, xend):
			checks += 1
			if img[y][x]:
				count += 1
			
	return count, checks


# img data
bild1 = [[0,0,0,0,0,0,0,0,0,0],
		 [0,1,0,0,0,0,0,0,0,1],
		 [0,0,0,0,0,1,1,0,0,0],
		 [0,0,0,1,0,1,1,0,0,0],
		 [0,0,0,0,0,0,0,0,0,0],
		 [0,0,1,0,0,0,0,0,0,0],
		 [1,0,0,0,0,0,0,0,1,0],
		 [0,0,0,0,1,0,0,0,0,0],
		 [0,0,0,0,0,0,0,1,0,0],
		 [0,1,1,0,0,0,0,0,0,0]]

bild2 = [[0,0,0,0,0,0,0,0,0,0],
		 [0,1,0,0,0,0,0,0,0,1],
		 [0,0,0,0,0,1,1,0,0,0],
		 [0,0,0,1,0,1,1,0,0,0],
		 [0,0,0,0,0,0,0,0,0,0],
		 [0,0,0,1,0,0,0,0,0,0],
		 [1,0,0,0,0,0,0,0,1,0],
		 [0,0,0,0,1,0,0,0,0,0],
		 [0,0,0,0,0,0,0,1,0,0],
		 [0,1,1,0,0,0,0,0,0,0]]
