"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
primeiro_nome = input("Digite seu primeiro nome: ")
tamanho_nome = len(primeiro_nome)

if tamanho_nome <= 4:
    print("Seu primeiro nome é curto")
elif tamanho_nome in [5, 6]:
    print("Seu primeiro nome é normal")
elif tamanho_nome > 6:
    print("Seu primeiro nome é grande")
else:
    print("Algo deu errado!")