idProduct = 0
qntProduct1 = 10
qntProduct2 = 10
qntProduct3 = 10
qntProduct4 = 10
qntProduct5 = 10
selectedProduct = ""
qntCentavos5 = 0
qntCentavos10 = 0
qntCentavos25 = 0
qntCentavos50 = 0
qntNota1 = 0
qntNota2 = 0
qntNota5 = 0
qntNota10 = 0
qntNota20 = 0
qntNota50 = 0
qntNota100 = 0


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
    print()
    print("-----------------------------------")
    print("Número|  Bebida          | Quantidade")
    print("  1   |  Coca-Cola       |   ", qntProduct1)
    print("  2   |  Fanta Uva       |   ", qntProduct2)
    print("  3   |  Fanta Laranja   |   ", qntProduct3)
    print("  4   |  Sprite          |   ", qntProduct4)
    print("  5   |  Água mineral    |   ", qntProduct5)
    print("-----------------------------------")
    print()
    print("A máquina está com as seguintes notas:")
    print()
    print("-----------------------------------")
    print("Nota R$ | Quantidade | R$ Total")
    print("  0,05  |     {}     |    {:.2f}".format(qntCentavos5, qntCentavos5 * 0.05))
    print("  0,10  |     {}     |    {:.2f}".format(qntCentavos10, qntCentavos10 * 0.1))
    print("  0,25  |     {}     |    {:.2f}".format(qntCentavos25, qntCentavos25 * 0.25))
    print("  0,50  |     {}     |    {:.2f}".format(qntCentavos50, qntCentavos50 * 0.50))
    print("  1,00  |     {}     |    {:.2f}".format(qntNota1, qntNota1 * 1))
    print("  2,00  |     {}     |    {:.2f}".format(qntNota2, qntNota2 * 2))
    print("  5,00  |     {}     |    {:.2f}".format(qntNota5, qntNota5 * 5))
    print("  10,00 |     {}     |    {:.2f}".format(qntNota10, qntNota10 * 10))
    print("  20,00 |     {}     |    {:.2f}".format(qntNota20, qntNota20 * 20))
    print("  50,00 |     {}     |    {:.2f}".format(qntNota50, qntNota50 * 50))
    print("  100,00|     {}     |    {:.2f}".format(qntNota100, qntNota100 * 100))
    print("-----------------------------------")
    print("A máquina possui R$ {:.2f}".format(qntCentavos5 * 0.05 +
          qntCentavos10 * 0.1 + qntCentavos25 * 0.25 + qntCentavos50 * 0.50 +
          qntNota1 * 1 + qntNota2 * 2 + qntNota5 * 5 + qntNota10 * 10 +
          qntNota20 * 20 + qntNota50 * 50 + qntNota100 * 100))
    print()

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
