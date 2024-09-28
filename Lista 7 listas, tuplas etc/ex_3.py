"""
faça um programa que receba como entrada uma lista de númeors representando uma mensagem codificada, armazene esses valores em uma lista e depois traduza a mensagem de acordo com o código
"""
from rich import print

# Criando um dicionário com a cifra
cifra = {0: ' ', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

codigo_usuario = input('Digite o codigo separando por espaços:\n')
codigo_usuario = codigo_usuario.split()    # Retirando os espaços e transformando em uma lista

codigo_usuario_numeros = []    # Criando uma lista para ser a lista do tipo int
# Utilizando o for iterar o codigo digitado pelo usuário, transforma-lo em tipo int e armazena-lo na nova lista
for i in codigo_usuario:
    codigo_usuario_numeros.append(int(i))

mensagem_decodificada = ''    # Colocando aspas para ir concatenando 
for i in codigo_usuario_numeros:    # Percorrendo a lista de números inteiros
    mensagem_decodificada = mensagem_decodificada + cifra[i]    # Acrescentando letra por letra utilizando o indice i, que buscará a informação no dicionário

print(f'[green]A mensagem decodificada é:[/][red]\n{mensagem_decodificada}')
input()