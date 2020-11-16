def maior_palavra(frase):
    lista=[]
    msg=''
    for i in range(len(frase)):
        if frase[i] == ' ':
            lista.append(msg)
            msg=''
        elif i==(len(frase)-1):
            msg+=frase[i]
            lista.append(msg)
            msg=''
        else:
            msg+=frase[i]

    maior=lista[0]
    for i in range(len(lista)):
        if len(lista[i]) >= len(maior):
            maior=lista[i]
    return maior
