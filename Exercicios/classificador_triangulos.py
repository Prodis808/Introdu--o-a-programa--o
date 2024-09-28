lado1 = float(input('Informe o primeiro lado do triângulo: \n'))
lado2 = float(input('Informe o segundo lado do triângulo: \n'))
lado3 = float(input('Informe o terceiro lado do triângulo: \n'))

if (lado1 == lado2 and lado1 == lado3):
    print('Esse triângulo é "EQUILÁTERO"')
elif (lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    print('Esse triânguo é "ISOCELES"')
else:
    print('Esse triângulo é "ESCALENO"')


