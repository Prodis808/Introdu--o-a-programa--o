"""
Escreva um programa que receba cinco valores do usuário e os armazene em uma lista.
"""

lista = []    # Criando uma lista vazia

for i in range(5):    # Criando um laço para pedir o valor 5 vezes e acrescentar na lista utilizando a funçao .append
    lista.append(input('Informe um valor:'))
print(lista)

