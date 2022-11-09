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

# not in place, middle is inclusive
def merge_faster_more_space(_array, start, middle, end):
    # code to merge the 2 unsorted parts of the list
    # into a new list and overwrite the main list with
    # the sorted values at the right indices
    i = start
    j = middle + 1
    result = []
    # compare and add elements
    while i < middle + 1 and j < end + 1:
        if _array[i] < _array[j]:
            result.append(_array[i])
            i += 1
        else:
            result.append(_array[j])
            j += 1

    # add rest of the unfinished array
    if i < middle + 1:
        result += _array[i:middle + 1]
    else:
        result += _array[j:end + 1]

    # write back into original array
    for i in range(start, end + 1):
        _array[i] = result[i - start]
    
# in place merge
def merge_in_place_slow(_array, start, middle, end):
    j = end
    while True:
        # get element of second array where the largest element of first array is bigger
        # stops at least when j == middle
        while _array[j] >= _array[middle] and j > middle:
            j -= 1

        # check if finished
        if j < middle + 1:
            break

        # swap the element of array 1 into array 2
        swap(_array, middle, j)

        # sort first array to make value from array 2 be at the right place
        k = middle
        while (
            _array[k] < _array[k - 1] and k > 0 and k > start
        ):  # k > start so it remains in the part of the array
            swap(_array, k, k - 1)
            k -= 1

# in place sort
def mergesort(_array, start, end):
    # if length of array is 1 or 2, sorting is easy and it can be returned
    if end - start == 0:
        return
    elif end - start == 1:
        if _array[start] > _array[end]:
            swap(_array, start, end)
        return
    else:
        # sort parts of array if the part is of length 3 or longer
        middle = start + (end - start) // 2
        # split in two parts
        mergesort(_array, start, middle)
        mergesort(_array, middle + 1, end)

        # merge these already sorted parts into a sorted
        # part which can be used in the next upper recursion step
        merge_faster_more_space(_array, start, middle, end)
        # merge_in_place_slow(_array, start, middle, end)

        return


# test program
liste = gen(100)
print(liste)
mergesort(liste, 0, len(liste) - 1)
print(liste)
