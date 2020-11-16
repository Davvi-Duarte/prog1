seq=input().split()
cont=0
for i in range(len(seq)):
    if i == (len(seq)-1):
        break
    elif int(seq[i]) == int(seq[i+1]):
        cont+=1
print(cont)


