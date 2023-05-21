# #Q15: WAP to calculate sum of digits of a number

# n = input("Enter any number:")
# num =0
# total =0
# l = int(len(n))
# s=n.split()
# while(num <=(l-1)):
#     total += int(s[0][num])
#     num += 1
# print("Sum of digits of a number:",total)

n = input("Enter any number:")
total =0
l = int(len(n))
s=list(n)
for i in range(l):
    total += int(s[i])
print("Sum of digits of a number:",total)


