row =int(input("Enter range for pyramid: "))
for i in range(row):
    p=""
    for j in range(i+1):
        p=p+" "+str((i+1)*(j+1))
    print(p)