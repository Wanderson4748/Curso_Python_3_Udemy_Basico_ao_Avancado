""" 
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +

Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

# append - adicionar valor ao final
# pop - remove o ultimo valor ao final
# insert - inserir um valor em um índice da lista

# insert(100000, 'valor') - insere no ultimo indice possivel da lista
# append('valor') - insere no ultimo indice

"""

lista = [10, 20, 30, 40]
lista.append(99)
lista.append(100)
lista.append(101)
lista.pop()
del lista[0]
lista.insert(1, 'Wanderson')
#lista.clear()

print(lista)