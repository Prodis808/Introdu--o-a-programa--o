#entrada do valor e forma de pagamento.
valor = float(input('Informe o valor da sua compra: \n'))
forma_pagamento = str(input('Aceitamos Dinheiro, Cheque e Cartão, como gostaria de pagar? \n')).strip().upper()

#coloquei o while para captar apenas o que está dentro da lista abaixo, para que assim o programa caminhe para o resultado correto.
while (forma_pagamento not in ['DINHEIRO', 'CHEQUE', 'CARTÃO', 'CARTAO']): 
    forma_pagamento = str(input('Forma de pagamento inválida, insira novamente a forma de pagamento: \n')).strip().upper()

#nesse momento meu programa ja filtrou as entradas diferentes das str que estão na lista, e agora meu programa começa a condicionar e filtrar os resultados
if (forma_pagamento == 'DINHEIRO' and valor >= 100):
    valor_desconto = valor - (valor * 10/100)
    print('Você ganhou um desconto de 10%, sua compra passou de R${} para R${} ' .format(valor, valor_desconto))
elif (forma_pagamento == 'DINHEIRO' and valor < 100):
    print('Você não atendeu aos requisitos para garantir o desconto, portanto sua compra ficou no total de R${}  ' .format(valor))
elif (forma_pagamento == 'CHEQUE'):
    print('Você não atendeu aos requisitos para garantir o desconto, portanto sua compra ficou no total de R${}  ' .format(valor))
elif (forma_pagamento == 'CARTAO' or forma_pagamento == 'CARTÃO'):
    tipo_cartao = str(input('Cartão de Débito ou Crédito? \n')).strip().upper()

#aqui eu repito o mesmo while do inicio, para filtrar as 2 funçoes do cartao e evitar erros no meu programa   
    while (tipo_cartao not in ['DÉBITO', 'DEBITO', 'CRÉDITO', 'CREDITO']):  
        tipo_cartao = str(input('Forma inválida, escolha Débito ou Crédito. \n')).strip().upper()

    if (tipo_cartao == 'DÉBITO' or tipo_cartao == 'DEBITO'):
       print('Você não atendeu os requisitos para garantir o desconto, portanto sua compra ficou no total de R${} e você pagou no cartão de débito' .format(valor)) 
    else:
        quantidade_parcelas = int(input('Você pode parcelar em até 3 vezes. Em quantas vezes quer parcelar? \n'))

#na parte de cartao de crédito eu repeti o while para filtrar novamente e o programa so funcionar se o usuario colocar 1, 2 ou 3
        while (quantidade_parcelas not in [1, 2, 3]):
            quantidade_parcelas = int(input('Você não pode parcelar em mais de 3 vezes, em quantas parcelas você quer parcelar? \n'))
        
        if (quantidade_parcelas == 1):
            print('Você não atendeu os requisitos para garantir o desconto, portanto sua compra ficou no total de R${} e você pagou no Crédito em 1 parcela.' .format(valor))
        elif (quantidade_parcelas == 2):
            print('Você não atendeu os requisitos para garantir o desconto, portanto sua compra ficou no total de R${} e você pagou no Crédito em 2 parcelas de R${:.2f}' .format(valor, (valor / 2)))
        else:
            print('Você não atendeu os requisitos para garantir o desconto, portanto sua compra ficou no total de R${} e você pagou no Crédito em 3 parcelas de R${:.2f}' .format(valor, (valor / 3)))
            