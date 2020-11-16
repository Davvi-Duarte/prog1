def merge_invertido(l1, l2):
    a=0
    b=0
    soma=len(l1)+len(l2)
    saida=[]
    clone1=[]
    clone2=[]
    
    for i in range(len(l1)-1, -1, -1):
        clone1.append(l1[i])
    
    for i in range(len(l2)-1,-1,-1):
        clone2.append(l2[i])
    
    for i in range(soma):
        if b==len(l2):
            saida.append(clone1[a])
            a+=1
        elif a==len(l1):
            saida.append(clone2[b])
            b+=1
        elif clone1[a] >= clone2[b]:
            saida.append(clone1[a])
            a+=1
        elif clone1[a] <= clone2[b]:
            saida.append(clone2[b])
            b+=1
    return saida
        

