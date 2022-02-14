
a=0
sum=0
max=0
b=0
maxb=0
while(True):
    a=int(input())
    b=a
    if(a==0): break
    while(a>0):
        sum+=a%8
        a//=8
    if(sum>max):
        max=sum
        maxb=b
    sum=0
print(maxb)
