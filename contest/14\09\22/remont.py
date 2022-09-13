a=input().split(" ")
l=int(a[0])
w=int(a[1])
h=int(a[2])
if((2*l*h+2*w*h)%16 >0):
    print((2*l*h+2*w*h)//16 +1)
else:
    print((2*l*h+2*w*h)//16)
