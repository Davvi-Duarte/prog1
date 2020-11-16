listanome=[]
listasomas=[]
controller1=""
controller2=""
somador=0
while controller1 != "**":
    nome=input()
    soma=0
    listanome.append(nome)
    if nome == "**":
        controller1="**"
        break
    while controller2 !="*":
        atividades=input()
        if atividades == "*":
            controller2="*"
            listasomas.append(str(soma))
            break
        else:
            soma+=int(atividades)
listanome.pop()
print('Relatório de novas questões:\n')

for i in range(len(listanome)):
    somador+=int(listasomas[i])
    print(f'{listanome[i]}: {listasomas[i]}')
print('---')
print(f'Total de novas questões: {somador}')


