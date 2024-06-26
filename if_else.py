import os
os.system('cls')
##sempre usar para limpar o terminal ##


#   IF   /   ELIF   / ELSE
#   SE  / SE NÃO SE / SE NÃO

entrada = input(' Voce quer entrar ou sair ?')

if entrada == 'entrar':
    print('Seja bem vindo, Voce entrou no sistema')
    print(123)
elif entrada == 'sair':
    print('Voce saiu do sistema! vá com Deus')

else: 
    print('voce não digitou nem entrar nem sair')

print('fora dos ifs')