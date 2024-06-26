import os
os.system('cls')
## sempre usar para limpar o terminal ##

nome = input('Digite seu nome por favor:  ' )
idade = input('Digite sua idade por favor:  ' )

print(f'O nome digitado foi: {nome} e a idade digitada foi: {idade}')

if nome == nome and idade == idade:
 print(f'Seu nome é: {nome}' )
 print(f'Seu nome invertido é: {nome [::-1]}')      
 if ' ' in nome:
     print('seu nome contem espaço')
 else:
     print('seu nome NÃO contem espaço.')    
 print(f'Seu nome tem {len (nome)} letras')  
 print(f'A primeira letra do seu nome é: {nome [0]}')
 print(f'A ultima letra do seu nome é:  {nome [-1]}')
else:
 print('campos vazios')              