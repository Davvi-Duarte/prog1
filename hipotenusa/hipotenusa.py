import math
cateto1=float(input('Medida do Cateto 1? '))
cateto2=float(input('Medida do Cateto 2? '))
quadhipo=(cateto1**2)+(cateto2**2)
hipo=math.sqrt(quadhipo)
print(f'Medida da Hipotenusa: {hipo:.2f}')

