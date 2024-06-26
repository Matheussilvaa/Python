import os
os.system('cls')
## sempre usar para limpar o terminal ##

nome = 'matheus'
indice = 0
novo_nome = ''

while indice < len(nome):
     letra = nome[indice]
     novo_nome += f'*{letra}'
     indice += 1

print(novo_nome)