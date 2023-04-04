def llx(sp,l):
    a=Truei
    while a:
        for i in range (l-1):
            if sp[i]>=sp[i+1]:
                sp[i],sp[i+1]=sp[i+1],sp[i]
        if all (sp[i]<=sp[i+1] for i in range (l-1)):
            a=False
    return sp
sp=[49, 48, 35, 23, 14, 18, 50, 70, 80, 82, 85, 86, 92, 94, 96]
l=len(sp)-1
while l>2:
    l=l//2
    if (sp[l]>=sp[l-1]):
        sp=sp[:l]
        print(sp)
    else:
        sp=sp[l:]
        print(sp)
print(min(sp))
