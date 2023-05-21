n = int(input("Enter the upper limit: ")) 
prime_sum = 0 
for num in range(2, n+1): 
    if num > 1: 
        for i in range(2, num): 
            if num % i == 0: 
                break 
        else: 
            prime_sum += num 
            print(num,end=",")
print(f"\nThe sum of all prime numbers between 1 and {n} is {prime_sum}.") 
