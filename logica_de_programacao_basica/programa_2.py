"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input("Olá, Tudo bem? Gostaria de saber que horas são agora, por favor: ")
verif_dia = entrada[0:2]
bom_dia = ["0","1","2","3","4","5","6","7","8","9","10","11"]
boa_tarde = ["12","13","14","15","16","17"]
boa_noite = ["18","19","20","21","22","23"]

if verif_dia in bom_dia:
    print("Bom dia")
elif verif_dia in boa_tarde:
    print("Boa tarde")
elif verif_dia in boa_noite:
    print("Boa noite")
else:
    print("Você não digitou as horas corretamente")