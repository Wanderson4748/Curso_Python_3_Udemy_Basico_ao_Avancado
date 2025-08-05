"""
enumerate - enumera iteráveis (índices)
"""
tupla = 'Wanderson', 'Tiago', 'Josué'
lista1 = list(tupla)
lista1.append('lista1')
lista2 = list(tupla)
lista2.append('lista2')
lista3 = list(tupla)
lista3.append('lista3')

print('O valor da lista1 é', lista1
      ,'\n')
print('O valor da lista2 é', lista2
      ,'\n')
print('O valor da lista3 é', lista3
      ,'\n')

lista_enumerada1 = enumerate(lista1, start=10)
print('A lista1 enumerada é:')
print(next(lista_enumerada1))
print(next(lista_enumerada1))
print(next(lista_enumerada1))
print('\n')

lista_enumerada2 = list(enumerate(lista2, start=1))
print('A lista_enumerada2 é:', lista_enumerada2)
for item in lista2:
    print('\n')
    print(item)
print('\n')
   
lista_enumerada3 = list(enumerate(lista3, start=1))
print('A lista_enumerada3 é:', lista_enumerada3)
indice_le3 = range(len(lista_enumerada3))

for i in indice_le3:
    if lista3[i] == 'lista3':
        print(f'O item: {lista3[i]} está no índice: {i}')
print('\n')

lista4 = ['Wanderson', 'Tiago', 'Josué']
lista4.append('lista4')

for indice, nome in enumerate(lista4):
    print(indice, nome)