 a= int(input())
 b= int(input())
 c= int(input())
 if(a<b+c and b<c+a and c<a+b):
     if(c**2==b**2+a**2 or a**2==b**2+c**2 or b**2==c**2+a**2):
         print("прямоугольный")
     elif(c**2>b**2+a**2 or a**2>b**2+c**2 or b**2>c**2+a**2):
         print("тупоугольный")
     else:
         print("остроугольный")
