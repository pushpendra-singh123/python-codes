# (a) Using len() function:- 
string = "Hello, world!" 
length = len(string) 
print(length) 

# (b) Using a loop:- 
string = "Hello, world!" 
count = 0 
for char in string: 
    count += 1 
print(count) 

# (c) Using len() with a list comprehension:- 
string = "Hello, world!" 
char_list = [char for char in string] 
length = len(char_list) 
print(length) 

# (d) Using len() function with split() function:-  
string = "Hello, world!" 
word_list = string.split() #it will convert into two element of list then output is 2
length = len(word_list) 
print(length) 