str1=input("enter a string: ")
l=len(str1)
if l>2:
    if str1[-3:] == "ing":
        str1+="ly"
    else:
        str1+="ing"
print(str1)