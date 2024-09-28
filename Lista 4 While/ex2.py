numero = float(input('Informe um número (o programa vai parar apenas se você digitar -1): '))
maior = 0
menor = 0

while numero != -1:
    numero = float(input('Informe agora outro número: '))
    
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

soma = maior + menor
print('O maior valor digitado é: ', maior)
print('O menor valor digitado é: ', menor)
print('A soma entre os valores digitados é: ', soma)


    