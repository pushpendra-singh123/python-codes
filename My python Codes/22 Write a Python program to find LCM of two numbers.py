num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: ")) 
if num1 > num2: 
    greater = num1 
else: 
    greater = num2 
    lcm = greater 
while True: 
    if lcm % num1 == 0 and lcm % num2 == 0: 
        break 
    lcm += greater 
print(f"The LCM of {num1} and {num2} is: {lcm}") 