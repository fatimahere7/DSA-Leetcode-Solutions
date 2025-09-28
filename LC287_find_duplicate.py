

# O(1) space complexity floyed's slow fast pointer approach where we assme array as linkedlist
def find_duplicate(arr):
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow


# O(n), space complexity O(n)
# map = {}
# for i in range(len(arr)):
#     if arr[i] in map:
#         print(arr[i])
#     map[arr[i]]= True

arr = [3, 1, 2, 4, 2]
print(find_duplicate(arr))



