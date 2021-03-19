def longlength(a): 
    m = len(a[0]) 
    temp = a[0] 
    for i in a: 
        if(len(i)>m): 
            m = len(i) 
            temp = i 
    print("The length of longest word in the list: ",m) 
a = ["grapes","apple","burger"] 
longlength(a)