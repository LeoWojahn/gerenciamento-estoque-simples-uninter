import os

# Loop para servir como menu, onde ele sempre espera uma opção das abaixo. Caso contrário, retorna ao usuário para escolher uma dessas opções.
while True:
    print("")
    print("Adicionar Produto      [1]")
    print("Adicionar Funcionário  [2]")
    print("Entrada de Produto     [3]")
    print("Saída de Produto       [4]")
    print("Movimentações          [5]")
    print("Sair                   [6]")

    opcao = str(input("Digite uma opção [Nº]: "))

    if opcao not in ["1", "2", "3", "4", "5", "6"]:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Por favor, digite o número referente a opção!")

    if opcao == "6":
        break