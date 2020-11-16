def filtra_lista(num, lista):
    novalista=[]
    for i in range(len(lista)):
        if i == 0 and num>0:
            novalista.append(lista[i])
        elif (i%num)==0:
            novalista.append(lista[i])
    return novalista
