"""
Faça um programa que crie uma lista com os valores de 1 a 500 e depois imprima os
elementos dessa lista na vertical usando outro laço.
"""

lista = []

for i in range(1, 501):    # Criando um laço para gerar a lista de 1 a 500 utilzando .append
    lista.append(i)

for lista in range(1, i+1):    # Laço para percorrer a lista e printar cada número por vez, para que assim fique na vertical
    print(lista)
