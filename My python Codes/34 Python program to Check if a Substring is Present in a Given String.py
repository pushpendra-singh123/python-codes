string = input("Enter a string: ") 
substring = input("Enter a substring: ") 
if substring in string: 
    print(f"{substring} is present in {string}.") 
else: 
    print(f"{substring} is not present in {string}.")