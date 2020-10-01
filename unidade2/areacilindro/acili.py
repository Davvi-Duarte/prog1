from math import pi
print('Cálculo da Superfície de um Cilindro')
print('---')
diametro=float(input('Medida do diâmetro? '))
altura=float(input('Medida da altura? '))

raio= diametro/2
area= (2*(pi*raio**2))+(2*(pi*raio*altura))

print('---')
print(f'Área calculada: {area:.2f}')
