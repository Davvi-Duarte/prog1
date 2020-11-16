cont=0
maior1=0
maior2=0
penalizacao=0
media=0
apr='cursando'
print('Mastery Learning')
print('Cálculo da nota na unidade\n')
while True:
    if cont<1:
        notas=input('Nota? ')
        cont+=1
        maior1+=float(notas)
    else:
        if cont>1:
            penalizacao+=0.5
        cont+=1
        notas= input('Nota? ')
        if float(notas)>maior1:
            maior2=maior1
            maior1=float(notas)
        elif float(notas)>maior2:
            maior2=float(notas)
        media=(maior1+maior2)/2
        if media>=6.0:
            apr='aprovado'
        print(f'Média: {media:.1f} ({apr})')
        print(f'Penalização: {penalizacao:.1f}\n')
        if apr == 'aprovado':
            break
print('===')
print(f'Notas válidas: {maior1:.1f} e {maior2:.1f}')
print(f'Média parcial na unidade: {media:.1f}')
print(f'Penalizações: {penalizacao:.1f}')
print(f'Média final na unidade: {media-penalizacao:.1f}')
