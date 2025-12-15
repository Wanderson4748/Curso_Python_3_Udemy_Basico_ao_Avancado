perguntas = [
    {
        'pergunta': 'Quanto é 8*8?',
        'opções': [0, 1, 40, 64],
        'resposta': '64',
    },
    {
        'pergunta': 'Quanto é 5*9?',
        'opções': [10, 78, 45, 21],
        'resposta': '45',
    },
]

print('Perguntas e resposta com o Wan Wan')

for item in perguntas:
    print(item['pergunta'])
    print("Opções:", item['opções'])

    resposta = input(f"Sua resposta:")

    if resposta == item['resposta']:
        print("✔ Acertou!\n")
    else:
        print("❌ Errou!\n")