num = int(input("Enter a number: ")) 
reverse = 0 
temp = num 
while temp > 0: 
    digit = temp % 10 
    reverse = reverse * 10 + digit 
    temp //= 10 
if num == reverse: 
    print(f"{num} is a palindrome number") 
else: 
    print(f"{num} is not a palindrome number")