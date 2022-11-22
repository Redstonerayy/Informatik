import random

# set seed so output is comparable
random.seed(10)

# swap to  values of array at indices i1, i2
def swap(array_, i1, i2):
    temp = array_[i1]
    array_[i1] = array_[i2]
    array_[i2] = temp


# generate random unsorted list
def gen(length: int):
    liste = [random.randint(0, 100) for i in range(length)]
    return liste


def merge(arr1, arr2):
    # merge two sorted lists into one sorted list
    # and return this list
    i = 0
    j = 0
    result = []
    # compare and add elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # add rest of the unfinished array
    if i < len(arr1):
        result += arr1[i:]
    else:
        result += arr2[j:]

    return result


def mergesort(_array):
    # for lists of length 2 or less return it
    # in sorted form
    if len(_array) == 1:
        return _array
    elif len(_array) == 2:
        if _array[0] > _array[1]:
            return [_array[1], _array[0]]
        return _array
    else:
        # recursively call the sort on two parts of the list
        middle = len(_array) // 2
        return merge(mergesort(_array[:middle]), mergesort(_array[middle:]))


liste = gen(100)
print(liste)
liste = mergesort(liste)
print(liste)
