import random

def gen(length, max):
	return [random.randint(0,max) for i in range(length)]

def mergesort(array_ : list[int]) -> list[int]:
	# only one element, it is min and max
	if len(array_) == 1 :
		return array_
	# two elements, smaller to left side
	elif len(array_) == 2:
		if array_[0] < array_[1]:
			return [array_[0], array_[1]]
		return [array_[1], array_[0]]
	#recursion
	else:
		# split array
		pindex = 0
		pivot = array_[pindex]		
		b1 = []
		b2 = []
		# sort based on pivot element
		for num in array_:
			if num < pivot:
				b1.append(num)
			else:
				b2.append(num)
		# if b1 is empty, the pivot is the smallest element. add it
		# to b1, remove it from b2
		if not b1:
			b2.remove(pivot)
			b1 = [pivot]

		p1 = mergesort(b1)
		p2 = mergesort(b2)
		# merge
		return [*p1,*p2]

print(mergesort([14,2,4,5,3,8,11,9]))
print(mergesort(gen(100,1000)))
