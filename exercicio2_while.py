import os
os.system('cls')
## sempre usar para limpar o terminal ##

#calculadora com while  



while True:
    valor1 =input('entre com o valor:')
    valor2 = input('entre com o segundo numero: ')
    operador = input('Digite o operador (+-/*):')

    try:
     num_1_float = float(valor1)
     nume_2_float = float (valor2)
     numero_valido = True
    except:
        numero_validos = None

        if numero_validos is None:
            print('Um ou Ambos numeros são invalidos')
            continue
        operador_permitido ='+-/*'
        if operador not in operador_permitido:
            print('Operador invalido')
            continue
        if len(operador) >1 :
            print('Apenas um operador')
            continue

    sair = input('quer sair? [s]im:'). lower( ).startswith('s')
    if sair is True:
        break
    
    print(sair)