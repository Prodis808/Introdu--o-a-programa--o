"""
Crie um programa que leia uma matriz 3x3 e troque os elementos da linha 2 pela coluna 2 e vice-versa
"""

# Lendo a matriz 3x3
from rich import print
from matriz_utils import matriz3x3

matriz = matriz3x3()    # Utilizando um def já criado por mim

print('[green]Matriz com valores informados pelo usuário')    # Imprimindo a matriz no formato 3x3
for i in matriz:
    print(i)
print("")

# Invertendo os valores
for i in range(3):
    temporaria = matriz[i][1]    # Criando uma variável temporária para não perder o valor durante a troca
    matriz[i][1] = matriz[1][i]    # Acessando cada indice e trocando manualmente
    matriz[1][i] = temporaria    
    
print('[green]Matriz com elementos da linha 2 na coluna 2 e vice-versa')
for i in matriz:    # Imprimindo a matriz no formato 3x3
    print(i)

