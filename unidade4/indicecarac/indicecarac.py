a=input()
b=input()
lista=[]

for i in range(len(b)): 
    flag=False
    string=''
    for x in range(len(a)):
        if a[x]==b[i]:
            string += str(x) + ' '
            flag = True
    if flag == False:
        j = -1
        lista.append(j)
    else:
        j = ''
        string = list(string)
        string.pop()
        for k in string:
            j += k
        lista.append(j)

for posicao in lista:
    print(posicao)
