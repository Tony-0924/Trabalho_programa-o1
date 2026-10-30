
print("PROGRAMA FRUTAS")

nome = input("Nome do ficheiro a ler/escrever: ")

frutas = []

try:
    with open(nome, "r", encoding="utf-8") as ficheiro:
        frutas = ficheiro.readlines()
    print('Ficheiro "' + nome + '" carregado!')
except FileNotFoundError:
    print("O ficheiro ainda não existe.")

opcao = -1

while opcao != 0:
    print("Opções:")
    print("1) Ler o ficheiro")
    print("2) Acrescentar ao ficheiro")
    print("3) Criar/Sobrescrever o ficheiro")
    print("0) Sair")

    opcao = int(input("> "))

    if opcao == 1:
        try:
            with open(nome, "r", encoding="utf-8") as ficheiro:
                frutas = ficheiro.readlines()

            for fruta in frutas:
                print(fruta.strip())

        except FileNotFoundError:
            print("O ficheiro não existe!")

    elif opcao == 2:
        fruta = input("Nome da fruta: ")

        with open(nome, "a", encoding="utf-8") as ficheiro:
            ficheiro.write(fruta + "\n")

        frutas.append(fruta + "\n")
        print("Fruta acrescentada!")

    elif opcao == 3:
        frutas = []
        quantidade = int(input("Quantas frutas deseja guardar? "))

        for i in range(quantidade):
            fruta = input("Fruta " + str(i + 1) + ": ")
            frutas.append(fruta + "\n")

        with open(nome, "w", encoding="utf-8") as ficheiro:
            ficheiro.writelines(frutas)

        print("Ficheiro criado/sobrescrito!")

    elif opcao == 0:
        print("Programa terminado!")

    else:
        print("Opção inválida!")
