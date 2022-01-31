a = int(input())
u=1
sum=0
for i in range(1,a+1):
    u*=i
    sum+=1/u
print(sum)
