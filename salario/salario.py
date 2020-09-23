salario_bruto=float(input())
horas_de_trabalho=float(input())
ganhos_por_hora=salario_bruto / horas_de_trabalho
IR=salario_bruto * 0.11
INSS=salario_bruto * 0.08
sindicato=salario_bruto * 0.05

salario_liquido=salario_bruto-IR-INSS-sindicato
hora_liquida=salario_liquido/horas_de_trabalho

print(f'Salário Bruto = {salario_bruto:.2f}')
print(f'Hora Bruta = {ganhos_por_hora:.2f}')
print(f'Desconto IR = {IR:.2f}')
print(f'Desconto INSS = {INSS:.2f}')
print(f'Desconto Sindicato = {sindicato:.2f}')
print(f'Salário Líquido = {salario_liquido:.2f}')
print(f'Hora Líquida = {hora_liquida:.2f}')
