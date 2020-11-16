def senha_segura(senha):
    sen=""
    if len(senha)<4:
        return "Senha insegura"
    else:
        for i in range(len(senha)):
            if i%2==0:
                if int(senha[i])%2==0:
                    sen="Senha insegura"
                    return sen
                    break
                else:
                    sen="Senha segura"
            else:
                if int(senha[i])%2==0:
                    sen="Senha segura"
                else:
                    sen="Senha insegura"
                    return sen
                    break
        return sen
    



