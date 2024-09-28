from rich import print

print('[blue]Calculador de potências usando for.')

base = float(input('Infome a base: '))
expoente = int(input('Informe o expoente: '))

resultado = 1
for i in range(expoente):
    resultado *= base
    
print(resultado)