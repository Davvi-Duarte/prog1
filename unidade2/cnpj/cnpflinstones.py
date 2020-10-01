cnpj = input()

n1=float(cnpj[0])
n2=float(cnpj[1])
n3=float(cnpj[3]) 
n4=float(cnpj[4])
n5=float(cnpj[5])
n6=float(cnpj[7])
n7=float(cnpj[8])
n8=float(cnpj[9])

proc = 1+n1+n2+n3+n4+n5+n6+n7+n8

print(f'{n1}{n2}.{n3}{n4}{n5}.{n6}{n7}{n8}/0001-{proc:02.0f}')
