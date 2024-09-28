"""
Escreva um programa que leia frases, repetidamente, e que gere um dicionário para cada frase lida. As chaves do dicionário serão os caracteres digitados, e os valores devem consistir no número de vezes que o caractere aparece na frase. O programa deve exibir, para cada frase, seu dicionário correspondente e ser encerrado quando o usuário digitar 1
exemplo: Frase -> Dados
         Dicionário -> {'D': 2, 'a': 2, 'o': 1, 's': 1}
"""

frase = input("Digite uma frase (digite '1' para sair): ")

while frase != '1':
    dicionario = {}
    for caractere in frase:
        if caractere in dicionario:
            dicionario[caractere] += 1
        else:
            dicionario[caractere] = 1
    
    print("Frase ->", frase)
    print("Dicionário ->", dicionario)
    
    frase = input("Digite uma frase (digite '1' para sair): ")

print("Programa encerrado.")