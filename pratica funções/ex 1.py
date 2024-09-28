"""
Escreva um programa para ler um valor inteiro e calcular seu dobro,
utilizando a função dobra() que recebe um número por parâmetro e
retorna seu dobro
"""

def dobra(n):
    dobro = n * 2
    return dobro

n = float(input('Informe um número qualquer: '))
num_dobrado = dobra(n)
print(f'A dobra de {n} é {num_dobrado}')
