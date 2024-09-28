from rich import print

deposito_inicial = float(input('Informe o valor do depósito inicial: '))
taxa_juros = float(input('Informe o valor da taxa de juros: '))

print('[green] Calculador de juros. ')

valor_para_calcular = deposito_inicial
contador_mes = 0
soma_juros = 0

for i in range(1, 25):
    contador_mes += 1   # Contando os meses de 1 a 24
    juros = (taxa_juros/100) * valor_para_calcular   # Calculando o juros mês a mês
    soma_juros += juros    # Somando o total dos juros
    valor_para_calcular += juros    # Calculando o valor + juros
    print(f'Mês {contador_mes} Total de R$ {valor_para_calcular :.2f}')

print(f'[gree]Soma dos juros R${soma_juros :.2f}')