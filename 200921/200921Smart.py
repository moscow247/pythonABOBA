a=float(input())
b=float(input())
c=float(input())

sumCc=0
mainCc=0

#

if(a+b>c and a+c>b and b+c>a):
    sumCc=((a+b+c)-max(a,b,c)-min(a,b,c))**2 + min(a,b,c)**2
    mainCc=max(a,b,c)**2
    if(mainCc==sumCc):
        print("Прямоугольный => остроугольный")
    if(mainCc>sumCc):
        print("Равносторонний => остроугольный" if a==b and b==c and a==c else ("Равнобедренный, остроугольный" if a==b or b==c or a==c else "просто остроугольный"))
    if(mainCc<sumCc):
        print("Равнобедренный, тупоугольный" if a==b or a==c or b==c else "просто тупоугольный")
else:
    print("Треугольника с такими сторонами не существует, надо лучше подбирать числа :(")
