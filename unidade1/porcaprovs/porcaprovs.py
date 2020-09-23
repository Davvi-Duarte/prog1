print('Análise da Turma\n===')

numaprovados=int(input('Número de aprovados? '))
numreprovados=int(input('Número de reprovados? '))

print('---')

total = numaprovados+numreprovados

aprovados = (numaprovados*100)/total
reprovados = (numreprovados*100)/total

print(f'Total de alunos na turma: {total}')
print(f'Aprovados: {numaprovados} = {aprovados:.1f}%')
print(f'Reprovados: {numreprovados} = {reprovados:.1f}%')
