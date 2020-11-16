a=int(input())
b=int(input())
lim=int(input())
for i in range(1, lim+1):
    if (i%a==0) and (i%b==0):
        print (i)
