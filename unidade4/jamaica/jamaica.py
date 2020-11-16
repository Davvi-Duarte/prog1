frase=input()
chave=input()
msg=""
for i in range(len(frase)):
    if str(i) == frase[i]:
        msg += chave[i]
    else:
        msg += frase[i]

print (msg)

