seq=input().split()
fator=int(input())
result=[]
pares=0
for i in range(len(seq)-1):
    if ((int(seq[i])*fator) == int(seq[i+1])) or ((int(seq[i+1])*fator) == int(seq[i])):
        pares+=1
        result.append(f'{seq[i]} {seq[i+1]}')
print(f'{pares} par(es)')
for i in range(len(result)):
    print(result[i])



