"""
Crie um programa que imprima, na tela, os números inteiros de
1 a 10. Para isso, utilize uma estrutura de repetição do tipo
while. A invocaçãao da sua  operação  de saída de dados não  pode
imprimir os valores literalmente:   é preciso que  o print sempre
imprima o conteúdo  de  alguma variável, dentro de um laço, para
que  a automação da  solução faça sentido.           
"""

num =  1

while num <= 10:

    print(f"{num} ", end = "")
    
    num += 1 



""""
1 - Crie um programa que imprima os números inteiros de 10 a 1. 
Ou seja, deve-se imprimir em ordem decrescente, iniciando em 10 
e encerrando em 1. Utilize o while.

2 - Crie um programa que continue pedindo, repetidas vezes, para que
o usuário insira um número qualquer. O programa deve se encerrar 
somente quando o usuário inserir o valor 0 (zero).
"""

#ex1
num_dec = 10

print("\nex1")
while num_dec >= 1:

    print(f"{num_dec} ", end = "")
    
    num_dec -= 1 

#ex2
print("\n\nex2")
number_0 = int(input("Digite o número 0: "))

while number_0 !=  0:
    print("\nDigite o número 0")
    number_0 = int(input("\nDigite o número 0: "))

if number_0 == 0:
    print("\nNúmero correto\n")
