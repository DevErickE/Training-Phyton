# Aplicando todas as palavras reservadas do Phyton

# Exercício - Projeto Completo "Sistema de Aventura Python"

"""
Regras:
Você precisa obrigatoriamente:

Criar funções (def)
Usar estruturas de decisão (if, elif, else)
Repetição (while, for)
Manipular listas ou objetos (class)
Fazer importação de módulos (import random)
Usar exceções (try, except, raise)
Mostrar o uso de break e continue
Criar funções anônimas (lambda)
Usar global e nonlocal
Usar True, False, None
Trabalhar com and, or, not, is, in
Criar classes com pass e assert
Testar conceitos de escopo com with
Trabalhar com funções assíncronas (async, await)
Usar yield para gerar valores
Utilizar palavras como from e as

"""
nome  = str()
escolha = ''

print("\nSistema de Aventura Python")

nome = input("\nDigite seu nome jogador: ")

while len(nome) < 5:  #len() limita os caracteres, inserir dentro do () o apelido da
    print("Crie um nome com no mínimo 5 caracteres")
    nome = input("\nDigite seu nome jogador: ")

print(f"\nVamos iniciar sua jornada {nome}\n")    

print("Bravo jogador voce acabou de acordar e percebe que sua casa esta sendo invadida por zumbis" \
"comedores de cerebros qual a melhor opção para sair desta situação?")

print("\nA) Pegar um machado e começar a bater em todos eles")
print("B) Ir para o porão e trancar a porta")

escolha = input("\nEscolha A ou B: ")

while escolha != 'A' and escolha != 'B' and escolha != 'a' and escolha != 'b':
    print("\nEscolha inválida! Digite apenas A ou B.\n")
    escolha = input("Escolha A ou B: ")

if escolha == 'A' or escolha == 'a':
    print("\nOpção A - Você pegou o machado, porém não teve tanta sorte, pois eram muitos zumbis e você acabou morrendo :(\n")

if escolha == 'B' or escolha == 'b':
    print("\nOpção B - Você vai em direção ao porão e consegue trancar a porta. Por lá você começa "
          "a criar alguma estratégia para sair da casa e fugir deste apocalipse zumbi.\n") 
    

print("")

