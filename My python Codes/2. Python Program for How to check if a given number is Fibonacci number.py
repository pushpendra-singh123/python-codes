n = int(input("Enter the number you want to check: "))
a  = 1; b = 1;c = 0
if(n==0 or n==1):
    print(f"{n} is fibonacci number")
else:
    while(c<n):
        c = a+b
        b = a
        a = c
        if(c==n):
            print(f"{n} is fibonacci number")
            break
        else:
            print(f"{n} is not fibonacci number")
            break
