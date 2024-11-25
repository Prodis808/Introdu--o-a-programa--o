"""
Desenvolva um programa que solicite a digitação de um número de CPF no formato
xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos
verificadores dos caracteres de formatação. (Dica: Pesquise na Internet como os números
de CPF são formados)
"""

# Função para validação de cpf
def verificador_cpf(cpf):

    # Formatando o cpf e verificando se possui 11 digitos
    cpf_formatado = cpf[:3] + cpf[4:7] + cpf[8:11] + cpf[12:]
    while len(cpf_formatado) != 11:
        cpf = input('cpf está incorreto digite seu cpf no formato (xxx.xxx.xxx-xx): ')
        cpf_formatado = cpf[:3] + cpf[4:7] + cpf[8:11] + cpf[12:]
    
    # Calculando o DV1
    soma_dv1 = 0
    contador = 10
    for i in range(9):
        soma_dv1 += int(cpf_formatado[i]) * contador    # Colocando o tipo int para conseguir realizar as operações aritméticas
        contador -= 1
    resto_dv1 = 11 - (soma_dv1 % 11)    # Subtraindo de 11 o resto da divisao
    
    if resto_dv1 > 9:    # Verificando os resultados
        dv1 = 0
    else:
        dv1 = resto_dv1

    # Calculando o DV2
    soma_dv2 = 0
    contador = 11    # Contador adicionou +1 pois o dv1 está incluso
    for i in range(10):    # Nesse caso o range é maior pois o dv1 está incluido
        soma_dv2 += int(cpf_formatado[i]) * contador    # Colocando o tipo int para conseguir realizar as operações aritméticas
        contador -= 1
    resto_dv2 = 11 - (soma_dv2 % 11)    # Subtraindo de 11 o resto da divisao

    if resto_dv2 > 9:     # Verificando os resultados
        dv2 = 0
    else: 
        dv2 = resto_dv2
    
    # Comparando resultados e retornando a validade correspondente do cpf
    if dv1 == int(cpf_formatado[9]) and dv2 == int(cpf_formatado[10]):    # Função int() para o programa comparar números com números ao invés de números com str
        validade = True
    else:
        validade = False
    return validade

# Começo do código
def main():
    cpf = input('Digite seu cpf no formato (xxx.xxx.xxx-xx): ')
    resultado = verificador_cpf(cpf)
    if resultado:
        print(f'CPF {cpf} é válido.')
    else:
        print(f'CPF {cpf} é inválido.')

# Verificador
if __name__ == '__main__':
    main()