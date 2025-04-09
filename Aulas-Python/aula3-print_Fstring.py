b = 10
print(b) # Imprimindo o valor 10

print(f"O valor inteiro é: {10: d}") # Conversor Decimal (base 10)
print(f"O valor inteiro é: {10: b}") # Conversor Binário (base 2)
print(f"O valor inteiro é: {10: o}") # Conversor Octal (base 8)
print(f"O valor inteiro é: {10: x}") # Conversor (base 16)

print(f"O valor inteiro é: {3.14159265: f}") # Valor de Pi
print(f"O valor inteiro é: {3.14159265: .2f}") # Valor de Pi 2 casas decimais
print(f"O valor inteiro é: {3.14159265: .3f}") # Valor de Pi 3 casas decimais

# Lição para treino
# Crie um programa que imprima, na tela, nome, idade, salário e nacionalidade de uma pessoa.
# Utilizando formatação por meio de f-strings.

nome = "João"
idade = 20
salario = 2.500
nacionalidade = "Brasileiro"
print (f"\nNome: {nome} ")
print (f"Idade: {idade} Anos")
print (f"Salário: {salario: .3f}")
print (f"Nacionalidade: {nacionalidade}")
