divida = float(input('Informe o valor da sua dívida: '))
juros_mensal = float(input('Informe agora quantos % de juros cresce todo mês: '))
valor_mensal_pago = float(input('Quanto pretende pagar por mês em R$? '))
meses = 0
soma_juros = 0
total_pago = 0

if valor_mensal_pago <= divida * (juros_mensal / 100):
    print(f'Pagando {valor_mensal_pago} todo mês você nunca quitará sua dívida, pois estará pagando apenas os juros. ')
else:
    while divida > 0:  # Condição para verificar se a dívida é maior que zero
        soma_juros += divida * (juros_mensal / 100)    # Calculando o somatorio dos juros
        divida += divida * (juros_mensal / 100)    # Calculando a dívida atribuida com juros 

        if divida < valor_mensal_pago:    # Condição para evitar que o usuario pague além do necessário
            valor_mensal_pago = divida    # Atribuindo o valor a ser pago pelo valor da divida atual, para que assim pague apenas o suficiente

        divida -= valor_mensal_pago    # Calculando a divida - o valor pago pelo usuario
        total_pago += valor_mensal_pago    # Calculando quanto que vai ser pago no somatório final
        meses += 1    # Contador de meses

print(f'Sua dívida foi paga em {meses} meses.')
print(f'Você pagou um valor total de R$ {total_pago :.2f}.')
print(f'Você pagou um total de R$ {soma_juros :.2f} em juros.')
