n = 11
endl = "\n"
for i in range(1,n//2+1):
    print("*" * i,end="")
    print(" " * (2*((n//2)-i)+1),end="")
    print("*" * i , end=endl)
print("*" * n, end=endl)
for i in range(n//2 , 0 , -1):
   print("*" * i, end="")
   print(" " * (2*((n//2)-i)+1), end="")
   print("*" * i, end=endl)
      

# def butterfly(n: int):
#     for i in range(1, n + 1):
#         print("*" * i, end="")
#         print(" " * (2 * (n - i)), end="")
#         print("*" * i)

#     for i in range(n - 1, 0, -1):
#         print("*" * i, end="")
#         print(" " * (2 * (n - i)), end="")
#         print("*" * i)


# butterfly(51)

    
    
    
    
    
    
    