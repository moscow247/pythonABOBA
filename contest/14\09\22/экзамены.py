a=input().split(" ")
x=int(a[0])
m=int(a[1])
f=int(a[2])
n=int(a[3])
two=0
oneM=0
oneF=0

#

x-=n
if(m>f):
    if(x-m<0):
        two=abs(x-m)
    else:
        two=abs(x-m-f)
    oneM = m - two
    oneF = f - two
elif(m<f):
    if(x-f<0):
        two=abs(x-f)
    else:
        two=abs(x-m-f)
    oneM = m - two
    oneF = f - two
elif(m==f):
    if(m==x):
        two=m
    elif(m!=x and x!=0):
        oneF=f
        oneM=m
print(two, oneM, oneF)
