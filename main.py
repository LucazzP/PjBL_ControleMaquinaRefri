idProduct = 0
qntProduct1 = 10
qntProduct2 = 10
qntProduct3 = 10
qntProduct4 = 10
qntProduct5 = 10
selectedProduct = ""


def SelectProduct():
    global idProduct
    print("")
    print("-----------------------------------")
    print("Número|  Bebida          | Valor")
    print("  1   |  Coca-Cola       | R$ 3,50")
    print("  2   |  Fanta Uva       | R$ 4,00")
    print("  3   |  Fanta Laranja   | R$ 3,00")
    print("  4   |  Sprite          | R$ 4,50")
    print("  5   |  Água mineral    | R$ 2,50")
    print("-----------------------------------")
    print("")
    idProduct = int(input("Digite o número da bebida desejada: "))

    VerifyIDProduct()

def AreaAdm():
    print("Olá Administrador!")
    print("A máquina possui o seguinte estoque:")
    print("")
    print("-----------------------------------")
    print("Número|  Bebida          | Quantidade")
    print("  1   |  Coca-Cola       |   ", qntProduct1)
    print("  2   |  Fanta Uva       |   ", qntProduct2)
    print("  3   |  Fanta Laranja   |   ", qntProduct3)
    print("  4   |  Sprite          |   ", qntProduct4)
    print("  5   |  Água mineral    |   ", qntProduct5)
    print("-----------------------------------")
    print("")

def VerifyIDProduct():
    if idProduct == 996:
        # Área do admnistrador
        AreaAdm()
    elif 0 < idProduct <= 5:
        # Converção de ID para String dos produtos
        if idProduct == 1:
            selectedProduct = "Coca-Cola"
        elif idProduct == 2:
            selectedProduct = "Fanta Uva"
        elif idProduct == 3:
            selectedProduct = "Fanta Laranja"
        elif idProduct == 4:
            selectedProduct = "Sprite"
        elif idProduct == 5:
            selectedProduct = "Água Mineral"

        # Verificação bebida
        print("Você selecionou a bebida de {}, está correto ou deseja alterar?: (S/N)".format(selectedProduct))
        simOuNao = input()

        if simOuNao == "s" or simOuNao == "S":
            print("Beleza")
        else:
            SelectProduct()

    else:
        print("Você digitou um produto inválido, por favor, digite novamente o produto desejado:")
        SelectProduct()


SelectProduct()
