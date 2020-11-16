valor=0
cont=0
while True:
    num=float(input())
    valor+=num
    cont+=1
    media=valor/cont 
    if num<media:
        cont-=1
        valor-=num
        media=valor/cont
        print(f'Saldo total do FIS: R${valor:.2f}.')
        print(f'Média das contribuições: R${media:.2f}.')
        break
    else:
        pass
