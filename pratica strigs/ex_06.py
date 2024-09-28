"""
Refaça o Exercício 1 usando as funções para manipulação de strings de
Python.
"""

def removedor_espacos(string):
    string_sem_espaco = ''
    string = string.split()
    for letra in string:
        string_sem_espaco += letra
    return string_sem_espaco

def main():
    string = (input('Informe uma string aleatoria: '))
    print(removedor_espacos(string))

if __name__ == '__main__':
    main()