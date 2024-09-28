"""
Escreva um programa em Python que simule o lançamento de um dado x vezes e imprima
o percentual de surgimento de cada face do dado. O valor x é introduzido pelo usuário, sendo que zero encerra o programa. o programa devera utilizar um array para armazenar o número de aparecimento de cada face
Dica: A função randint(ini, fim) do pacote random gera números
aleatórios no intervalo [inicio, fim]
"""
# Inicio do programa
from rich import print
import random

quantidade_lancamentos = 1
while quantidade_lancamentos != 0:
    quantidade_lancamentos = int(input('Informe a quantidade de vezes que o dado será lançado: '))
    if quantidade_lancamentos == 0:
        break
    else:
        array = [['Lado 1:'], ['lado 2:'], ['Lado 3:'], ['Lado 4;'], ['Lado 5:'], ['Lado 6:']]
        l1 = 0
        l2 = 0
        l3 = 0
        l4 = 0
        l5 = 0
        l6 = 0
        for i in range(quantidade_lancamentos):
            numero_sorteado = random.randint(1,6)
            if numero_sorteado == 1:
                l1 += 1      
            elif numero_sorteado == 2:
                l2 += 1
            elif numero_sorteado == 3:
                l3 += 1
            elif numero_sorteado == 4:
                l4 += 1
            elif numero_sorteado == 5:
                l5 += 1
            elif numero_sorteado == 6:
                l6 += 1
        array[0].append(l1)
        array[1].append(l2)
        array[2].append(l3)
        array[3].append(l4)
        array[4].append(l5)
        array[5].append(l6)
        print('[green]Quantidade de vezes que cada lado apareceu: ')
        print(array)
        print('')
if quantidade_lancamentos == 0:
    print('[red]Programa finalizado.')