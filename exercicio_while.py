import os
os.system('cls')
## sempre usar para limpar o terminal ##

nome = 'matheus'
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

indice = 0
novo_nome =''


while indice < len(nome):
    letra = nome[indice]
    novo_nome+= f'*{letra}'
    indice += 1
    
    print(f'{novo_nome}')
    print(f'{letra}')

    #while de acumulação que se acumula dentro da variavel novo_nome