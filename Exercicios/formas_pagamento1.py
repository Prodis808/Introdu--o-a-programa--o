valor = float(input('Informe o valor da sua compra: \n'))
forma_pagamento = str(input('Qual forma de pagamento? \n')).strip().upper()

while (forma_pagamento not in ['DINHEIRO', 'CHEQUE']):
    forma_pagamento = str(input('Forma de pagamento inválido, insira novamente a forma de pagamento: \n')).strip().upper()

if (valor >= 100 and forma_pagamento == 'DINHEIRO'):
    valor_desconto = valor - (valor * 10/100)
    print('Você ganhou um desconto de 10%, sua compra passou de R${} para R${} ' .format(valor, valor_desconto))
else:
    print('Você não atendeu os requisitos para garantir o desconto, portanto sua compra ficou no total de R${} ' .format(valor))

