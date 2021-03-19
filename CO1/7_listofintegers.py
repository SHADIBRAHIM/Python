l1=[2,3,1,4,10]
l2=[4,3,1,2,10]
if len(l1)==len(l2):
    print("Same length")
else:
    print("Not same length")
if sum(l1)==sum(l2):
    print("Same sum value")
else:
    print("Not same sum value")
check=any(item in l1 for item in l2)
if check is True:
    print("Common value present")
    
else:
    print("Common value not present")