a=[[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9]]
max=a[0][0]
min=a[0][0]
sum=0
mm=0

#########

for i in range(len(a)):
    for j in range(len(a[i])):
        if(a[i][j] > max): max=a[i][j]
        if(a[i][j] < min): min=a[i][j]
        if((i+1)%2==0): sum+=a[i][j]
print(max, min, sum, max-min)
