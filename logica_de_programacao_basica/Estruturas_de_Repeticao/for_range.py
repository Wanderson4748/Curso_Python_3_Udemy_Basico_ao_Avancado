"""
For + Range
range -> range(start, stop, step)
"""
for i in range(10):
    print(i)
    if i == 2:
        print('i é 2, pulando...')
        continue
    
    if i == 8:
        print('i é 8, seu else não executará')
        break
    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso')

"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""