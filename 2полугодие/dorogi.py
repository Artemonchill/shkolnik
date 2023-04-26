from itertools import product
tab=[[0,712,673,1075,875,1622,423],
     [712,0,1385,1800,1577,2348,1128],
     [673,1385,0,1499,239,2046,244],
     [1075,1800,1499,0,1287,551,1266],
     [875,1577,239,1287,0,1835,442],
     [1622,2348,2046,551,1835,0,1813],
     [423,1128,244,1266,442,1813,0]]
alf='0123456'
a=product(alf, repeat=7)
maxi=0
p=0
for i in a:
     if all(i.count(x)==1 for x in alf):
          s=0
          for l in range(len(i)-1):
               s+=tab[int(i[l])][int(i[l+1])]
          if s>=maxi:
               maxi=s
               p=i
print(maxi,' '.join(p))
          
