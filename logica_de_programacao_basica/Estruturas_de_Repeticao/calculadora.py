<<<<<<< HEAD
""" Calculadora com while """

# Pedir o primeiro numero, segundo numero e um operador (adição, subtração, multiplicação e divisão)

while True:
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    print(sair)
"""
primeiro_numero = float(input('digite o primeiro numero: '))
segundo_numero = float(input('Digite o segundo numero: '))
operador = 
"""
=======
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+=/*): ')

    numeros_validos = None
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números estão inválidos')
        continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
>>>>>>> 6a03e5ea00df3ff462095dc90fea9c7a3464d773
