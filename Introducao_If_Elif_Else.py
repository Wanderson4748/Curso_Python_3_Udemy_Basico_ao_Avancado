entrada = input("Quanto que é 87 + 34: ")
entrada = float(entrada)
tipo_entrada = type(entrada)

if entrada == int(121):
    print(f"{entrada}? Resposta Correta.")
    
elif tipo_entrada == type(float):
    print("Que resposta ruim")

elif entrada < int(121):
    print(f"{entrada}? Voce errou, o resultado é maior.")

elif entrada > int(121):
    print(f"{entrada}? Voce errou, o resultado é menor.")