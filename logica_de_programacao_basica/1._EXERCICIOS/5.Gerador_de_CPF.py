import random
for _ in range(100):
      nove_digitos = ''
      for i in range(9):
            nove_digitos += str(random.randint(0, 9))
      contador_regressivo_d1 = 10
      contador_regressivo_d2 = 11

      resultado_d1 = 0
      resultado_d2 = 0

      for digito in nove_digitos:
            resultado_d1 += int(digito) * contador_regressivo_d1
            contador_regressivo_d1 -= 1

      digito_1 = (resultado_d1 * 10) % 11
      digito_1 = digito_1 if digito_1 <= 9 else 0

      dez_digitos = nove_digitos + str(digito_1)

      for digito in dez_digitos:
            resultado_d2 += int(digito) * contador_regressivo_d2
            contador_regressivo_d2 -= 1

      digito_2 = (resultado_d2 * 10) % 11
      digito_2 = digito_2 if digito_2 <= 9 else 0

      cpf_gerado = nove_digitos + str(digito_1) + str(digito_2)

      print(cpf_gerado) 