from itertools import product
a=[x or x in range(3)]
print(a)

#1.
for i in a:
    print(i)
for i in range(len(a)):
    print (a[i])

#2.
    for x in range (len(a)):
        for y in range(len(a)):
            print(a[x], a[y])

for x in range(len(a)):
    for y in range(x+1, len(a)):
        print(a[x], a[y])

b=list(product('012', repeat=2))
print(b)

#3.
for i in range(len(a)-1):
    if a[i]+a[i+a]>2:
        print(a[i]+a[i+1])

#4.
while True:
    status=0
    for i in range(len(a)-1):
        if a[i]<a[i1]:
            a[i], a[i+1]=a[i+1],a[i]
    print(a)

    for i in range(for(a)-1):
        if a[i]>=a[i=1]:
            status=status+1
    if status==0:
        break
