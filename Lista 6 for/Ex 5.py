from rich import print

eleitores = int(input('Informe o número de eleitore: '))
print('Candidato Bolsonaro = 22 \nCandidato Lula = 13 \nCandidato Ciro = 12')

soma_ciro = 0
soma_lula = 0
soma_bolsonaro = 0
for i in range(eleitores):
    candidato = int(input('Digite o número do candidato e aperte enter até o final de todos os eleitores: '))

    while candidato not in [12, 13, 22]:
        candidato = int(input('Número inválido, Digite 12, 13 ou 22 conforme sua opção: '))
    
    if candidato == 12:
        soma_ciro += 1
        print('[green]Candidato Ciro selecionado!')
    elif candidato == 13:
        soma_lula += 1
        print('[green]Candidato Lula selecionado!')
    else:
        soma_bolsonaro += 1
        print('[green]Candidato Bolsonaro selecionado!')

print('[blue]Quantidade de Votos para cada eleitor')
print(f'Votos para Ciro {soma_ciro}')
print(f'Votos para Lula {soma_lula}')
print(f'Votos para Bolsonaro {soma_bolsonaro}')

if soma_ciro > soma_lula and soma_ciro > soma_bolsonaro:
    print('[green]Ciro Ganhou as eleições.')
elif soma_lula > soma_ciro and soma_lula > soma_bolsonaro:
    print('[green]Lula Ganhou as eleições.')
elif soma_bolsonaro > soma_ciro and soma_bolsonaro > soma_lula:
    print('[green]Bolsonaro Ganhou as eleições.')