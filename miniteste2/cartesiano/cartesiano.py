x=float(input())
y=float(input())

print(f'({x:.1f}, {y:.1f})')

if x>0 and y>0:
    print('no primeiro quadrante')
elif x<0 and y>0:
    print('no segundo quadrante')
elif x<0 and y<0:
    print('no terceiro quadrante')
elif x>0 and y<0:
    print('no quarto quadrante')
elif x==0 and y==0:
    print('na origem')
elif y==0:
    print('sobre o eixo dos x')
elif x==0:
    print('sobre o eixo dos y')

