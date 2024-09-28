"""
Faça um programa em Python que leia um número de telefone e
corrija o número no caso deste conter somente 8 dígitos,
acrescentando o '9' na frente. O usuário pode informar o número com
ou sem o traço separador. Corrija caso ele informe o número sem o
traço separador.
Exemplo:
Informe seu número de telefone: 88715498
Telefone corrigido: 98871-5498
"""

def formatador_numeros(numero):

    numero = numero.split('-')    # Removendo os hifens para auxiliar no processo
    numero = ''.join(numero)    # Juntando os numeros após a separação    

    if len(numero) == 8:    # Verificando se o comprimento é 8, caso seja adiciona o 9 antes e coloca o hifen
        numero_formatado = '9' + numero
        numero_formatado = numero_formatado[:5] + '-' + numero_formatado[5:]    # Separando os 9 numeros, do indice 0 até o indice 4, adiciona o hifen e coloca o resto do numero

    elif len(numero) == 9:    # Verificando se o comprimento é 9, caso seja, apenas coloca o hifen
        numero_formatado = numero[:5] + '-' + numero[5:]    # Separando os 9 numeros, do indice 0 até o indice 4, adiciona o hifen e coloca o resto do numero

    return numero_formatado

def main():

    numero = input('Digite um número de telefone: ')
    print(formatador_numeros(numero))

if __name__ == '__main__':
    main()