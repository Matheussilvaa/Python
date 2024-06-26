import os
os.system('cls')
## sempre usar para limpar o terminal ##

# CONSTANTE = "variaveis" que não vão mudar sempre e maiusculo  exemplo---> RADAR_1 = 60 
# muitas condições no mesmo if (ruim)
#<-- contagem de complexidade (ruim)

velocidade = 59 #velocidade atual do carro
local_carro = 100 # local em que o carro está  

RADAR_1 = 60 #velocidade maxima do radar 1
LOCAL_1 = 100 #Local onde esta o radar 1 
RADAR_RANGE = 1 # a distancia onde o radar pega

velocidade_carro_passou_radar1 = velocidade > RADAR_1
carro_passou_radar1 =  local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar1 = carro_passou_radar1 and velocidade_carro_passou_radar1

if velocidade_carro_passou_radar1:
    print ('o carro passou da velocidade do radar 1')
    if carro_multado_radar1:
        print('Carro foi multado no radar 1')
else:
   print(f'O carro estava na velocidade {velocidade}')
   print(f'O Carro não passou da velocidade do radar 1 que é {RADAR_1}')