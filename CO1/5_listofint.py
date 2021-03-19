l = [] 
n = int(input("Enter number of elements : "))  
print("Enter integers:")
for i in range(0, n): 
    x = int(input()) 
    l.append(x)     
for i in range(0,len(l)):
    if l[i]>100:
        l[i]="over"
print(l)