"""
Crie um programa para gerar uma matriz de dimensões 3x3 preenchida com valores
informados pelo usuário. 

Além disso, o programa deverá solicitar que o usuário digite um
valor e irá verificar se ele pertence à matriz. 
"""

# Criando a matriz 3x3 com valores fornecidos pelo usuário
from rich import print
matriz = []    # Criei uma lista para ser a matriz
for i in range(1, 4):   # Iniciando laço para criar 3 linhas (3 listas)
    linha = []    # Criando a lista "linha"
    for j in range(1, 4): # Outro laço para fazer número a número
        valor = int(input(f'informe o valor para a posição [{i}][{j}]: '))    # Input para solicitar o valor de cada elemento ao usuário
        linha.append(valor)    # Adicionando cada valor a lista "linha", Observe que esse laço irá se repetir 9 vezes    
    matriz.append(linha)    # Adicionando a lista linha na matriz, atribuindo uma lista vazia a "linha" e começando novamente o mesmo processo

# Printando
print('[green]MATRIZ:')
for i in matriz: # Ele printa a lista pois nesse for está acontecendo uma leitura da matriz, e a matriz na verdade é uma lista, ou seja, o primeiro termo da "Matriz"(lista) é outra lista
    print(i)
print('')

# Verificando se o número está na matriz

valor_verificar = int(input('Digite o valor que deseja verificar na matriz: '))

encontrado = False    # Criando um variável do tipo booleano para fazer a verificaçao
for linha in matriz:    # Percorrendo cada linha da matriz
    if valor_verificar in linha:    # Verificando se o valor está na lista, se não estiver ele repete o processo com a próxima linha...
        encontrado = True   # Caso o número esteja na matriz ele modifica a variável para True
        break

# Condicionais para printar
if encontrado == True:
    print(f'O número {valor_verificar :.0f} está na matriz.')      
else:
    print(f'O número {valor_verificar :.0f} não está na matriz.')








































