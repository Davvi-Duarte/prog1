numeros=[]
cont=0
soma=0
while True:
    num=input()
    if num == 'fim':
        break
    else:
        numeros.append(num)
        cont+=1

for i in range(len(numeros)):
    n=int(numeros[i])
    soma += n

media=soma/cont

print(f'{media:.2f}')

for i in range(len(numeros)):
    if int(numeros[i])<media:
        print(f'{i+1} {numeros[i]}')

