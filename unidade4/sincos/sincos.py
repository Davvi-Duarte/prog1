import math
grau=float(input())
acresc=float(input())
vezes=int(input())
print('|Angulo|   Seno|Cosseno|')
for i in range(vezes):
    a=math.radians(grau)
    sen=abs(math.sin(a))
    cos=abs(math.cos(a))
    print(f'|{grau:>6,.1f}|{sen:>7,.5f}|{cos:>7,.5f}|')
    grau += acresc
