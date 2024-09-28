from rich import print
produto = -1
saldo_compra = 0
total_itens = 0

while produto != 0:    # Criando condição para manter o loop enquanto o usuário não digitar 0

    # Criando tabela de opções para o usuário
    print('-' * 14)
    print('Loja do Vasco.')
    print('-' * 14)
    print('')
    print('Lista de produtos:')
    print('<0>  Para ver o Total do carrinho')
    print('<1>  Para comprar uma camiseta número 10 do vascão por apenas R$ 5,50')
    print('<2>  Para comprar uma bermuda do vascão por apenas R$ 2,30')
    print('<3>  Para comprar uma garrafa térmica personalizada do vascão por apenas R$ 4,75')
    print('<4>  Para comprar uma chuteira do vascão por apenas R$ 6,80')
    print('<5>  Para comprar uma camisa do maior time do Brasil (CORINTHIANS) por apenas R$ 9,30')
    print('')
    produto = int(input('Informe o número correspondente ao produto desejado: '))    

    # Criando Lista para o programa rodar apenas se o usuário digitar um número entre os 6 ditos
    while produto not in [0, 1, 2, 3, 4, 5]:
        produto = int(input('Código inválido, informe um número presente na tabela acima: '))
    
    if produto == 1:   
        print('Excelente escolha, camiseta número 10 do vascão adicionada ao carrinho. ')
        saldo_compra = saldo_compra + 5.50    # Calculando o total a ser pago
        total_itens += 1    # Calculando a quantidade de itens
    elif produto == 2:
        print('Excelente escolha, bermuda do vascão adicionada ao carrinho. ')
        saldo_compra = saldo_compra + 2.30
        total_itens += 1
    elif produto == 3:
        print('Excelente escolha, garrafa térmica personalizada do vascão adicionada ao carrinho. ')
        saldo_compra = saldo_compra + 4.75
        total_itens += 1
    elif produto == 4:
        print('Excelente escolha, chuteira do vascão adicionada ao carrinho. ')
        saldo_compra = saldo_compra + 6.80
        total_itens += 1
    elif produto == 5:
        print('Você acaba de fazer a melhor escolha possível, pois CORINTHINAS > VASCO, camisa do maior time do Brasil adicionada ao carrinho ')
        saldo_compra = saldo_compra + 9.30
        total_itens += 1
    else:    # Montando a área do carrinho de compras
        print('-' * 20)
        print('Carrinho de compras.')
        print('-' * 20)
        print('')
        print(f'Você selecionou um total de {total_itens} itens.')
        print(f'O valor a ser pago é R$ {saldo_compra :.2f} ')
        
        # Começando bloco de pagamentos
        forma_pagamento = str(input('Aceitamos Dinheiro, Cartão (em até 10x sem juros), e Pix, como gostaria de pagar? ')).strip().upper()
      
        while forma_pagamento not in ['DINHEIRO', 'CARTAO', 'CARTÃO', 'PIX']:    # Criando condição para o programa rodar apenas se o usuário digitar uma das 3 opções disponíveis
            forma_pagamento = str(input(f'{forma_pagamento} não é aceita em nosso sistema, por favor escolha apenas uma das 3 opções acima.')).strip().upper()

        #   BLOCO PARA PAGAMENTO EM DINHEIRO
        if forma_pagamento == ('DINHEIRO'):
            print('Forma de pagamento DINHEIRO selecionada')
            valor_pago_cliente = float(input('Quantos reais em dinheiro? '))    # Calculando troco se houver

            while valor_pago_cliente < saldo_compra:    # Condição para verificar se o valor pago é suficiente para finalizar a compra
                valor_pago_cliente = float(input(f'R$ {valor_pago_cliente} insuficiente para a compra, falta R$ {saldo_compra - valor_pago_cliente} informe um valor maior ou igual a R$ {saldo_compra}: '))

            if valor_pago_cliente > saldo_compra:
                troco = valor_pago_cliente - saldo_compra
                print(f'Agradecemos a preferência, aqui está seu troco no valor de R$ {troco :.2f} até a próxima! ')

            elif valor_pago_cliente == saldo_compra:
                troco = 0
                print('Agradecemos a preferência, até a próxima! ')
            
        # BLOCO PARA PAGAMENTOS EM CARTÃO
        elif forma_pagamento == 'CARTAO' or forma_pagamento == 'CARTÃO':    
            tipo_cartao = str(input('Crédito ou Débito? ')).strip().upper()

            while tipo_cartao not in ['CRÉDITO', 'CREDITO', 'DÉBITO', 'DEBITO']:    # Condição para programa prosseguir apenas se o usuário digitar uma das 2 opções
                tipo_cartao = str(input('Forma de pagamento indisponível no momento, Débito ou Crédito? ')).strip().upper()

            if tipo_cartao == 'CRÉDITO' or tipo_cartao == 'CREDITO':    # CARTÃO DE CRÉDITO E PARCELAS
                parcelas = int(input('Poderá parcelar em até 10x sem juros, em quantas vezes deseja parcelar? '))
                print(f'Agradecemos a preferência, até a próxima! Compra no valor de {saldo_compra} realizada no crédito em {parcelas} vezes.')
               
            if tipo_cartao == 'DÉBITO' or tipo_cartao == 'DEBITO':    # CARTÃO DE DÉBITO
                print(f'Compra no valor de {saldo_compra} paga no Débito. Agradecemos a preferência, até a próxima!')

        # BLOCO PARA PAGAMENTOS EM PIX  
        elif forma_pagamento == 'PIX':
                print(f'Compra no valor de {saldo_compra} paga no PIX. Agradecemos a preferência, até a próxima!')
