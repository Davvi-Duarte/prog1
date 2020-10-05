congelado=float(input())
descongelado=float(input())

agua=congelado-descongelado

porcentagem=(agua*100)/congelado

if porcentagem<5:
    print(f'{porcentagem:.1f}% do peso do produto é de água congelada.')
    print('Produto qualis A.')

elif porcentagem<10:
    print(f'{porcentagem:.1f}% do peso do produto é de água congelada.')
    print('Produto em conformidade.')

else:
    print(f'{porcentagem:.1f}% do peso do produto é de água congelada.')
    print('Produto não conforme.')


