"""
Desenvolva um programa que recebe uma string e depois a exiba de
forma invertida
"""
# Def para inverter
def str_invertida(string):
    string_invertida = ''
    
    # Iterando sobre a string
    for i in range(len(string)-1, -1, -1):    # Utilizando o len para indicar o tamanho da lista e utilizando o -1 para incluir a primeira letra
        string_invertida += string[i]    # Utilizando o indice para concatenar
    
    return string_invertida

# Programa principal
def main():
    string = input('Informe uma string qualquer: ')
    print(str_invertida(string))
    
if __name__ == '__main__':
    main()