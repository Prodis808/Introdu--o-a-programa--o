print('----------CALCULADOR DE MÉDIA E CLASSIFICADOR----------')

nota1 = float(input('Informe sua nota da sua primeira prova: \n'))
nota2 = float(input('Informe sua nota da sua segunda prova: \n'))

media = (nota1 + nota2) / 2

if (media >= 9):
    print('Parabéns, sua media aritmética simples é {:.2f} e sua classificação em relação a sua nota é A' .format(media))
elif (media >= 7.5):
    print('Parabéns, sua media aritmética simples é {:.2f} e sua classificação em relação a sua nota é B' .format(media))
elif (media >= 6):
    print('Você precisa rever o conteúdo, sua media aritmética simples é {:.2f} e sua classificação em relação a sua nota é C' .format(media))
elif (media >= 4):
    print('Você precisa rever o conteúdo, sua media aritmética simples é {:.2f} e sua classificação em relação a sua nota é D' .format(media))
else:
    print('Você está reprovado, sua media aritmética simples é {:.2f} e sua classificação em relação a sua nota é D' .format(media))


