
al = input("Enter any alphabate:")
ac = al.lower()
if(len(al)<2):
    if(ac >="a" and ac <="z"):
    # print(ac)
        if(ac=="a" or ac=="e" or ac=="i" or ac=="o" or ac=="u"):
            print(f"{al} is vowel")
        else:
            print(f"{al} is consonant")
    else:
        print("Incorrect input")
else:
    print("Incorrect input")