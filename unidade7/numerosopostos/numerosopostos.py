def apaga(lista):
    for i in range(len(lista)):
        lista.pop()
    return

def lista_so_com_oposto(lista):
    opostos=[]
    for i in range(len(lista)):
        for j in range(len(lista)-1,-1,-1):
            if (lista[i]+lista[j])==0:
                opostos.append(lista[i])
                break
    apaga(lista)
    for i in range(len(opostos)):
        lista.append(opostos[i])
    return None
