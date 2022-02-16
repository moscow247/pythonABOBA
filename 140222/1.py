
a=[[0 for i in range(10)] for j in range(10)]


for i in range(10):
    for j in range(10):
        a[i][j]=25+j*2
print(a)
