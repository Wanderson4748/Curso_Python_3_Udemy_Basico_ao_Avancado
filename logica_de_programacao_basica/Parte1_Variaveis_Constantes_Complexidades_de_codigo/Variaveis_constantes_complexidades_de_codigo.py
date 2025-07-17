"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = input("Você está dirigindo na rodovia, deseja andar a qual velocidade? Detalhe, tem um radar a 2 quilometros, pode digitar: ") # Velocidade Atual do Carro
velocidade = int(velocidade)
local_carro = 109 # Local em que o carro está na estrada

RADAR_2 = 85 # Velocidade máxima do radar 2
LOCAL_RADAR_2 = 110 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

if velocidade > RADAR_2:
    print("Velocidade do carro passou do radar 2")

if local_carro >= (LOCAL_RADAR_2 - RADAR_RANGE) and \
    local_carro <= (LOCAL_RADAR_2 + RADAR_RANGE) and \
        velocidade > RADAR_2:
    print("Carro multado em radar 2")
else:
    print("Você passou dentro da velocidade correta no radar!")