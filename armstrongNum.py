# A number is Armstrong if the sum of its digits raised to the power of the number 
# of digits equals the number itself.
# Example: 153 → 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✅
# 370 → 3³ + 7³ + 0³ = 370 ✅


# Input number
num = int(input("Enter a number: "))

# Convert number to string to count digits
order = len(str(num))

# Calculate the sum of the powers of digits
sum = 0
temp = num

while temp > 0:
    digit = temp%10
    sum += digit ** order
    temp //=10

# Check if Armstrong
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
