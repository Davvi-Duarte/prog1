numero=int(input())
num=[]
menorext=0
menor=0
maior=0
for i in range(numero):
    val=int(input())
    num.append(val)


if int(num[0]) < int(num[len(num)-1]):
    menorext += int(num[0])
elif int(num[0])==int(num[len(num)-1]):
    menorext += int(num[0])
else: 
    menorext += int(num[len(num)-1])

for i in range(len(num)):
    if menorext < num[i]:
        maior+=1
    elif menorext > num[i]:
        menor+=1
print(f'Menor dos extremos: {menorext}')
print(f'{menor} número(s) abaixo do menor')
print(f'{maior} número(s) acima do menor')


