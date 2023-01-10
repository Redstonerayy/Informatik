def mirror_horizontal(bild):
	width = len(bild[0])
	height = len(bild)
	for x in range(width):
		for y in range(height // 2):
			temp = bild[y][x]
			bild[y][x] = bild[height - 1 - y][x]
			bild[height - 1 - y][x] = temp

def mirror_vertical(bild):
	width = len(bild[0])
	height = len(bild)
	for y in range(height):
		for x in range(width // 2):
			temp = bild[y][x]
			bild[y][x] = bild[y][width - 1 - x]
			bild[y][width - 1 - x] = temp

def rotate(bild, angle): # 1, 2, 3 = 90*, 180*, 270* to the right
	width = len(bild[0])
	height = len(bild)
	if angle == 1 or angle == 3:
		pass
	else: # 180*	
		for x in range(width):
			for y in range(height // 2):
				temp = bild[y][x]
				bild[y][x] = bild[height - 1 - y][width - 1 - x]
				bild[height - 1 - y][width - 1 - x] = temp

def printbild(bild):
	for row in bild:
		print(row)

bild = [
	[1, 2, 3],
	[4, 5, 6]
]

printbild(bild)
# mirror_vertical(bild)
# mirror_horizontal(bild)
rotate(bild, 2)
printbild(bild)

