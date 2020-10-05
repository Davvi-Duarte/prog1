opcao=int(input())
if opcao==1:
    metrocub=int(input())
    calculo=metrocub*80
    if calculo>=200:
        print(f'R$ {calculo},00')
        print('Brinde!')
    else:
        print(f'R$ {calculo},00')
elif opcao==2:
    metrocub=int(input())
    calculo=metrocub*50
    if calculo>=200:
        print(f'R$ {calculo},00')
        print('Brinde!')
    else:
        print(f'R$ {calculo},00')

elif opcao==3:
    print('R$ 50,00')

