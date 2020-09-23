grau=int(input())
minuto=int(input())
segundo=int(input())

grausdecimais= grau+(minuto/60)+(segundo/3600)

print(f'graus = {grausdecimais:.4f}')
