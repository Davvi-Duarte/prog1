def gera_emails(nomes):
    email=[]
    for i in range(len(nomes)):
        a=""
        nome=""
        nome=nomes[i].split()
        a+=nome[0]+"."+nome[len(nome)-1]+"@ccc.ufcg.edu.br"
        email.append(a.lower())
    return email



