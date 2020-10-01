capacidade=float(input('Capacidade de revestimento? '))
print("")
print('== Dados do vão a revestir ==')
comprimento=float(input('Comprimento? '))
largura=float(input('Largura? '))
altura=float(input('Altura? '))

calc1= comprimento*largura
calc2= (comprimento*altura)*4
total= calc1+calc2
print("")
print('== Resultados ==')

print(f'Área total a revestir: {total:.1f} m2')
print(f'Número de caixas: {total/capacidade:.0f}')
