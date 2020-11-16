def ordenacao(lista,i,j):
    aux = lista[j]
    lista[j] = lista[i]
    lista[i] = aux 

def ajeita_lista(lista):

    while True:
        ok = True
        for i in range(len(lista) - 1):
            if lista[i] % 2 != 0:
                if lista[i+1] % 2 == 0:
                    ordenacao(lista, i, i+1)
                    ok = False
            
                elif lista[i+1] < lista[i]:
                    ordenacao(lista, i, i+1)
                    ok = False
            else:

                if lista[i+1]%2 == 0 and lista[i+1] > lista[i]:
                    ordenacao(lista, i, i+1)
                    ok = False

        if ok: break
