"""
O def é usado para definir uma função

def nome_da_funcao(parametros):
    bloco de código

nome_da_funcao(argumentos)
"""

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)