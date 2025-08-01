palavra_secreta = 'Perfume'
palavra_atual = '*' * len(palavra_secreta)
tentativas = 0

while '*' in palavra_atual:
    letra = input('Digite uma letra: ').lower()
    nova_palavra = ''
    
    for i in range(len(palavra_secreta)):
        if letra == palavra_secreta[i]:
            nova_palavra += letra
        else:
            nova_palavra += palavra_atual[i]