l = [] 
n = int(input("Enter number of elements : "))  
for i in range(0, n): 
    c =input("Enter color: ")
    l.append(c)
print("first color: ",l[0])
print("Last color: ",l[n-1])
