"""
Faça um programa que leia dois vetores com cinco elementos e gere um terceiro vetor de 10 elementos, cujo valores deverão ser compostos pelos elementos intercalados dos dois outros vetores

"""

from rich import print
# Criando 2 vetores com 5 elementos

vetor1 = []
vetor2 = []
for i in range(1, 6):
    n1 = int(input(f'Informe o {i}° valor para o vetor 1: '))
    n2 = int(input(f'Informe o {i}° valor para o vetor 2: '))
    vetor1.append(n1)
    vetor2.append(n2)

# Intercalando cada vetor

vetor_intercalado = []
for i in range(5):
    vetor_intercalado.append(vetor1[i])    # Utilizando o i para identificar o indice certo da lista
    vetor_intercalado.append(vetor2[i])
print(vetor_intercalado)
