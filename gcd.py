# Find GCD of two numbers using Euclidean Algorithm

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b   # keep replacing until b becomes 0

print("GCD is:", a)
