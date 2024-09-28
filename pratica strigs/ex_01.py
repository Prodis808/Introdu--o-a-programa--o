"""
Escreva um programa para construir uma string a partir da eliminção
de espaços em branco de uma string inicial.
"""

def removedor_espaco(string):
    frasesemespaco = ''

    for i in string:
        if (i != ' '):
            frasesemespaco += i
    return frasesemespaco

def main():
    string = input('Informe uma string: ')
    print(removedor_espaco(string))
        
if __name__ == '__main__':
    main()
    