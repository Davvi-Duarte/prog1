def insere_na_fila(lista,n,h):
    tupla=(n, h)
    ind=0
    a=len(lista)
    if a==0:
        lista.append(tupla)
    else:
        for i in range(a-1,-1,-1):
            if lista[i][1]<h:
                if i==a-1:
                    ind=a
                else:
                    ind=i+1
                    if lista[ind][1]==h:
                        ind+=1
                break
        if (not h=='') or (not ind!=a):
            lista.append(tupla)
            while lista[ind][1]!=h:
                lista.append(lista.pop(ind))
    return

