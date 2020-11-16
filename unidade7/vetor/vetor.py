def altera_vetor_por_escalar(lista, fator):
    backup=[]
    for i in range(len(lista)):
        backup.append(lista.pop())
    for j in range(len(backup)-1,-1,-1):
        lista.append(int(backup[j])*int(fator))
    return None
