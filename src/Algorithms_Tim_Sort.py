'''A program that implements the Tim Sort algorithm. It compares it to 
merge sort and performs a few different test cases on it. The time complexity
will also be noted when comparing.'''

import random
import time

# Use this to change the minimum merge length that is allowed. Should be between 32 and 64 to have
# the best results.
MIN_MERGE = 32

# Calculates the time it takes to run a given function.


def calculateTime(function: object, *args, **kwargs) -> None:
    startTime = time.perf_counter()
    output = function(*args, **kwargs)
    finalTime = time.perf_counter()
    print(f'The time was {finalTime - startTime} for {function.__name__}')
    return output

# The runs in the tim sort are the sub arrays.
# This trys to ensure that the len of sub arrays
# are all around the same size. This allows for better runtime.


def calcMinRun(n):
    r = 0
    # This makes sure that the size of each run is optimal.
    while n >= MIN_MERGE:
        r |= n & 1  # The bitwise or operator.
        n >>= 1
    return n + r


# Sorts a given array using insertion sort.
# Each of these the arrays it will work on will not be greater the
# run length that was calculated. This is to ensure the algorithm
# runs as efficient as possible.
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# A helper merge function that merges each of the arrays.
def merge_tim_sort(arr, l, m, r):
    # Gives the proper length to left and right arrays.
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    # This simply merges the sub arrays back together.
    # This can be handled better to check the final value in one array
    # and compare it to the starting value in the other. This could save
    # any comparison and just allow for the new merged array to sorted instantly.
    left_spot, right_spot, merged_spot = 0, 0, l
    while left_spot < len1 and right_spot < len2:
        if left[left_spot] <= right[right_spot]:
            arr[merged_spot] = left[left_spot]
            left_spot += 1

        else:
            arr[merged_spot] = right[right_spot]
            right_spot += 1

        merged_spot += 1

    # Adds any remaining elements to the merged array.
    while left_spot < len1:
        arr[merged_spot] = left[left_spot]
        merged_spot += 1
        left_spot += 1

    while right_spot < len2:
        arr[merged_spot] = right[right_spot]
        merged_spot += 1
        right_spot += 1


# The main Tim Sort algorithm. Takes an array and sorts that same array.
# There are more optimal ways to check if each sub array is reversed
# and to simply reverse them. This would further help the time complexity of this
# algorithm.
def timSort(arr):
    array_length = len(arr)
    # This number should be optimal to give fast algorithm results.
    # By optimal it means runs of similar length.
    min_Run = calcMinRun(array_length)

    # Sorts each sub array.
    for start in range(0, array_length, min_Run):
        end = min(start + min_Run - 1, array_length - 1)
        # This is the optimal size of an array to use this sorting method.
        # Anything larger would not be efficient.
        insertionSort(arr, start, end)

    # Will merge all the sub arrays together. Each array will get larger,
    # and will merge together arrays of similar size. This allows the merge
    # to be as efficient as possible.
    size = min_Run
    while size < array_length:

        # Start at the left of a sub array and find the next
        # sub array. Merge them together and find the next position
        # to start.
        for left in range(0, array_length, 2 * size):
            # Gets index of each sub array.
            mid = min(array_length - 1, left + size - 1)
            right = min((left + 2 * size - 1), (array_length - 1))
            # This is to check and make sure the array is at a proper length to merge.
            if mid < right:
                merge_tim_sort(arr, left, mid, right)

        # This is the new size of the merge array. This will allow it to keep
        # track of where it needs to merge.
        size = 2 * size

# This takes a list as input and sorts it. Uses
# a helper function to allow it to work correctly.


def mergeSort(inputList):
    # This means the list is sorted since it has only 1 element.
    if len(inputList) < 2:
        return inputList
    else:
        # This creates 2 new lists and returns them to the same function while
        # calling the helper to merge them together.
        mid = int(len(inputList) / 2)
        tempList1 = inputList[:mid]
        tempList2 = inputList[mid:]
        # Returns the sorted list.
        return mergeSortHelper(mergeSort(tempList1), mergeSort(tempList2))


# This is the helper function for merge sort. It takes 2
# lists and returns a sorted combination of them.
def mergeSortHelper(inputList1, inputList2):
    tempList = []
    # This makes sure they are not empty
    # and continues to add elements to the new list.
    while ((inputList1 != []) and (inputList2 != [])):
        if inputList1[0] <= inputList2[0]:
            tempList.append(inputList1[0])
            del inputList1[0]
        else:
            tempList.append(inputList2[0])
            del inputList2[0]
    if inputList1 != []:
        for i in range(len(inputList1)):
            tempList.append(inputList1[i])
        del inputList1
    if inputList2 != []:
        for i in range(len(inputList2)):
            tempList.append(inputList2[i])
        del inputList2
    # This returns the new sorted list.
    return tempList

# Generate a list of with the specified number of random integers.


def generate_list(amount):
    temp_list = [random.randint(0, 1000000) for x in range(amount)]
    return temp_list


if __name__ == "__main__":
    listTest1000T = generate_list(1000)
    listTest1000M = listTest1000T.copy()
    print("Input size of 1000 \n")
    list1 = calculateTime(mergeSort, listTest1000M)
    calculateTime(timSort, listTest1000T)
    print('\n')

    listTest10000T = generate_list(10000)
    listTest10000M = listTest1000T.copy()
    print("Input size of 10000 \n")
    list1 = calculateTime(mergeSort, listTest10000M)
    calculateTime(timSort, listTest10000T)
    print('\n')

    listTest50000T = generate_list(50000)
    listTest50000M = listTest50000T.copy()
    print("Input size of 50000 \n")
    list1 = calculateTime(mergeSort, listTest50000M)
    calculateTime(timSort, listTest50000T)
    print('\n')

    listTest100000T = generate_list(100000)
    listTest100000M = listTest100000T.copy()
    print("Input size of 100000 \n")
    list1 = calculateTime(mergeSort, listTest100000M)
    calculateTime(timSort, listTest100000T)
    print('\n')

    listTest500000T = generate_list(500000)
    listTest500000M = listTest500000T.copy()
    print("Input size of 500000 \n")
    list1 = calculateTime(mergeSort, listTest500000M)
    calculateTime(timSort, listTest500000T)
    print('\n')
