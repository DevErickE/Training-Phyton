# Crie um programa que peça ao usuário que informe dois numeros
# Calcule a soma, subtração, multiplicacao e divisão, ao final imprima os resultados
# OBS: imprimirá também o resto da divisão

print("\nCálculo das Operações Aritiméticas\n")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print(f"\nResultado da soma: {soma}")
print(f"Resultado da subtracao: {subtracao}")
print(f"Resultado da multiplicacao: {multiplicacao}")
print(f"Resultado da divisao: {divisao}")
print(f"Resto da divisão: {resto}")

# Criar uma variavel inteira e dessa variável, imprimirá 2 coisas:
# incrementa a essa variavel em 1 unidade e decrementa em 1 unidade.

print("\nResultado de Incremento e Decremento")
a = 20
incremento = a + 1
decremento = a - 1

print(f"\nvalor incrementado: {incremento}")
print(f"valor decrementado: {decremento}")



# Usuário informa 3 numeros com casas decimais
# Calcula a  média entre esses 3 números e mostra
# O resultado na tela, so mostrando 2 casas decimais

print("\nMedia entre 3 notas!")
a = float(input("\nDigite o primeiro nota: "))
b = float(input("Digite o segundo nota: "))
c = float(input("Digite o terceiro nota: "))

media = (a + b + c) / 3

print(f"\nA media entre essas notas é: {media}\n")
