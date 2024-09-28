valor_hora = float(input('Quanto você ganha por hora em R$? \n'))
horas_trabalhadas = int(input('Quantas horas você trabalha em um mês? \n'))

salariobruto = (valor_hora * horas_trabalhadas)
ir = salariobruto * 11/100
inss = salariobruto * 8/100
sindicato = salariobruto * 5/100
salarioliquido = salariobruto - (ir + inss + sindicato)

print('Salário bruto R$ {}' .format(salariobruto))
print('Imposto de renda R$ {}' .format(ir))
print('Inss R$ {}' .format(inss))
print('Sindicato R$ {}' .format(sindicato))
print('Salário liquido R$ {}' .format(salarioliquido))
