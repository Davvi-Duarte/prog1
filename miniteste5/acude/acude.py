limite=float(input())
atual=float(input())
if  atual>=limite and atual!=0:
    print('Açude passou a liberar água.')
    print(f'Nível: {atual:.2f}')
else:
    while True:
        operacao=input().split(" ")
        if operacao[0] == 'chuva' or operacao[0]=='afluente':
            atual+=float(operacao[1])            
        if operacao[0]=='demanda' and atual<=0:
            atual=0
        elif operacao[0] == 'demanda':
            demanda=float(operacao[1])
            if atual != 0:
                atual = atual - demanda
        if atual >= limite:
            print('Açude passou a liberar água.')
            print(f'Nível: {atual:.2f}')
            break



