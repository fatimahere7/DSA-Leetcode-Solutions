def fibonaci(num):
    a,b = 0 , 1
    for i in range(num):
        print(a, end=" ")
        a,b = b, a+b

def fib_recursive(n):
    if n <=1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)        
       
n = 10
for i in range(n):
    print(fib_recursive(i), end=" ")

