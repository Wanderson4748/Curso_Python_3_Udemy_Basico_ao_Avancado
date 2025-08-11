import decimal

numero_1 = 0.1
numero_2 = 0.70
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))

numero_4 = decimal.Decimal('1.5')
numero_5 = decimal.Decimal('1.1')
numero_6 = numero_4 + numero_5

print(numero_6)