num=int(input())
numero=[]
maior=[0]
menor=[]
tot=0
repeat=0
media=[]
for i in range(num):
    tot=0
    a=int(input())
    numero.append(a)
    if a>maior[0]:
        maior.pop()
        maior.append(a)
    if not menor==[]:
        if a<menor[0]:
            menor.pop(0)
            menor.append(a)
    else:
        menor.append(a)
    repeat+=1
    for i in range(len(numero)):
        tot += numero[i]
    media=tot/repeat
    if not i+1 == num:
        print(f'Parcial {i + 1}:')
        print(f'menor: {menor[0]}; maior: {maior[0]}; média: {media:.2f}')
        print('====')
    else: break
print('Final:')
print(f'menor: {menor[0]}; maior: {maior[0]}; média: {media:.2f}') 
