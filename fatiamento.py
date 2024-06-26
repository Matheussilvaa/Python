import os
os.system('cls')
## sempre usar para limpar o terminal ##

# fatiamento de strings
#  0 1 2 3 4 5 6 7 8
#  o l á   m u n d o
# -9 8 7 6 5 4 3 2 1
# fatiamento [i:f:p]  [::]
# [i = inicio... f = Final .... p = passo][:: = ]
# OBS: a função len retorna a quantidade de caracteres de string
#print ( len ( variavel ) )

ola = 'olá mundo'
print (ola)
print(ola[0:2]) #exemplo d fatiamento [ i = inicio... f = final ]
print (len(ola)) #exemplo len 
print (ola [0:9:2])  # exemplo do passo  
print(ola [ :: -3]) #passo para tras