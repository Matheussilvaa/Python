import os
os.system('cls')
##sempre usar para limpar o terminal ##

# INPUT e a mesma coisa que o Scanner porem ela sempre retorna um string

#nome = input('Qual o seu nome ? ' )

#print(f'O seu nome é {nome=}')

# transformando o input em um int
## numero1 = int (input('Digite um numero: '))

numero1 = input('Digite um numero: ')
numero2 =  input('Digite outro numero: ')

int_numero1 = int (numero1)
int_numero2 = int (numero2)
print (f' A soma dos numeros é: {int_numero1 + int_numero2}')
