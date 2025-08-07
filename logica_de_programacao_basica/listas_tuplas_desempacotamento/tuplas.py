"""
Tipo Tupla - uma lista imutável
"""
frutas = 'Maçã', 'Banana', 'Mamão'
frustas_list = list(frutas)
frustas_list.append('Goiaba')
frutas2 = tuple(frustas_list)
print(f'A Tupla original é: {frutas}'
      '\n'
      f'A tupla virou lista e foi adicionado um novo ítem: {frustas_list}'
      '\n'
      f'A lista de frutas virou tupla de novo: {frutas2}')