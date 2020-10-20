palavra=input()
flag=False
for i in range(len(palavra)):
    if palavra[i] in "AEIOUaeiou":
        flag=True
        print(palavra[i])
        break

if flag==False:
    print('-')
    
