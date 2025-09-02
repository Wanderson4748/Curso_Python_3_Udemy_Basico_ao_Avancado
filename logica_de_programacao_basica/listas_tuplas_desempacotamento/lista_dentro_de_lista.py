"""
Lista de listas e seus índices
"""

salas = [
    # 0        1
    ['Maria', 'Helena',], # 0

    # 0
    ['Elaine', ], # 1

    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20)], # 2

]
"""
print(salas[0][1]) # Helena
print(salas[1][0]) # Elaine
print(salas[2][2]) # Eduarda
print(salas[2][3][2]) # 20
"""
for sala in salas:
    print(f'Sala: {sala}')
    for item in sala:
        print(f'Item: {item}')