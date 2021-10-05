
a = int(input())
print(a*0.08 if (a*0.08 <= 100 and a*0.05 < a*0.08) else a*0.05 if (a*0.05 > 100) else 100)
