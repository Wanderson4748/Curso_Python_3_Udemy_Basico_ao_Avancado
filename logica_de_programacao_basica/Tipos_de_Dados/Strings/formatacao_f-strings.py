"""Formatação Básica de strings
f - float

"""
variavel = 'ABC'
print(f'{variavel: <15}')
print(f'{variavel: >15}')
print(f'{variavel:$^15}')
print(f"{1000.45456456456:0=+10,.1f}")
print(f"O hexadecimal de 1500 é {1500:08x}")