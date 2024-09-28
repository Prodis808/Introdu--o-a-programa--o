"""
Escreva um programa que elimina os brancos de uma string digitada pelo usuário. (Dica:
Crie uma nova string, atribuindo a ela os caracteres digitados que são diferentes de
branco) 
"""

def removedor_espacos(string):
    string_formatada = ''
    for i in string:
        if i != ' ':
            string_formatada += i
    return string_formatada

def main():
    string = input('Informe uma string a ser formatada: ')
    print(f'A string formatada é {removedor_espacos(string)}')

if __name__ == '__main__':
    main()