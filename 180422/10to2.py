while True:
    a = int(input())
    b=""
    while a>0:
        b+=str(a%2)
        a//=2
    z=""
    for i in range(len(b)):
        z+=b[(len(b)-1)-i]
    print(z)
