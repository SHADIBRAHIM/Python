n= int(input("Enter limit for fibanaucci: "))
n1=0
n2=1
count = 0
if n <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci series:")
   while count<n:
       print(n1)
       temp = n1 + n2
       n1 = n2
       n2 = temp
       count+=1
4