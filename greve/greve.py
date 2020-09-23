abstencao = int(input())
favor = int(input())
contra = int(input())
total = abstencao+favor+contra

porcabs=(abstencao * 100) / total
porcfavor=(favor * 100) / total 
porccontra=(contra * 100) / total

print('Resultado da Votação\n')
print(f'{abstencao} abstenções ({porcabs:.2f}%)')
print(f'{favor} a favor ({porcfavor:.2f}%)')
print(f'{contra} contra ({porccontra:.2f}%)')
