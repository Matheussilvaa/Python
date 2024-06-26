import os
os.system('cls')
## sempre usar para limpar o terminal ##

#numero =  float(input('Digite um numero inteiro '))

#numero_inteiro = int(numero)



#if  numero_inteiro == numero and numero == numero_inteiro:   aqui esta errado 
 #   print('voce digitou um numero inteiro')         
#else:
 #    print('voce não digitou um numero inteiro ')

#if numero_inteiro % 2 ==0 :
    # print('Numero é par')
#else:
#    print("O número é ímpar.")


#horario = int(input('Quantas horas ? '))


#if horario <=0 <11:
 #   print('Bom dia')
#elif horario <=12 <17:
 #   print('boa tarde')
#elif horario <=18 <=23:
#    print('boa noite')
#else:
 #   print('Fora do formato desejado')


nome = input('Ecreve seu primeiro nome por favor ')
nome_int = int(nome)
letras_4 = int(4) 
letras_5 = int(5,6)
letras_6 = int(6)

if nome_int == letras_4:
    print('seu nome é curto ')
elif nome_int >= letras_5:
    print('seu nome é normal ')
elif nome_int >= letras_6:
    print('seu nome é muito grande ')
else:
    print('não escreveu nada')