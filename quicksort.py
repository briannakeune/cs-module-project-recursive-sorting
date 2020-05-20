# Divide an conquer -- sounds a bit like binary search.

'''
[5, 9, 7, 7, 2, 8, 1, 6]

1. Find a pivot
    - use the midpoint
    - pick the first/last element
2. Partition all the data around the pivot
=> [3, 2, 1] [5] [9, 7, 8,6]
=> [2, 1] [3] [5][7, 8, 6] [9]
=> [1][2][3][5][6][7, 8][9]
=> [1][2][3][5][6][7][8][9]
=> [1, 2, 3, 5, 6, 7, 8, 9]

runtime: O(n log n) / best possible runtime for general purpose sorting algos
'''

# recursive algo
# when writing a recurisive algo/implementation
# 1. what's our base (terminating) case
# 2. if we aren't in the base case,
#    how are we moving towards the base case


# this current set up takes a lot of memory
def partition(data):
    # pick the first element in data as our pivot
    pivot = data[0]
    left = []
    right = []

    # skipping over first element, because that's already sorted in pivot
    for x in data[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return left, pivot, right


def quicksort(data):
    # base case
    if len(data) is 0:
        return data

    # partition handles picking the pivot element
    # and partitioning the data around the pivot
    # left is the left sub-list
    # right is the right sub-list
    left, pivot, right = partition(data)

    # recursion continues until left/right are sorted to then + all sorted arrays.
    return quicksort(left) + [pivot] + quicksort(right)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def optimized_partition(data, start, end):
    # pick the first element in data as our pivot
    pivot = data[start]

    i = start + 1
    j = start + 1

    # partitioning step to move elements around the pivot
    while j <= end:
        if data[j] <= pivot:
            data[j], data[i] = data[i], data[j]
            i += 1
        j += 1

    data[start], data[i - 1] = data[i - 1], data[start]

    # return the index of the pivot
    return i - 1

# more memory effienct by reusing the data type, and manipulating that.


def quicksort_optimized(data, start=0, end=None):
    if end is None:
        end = len(data) - 1
    if len(data) == 0:
        return data

    # returns the index of the pivot
    index = optimized_partition(data, start, end)

    # qs call for everything to the left of the pivot
    quicksort_optimized(data, start, index - 1)
    # qs call for everything to the right of the pivot
    quicksort_optimized(data, index + 1, end)
