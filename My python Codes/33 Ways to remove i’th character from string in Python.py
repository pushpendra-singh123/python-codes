# (a) Using slicing:- 
string = input("Enter a string: ") 
i = int(input("Enter the index of the character to remove: ")) 
new_string = string[:i] + string[i+1:] 
print("The new string with the i'th character removed is:", new_string) 

# (b) Using String concatination:- 
string = input("Enter a string: ") 
i = int(input("Enter the index of the character to remove:")) 
new_string = "" 
for j in range(len(string)): 
    if j != i: 
        new_string += string[j] 
print("The new string with the i'th character removed is:", new_string) 


#  (c) Using list comprehenion and join:- 
string = input("Enter a string: ") 
i = int(input("Enter the index of the character to remove: ")) 
new_string = "".join([string[j] for j in range(len(string)) if j != i]) 
print("The new string with the i'th character removed is:", new_string) 
