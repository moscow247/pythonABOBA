from random import randint

a = int(input())
l=[randint(-10000000000, 100000000000) for i in range(a)]
B = 0
M=0
k=0
m=int(input())
for i in range(len(l)):
    if(l[i]==m):
        k+=1
    elif(l[i] < m):
        M+=1
    elif(l[i] > m):
        B+=1
    print(l[i])
print(str(M) + " " + str(B) + " " +str(k))
