snake_str = "hello_world" 
components = snake_str.split('_') 
pascal_case = ''.join(x.title() for x in components) 
print(pascal_case) 