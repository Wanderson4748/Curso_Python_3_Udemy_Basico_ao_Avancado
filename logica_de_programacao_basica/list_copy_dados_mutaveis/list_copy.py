"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Wanderson', 'Sousa']
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a, lista_b)