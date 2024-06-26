import os
os.system('cls')
##sempre usar para limpar o terminal ##

# Operadores logicos 
# AND e igual a....... E    
# OR e igual a ...... OU 
# NOT e igual a........ NÃO
# (todas as condições precisam ser verdadeiras)
# se qualquer valor for considerado falso, a expressao inteira será avaliada naquele valor
# são considerados falsy 0 0.0 '' false
# tambem existe o tipo none que é usado para representar um não valor.


entrada = input('[E]ntrar ou [S]sair: ' )

senha_digitada = input('senha:')

senha_permitida = '1234'

if (entrada == 'E' or entrada == 'e' ) and senha_digitada == senha_permitida:
      print('Entrar')
else:
    print('Sair')