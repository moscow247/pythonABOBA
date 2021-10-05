a = int(input())
k = 0
whoIs = ""
cur = 0
index = 0
count = 1
lOne = [[0] for i in range(a-1)]
lTwo = [[0] for i in range(2*a-2)]
for i in range(len(lOne)):
    lOne[i] = input()
for i in range(len(lOne)):
    lTwo[i+k] = str(lOne[i]).split()[0]
    k += 1
    lTwo[i+k] = str(lOne[i]).split()[1]
for i in range(1, len(lTwo), 2):
    whoIs=lTwo[i]
    for j in range(0, len(lTwo)-1, 2):
        if(whoIs==lTwo[j]):
            cur+=1
    if(cur < 1):
        index=i
        break
    cur=0
print(lTwo[index])

whoIs = lTwo[index]
while(count < a):
    for i in range(1, len(lTwo), 2):
        if(whoIs==lTwo[i]):
            index=i
            count+=1
    print(lTwo[index-1])
    whoIs=lTwo[index-1]
