frase=input()
num1=int(input())
num2=int(input())
indice=num1
frasenova=''
for num in range(num1, num2):
    if num < (num2-1):
        if frase[indice]==' ':
            frasenova += ','
            frasenova += ' '
        else:
            frasenova += frase[indice]
            frasenova += ' ' 
    else:
        if frase[indice]!=' ':
            frasenova += frase[num] 
        else:
            frasenova += ','
    indice +=1
        

print(frasenova)








