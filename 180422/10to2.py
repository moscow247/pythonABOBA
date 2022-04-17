while True:
    a = int(input())
    b=""
    while a>0:
        b+=str(a%2)
        a//=2
    b=b[::-1]
    print(b)
