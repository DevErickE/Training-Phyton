"""

idade = 0
altura = 0.00
nome = ''

nome = str(input("Digite sua nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))


print(f"O {nome} tem {idade} anos e sua altura é de {altura : .2f}")

"""

# Declare quatro variáveis, id, do tipo inteiro, nome, do tipo string,
# salário, do tipo float e a variável brasileiro do tipo bool.
# Peça para que o usuário informe os dados acima.
# Ao final, imprima tudo na tela utilizando f-strings.


id = int(input("Informe o ID: "))
nome = str(input("Informe seu nome: "))
salario = float(input("Informe seu salário: "))
brasileiro = input("você É brasileiro?(sim ou não): ").strip().lower() == "sim"


print(f"ID - {id}")
print(f"nome - {nome}")
print(f"salario - {salario}")
print(f"basileiro - {brasileiro}")
