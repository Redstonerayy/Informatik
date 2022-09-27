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

diff = imagediff(bild1, bild2)
printimg(diff)
img1data = makeimg(bild1, "bild1.png")
img2data = makeimg(bild2, "bild2.png")
diffdata = makeimg(diff, "diff.png")
joined = [*img1data, *img2data, *diffdata]
imgfromdata(joined, 10, 30)

