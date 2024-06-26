import os
os.system('cls')
##sempre usar para limpar o terminal ##


# o if pode ser feito sozinho, mas o elif e o else depende do if para sobreviver.

condicao = False
condicao1 = True
condicao2 = False
condicao3 = True
condicao4 = False

#pode ser utilizado a quantidade de elif que eu quiser dentro do codigo 

if condicao:
    print('Este é o código do if')

elif condicao1: #este e um exmplo de varios elif dentro do if
    print('codigo para condição 1')
elif condicao2:  #este e um exmplo de varios elif dentro do if
    print('condição 2')
elif condicao3:  #este e um exmplo de varios elif dentro do if
    print('codigo para condição 3')
elif condicao4:   #este e um exmplo de varios elif dentro do if
    print(' condição 4')
    
else:
    print('nem uma condição foi satisfeita ')

print('FORA DO IF')