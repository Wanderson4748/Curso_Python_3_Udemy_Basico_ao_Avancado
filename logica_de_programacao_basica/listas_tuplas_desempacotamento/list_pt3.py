""" 
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
    Métodos úteis: 
        append - acrescenta um valor no ultimo indice da lista
        insert - insere um valor em um índice da lista
        pop - remove o valor do ultimo índice da lista
        del - remove o valor em um índice da lista
        clear - remove todos os valores da lista
        extend - estende a lista
        + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_c, lista_d)