# Q.11 Write a Python program to input basic salary of an employee and calculate its Gross
# salary according to following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%

basic_salary=int(input("Enter your basic salary: ")) 

if(basic_salary<=10000): 
    hra=basic_salary*0.2 
    Da=basic_salary*0.8 
elif(basic_salary<=20000): 
    hra=basic_salary*0.25 
    Da=basic_salary*0.9 
else: 
    hra=basic_salary*0.3 
    Da=basic_salary*0.95 
gross_salary=basic_salary+hra+Da 
print("Your gross salary is", gross_salary) 