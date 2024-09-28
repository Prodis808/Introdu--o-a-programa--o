from rich import print

print('[red]Calculador de tabuada')
numero_tabuada = int(input('Informe um número inteiro : '))

print(f'[green]Tabuada do {numero_tabuada}: ')
numero_calculado = 0
for i in range(1, 11, 1):
    numero_calculado += 1 
    print(f'{numero_tabuada} X {numero_calculado} = {numero_tabuada * numero_calculado}')