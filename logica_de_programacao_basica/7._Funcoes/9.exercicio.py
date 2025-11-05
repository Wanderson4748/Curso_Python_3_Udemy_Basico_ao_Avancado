# Exercicios
# Crie funções que duplicam, triplicam e quadriplicam
# O número recebido com parâmetro.

# Criação das funções
def duplica_num(numero: float) -> None:
    num_duplicado = numero * 2
    print(num_duplicado)
    
def triplica_num(numero: float) -> None:
    num_triplicado = numero * 3
    print(num_triplicado)
    
def quadriplica_num(numero: float) -> None:
    num_quadriplicado = numero * 4
    print(num_quadriplicado)

# Execução das funções 
duplica_num(3)
triplica_num(3)
quadriplica_num(4)

# OUTRA FORMA

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))
