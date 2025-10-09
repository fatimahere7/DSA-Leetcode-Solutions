nums = [1,2,3,4,5,6,7,8]
try:
    k = int(input("Enter no. of rotations to the left: "))
except ValueError:
    print(" Please enter a valid number!")
    exit()
k = k % len(nums)
rotated_array = nums[k:] + nums[:k]
print(rotated_array)