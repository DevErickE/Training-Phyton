#ex1
'''
num_20 = 1

while num_20 <= 20:
    print(f"{num_20}", end = " ")
    num_20 += 1
'''
#ex2
'''
num_x = int(input("Digite qualquer número (ele será mostrado pelo programa em decrescente): "))

while num_x >= 0:
    print(f"{num_x}", end = " ")
    num_x -= 1
'''

#ex3
'''
num_0 = int(input("Digite o numero 0(todos os números digitados ao final o programa irá mostrar a soma deles): "))

sum_value = 0

while num_0  != 0:
    print("Digite 0")
    sum_value += num_0 
    num_0 = int(input("Digite o numero 0(todos os números digitados ao final o programa irá mostrar a soma deles): "))

if num_0 == 0:
    
    print(f"\nNumero correto! A soma dos números digitados é: {sum_value}\\n")
'''

#ex4
'''
password = input("\nDigite a senha correta: ")

if password != '1234':
    print("\nSenha incorreta")
    password = input("\nDigite a senha correta(a senha so contêm números): ")
while password != '1234':
    print("\nSenha incorreta")
    password = input("\nDigite a senha correta(a senha é 1234): ")
print("\nSenha correta!\n")
'''

#ex5
'''
print("\nNúmeros pares de 0 a 50\n")

even_num  = 0

while even_num <= 50:
    print(f"{even_num}",  end = ' ')
    even_num += 2
print("\n")
'''

#ex6
'''
num_exit = ''

while num_exit != '3':
    print("\nMenu de Escolhas")
    print("[1] Ver perfil")
    print("[2] Ver mensagens")
    print("[3] Sair")

    num_exit = input("Digite: ")

    if num_exit == '1':
        print("Você está no perfil.")
    elif num_exit == '2':
        print("Você está nas mensagens.")
    elif num_exit != '3':
        print("Opção inválida! Digite novamente.")

print("\nSaiu do Menu!\n")
'''