# len
pessoa = {
    'nome': 'Wanderson',
    'sobrenome': 'Miranda',
    #'idade': 900,
}
print(len(pessoa))

##############################################################
# keys
print(pessoa.keys())

for chave in pessoa.keys():
    print(chave)

##############################################################
# values
print(pessoa.values())

for valores in pessoa.values():
    print(valores)

##############################################################
# items
print(pessoa.items())

for chave, valor in pessoa.items():
    print(f"Chave: {chave}, Valor: {valor}")

##############################################################
# setdefault
pessoa.setdefault('idade', 0)
print(pessoa['idade'])

##############################################################
# Shallow Copy e Deep Copy
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 999999

print(d1)
print(d2)

################################################################
# get
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
print(p1.get('nome'))

###############################################################
# pop
p2 = {
    'nome': 'Wanderson',
    'sobrenome': 'Sousa',
}

nome = p2.pop('nome')
print(nome)
print(p2.get('nome'))
print(p2)

###############################################################
# popitem

p3 = {
    'nome': 'Carlos',
    'sobrenome': 'José',
}

ultima_chave = p3.popitem()
print(p3)
print(ultima_chave)

##################################################################
# update
p1.update({
    'nome': 'novo valor',
    'idade': 30,
})
print(p1)

p1.update(nome='novo outro valor', idade=31)
print(p1)