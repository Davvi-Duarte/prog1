letra =  ""
while True:

    registro = input()
    if registro[0] == "S":
        break

    if registro[0] == "R":
        letra += registro[2]


    elif registro[0] == "P":
        registros = 0

        for i in letra:
            if i == registro[2]:
                registros += 1
                
        print(registros)


