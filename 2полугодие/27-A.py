with open ('27_A.txt') as f:
    n = [x for x in f]
    n.pop(0)
    sp=[ ]
    for i in n:
        sp.append(list(map(int, i.split())))
k=[ ]
for i in range(len(sp)):
    if sp[i][1] % 36==0:
        k.append(sp[i][1]//36)
    else: k.append((sp[i][1]//36)+1)
ind=[ ]
for i in range(len(sp)):
    ind.append(sp[i][0])
sp=list(zip(ind,k))
costs=[]
for i in sp:
     pos=i[0]
     cost=0
     for x in sp:
          cost=cost +abs(pos-x[0])*x[1]
     costs.append(cost)
print(min(costs))
