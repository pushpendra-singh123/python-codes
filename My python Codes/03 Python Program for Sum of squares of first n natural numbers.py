n = int(input("Enter the value of n: ")) 
m = int(input("Enter the value of m: ")) 
a, b = 0, 1 
fib = 0 
while n > 0: 
    fib = a + b 
    a, b = b, fib 
    if fib % m == 0: 
        n -= 1 
    print(f"The {n+1}-th multiple of {m} in the Fibonacci series is {fib}.") 
