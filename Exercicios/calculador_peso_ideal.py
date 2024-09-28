altura = float(input('Informe a sua altura:\n'))
sexo = str(input('Informe seu sexo biológico: (escreva Masculino ou Feminino)\n')).strip().upper()

while sexo not in ["MASCULINO", "FEMININO"]:
    sexo = str(input('Você digitou incorretamente. Informe seu sexo biológico: (escreva Masculino ou Feminino)\n')).upper()
  
if (sexo == 'MASCULINO'): 
    peso_ideal = (72.7 * altura) - 58
    print('O peso ideal para você é {:.2f}kg ' .format(peso_ideal))
else:
    peso_ideal = (62.1 * altura) - 44.7
    print('O peso ideal para você é {:.2f}kg ' .format(peso_ideal))





