def matriz3x3():
    matriz = []

    for i in range(1,4):
        linhas = []
        for j in range(1,4):
            valores = int(input(f'Digite um valor para a linha {i} coluna {j}: '))
            linhas.append(valores)
        matriz.append(linhas)
    return matriz

