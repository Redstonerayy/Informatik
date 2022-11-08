import random

# set seed so output is comparable
random.seed(10)


def swap(array_, i1, i2):
    temp = array_[i1]
    array_[i1] = array_[i2]
    array_[i2] = temp


# generate random list, which is sorted
def gen(length: int):
    liste = [random.randint(0, 100) for i in range(length)]
    return liste


def mergesort(_array, start, end):
    if end - start == 0:
        return
    elif end - start == 1:
        if _array[start] > _array[end]:
            swap(_array, start, end)
        return
    else:
        # sort parts
        middle = start + (end - start) // 2
        mergesort(_array, start, middle)
        mergesort(_array, middle + 1, end)

        # in place merge
        j = end
        while True:
            # get element where largest of first array is bigger
            while _array[j] >= _array[middle]:
                j -= 1

            # check if finished
            if j < middle + 1:
                break

            swap(_array, middle, j)

            # sort first array
            k = middle
            while (
                _array[k] < _array[k - 1] and k > 0 and k > start
            ):  # k > start so it remains in the part of the array
                swap(_array, k, k - 1)
                k -= 1

        return


liste = gen(15)
print(liste)
print("-----")
mergesort(liste, 0, len(liste) - 1)
print("-----")
print(liste)
