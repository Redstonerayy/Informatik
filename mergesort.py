import random

from regex import P

def gen(length):
	return [random.randint(1,1000) for i in range(length)]

def divide_and_conquer(array_ : list[int]) -> list[int]:
	# only one element, it is min and max
	if len(array_) < 2 :
		return array_
	# two elements, smaller is min, other max
	elif len(array_) == 2:
		if array_[0] < array_[1]:
			return [array_[0], array_[1]]
		return [array_[1], array_[0]]
	#recursion
	else:
		# split array
		pindex = 0
		pivot = array_[pindex]
		while True:
			b1 = []
			b2 = []
			for num in array_:
				if num < pivot:
					b1.append(num)
				else:
					b2.append(num)
			if not b1 and b2:
				pindex += 1
				#is sorted
				if pindex == len(array_):
					return array_
				pivot = array_[pindex]
				continue
			break

		print(b1)
		print(b2)
		print("----")

		p1 = divide_and_conquer(b1)
		p2 = divide_and_conquer(b2)
		# merge
		return [*p1,*p2]

print(divide_and_conquer([1,2,4,5,3,8,11,9]))