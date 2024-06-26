import os
os.system('cls')
## sempre usar para limpar o terminal ##


#numero_int = int (input('Digite um numero inteiro:  ' ))

#if numero_int == numero_int:
#   print('O número digitado é inteiro')
#   if numero_int % 2 == 0:
#      print('O número digitado é PAR')
#  else:
#      print('O número digitado é IMPAR')
#else:
#   print('O número digitado não e um número inteiro')


#horas = int( input(' Quantas horas são?:  '))

#if 0 <= horas <= 11:
#   print('Bom Dia!')
#elif 12 <= horas <= 17:
#      print('Boa Tarde')
#elif 18 <= horas <= 23:
#    print('Boa Noite')
#else:
#   print('Horario invalido! ')


nome = input('Digite seu nome:  ')
print (f'O seu nome possui {len(nome)} letras')

if len(nome) == 4:
    print('Seu nome é curto')
elif 5 <= len(nome) <=6:
    print('Seu nome e normal')
elif  len(nome) >= 7 :
     print('Seu nome é muito grande')
else:
  print('Nome digitado é invalido')