a=input()
vazia="1"
for i in range(1, len(a)):
    if i == 5:
        vazia += a[i]
        vazia += "0"
    else:
        vazia += a[i]
print (vazia)

