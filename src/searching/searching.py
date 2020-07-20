def linear_search(arr, target):
    # Your code here
    for i in range(0, (len(arr))):
        if arr[i] == target:
            return i
        
    return -1 # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    first = 0
    last = len(arr) - 1
    middle = 0

    while first <= last:
        middle = (last - first) // 2

        if arr[middle] == target:
            return middle
        elif target > middle:
            first = middle
        else: 
            last = middle

    return -1  # not found
