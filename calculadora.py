import os
os.system('cls')
## sempre usar para limpar o terminal ##

while True:
    numero1 = input('Digite um numero:  ')
    numero2 = input('Digite outro número:  ')
    operador = input('Digite o operador (+ ou - ou / ou *):  ')
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float (numero1)
        num_2_float = float(numero2)
        numeros_validos = True
    except:
        ...
    if numeros_validos is None:
        print('Um ou ambos números digitados são invalidos.')
        continue
    operadores_permitidos = ' + - / * '
    
    if operador not in operadores_permitidos:
        print('Operador digitado está invalido.')
        continue
    
    if len(operador) > 1 :
        print('Digite apenas um operador')
        continue

    print('Realizando a sua conta.....')
    print('Confira o resultado abaixo:')

    if operador == '+':
        print(f'{num_1_float}  +  {num_2_float}  =  ', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}  -  {num_2_float}  =  ', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}  /  {num_2_float}  =  ', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float}  *  {num_2_float}  =  ', num_1_float * num_2_float)

    sair = input('voce quer sair? [S]im: ').lower().startswith('s')

    if sair is True:
        break