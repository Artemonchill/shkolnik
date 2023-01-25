def f5():
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')
  print(f'| {N} |  |')

  "5-е" 
  
  for i in range(1,100):
    chislo=''
    num=(bin(i)[2:])
    if num.count('1')%2==0:
        chislo=num +'100'

    if num.count('1')%2!=0:
        chislo=num +'001'
    if int(chislo,2)>160:
        print (i)
        break
               
for i in range(1,100):
    chislo=''
    num=(bin(i)[2:])
    if num.count('1')%2==0:
        chislo=num +'100'

    if num.count('1')%2!=0:
        chislo=num +'001'
    if int(chislo,2)>160:
        print (i)
        break

          
"6-е"
        
  count=0
for a in range (1,8):
    for b in range (8):
        for c in range (8):
            for d in range (8):
                for e in range (8):
                    s=str(a)+str(b)+str(c)+str(d)+str(e)
                    if s.count('6')==1 and s.index('6')==len(s)-1 and int(s[len(s)-2])%2==0:
                        count+=1
                    if s.count('6')==1 and s.index('6')==0 and int(s[1])%2==0:
                        count+=1
                    if s.count('6')==1 and s.index('6')<len(s)-1 and s.index('6')>0 and int(s[s.index('6')-1])%2==0 and int(s[s.index('6')+1])%2==0:
                        count+=1
print(count)

from turtle import *
left(90)
for i in range(1):
    forward(150)
    right(90)
    forward(150)
    goto(0,0)
pu()
for x in range(0,16):
    for y in range(0,16):
        goto(x*10,y*10)
        dot(4)
done()

from itertools import product
nums=product('01234567',repeat=5)
k=0
n='16 36 56 76 61 63 65 67'
nn=n.split()
for n in nums:
    numb=''.join(n)
    sp=[]
    if numb.count('6')==1 and numb[0]!='0':
        for x in nn:
            if x in numb:
                sp.append(x)
        if not sp: 
            k+=1
print(k)


"12-e"

sp=[]
for num in range(2,1000):
    if all(num % delit !=0 for delit in range(2,num-1)):
        sp.append(num)
flag=False
for i in sp:
    for y in range (100):
        if y*4+117==i and flag==False:
            print(y, i)
            flag=True

            
"15-e"

for A in range(1,1000):
    if all(((x%2==0)<=(x%3!=0))or(x+A>=100) for x in range (1,100)):
        print(A)
        break
