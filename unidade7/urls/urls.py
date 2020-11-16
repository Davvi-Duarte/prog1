def split(frase, delimitador):
    lista = []
    palavra = ""
    for i in range(len(frase)):
        if frase[i] == delimitador:
            if palavra != "":

                lista.append(palavra)
                palavra = ""
        else:

            palavra += frase[i]
    if palavra != "":
        lista.append(palavra)

    return lista

def filtra_urls(lista):

    out = []
    check = []
    for i in range(len(lista)):

        url = split(lista[i], ".")
        check.append(url)
    for j in range(len(lista)):
        for k in range(len(check)):
            if check[j][k] == "google":

                out.append(lista[j])
    return out
