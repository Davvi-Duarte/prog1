def somatorio(numero):
    b=0
    for i in range(len(numero)):
       b+=int(numero[i])
    return b


def filtra_divisores(lista):
    for i in range(len(lista)-1,-1,-1):
        a=somatorio(str(lista[i]))
        if (lista[i]%a)==0:
            pass
        else:
            lista.pop(i)
    return None
