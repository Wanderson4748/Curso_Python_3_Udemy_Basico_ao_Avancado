"""
split e join com list e str
split - divide uma stirng
join - une uma string
"""
frase = 'Jesus, o caminho, a verdade e a vida'
lista_frases = frase.split(',')

for i,frase in enumerate(lista_frases):
    lista_frases[i] = lista_frases[i].strip()

print(lista_frases)