sp=[]
for i in range(2,1000):
    n=0
    for k in range(2, 117+4*i-1):
        if (117 + 4*i)%k==0:
            n=1
            break
    if  n==0:
        sp.append(i)
print(sp)
        
