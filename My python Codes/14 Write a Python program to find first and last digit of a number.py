num = int(input("Enter a number: ")) 
first_digit = num 
while first_digit >= 10: 
    first_digit //= 10 
last_digit = num % 10 
print(f"First digit: {first_digit}") 
print(f"Last digit: {last_digit}") 