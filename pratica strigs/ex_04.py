"""
Escreva um programa em Python que receba uma string e a imprima
na vertical e em formato de escada. Por exemplo, se o usuário digitar a
string FULANO, o programa deve exibir a seguinte saída:
F
FU
FUL
FULA
FULAN
FULANO
"""

def vertical(string):
    frase_escada = ''
    for i in range(len(string)):
        frase_escada += string[i]
        print(frase_escada)
        
def main():
    string = input('Informe uma string: ') 
    vertical(string)   

if __name__ == '__main__':
    main()