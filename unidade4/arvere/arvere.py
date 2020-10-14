tamanho=int(input())
arvore=[]
espaco=[]
for i in range(tamanho):
    arvore.append('o' + 2 * i * 'o')

for z in range(len(arvore)):
    espaco.append(' ' * ((len(arvore)-1) - int(z)))

for i in range(len(arvore)):
    print(espaco[i]+arvore[i])

print(espaco[0]+arvore[0])
