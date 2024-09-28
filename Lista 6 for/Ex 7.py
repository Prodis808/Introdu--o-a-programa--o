from rich import print
numero = int(input("Digite um número inteiro positivo: "))

if numero < 2:
    print("O número não é primo.")
else:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    else:
        print(numero, "é primo.")
        exit()

    print("O número não é primo.")