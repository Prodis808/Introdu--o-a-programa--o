"""
Suponha que se deseje processar um conjunto de valores representando altura e sexo (M/F) de um grupo de 10 pessoas.

a) leia este conjunto de dados e armazene-o em duas listas vinculadas, uma das quais contém as alutras e a outra contém os sexos dos indivíduos ✅

b) Determine a maior e a menor altura dentre esses indivíduos, indicando o sexo do indivíduo de maior altura e o sexo do individuo de menor altura ✅
 
c) Encontre a média de altura entre os individuos do sexo feminino e a média entre os individos do sexo masculino ✅

d) Determine o número total de individuos de cada sexo ✅
"""
from rich import print

# Lendo o conjunto de dados e armazenando em 2 listas vinculadas

array = []
lista_sexo = []
lista_alturas = []


for i in range(1, 11):    # Solicitando ao usuário o sexo e a altura de cada indivíduo
    sexo = str(input(f'Informe o sexo do indivíduo {i} (M/F): ')).upper()
    altura = int(input(f'Agora informe a altura do indivíduo {i} em cm: '))
    print('[green]Dados armazenados.')
    lista_sexo.append(sexo)
    lista_alturas.append(altura)
array.append(lista_sexo)    # Armazenando os dados na lista array
array.append(lista_alturas)


# Determinando maior e menor altura, indicando o sexo de ambos

maior = 0    # Declarando duas variáveis para verificar as alturas
menor = 999

for i in range(len(lista_alturas)):    # Percorrendo a lista alturas

    if lista_alturas[i] > maior:    # Verificando se o indice [i] é maior do que o número passado, se for o maior passa a ser ele
        maior = lista_alturas[i]
        sexo_maior = lista_sexo[i]    # Atribuindo a variável sexo_maior o sexo correspondente ao indice certo

    elif lista_alturas[i] < menor:    # Verificando se o indice [i] é o menor do que o número passado, se for o menor passa a ser ele
        menor = lista_alturas[i]
        sexo_menor = lista_sexo[i]    # Atribuindo a variável sexo_menor o sexo correspondente ao indice certo
print(f'[green]A maior altura pertence a uma pessoa do sexo {sexo_maior} e é de {maior}Cm[/]\n[red]Já a menor altura pertence a uma pessoa do sexo {sexo_menor} e é de {menor}Cm')
print('')

# Encontrando a média de altura entre individuos do sexo masculino e individuos do sexo feminino e determinando o total de individuos de cada sexo

contador_m = 'M'                        # Criando contadores para saber a quantidade de homens e mulheres
contador_m = lista_sexo.count('M')    
contador_f = 'F'
contador_f = lista_sexo.count('F')

soma_altura_m = 0
soma_altura_f = 0

for i in range(len(array)):    # Iterando sobre array para identificar a altura correta de acordo com os indices, e assim soma-la em sua variável certa
    for j in range(len(array[i])):
        if array[i][j] == 'M':
            soma_altura_m += lista_alturas[j]
        elif array[i][j] == 'F':
            soma_altura_f += lista_alturas[j]

media_m = soma_altura_m / contador_m
media_f = soma_altura_f / contador_f

print(f'[blue]A média das alturas masculinas é {media_m}[/]\n[red]A média de alturas feminina é {media_f}')
print('')
print(f'[blue]Total de homens: {contador_m}[/]\n[red]Total de mulheres: {contador_f}')
