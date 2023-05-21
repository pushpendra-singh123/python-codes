n = input("Enter any number:")
# print(len(n))
l = int(len(n))
s=n.split()
# print(s)
print("number is:",n)
if(s[0][0] == s[0][l-1]):
    print(" Both the first and last digit are same.",s[0][0])
else:
    print("First digit of is :",s[0][0])
    print("and last digit of is:",s[0][l-1])
