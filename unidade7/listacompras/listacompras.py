def adiciona_item(nome, lista):
    backup=[]
    if len(lista)==0:
        lista.append(nome)
        return
    else:
        for i in range(len(lista)-1, -1, -1):
            if nome<lista[i]:
                if nome<lista[i] and i == 0:
                    backup.append(lista.pop())
                    lista.append(nome)
                else:
                    backup.append(lista.pop())
            
            else:
                lista.append(nome)
                break
    
        if len(backup)==0:
            return
        else:

            for i in range (len(backup)-1, -1, -1):
                lista.append(backup[i])
            return
