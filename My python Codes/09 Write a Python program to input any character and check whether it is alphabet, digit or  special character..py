sp = input("Enter any character:")
ac = ord(sp)
print(ac)
if((ac>=97 and ac<=122) or (ac>=65 and ac<=90)):
    print(f"{ac} is alphabate.")
elif(ac>=48 and ac<=57):
    print(f"{sp} is digit.")
else:
    print(f"{sp} is special character.")
