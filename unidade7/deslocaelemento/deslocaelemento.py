def desloca(lista,origem,destino):
    numero=0
    for i in range(origem, destino):
        if origem<destino:
            numero=lista[origem]
            lista[origem]=lista[origem+1]
            lista[origem+1]=numero
            origem+=1
    return
