b = input()+" "
a=[]
t=""
for i in range(len(b)):
    if(b[i] != " "):
        t+=b[i]
    else:
        a.append(t)
        t=""
count=0
for i in range(len(a)):
    if(int(a[i]) < int(a[(i + 1) % len(a)]) + int(a[(i + 2) % len(a)]) and
            int(a[(i + 1) % len(a)]) < int(a[i]) + int(a[(i + 2) % len(a)]) and
            int(a[(i + 2) % len(a)]) < int(a[i]) + int(a[(i + 1) % len(a)])):
        if (int(a[i]) < int(a[(i + 3) % len(a)]) + int(a[(i + 4) % len(a)]) and
                int(a[(i + 3) % len(a)]) < int(a[i]) + int(a[(i + 4) % len(a)]) and
                int(a[(i + 4) % len(a)]) < int(a[i]) + int(a[(i + 3) % len(a)])):
            print(a[i])
            print(a[(i+3) % len(a)], a[(i+4) % len(a)])
            print(a[(i+1) % len(a)], a[(i+2) % len(a)])
            count = 1
            break
if(count == 0):
    print(0)

    
