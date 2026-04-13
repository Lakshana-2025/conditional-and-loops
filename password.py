password=input("Enter Password:")
digit=0
lower=0
upper=0
special=0
space=0
if len(password)<8 or len(password)>15:
    print("Invalid Password")
else:
    for ch in password:
        if ch>='0' and ch<='9':
            digit+=1
        elif ch>='A' and ch<='Z':
            upper+=1
        elif ch>='a' and ch<='z':
            lower+=1
        elif ch==' ':
            space+=1
        else:
            special+=1
    if digit>=1 and lower>=1 and upper>=1 and special>=1 and space==0:
        print("Password is Valid")
    else:
        print("Password is Invalid")
