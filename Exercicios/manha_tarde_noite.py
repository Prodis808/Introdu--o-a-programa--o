turno = str(input('Em que turno você estuda? \n')).strip().upper()

while turno not in ["M", "T", "N", "MANHA", "MANHÃ", "TARDE", "NOITE"]:
    turno= str(input('Valor inválido, você deve dizer Manhã, tarde ou noite.\n')).strip().upper()

if turno in ["M", "MANHA", "MANHÃ"]:
    print('Bom dia!')
elif turno in ["T", "TARDE"]:
    print('Boa tarde!')
else:
    print('Boa Noite!')
