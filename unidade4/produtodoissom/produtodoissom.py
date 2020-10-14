n=input()
par1=0
par2=0
impar1=0
impar2=0
for i in range(len(n)):
    if int(i)==0 or int(i)==2 or int(i)==4:
        par1=int(n[i])
        par2=par1+par2
    elif int(i)==1 or int(i)==3 or int(i)==5:
        impar1=int(n[i])
        impar2=impar1+impar2


print(f'{(par2*impar2):05}')
