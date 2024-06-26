import os
os.system('cls')
## sempre usar para limpar o terminal ##

# interpolação basica de string
# s - string
# d e i - int
# f  - float
# x e X --hexadecimal  (abcdef0123456789)
# > - Esquerda
# < -- Direita
# ^ -- centro
# sinal .... + ou -
# ex. : 0>-100,.1f
#conversion flags - !r..... !s.... !a......

variavel = 'abc'

print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{-5000.0000:+,.1f}')
print()