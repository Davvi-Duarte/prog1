def conta_palavras(num, palavras):
    lista=palavras.split(":")
    cont=0
    for i in range(len(lista)):
        if len(lista[i]) >= num:
            cont+=1
    return cont


