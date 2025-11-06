###############################################
#
# Escopos e Namespaces
# ** PARTE 2~
# ** A regra LEGB e como o Python a usa para resolver nomes~
# ** Modificar o comportamento do Python com `global` e `nonlocal`~
# ** PARA NERDS - varnames, freevars e cellvars~

# Certo ✅: Local --> Enclosing --> Global --> Built-In --> NameError ¬
# Errado ❌: Built-In --> Global --> Enclosing --> Local

# De nenhum escopo externo é possível usar algo de escopo interno

##############################################

variavel_global = "Variável Global"

def a_funcao_global() -> None:
    variavel_enclosing_da_funcao = "Variável Enclosing da função"
    
    def funcao_enclosing_da_funcao_global() -> None:
        variavel_local_da_funcao_enclosing = "Sou a variável local da função enclosing"
        