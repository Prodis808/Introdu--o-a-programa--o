"""
Faça um programa que solicite a data de nascimento (dd/mm/aaaa) e imprima com o
nome do mês por extenso.
Ex.:
Informe uma data: 25/10/2018
Data por extenso: 25 de outubro de 2018. 
"""

def formatador_data(data_nascimento):
    data_nascimento = data_nascimento.split('/')    # Splitando para trasformar em lista e conseguir manipular os indices separadamente
    lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']    # Criando uma lista de meses para utilizala na formatação

    data_nascimento[1] = int(data_nascimento[1])    # Transformando o indice 1 em inteiro, ou seja, transformando o mes em inteiro, para manipulalo na formatação

    data_formatada = f'{data_nascimento[0]} de {lista_meses[data_nascimento[1]-1]} de {data_nascimento[2]}'    # Atribuindo a auma variável a forma formatada, utilizando os indices para acessar os valores correspondentes a lista de meses

    return data_formatada

def main():
    data_nascimento = input('Informe sua data de nascimento no formato (dd/mm/aaaa): ')
    print(formatador_data(data_nascimento))

if __name__ == '__main__':
    main()
