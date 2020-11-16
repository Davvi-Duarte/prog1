lista=[]
cont=0
somador=0
while True:
    temp=input()
    if float(temp) > 9.9 and float(temp)<30.1:
        lista.append(temp)
        cont+=1
        somador+=float(temp)
    else:
        print(f'Temperatura inadequada! {float(temp):.2f}.')
        break
media=somador/cont

print(f'{cont} medições lidas dentro do padrão.')
print(f'Média = {media:.2f}.')
