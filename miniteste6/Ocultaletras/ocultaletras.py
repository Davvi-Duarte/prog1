def oculta_letras(palavra, exibir):
    msg=''
    for i in range(len(palavra)):
        cont=0
        a=palavra[i].lower()
        for j in range(len(exibir)):
            b=exibir[j].lower()
            if (b)==(a):
                cont+=1
            else:
                cont+=0
        if cont > 0:
            msg+=palavra[i]
        else:
            msg+="_"
    return msg
