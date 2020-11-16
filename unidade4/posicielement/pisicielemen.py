num=int(input())
seq=input().split()
indices=[]
saida=''
for i in range(len(seq)):
    if (int(seq[i])==num):
        indices.append(i)

for i in range(len(indices)):
    if i < (len(indices)-1):
        saida+=str(indices[i])
        saida+=' '
    elif i == (len(indices)-1):
        saida+=str(indices[i])

if saida=='':
    print('-1')
else:
    print(saida)


