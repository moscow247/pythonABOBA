from random import randint


a=[[randint(1, 1000) for i in range(10)] for j in range(10)]
print(a)
max=0
sum=0
b=0
pr=0

for i in range(10):
    for j in range(10):
        b=a[i][j]
        while(b>0):
            sum+=b%10
            b//=10
        if(max<sum):
            max=sum
            pr=i
        sum=0
print(pr)
