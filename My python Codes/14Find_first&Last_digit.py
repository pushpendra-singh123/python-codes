n = int(input("Enter any number:"))
num = n
if(n<=9):
    print("You have only one digit \n so first and last digit both are same.")
else:
    r = n%10
    while(n>=10):
        n = int(n/10)
        if(n<=9):
            print(n)
            break
print(f"your first digit is '{n}' and last digit is '{r}'")