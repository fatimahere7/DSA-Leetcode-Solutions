def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # merge two sorted halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # add leftovers
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Example
arr = [5, 3, 8, 4, 2, 7, 1]
print("MergeSort:", merge_sort(arr))
