pivot=int(input())
maiores=[]
menores=[]
while True:
    numeros=int(input())
    if numeros>=0:
        if numeros<=pivot:
            menores.append(numeros)
        elif numeros>pivot:
            maiores.append(numeros)
    else:
        break
print(menores)
print(pivot)
print(maiores)
