input_string = input("Enter a string: ") 
vowels = set('aeiou') 
if vowels.issubset(set(input_string.lower())): 
    print("String contains all vowels.") 
else: 
    print("String does not contain all vowels.") 