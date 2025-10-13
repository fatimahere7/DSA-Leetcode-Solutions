def quicksort(arr):
    if len(arr) <= 1:
        return arr  # base case
    pivot = arr[len(arr) // 2]  # pick the middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# Example
arr = [5, 3, 8, 4, 2, 7, 1]
print("QuickSort:", quicksort(arr))
