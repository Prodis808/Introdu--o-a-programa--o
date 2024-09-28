"""
Faça um programa que solicite a data de nascimento (dd/mm/aaaa) e
imprima com o nome do mês por extenso.
Ex.:
Informe uma data: 25/10/2018
Data por extenso: 25 de outubro de 2018
"""

def mes_extenso(data_nascimento):
    lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    data_formatada = f"{data_nascimento[0]} de {lista_meses[data_nascimento[1]-1]} de {data_nascimento[2]}"
    return data_formatada

def main():
    data_nascimento = input('Informe sua data de nascimento(dd/mm/aaaa): ').split('/')
    data_nascimento[1] = int(data_nascimento[1])
    print(mes_extenso(data_nascimento))

if __name__ == '__main__':
    main()