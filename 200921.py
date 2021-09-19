a=int(input())
b=int(input())
c=int(input())
if(a+b>c and a+c>b and b+c>a):
    if(max(a,b,c)**2==((a+b+c)-min(a,b,c)-max(a,b,c))**2 + min(a,b,c)**2):
        print("Прямоугольный, остроугольный")
    if(max(a,b,c)**2>((a+b+c)-min(a,b,c) -max(a,b,c))**2 + min(a,b,c)**2):
        if(a==b and b==c and a==c):
            print("Равносторонний")
        else: 
            if (a == b | b == c | a == c):
                print("Равнобедренный")
            else:
                print("просто остроугольный")
    if(max(a,b,c)**2<((a+b+c)-min(a,b,c)-max(a,b,c))**2 + min(a,b,c)**2):
        if(a==b | a==c| b==c):
            print("Равнобедренный")
        else: 
            print("просто тупоугольный")
else:
    print("Треугольника с такими сторонами не существует")
