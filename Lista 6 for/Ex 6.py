from rich import print

n = int(input('Digite o número de elementos da sequência de Fibonacci: '))

fibonacci_seq = [1, 1]  # Inicializa a sequência de Fibonacci com os dois primeiros elementos

if n <= 2:
    print(f'A sequência de Fibonacci com {n} elementos é {fibonacci_seq[:n]}')  # Exibe os primeiros n elementos se n for menor ou igual a 2
else:
    for i in range(2, n):
        prox_numero = fibonacci_seq[-1] + fibonacci_seq[-2]  # Calcula o próximo número de Fibonacci
        fibonacci_seq.append(prox_numero)  # Adiciona o próximo número à sequência
    
    print(f'A sequência de Fibonacci com {n} elementos é: {fibonacci_seq}')
