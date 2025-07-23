"""
Iterando strings com while
"""
#       012345678910
nome = 'Wanderson Sousa' # Iteráveis
indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += letra
    indice += 1
    
print(novo_nome)