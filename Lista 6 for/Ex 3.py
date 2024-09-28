from rich import print

quantidade_pessoas = int(input('Informe a quantidade de pessoas que você precisa calcular a média de idade: '))

soma_idades = 0
for i in range(1, quantidade_pessoas+1):
    idades = int(input('Informe a primeira idade, pressione enter e repita o processo até o fim. '))
    soma_idades += idades
media = soma_idades / quantidade_pessoas

if media <= 25:
    print(f'[blue]A média de idade dessa turma é {media:.1f} portanto é uma turma de jovens. ')
elif media > 25 and media <= 60:
    print(f'[green]A média de idades dessa turma é {media:.1f} portanto é uma turma de Adultos. ')
elif media > 60:
    print(f'[yellow]A média de idades dessa turma é {media:.1f} portanto é uma turma de Idosos. ')

