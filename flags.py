import os
os.system('cls')
## sempre usar para limpar o terminal ##

# flag (bandeira) - marca um local
# none = não valor
# is e is not = é ou não é (tipo, valor , identidade)
# id = identidade

condicao= True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faça algo')
else:
    print('não faça algo ')
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)