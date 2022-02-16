from random import randint


a=[[randint(1, 1000) for i in range(10)] for j in range(10)]
# print(a)
min=1001
pr=1

for i in range(10):
    for j in range(10):
        if (a[i][j]<min):
            min=a[i][j]
            pr=i*j
print(pr)
