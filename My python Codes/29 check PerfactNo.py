num = int(input("Enter a number: ")) 
sum = 0 
for i in range(1, num//2 + 1): 
    if num % i == 0: 
        sum += i 
if num == sum: 
    print(num, "is a Perfect number") 
else: 
    print(num, "is not a Perfect number") 