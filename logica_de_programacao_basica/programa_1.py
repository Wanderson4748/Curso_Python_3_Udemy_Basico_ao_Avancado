"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# PAR OU IMPAR?
 
entrada = input("Digite um número inteiro:")
is_digit = entrada.isdigit()

def par_ou_impar():
    if entrada % 2 == 0:
        return "Par"
    else:
        return "ímpar"

if is_digit:
    entrada = int(entrada)
    resultado = par_ou_impar()
    print(f"O número {entrada} é {resultado}")
else:
    print("Você não digitou um numero inteiro")