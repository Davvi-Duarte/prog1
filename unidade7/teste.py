l1=[1,2,3,4,5]
l2=[6]

def uniao_lista(l1, l2):
    cont=0
    for i in range(len(l2)):
        cont=0
        for j in range(len(l1)):
            if l2[i]==l1[j]:
                cont+=1
        if len(l2)==cont:
            return None 
        elif cont==0:
            l1.append(l2[i])
        cont=0
    print(l1)

uniao_lista(l1,l2)
