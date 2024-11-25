"""
Escreva um programa para construir uma string a partir da eliminção
de espaços em branco de uma string inicial.
"""

def removedor_espaco(string):
    nova_string = ''

    for i in (string):
        if (i != ' '):
            nova_string += i
    return nova_string

def main():
    string = input("Digite a string: ")
    print(removedor_espaco(string))

if __name__ == '__main__':
    main()