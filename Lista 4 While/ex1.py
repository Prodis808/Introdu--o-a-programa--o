contador = 0
soma = 0

while (contador < 500):
    contador += 1
    if (contador % 3 == 0 and contador % 2 != 0):
        print(contador)
        soma = soma + contador
print(soma)