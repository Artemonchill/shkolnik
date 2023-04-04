sp=[20,0,2,2,1,10]
o=[]
l=len(sp)
a=1
for i in range (l-1):
    if sp[i]>=sp[i+1]:
        sp[i],sp[i+1]=sp[i+1],sp[i]
while a==1:
    for i in range (l-1):
        if sp[i]>=sp[i+1]:
            sp[i],sp[i+1]=sp[i+1],sp[i]
    if all (sp[i]<=sp[i+1] for i in range (l-1)):
        a=2
print(sp)
