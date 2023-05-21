# Q. Python program to check whether the string is Symmetrical or Palindrome


# a = input("Enter string:")
# s = a[::-1]
# if s==a:
#     print("Palindrome")
# else:
#     print("Not palindrome")

string = input("Enter a string: ") 
if string == string[::-1]: 
    print("The string is symmetrical") 
else: 
    print("The string is not symmetrical") 
if string.replace(" ", "") == string.replace(" ", "")[::-1]: 
    print("The string is a palindrome") 
else: 
    print("The string is not a palindrome") 
