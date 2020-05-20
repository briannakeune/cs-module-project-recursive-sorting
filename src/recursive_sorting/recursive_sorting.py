# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # total amount of elements the sorted merged array will be
    elements = len(arrA) + len(arrB)
    # creating that space for the arrays
    merged_arr = [0] * elements

    index = 0
    # select the minimum of the two values
    # add the lower value to the merged arr
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            merged_arr[index] = arrA[0]
            # removing first index until one of the lists become 0
            del arrA[0]
        else:
            merged_arr[index] = arrB[0]
            del arrB[0]
        index += 1
    # when one list becomes empty,
    # copy all values from the
    # remaining array
    for i in arrA or arrB:
        merged_arr[index] = i
        index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    # splitting the array until sorted,
    # and becomes ready to merge
    middle_index = len(arr) // 2
    half1 = merge_sort(arr[:middle_index])
    half2 = merge_sort(arr[middle_index:])

    return merge(half1, half2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if len(arr) == 0:
        return arr


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
