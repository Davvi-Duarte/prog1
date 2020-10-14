a=input()
calculo1=0
calculo2=0
for i in range(len(a)):
    print (i)
    if int(a[i]) == 1:
        if i==0:
            calculo2 = 1
        else:    
            calculo1= (i) ** 2
            calculo2= calculo1 + calculo2
    print (calculo2)
    print (calculo1)
