def remove_menores(numero, lista):
    ficam=[]
    eliminados=[]
    if len(lista)==0:
        return 0
    else:
        for i in range(len(lista)-1, -1, -1):
            if lista[i]<numero:
                eliminados.append(lista.pop())
            else:
                ficam.append(lista.pop())
        if ficam == 0:
            return len(eliminados)
        else:
            for i in range(len(ficam)-1,-1,-1):
                lista.append(ficam[i])
            return len(eliminados)
