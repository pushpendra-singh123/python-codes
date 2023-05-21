# Q.10 Write a Python program to input marks of five subjects Physics, Chemistry, Biology,
# Mathematics and Computer. Calculate percentage and grade according to
# following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F


sub1=int(input("Enter marks of first subject: "))
sub2=int(input("Enter marks of second subject: "))
sub3=int(input("Enter marks of third subject: "))
sub4=int(input("Enter marks of forth subject: "))
sub5=int(input("Enter marks of 5th subject: ")) 
percentage=(sub1+ sub2+ sub3+ sub4+ sub5)/5 
if(percentage>=90): 
    print("Grade=A") 
elif(percentage>=80): 
    print("Grade=B") 
elif(percentage>=70): 
    print("Grade=C") 
elif(percentage>=60): 
    print("Grade=D") 
elif(percentage>=40): 
    print("Grade=E") 
else: 
    print("Grade=F") 