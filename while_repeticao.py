import os
os.system('cls')
## sempre usar para limpar o terminal ##

# repetições
# while (enquanto)
# executa uma ação enquanto uma condição for verdadeira
# loop infinito -> e quando um codigo não tem fim !
#qtd_linhas = 5
#qtd_colunas = 5

#linha = 1
#coluna = 1

#while linha <= qtd_linhas :
 
# while coluna <= qtd_colunas:
#  print()
#  print(f'{linha =} {coluna = }')
 # coluna += 1  
  #linha += 1 
  
   

#print('cabou')


qtd_linhas = 5
qtd_colunas = 5

linha = 1 

while linha <= qtd_linhas:
   coluna = 1
   while coluna <= qtd_colunas:
      print(f'{linha = } {coluna = }')
      coluna += 1
   linha += 1      
      
print(f'Acabou') 