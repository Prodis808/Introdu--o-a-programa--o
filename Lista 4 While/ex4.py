n1 = float(input('Digite um número: '))
n2 = float(input('Digite agora outro número: '))
n3 = n1
resto_divisao = n1 % n2
contador = 0
divisao = n1 / n2

while n3 >= n2:
    n3 = n3 - n2
    contador = contador + 1

print(f'O número {n1} divido por {n2} é {divisao}, pois {n2} cabe {contador} vezes dentro de {n1}')
print(f'O resto da divisão é {resto_divisao}')
    