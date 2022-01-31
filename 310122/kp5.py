max=0
sum=0
while True:
    a = int(input())
    if(a==0): break
    for i in str(format(a, 'o')):
        sum+=int(i)
    if(max<sum): max=sum
    sum=0
print(max)
