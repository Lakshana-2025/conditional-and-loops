s=input("Enter a string:")
result=""
i=0
while i<len(s):
    letter=s[i]
    number=int(s[i+1])
    result+=letter*number
    i+=2
print(result)
