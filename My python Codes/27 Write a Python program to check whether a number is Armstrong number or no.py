n=int(input("Enter a number:")) 
s=n 
b=len(str(n)) 
sum=0 
while(n>0): 
    r=n%10 
    sum=sum+(r**b) 
    n=n//10 
if s==sum: 
    print(f"The given number {s} is a armstrong number") 
else: 
    print(f"The given number {s} is not a armstrong number") 