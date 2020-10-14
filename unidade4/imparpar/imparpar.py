n=int(input())
par=0
impar=0
spar=0
simpar=0
for i in range(n):
    numeros=int(input())
    if (numeros%2) == 0:
        par+=1
        spar+=numeros
    elif (numeros%2) != 0:
        impar+=1
        simpar+=numeros
print(f'pares: {par}')
print(f'ímpares: {impar}')
print(f'média pares: {(spar/par):.1f}')
print(f'média ímpares: {(simpar/impar):.1f}')
