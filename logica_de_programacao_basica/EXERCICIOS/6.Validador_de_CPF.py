"""
Um problema que pode acontecer no validador de CPF é o seguinte: o usuário entra um CPF com caracteres repetidos ou inválidos.

Solução:
Faça um programa que corrija isso.
"""
import re
import sys
import os

os.system('cls')

print('Seja Bem Vindo ao Validador de CPF!\n')
entrada = input('Digite o CPF: ')
cpf = re.sub(r'[^0-9]', '', entrada) 
# Remove tudo que não for número

"""cpf = '62.096706360'\
    .replace('.', '')\
    .replace('-', '')\
    .replace(' ', '')"""

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    sys.exit('Você digitou dados sequenciais. Encerrando...')
nove_digitos = cpf[:9]
dez_digitos = cpf[:10]
contador_regressivo_d1 = 10
contador_regressivo_d2 = 11

resultado_d1 = 0
resultado_d2 = 0

for digito in nove_digitos:
      resultado_d1 += int(digito) * contador_regressivo_d1
      contador_regressivo_d1 -= 1

digito_1 = (resultado_d1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

for digito in dez_digitos:
      resultado_d2 += int(digito) * contador_regressivo_d2
      contador_regressivo_d2 -= 1

digito_2 = (resultado_d2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = nove_digitos + str(digito_1) + str(digito_2)

if cpf_gerado == cpf:
      print(f'o CPF {cpf} é válido.')
else:
      print(f'o CPF {cpf} é inválido.')