cont=0
melhores=[]
while True:
    lista=[]
    cadastro=input()
    if cadastro=="---":
        print(cont)
        break
    else:
        hoteis=cadastro.split(',')
        lista.append(hoteis)
        cont+=1
melhor=0
for i in range(len(lista)): 
    melhor=0
    comparação=[]
    comparação.append(lista[i][0])
    if i==0:
        melhor=int(comparacao[i])
    elif int(comparacao[i])<melhor:
        melhor=int(coparacao[i])
melhores.append(melhor)
print(melhores)

        



