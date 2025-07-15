"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
    Se nada for digitado em nome ou idade:
        exiba "Desculpe, você deixou campos vazios."
"""

nome = str(input("Digite seu nome: "))
idade = str(input("Digite sua idade: "))
nome_invertido = nome[::-1]

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome_invertido}")
    
    if " " in nome:
        print(f"Seu nome {nome} contém espaços")
    else:
        print(f"Seu nome {nome} não contém espaços")
    
    print(f"Seu nome {nome} tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    

else:
    print("Desculpe, você deixou os campos vazios")