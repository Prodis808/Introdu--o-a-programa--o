"""
Desenvolva um programa que recebe uma string e depois a exiba de
forma invertida
"""
def inverte(string):
    nova_string=''
    for i in range(len(string)-1, -1, -1):
        nova_string += string[i]
    return nova_string

def main():
    string = input("Digite a string: ")
    print(inverte(string))

if __name__ == '__main__':
    main()