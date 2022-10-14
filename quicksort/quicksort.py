# swap 2 elements of array

def swap(array_, i1, i2):
    array_[i1], array_[i2] = array_[i2], array_[i1]
    return array_

# partition range of the array
def lomuto_partition(array_, start, end):
    # last element as pivot(slow)
    pivot = array_[end]

    # set counter which says where to swap the next element
    i = start - 1

    # iterate through the array
    # place elements smaller than the pivot at
    # the left side at positon i
    # i is incremented each time a swap occurs
    for j in range(start, end):
        if array_[j] < pivot:
            i += 1
            swap(array_, i, j)

    # swap pivot to the position right of the last smaller element
    swap(array_, i + 1, end)

    return i

# recursive function
def quicksort(array_, start, end):
    # start < 0 means that no element was swapped(already sorted)
    # start >= end means that the range is smaller than 2 so no sorting needed
    if (start >= end or start < 0):
        return
    
    # partition
    edge = lomuto_partition(array_, start, end)

    # recursively call the function
    # left side, from start to the positon the last smaller element
    # was swapped to
    quicksort(array_, start, edge)
    # right side, from the element right to the pivot, as the pivot is
    # already in the right place , to the end of the previous range
    quicksort(array_, edge + 2, end)

# sort list
liste = [3, 4, 1, 6, 7, 2, 1, 1, 0, 6]
quicksort(liste, 0, len(liste) - 1)
print(liste)
