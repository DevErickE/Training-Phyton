'''
Crie um programa que peça para que o usuario informe  um
número inteiro compreendido entre 1 e 7.
*   Imprima ""domingo". caso o número seja  1;
*   Imprima "segunda-feira", caso o número seja 2;
*   Imprima "terça-feira", caso o número seja 3; 
    ...
*   Imprima "sábado",caso o número seja 7;
*   Imprima "número inválido", caso o número não esteja
    compreendido no intervalo de 1 a 7.
'''

print("\nDias da Semana!\n")

number = int(input("Digite um número de (1  a 7): "))

if number == 1:
    print("\nDomingo\n")
elif number == 2:
    print("\nSegunda-Feira.\n")
elif number == 3:
    print("\nTerça-Feira.\n")
elif number == 4:
    print("\nQuarta-Feira.\n")
elif number == 5:
    print("\nQuinta-Feira.\n")
elif number == 6:
    print("\nSexta-Feira.\n")
elif number == 7:
    print("\nSábado.\n")
else:
    print("\nDigito Inválido.\n")

'''
Crie um programa que receba um número inteiro de 1
a 12. Imprima, por extenso, o nome do respctivo mês 
de acordo com o calendário.  Por exemplo, se o
número for  1, então  imprima  "janeiro", na tela. Imprima
"mês inválido", caso o número informado não esteja  
compreendido entre 1 e 12.
'''

print("\nMeses do Ano!\n")

number = int(input("Digite um número de (1  a 12): "))

if number == 1:
    print("\nJaneiro\n")
elif number == 2:
    print("\nFevereiro.\n")
elif number == 3:
    print("\Março.\n")
elif number == 4:
    print("\nAbril.\n")
elif number == 5:
    print("\Maio.\n")
elif number == 6:
    print("\nJunho.\n")
elif number == 7:
    print("\nJulho.\n")
elif number == 8:
    print("\nAgosto.\n")
elif number == 9:
    print("\nSetembro.\n")
elif number == 10:
    print("\nOutubro.\n")
elif number == 11:
    print("\nNovembro.\n")
elif number == 12:
    print("\nDezembro.\n")
else:
    print("\nDigito Inválido.\n")
