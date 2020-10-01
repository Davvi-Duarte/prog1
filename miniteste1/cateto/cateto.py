import math
hipotenusa=float(input('hipotenusa? '))
cateto=float(input('cateto? '))

calculo=math.sqrt((hipotenusa+cateto)*(hipotenusa-cateto))

print(f'hipotenusa: {hipotenusa:.2f}')
print(f'cateto 1: {cateto:.2f}')
print(f'cateto 2: {calculo:.2f}')
