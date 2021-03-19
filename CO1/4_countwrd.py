s=input("Enter a sentence: ")
word=input("Enter word to be counted: ")
a=[]
count=0
a=s.split(" ")
for i in range(0,len(a)):
    if (word==a[i]):
        count=count+1
print("Count:",count)
