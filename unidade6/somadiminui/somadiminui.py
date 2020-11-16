def soma_diminui_vizinhos(lista):
    total=0
    cont=1
    if len(lista)==0:
        return 0
        print(total)
    else:
        for i in range(len(lista)):
            if i==0:
                total+=lista[i]
                cont+=1
            elif cont%2==0:
                total+=lista[i]
                cont+=1
            else:
                total-=lista[i]
                cont+=1
        return total
    
