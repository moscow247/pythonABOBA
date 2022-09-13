k=int(input())
flower=["G", "C", "V"]
c=""
for i in range(k):
    c=flower[1]
    flower[1]=flower[2]
    flower[2]=c
    c=flower[1]
    flower[1]=flower[0]
    flower[0]=c
for i in flower:
    print(i, end="")
    
