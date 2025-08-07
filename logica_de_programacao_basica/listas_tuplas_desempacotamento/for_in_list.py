"""
lista_a = ['Wanderson', 'João', 'Pedro']

for nome in lista_a[0]:
    print(nome, type(nome))
print('\n')
for nome in lista_a[1]:
    print(nome, type(nome))
print('\n')
for nome in lista_a[2]:
    print(nome, type(nome))
print('\n')
"""

lista = ['Arroz', 'Feijão', 'Macarrão', 'Frango']
lista.append('João')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))