num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: ")) 
if num1 < num2: 
    smaller = num1 
else: 
    smaller = num2 
    hcf = 1 
for i in range(1, smaller+1): 
    if num1 % i == 0 and num2 % i == 0: 
        hcf = i 
print(f"The HCF of {num1} and {num2} is: {hcf}")