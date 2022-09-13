
k=int(input())
c=0
s1=0
s2=0
for i in range(k):
    s1=(k - 5 * i)
    s2=(k-3*i)
    if(s1<0):s1=1
    if(s2<0):s2=1
    if(s2%5==0):
        print("YES")
        c=1
        break
    elif(s1%3==0):
        print("YES")
        c=1
        break
if(c==0):print("NO")
