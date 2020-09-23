precotij=float(input('Digite o preço da unidade do tijolo (Em reais): '))
alturatij=float(input('Digite a altura do tijolo (Em metros): '))
comprimentotij=float(input('Digite o comprimento do tijolo (Em metros): '))
alturaparede=float(input('Digite a altura das paredes (Em metros): '))
comprimentoparede=float(input('Digite o comprimento das paredes (Em metros): '))

num_tijolos_altura = alturaparede / alturatij
num_tijolos_largura = comprimentoparede/ comprimentotij
num_tijolos_total = num_tijolos_altura * num_tijolos_largura
print (f'O número total de tijolos é {num_tijolos_total:.1f} e o orçamento final é de R$ {num_tijolos_total*precotij:.1f}')
