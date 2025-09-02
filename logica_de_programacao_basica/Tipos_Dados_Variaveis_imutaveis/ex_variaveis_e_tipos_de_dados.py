import datetime
nome = str("Wanderson")
sobrenome = str("Sousa Rodrigues")
idade = int(20)
ano_nascimento = datetime.datetime.today().year - idade
maior_de_idade = idade >= 18
altura_metros = float(1.67)

if maior_de_idade:
    maior_de_idade = "Sim"
else:
    maior_de_idade = "Não"

print(f"Nome: {nome}\nSobrenome: {sobrenome}\nIdade: {idade}\nAno de nascimento: {ano_nascimento}\nÉ maior de idade? {maior_de_idade}\nAltura em metros: {altura_metros}")