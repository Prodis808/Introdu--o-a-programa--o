#iniciei com operação = 0 para que o while funcionasse perfeitamente em loop até o usuário digitar 4
saldo = 0
operacao = 0

while operacao != 4:
    print('-' * 21)
    print('Gerenciador Bancário.')
    print('-' * 21)
    print('Lista de operações:')
    print('<1>  Para Depositar')
    print('<2>  Para Sacar')
    print('<3>  Para Consultar Saldo')
    print('<4>  Para Sair')
    print('')
    operacao = int(input('Informe o Número relacionado a operação desejada. \n'))

#aqui eu coloco o if para filtrar os outros números além dos 4 permitidos pelo programa
    if operacao not in [1, 2, 3, 4]:
        print('Informe apenas um dos 4 números acima. \n')
    else:

#aqui começa os codigos relacionados a cada operaçao            
        if (operacao == 1):
            valor_deposito = float(input('Informe o valor em R$ que você gostaria de depositar: R$ '))
            saldo = saldo + valor_deposito
            print('Pronto, seu saldo atual é R$ {}' .format(saldo))
        elif(operacao == 2):
            valor_saque = float(input('Informe o valor em R$ que você gostaria de sacar: '))
            if (valor_saque <= saldo):
                saldo = saldo - valor_saque
                print('Saque no valor de R$ {} realizado com sucesso, seu saldo atual é de R$ {} ' .format(valor_saque, saldo))
            else:
                print('Saque no valor de R$ {} indisponível, pois seu saldo atual é de R$ {} ' .format(valor_saque, saldo))
        elif (operacao == 3):
            print('Seu saldo atual é R$ {} ' .format(saldo))

#por fim, aqui é a quebra do while, onde o programa finaliza o loop e mostra a frase de saida
if operacao == 4:
    print('Gerenciador Bancário finalizado com sucesso!')