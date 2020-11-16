def maior_numero(lista):
    a = lista[0]
    for i in range(len(lista)):
        if lista[i] > a:
            a = lista[i]
    return a
def remove_divisores_do_maior(lista):
    maiornumero=maior_numero(lista)
    for i in range(len(lista)-1,-1,-1):
        if (maiornumero%lista[i])==0:
            lista.pop(i)
    return None
    
