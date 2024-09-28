produto = -1
saldo_compra = 0
total_itens = 0


while produto != 0:    # Criando condição para manter o loop enquanto o usuário não digitar 0

    # Criando tabela para o usuário escolher
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
    produto = int(input('Informe o númeor correspondente ao produto desejado: '))    

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

