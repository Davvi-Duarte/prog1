def verifica_esteira(l1,l2):
    indices = []
    for i in range(len(l2)):
        for j in range(len(l1)):
            if l2[i] == l1[j]:
                indices.append(j)
                break
    if len(l2) != len(indices):
        Verifica = False
    else:
        Verifica = True
    for i in range(len(indices)-1):
        if (indices[i + 1] - indices[i]) < 0:
            Verifica = False
            break

    return Verifica
