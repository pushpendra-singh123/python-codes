n = int(input("Enter a number: ")) 
a, b = 0, 1 
for i in range(n): 
    a, b = b, a + b 
print(f"The {n}-th Fibonacci number is {a}.") 