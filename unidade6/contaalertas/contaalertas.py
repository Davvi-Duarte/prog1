def conta_alertas_acude(lista):
    cont=0
    for i in range(len(lista)):
        if lista[i]<17:
            if i== 0:
                if abs(lista[i]-17)<10:
                    cont+=1
            else:
                if abs(lista[i]-lista[i-1])<10:
                    cont+=1
    return cont
