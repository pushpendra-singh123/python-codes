string = input("Enter a string: ") 
shorthands = {"u": "you", "r": "are", "2": "to", "4": "for", "b": "be", "n": "and"} 
for shorthand, full_form in shorthands.items(): 
    string = string.replace(shorthand, full_form) 
    word_freq = {word: string.split().count(word) for word in set(string.split())} 
for word, freq in word_freq.items(): 
    print(f"{word}: {freq}") 