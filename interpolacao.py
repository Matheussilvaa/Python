import os
os.system('cls')
## sempre usar para limpar o terminal ##


# interpolação basica de string
# s - string
# d e i - int
# f  - float
# x e x --hexadecimal  (abcdef0123456789)

nome = 'matheus'
idade = 28.05
variavel = '%s, a sua idade é %.2f' %(nome, idade)

print(variavel )
print('o hexadecimal de %d e %x'%(15,15))