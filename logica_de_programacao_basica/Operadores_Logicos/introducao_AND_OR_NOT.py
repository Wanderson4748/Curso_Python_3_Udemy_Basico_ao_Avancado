entrada = input("[E]ntrar [S]air ")
senha_digitada = input("Senha: ")

senha_permitida = "123456"

if not entrada == "E" or "e" and senha_digitada == senha_permitida:
    print("Entrar")

else:
    print("Sair")