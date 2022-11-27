# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

    # the last element is the pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1

# function to perform quicksort
def quickSort(array, low, high):
    if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSort(array, pi + 1, high)


data = [2,5,0,9,1,3,4,7]
print('Unsorted Array:')
print(data)

quickSort(data, 0, len(data) - 1)

print('\nSorted Array in Ascending Order:')
print(data)