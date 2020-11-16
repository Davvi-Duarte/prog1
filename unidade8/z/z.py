def z_inicial(lista):
    cont=0
    if len(lista) == 0:
        return 
    else:
        for i in range(len(lista)):
            if lista[i][0] == "z" or lista[i][0] == "Z":
                cont+=1
        return cont

lista=input().split()
print(z_inicial(lista))

