####################################################################
# O que é escopo
#
# Escopo é a região do código onde um nome está diretamente acessível.
# Ele determina os limites e o tempo de vida dos nomes definidos internamente.
#
# Escopo é usado para encapsular o código e evitar colisões de nomes e efeitos
# colaterais indesejados.
#
# O Python tem quatro tipos de escopos: Built-In, Global, Enclosing e Local.
# Esses escopos são dinâmicos. O interpretador pode criar e apagar em tempo de
# execução.
#
# Cada escopo tem seu "espaço de nomes" (namespace), que é um local onde os
# nomes e seus respectivos objetos são armazenados.
#######################################################################


# nome definido no espaço global
um_nome = "um_nome (GLOBAL)"

def func_global(sou_local:str) -> None:
    um_nome = "um_nome (LOCAL)"
    outro_nome = "outro_nome (LOCAL)"
    print("LOCALS (namespace da função)")
    print(locals())
    print()
    
    # Parâmetros de funções também são do escopo local da função
    print(f"Dentro da função: {um_nome}, {outro_nome}, {sou_local}")
    
func_global('sou_local')

# ISSO NÃO FUNCIONA
# print(outro_nome, sou_local)

# Isso é injetado automaticamente pelo Python no escopo global
print("Nome do módulo:", __name__)
print("Arquivo do módulo:", __file__)
print("Documentação do módulo:", __doc__)
print()

######################################################################

# O que é namespace?
#
# Namespace é uma estrutura de dados real que mapeia nomes para objetos.
# Cada chave é o nome que você define e o valor é o objeto correspondente no seu código.
# Sempre que você cria um nome, essa associação é guardada dentro de um namespace
#
# Vamos usar globals() e locals() no mesmo código anterior e confirmar isso.
#
# globals(): Retorna um dicionário que representa o namespace global do módulo atual.
#   - Isso inclui todos os noems definidos na raiz do arquivo.
#
# locals(): Retorna um dicionário com os nomes definidos no escopo local onde a função está sendo executada.
#   - Importante: ela só inclui nomes que já foram definidos antes da sua chamada.

######################################################################

