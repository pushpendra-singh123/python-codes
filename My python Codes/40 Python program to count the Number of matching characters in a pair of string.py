string1 = input("Enter the first string: ") 
string2 = input("Enter the second string: ") 
matching_chars = 0 
for char1 in string1: 
    for char2 in string2: 
        if char1 == char2: 
            matching_chars += 1 
print(f"Number of matching characters: {matching_chars}") 