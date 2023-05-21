#Q15: WAP to calculate product of digits of a number

# n = input("Enter any number:")
# num =0
# prod=1
# l = int(len(n))
# s=n.split()
# while(num <=(l-1)):
#     prod *= int(s[0][num])
#     num += 1
# print("Product of digits of a number:",prod)


n = input("Enter any number:")
product =1
l = int(len(n))
s=list(n)
for i in range(l):
    product *= int(s[i])
print("Product of digits of a number:",product)

