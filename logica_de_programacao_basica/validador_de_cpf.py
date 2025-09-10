"""
CPF: 620.967.063-60
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começaando de 10

Ex:   620.967.063-60 (62096706360)
      10  9  8  7  6  5  4  3  2
*     6   2  0  9  6  7  0  6  3
      60  18 0  63 36 35 0  18 6

Somar todos os resultados:
60+18+63+36+35+18+6 = 236

multiplica por 10
236x10 = 2360

resto da divisao por 11
6

Se maior que 9 o resultado é 0
ao contrario disso o resultado é valor da conta
"""
cpf = '62096706360'
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
