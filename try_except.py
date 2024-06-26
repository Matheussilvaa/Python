import os
os.system('cls')
## sempre usar para limpar o terminal ##

# introdução ao try/except
# try ---> tentar executar um codigo
#except --> ocorreu algum erro ao tentar executar

#print(1234)
#print('matheus')

numero_str = input('vou dobra o numero que vc digitar ' )

try:
    print('str',numero_str)
    numero_float = float(numero_str)
    print('float', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2} ') 
except:
 print('isso não e um numero')