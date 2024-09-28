"""
Escreva um programa em Python que simule o lançamento de um dado x vezes e imprima
o percentual de surgimento de cada face do dado. O valor x é introduzido pelo usuário.
Seu programa deverá utilizar uma lista para armazenar os números de aparecimento de
cada face. Dica: A função randint(ini, fim) do pacote random gera números
aleatórios no intervalo [inicio, fim]
"""

# Jogando o dado x vezes e imprimindo o percentual de surgimento de cada face do dado
from random import randint
from rich import print

x = int(input('Informe quantas vezes o dado será jogado: '))    # Solicitando a quantidade de vezes
while x <= 0:
    x = int(input('Informe um número inteiro e maior que zero, pois você está simulando o lançamento de um dado, e não da para jogar 0 vezes...\n'))

lista = []
valor = 0

for i in range(1, x+1):    # Criando um laço para sortear um número pela quantidade de vezes solicitada pelo usuário
    valor = randint(1, 6)    # Função para sortear um número de 1 a 6
    print(f'[green]Lançamento {i}, resultado {valor}')
    lista.append(valor)    # Adicionando cada valor a lista

# Imprimindo o percentual de cada número
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0 
num6 = 0 
for i in lista:    # Percorrendo a lista e verificando cada elemento
    if i == 1:
        num1 += 1
    elif i == 2:
        num2 += 1
    elif i == 3:
        num3 += 1
    elif i == 4:
        num4 += 1
    elif i == 5:
        num5 += 1
    else:
        num6 += 1
print(f'[blue]Número 1 apareceu {num1} vezes.[/]\nNúmero 2 apareceu {num2} vezes.\n[blue]Número 3 apareceu {num3} vezes.[/]\nNúmero 4 apareceu {num4} vezes.\n[blue]Número 5 apareceu {num5} vezes.[/]\nNúmero 6 apareceu {num6} vezes. ')
input()