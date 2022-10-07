import random

def gen(length):
	return [random.randint(1,1000) for i in range(length)]

def divide_and_conquers(array_ : list[int]) -> tuple[int, int]:
	# only one element, it is min and max
	if len(array_) == 1:
		return array_[0], array_[0]
	# two elements, smaller is min, other max
	elif len(array_) == 2:
		if array_[0] < array_[1]:
			return array_[0], array_[1]
		return array_[1], array_[0]
	#recursion
	else:
		# split array
		# find min, max for each array
		min1, max1 = divide_and_conquers(array_[:len(array_)//2])
		min2, max2 = divide_and_conquers(array_[len(array_)//2:])
		# check which array has the large or smaller min, max
		return min1 if min1 < min2 else min2, max1 if max1 > max2 else max2 

liste = [25, 6,7,10,3,20,5,13,9,8]
print(divide_and_conquers(liste))
print(divide_and_conquers(gen(100)))
