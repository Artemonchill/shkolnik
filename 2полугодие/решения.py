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
  
  "2-e"
  for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not(y<=x)or(z<=w) or not (z))==False:
                    print(x,y,z,w)

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
        
        
 "16-e"
        import sys
sys.setrecursionlimit (3000)
it1=1
it2=1
for i in range(1,2024):
    it1=it1*i
for i in range(1,2021):
    it2=it2*i
print(it1/it2)


"17-е"
with open('17.txt') as f:
    nums =[int(x) for x in f]
    a=list(map(abs,nums))
    count=0
    sp=[]
    for i in range (len(nums)-1):
        if abs(nums[i])%10==3:
            sp.append(nums[i])
    maxi=max(sp)**2
    sqrt=[]
    for i in range (len(a)-1):
        if ((a[i] % 10==3 and a[i+1] %10!=3) or (a [i]%10!=3 and a[i+1]%10==3)) and (a[i]**2+a[i+1]**2)>=maxi:
            count+=1
            sqrt.append(a[i]**2+a[i+1]**2)
    print(count)
    print(max(sqrt))

       
 "23-е"

from itertools import product
def f(x,y,z):
    count=0
    for i in range(2,z):
        b = product('12', repeat = i)
        print(i)
        for  n in b:
            a=x
            if x==10 and n.count ('2')>1:
                continue
            for l in n:
                if l=='1':
                    a+=1
                else:
                    a*=2
                if a==17:
                    break
            if a==y:
                count+=1
    return count
k=f(10,35,24)
p=f(1,10,10)
print(k*p)



def f(x,y):
    if x>y or x==17:
        return 0
    elif x==y:
        return 1
    return f(x+1,y) + f(x*2,y)
print (f(1,10)*f(10,35))

"24-e"

with open('24.txt') as f:
    s=f.readline().replace('C','S').replace('D','S').replace('F','S')
    s=s.replace('A','G').replace('O','G')
    s=s.replace('SG','*')
    cnt=0
    m=[]
    for i in s:
        if i=='*':
            cnt+=1
        else:
            m.append(cnt)
            cnt=0
print(max(m))

with open('24.txt') as f:
    s=f.readline().replace('AB','1').replace('AC','1')
    s=s.replace('A',' ').replace('B',' ').replace('C', ' ')
    print(max(len(x)) for x in s.split())

"25-e"

for i in range(2023,10**10,2023):
    n=str(i)
    if n [0]=='1' and n[2:6]=='2139' and n[-1]=='4':
        print(i,i//2023)

 for a in range(10):
    for b in range(10):
        x=int(f'12345{a}6{b}8')
        if x % 17 ==0:
            print(x, x//17)       
        
        
"26-e"

with open ('26.txt') as f:
    S=[int(x) for x in f]
    S.pop(0)
    S.sort(reverse=True)
    n,mini=1, S[0]
    for i in range(1,len (S)):
        if S[i] + 3<=mini:
            mini = S[i]
            n+=1
    print(n,mini)
