"""
Faça um programa que leia duas strings e informe o conteúdo delas seguido do seu
comprimento. Informe também se as duas strings possuem o mesmo comprimento e são
iguais ou diferentes no conteúdo. 
"""

def verificador_strings(string1, string2):

    # Informando o conteudo e tamanho delas
    print(f'Conteudo da primeira string = {string1}, e o comprimento dela é {len(string1)}. ')
    print(f'Conteudo da segunda string = {string2}, e o comprimento dela é {len(string2)}. ')

    # Verificando igualdade de comprimento e de conteudo    
    if string1 == string2 :    # Verificando se elas sao identicas
        print('As strings são completamentes identicas, tamanho e conteudo.')
    elif string1 != string2 and len(string1) != len(string2):    # Verificando se elas sao completamente diferentes
        print('As strings possuem conteudos diferentes, e quantidade de caracteres diferentes.')
    elif string1 != string2 and len(string1) == len(string2):    # Verificando se elas possuem apenas o mesmo tamanho
        print(f'Elas possuem conteudos diferentes, porém a mesma quantiade de caracteres.')
    
def main():
    string1 = input('Informe a primeira string: ')
    string2 = input('Informe a segunda string: ')
    verificador_strings(string1, string2)
    
if __name__ == '__main__':
    main()
    