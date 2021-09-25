xi = int(input("Введите число: "))
xs = str(xi)
sum=0
k=0
reverse=""
xiMax=int(xs[0])


for i in xs:
    sum += int(i)
    if(int(i) > xiMax):
        xiMax = int(i)
while (xi>0):
    if(xi%16==13):
        k+=1
    xi//=16
reverse=xs[::-1]
print(sum, xiMax, k, reverse, int(xs[0])+int(xs[len(xs)-1]))
