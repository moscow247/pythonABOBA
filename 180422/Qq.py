a=int(input())
n=[]

for i in range(a):
    n.append(input())
n.sort()
if(len(n)%2==1):
   print(n[len(n)//2+1])
else:
   print((n[len(n)//2]+n[len(n)//2+1])/2)
