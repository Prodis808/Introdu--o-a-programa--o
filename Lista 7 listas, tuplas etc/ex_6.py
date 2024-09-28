import math
"""
Escreva um programa que leia as coordenadas de N pontos do plano cartesiano e que exiba as distâncias mnima e máxima e média entre esses pontos. O programa deve representar os pontos como uma lista de tuplas e deve adotar a distância euclidiana para aferir a distância dentre dois pontos
"""

# Função para calcular a distância euclidiana entre dois pontos
distancia = lambda p1, p2: math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Número de pontos
N = int(input("Digite o número de pontos: "))

# Lista para armazenar os pontos
pontos = []

# Loop para receber as coordenadas dos pontos
for i in range(N):
    x = float(input(f"Digite a coordenada x do ponto {i+1}: "))
    y = float(input(f"Digite a coordenada y do ponto {i+1}: "))
    pontos.append((x, y))

# Cálculo das distâncias mínima, máxima e média
distancia_min = float('inf')
distancia_max = float('-inf')
distancia_total = 0

for i in range(N):
    for j in range(i+1, N):
        dist = distancia(pontos[i], pontos[j])
        distancia_min = min(distancia_min, dist)
        distancia_max = max(distancia_max, dist)
        distancia_total += dist

average_distancia = distancia_total / (N * (N - 1) / 2)

# Exibição dos resultados
print(f"Distância mínima entre os pontos: {distancia_min}")
print(f"Distância máxima entre os pontos: {distancia_max}")
print(f"Distância média entre os pontos: {average_distancia}")
