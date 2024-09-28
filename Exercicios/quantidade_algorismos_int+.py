numero = int(input('Informe um número inteiro e positivo: '))
contador_algarismos = 0

while (numero <= 0):
    numero = int(input('Digite APENAS números inteiros e positivos>: '))
    
while (numero > 0):
    numero = numero // 10
    contador_algarismos = contador_algarismos + 1
        
print('A quantidade de algorismos é {}' .format(contador_algarismos))