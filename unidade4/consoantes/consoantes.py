q=int(input())
cont=0
for i in range(q):
    a=input()
    if not a[0] in "AEIOUaeiou":
        cont += 1
print(f'total de palavras: {q}')
print(f'iniciadas por consoantes: {cont} ({(cont*100)/q:.2f}%)')
