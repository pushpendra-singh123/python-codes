# Q. Write a Python program to check whether a number is Strong number or not (Also 
# known as Robinson number/ Krishnamurthy Number / Peterson number.)

num = int(input("Enter a number: ")) 
sum = 0 
temp = num 
while temp > 0: 
    digit = temp % 10 
    fact = 1 
    for i in range(1, digit+1): 
        fact *= i 
        sum += fact 
        temp //= 10 
if num == sum: 
    print(num, "is a Strong number") 
else: 
    print(num, "is not a Strong number") 