senha_correta = str('corinthians')
tentativas = 1
senha_usuario = input('Digite sua senha para efetuar o login: \n')

while (tentativas < 3 and senha_usuario != senha_correta):
    senha_usuario = input('Senha incorreta, tente novamente: \n')
    tentativas = tentativas + 1
    
if (senha_usuario == senha_correta):
    print('login efetuado com sucesso!')
else: 
    print('Tentativas excedidas, login bloqueado!')

