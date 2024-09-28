from rich import print
print('-' * 54)
print('')
print('Calculadora De raiz quadrada, usando método de Newton')
print('')
print('-' * 54)
print('')
print('')

num = float(input('Informe um número para calcular a raiz quadrada dele utilizando o método de Newton: '))
b = 2
p = (b + num / b) / 2

while abs(b - p) >= 0.0001: 
    b = p
    p = (b + num / b) / 2    # Utilizando a fórmula de Newton
    
print(f'O valor da Raiz Quadrada de {num :.0f} é {b :.0f} ') 