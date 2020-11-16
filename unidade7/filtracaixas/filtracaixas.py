def filtra_caixas_indisponiveis(lista, numero):
    for i in range(len(lista)-1,-1,-1):
        if lista[i]<numero:
            lista.pop(i)
    return
