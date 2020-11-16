def maior_valor(lista):
    maior = lista[0]
    for valor in lista:
        if valor > maior:
            maior = valor
    return maior

def remove_palavras_com_mais_vogais(palavras):
    if len(palavras) == 0:
        return None
    count = 0
    numeros = []
    for palavra in palavras:
        for letra in palavra:
            if letra in "aeiouAEIOU":
                count += 1
        numeros.append(count)
        count = 0
    #maior = palavras[0]

    for i in range(len(numeros) -1, -1, -1):
        if numeros[i] == maior_valor(numeros):
            palavras.pop(i)
    return 
