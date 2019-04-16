##### Variáveis #####
##master##


isRunning = True
idProduct = 0
qntProduct1 = 10
qntProduct2 = 10
qntProduct3 = 10
qntProduct4 = 10
qntProduct5 = 10
quantiaAdd = 0
produtoExtraQnt1 = 10
produtoExtraQnt2 = 10
produtoExtraQnt3 = 10
produtoExtraQnt4 = 10
produtoExtraQnt5 = 10
produtoExtraNome1 = ""
produtoExtraNome2 = ""
produtoExtraNome3 = ""
produtoExtraNome4 = ""
produtoExtraNome5 = ""
produtoExtraPreco1 = 0
produtoExtraPreco2 = 0
produtoExtraPreco3 = 0
produtoExtraPreco4 = 0
produtoExtraPreco5 = 0
nameSelectedProduct = ""
qntCentavos05 = 0
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
notaInserida = 0.0
valorTotalInserido = 0
valorBebida = 0
notaTroco = 0
valorTroco = 0
qntCentavosMaquina05 = 20
qntCentavosMaquina10 = 20
qntCentavosMaquina25 = 20
qntCentavosMaquina50 = 20
qntNotaMaquina1 = 10
qntNotaMaquina2 = 10
qntNotaMaquina5 = 10
qntNotaMaquina10 = 0
qntNotaMaquina20 = 0
qntNotaMaquina50 = 0
qntNotaMaquina100 = 0
credito = 0
cancelar = 0
notaQuantia = 0

##### Início #####

# Selecionar Bebida

while isRunning:

    valorTotalMaquina = qntCentavosMaquina05 * 0.05 + qntCentavosMaquina10 * 0.1 + qntCentavosMaquina25 * 0.25 + \
                        qntCentavosMaquina50 * 0.50 + qntNotaMaquina1 * 1 + qntNotaMaquina2 * 2 + qntNotaMaquina5 * 5 + \
                        qntNotaMaquina10 * 10 + qntNotaMaquina20 * 20 + qntNotaMaquina50 * 50 + qntNotaMaquina100 * 100

    if credito > 0:
        print("-----------------------------------------------------")
        print("A máquina está com R$ {:.2f} de créditos!! Aproveite!".format(credito))
        print("-----------------------------------------------------")
        valorTotalInserido = credito
    print()
    print("-----------------------------------")
    print("Número|  Bebida          | Valor")
    print("  1   |  Coca-Cola       | R$ 3.50")
    print("  2   |  Fanta Uva       | R$ 4.00")
    print("  3   |  Fanta Laranja   | R$ 3.00")
    print("  4   |  Sprite          | R$ 4.50")
    print("  5   |  Água mineral    | R$ 2.50")
    if quantiaAdd >= 1:
        print("  6   |  {}    | R$ {}".format(produtoExtraNome1, produtoExtraPreco1))
    if quantiaAdd >= 2:
        print("  7   |  {}    | R$ {}".format(produtoExtraNome2, produtoExtraPreco2))
    if quantiaAdd >= 3:
        print("  8   |  {}    | R$ {}".format(produtoExtraNome3, produtoExtraPreco3))
    if quantiaAdd >= 4:
        print("  9   |  {}    | R$ {}".format(produtoExtraNome4, produtoExtraPreco4))
    if quantiaAdd >= 5:
        print("  10   |  {}    | R$ {}".format(produtoExtraNome5, produtoExtraPreco5))
    print("-----------------------------------")
    print("")
    idProduct = input("Digite o número da bebida desejada: \n")

    # Verificar se é numero
    if idProduct is 1 or 2 or 3 or 4 or 5 or 996:
        idProduct = int(idProduct)
    else:
        idProduct = 404

    if idProduct == 996:  # 996 = admPassword
        # Área do admnistrador
        print("Olá Administrador!")
        print()
        print("A máquina está com as seguintes notas:")
        print()
        print("-----------------------------------")
        print("Nota R$ | Quantidade | R$ Total")
        print("  0,05  |     {}     |    {:.2f}".format(qntCentavosMaquina05, qntCentavosMaquina05 * 0.05))
        print("  0,10  |     {}     |    {:.2f}".format(qntCentavosMaquina10, qntCentavosMaquina10 * 0.1))
        print("  0,25  |     {}     |    {:.2f}".format(qntCentavosMaquina25, qntCentavosMaquina25 * 0.25))
        print("  0,50  |     {}     |    {:.2f}".format(qntCentavosMaquina50, qntCentavosMaquina50 * 0.50))
        print("  1,00  |     {}     |    {:.2f}".format(qntNotaMaquina1, qntNotaMaquina1 * 1))
        print("  2,00  |     {}     |    {:.2f}".format(qntNotaMaquina2, qntNotaMaquina2 * 2))
        print("  5,00  |     {}     |    {:.2f}".format(qntNotaMaquina5, qntNotaMaquina5 * 5))
        print("  10,00 |     {}     |    {:.2f}".format(qntNotaMaquina10, qntNotaMaquina10 * 10))
        print("  20,00 |     {}     |    {:.2f}".format(qntNotaMaquina20, qntNotaMaquina20 * 20))
        print("  50,00 |     {}     |    {:.2f}".format(qntNotaMaquina50, qntNotaMaquina50 * 50))
        print("  100,00|     {}     |    {:.2f}".format(qntNotaMaquina100, qntNotaMaquina100 * 100))
        print("-----------------------------------")
        print("A máquina possui R$ {:.2f}".format(valorTotalMaquina))
        print()
        print()
        print("A máquina possui o seguinte estoque:")
        print()
        print("-----------------------------------")
        print("Número|  Bebida          | Quantidade")
        print("  1   |  Coca-Cola       |   ", qntProduct1)
        print("  2   |  Fanta Uva       |   ", qntProduct2)
        print("  3   |  Fanta Laranja   |   ", qntProduct3)
        print("  4   |  Sprite          |   ", qntProduct4)
        print("  5   |  Água mineral    |   ", qntProduct5)
        if quantiaAdd >= 1:
            print("  6   |  {}    |   {}".format(produtoExtraNome1, produtoExtraQnt1))
        if quantiaAdd >= 2:
            print("  7   |  {}    |   {}".format(produtoExtraNome2, produtoExtraQnt2))
        if quantiaAdd >= 3:
            print("  8   |  {}    |   {}".format(produtoExtraNome3, produtoExtraQnt3))
        if quantiaAdd >= 4:
            print("  9   |  {}    |   {}".format(produtoExtraNome4, produtoExtraQnt4))
        if quantiaAdd >= 5:
            print("  10   |  {}    |   {}".format(produtoExtraNome5, produtoExtraQnt5))
        print("-----------------------------------")

        loopMenu = 1

        while loopMenu == 1:

            # Adicionando dinheiro ao caixa e produtos ao estoque
            addProduto = int(input("--------------------------------------------------------\n"
                                   "Adicionar/remover produtos ou moedas?, escolha uma opção:\n"
                                   " Opção |   Descrição \n"
                                   " 1     |   Quantia de Produtos       \n"
                                   " 2     |   Moedas \n"
                                   " 3     |   Adicionar Novos Produtos\n"
                                   " 4     |   Sair\n"
                                   "--------------------------------------------------------\n"))
            if addProduto == 4:
                loopMenu = 0

            # Adicionar Produtos
            while addProduto == 3:

                if quantiaAdd >= 5:
                    print("Numero maximo de produtos adicionados a maquina")
                else:
                    nomeProduto = str(input(" Digite o nome do produto a adicionar: \n"))
                    precoProduto = float(input("Digite o preco do produto: \n"))

                sairMenu = 0

                if quantiaAdd == 0:
                    produtoExtraNome1 = nomeProduto
                    produtoExtraPreco1 = precoProduto

                if quantiaAdd == 1:
                    produtoExtraNome2 = nomeProduto
                    produtoExtraPreco2 = precoProduto

                if quantiaAdd == 2:
                    produtoExtraNome3 = nomeProduto
                    produtoExtraPreco3 = precoProduto

                if quantiaAdd == 3:
                    produtoExtraNome4 = nomeProduto
                    produtoExtraPreco4 = precoProduto

                if quantiaAdd == 4:
                    produtoExtraNome5 = nomeProduto
                    produtoExtraPreco5 = precoProduto

                if quantiaAdd < 5:
                    quantiaAdd += 1

                print()
                print("-----------------------------------")
                print("Número|  Bebida          | Valor")
                print("  1   |  Coca-Cola       | R$ 3.50")
                print("  2   |  Fanta Uva       | R$ 4.00")
                print("  3   |  Fanta Laranja   | R$ 3.00")
                print("  4   |  Sprite          | R$ 4.50")
                print("  5   |  Água mineral    | R$ 2.50")
                if quantiaAdd >= 1:
                    print("  6   |  {}    | R$ {}".format(produtoExtraNome1, produtoExtraPreco1))
                if quantiaAdd >= 2:
                    print("  7   |  {}    | R$ {}".format(produtoExtraNome2, produtoExtraPreco2))
                if quantiaAdd >= 3:
                    print("  8   |  {}    | R$ {}".format(produtoExtraNome3, produtoExtraPreco3))
                if quantiaAdd >= 4:
                    print("  9   |  {}    | R$ {}".format(produtoExtraNome4, produtoExtraPreco4))
                if quantiaAdd >= 5:
                    print("  10   |  {}    | R$ {}".format(produtoExtraNome5, produtoExtraPreco5))
                print("-----------------------------------")
                print("")

                sairMenu = int(input("-------------------------------------\n"
                                     "Deseja sair ?, escolha uma opção:\n"
                                     " Opção |   Descrição \n"
                                     "\n"
                                     " 1     |   Adicionar mais produtos      \n"
                                     " 2     |   Voltar ao menu\n"
                                     " 3     |   Sair do modo Administrador \n"
                                     "-----------------------------------\n"))

                if sairMenu == 1:
                    addProduto = 3

                if sairMenu == 2:
                    addProduto = 0

                if sairMenu == 3:
                    loopMenu = 0
                    addProduto = 0

            # Produtos
            while addProduto == 1:
                produtoAdicionar = float(input("Qual bebida deseja adicionar?: \n"))

                if produtoAdicionar == 1:
                    produtoQuantia = int(input("Digite a quantia de Coca-Cola que deseja adicionar: \n"))
                    qntProduct1 += produtoQuantia
                elif produtoAdicionar == 2:
                    produtoQuantia = int(input("Digite a quantia de Fanta Uva que deseja adicionar: \n"))
                    qntProduct2 += produtoQuantia
                elif produtoAdicionar == 3:
                    produtoQuantia = int(input("Digite a quantia de Fanta Laranja que deseja adicionar: \n"))
                    qntProduct3 += produtoQuantia
                elif produtoAdicionar == 4:
                    produtoQuantia = int(input("Digite a quantia de Sprite que deseja adicionar: \n"))
                    qntProduct4 += produtoQuantia
                elif produtoAdicionar == 5:
                    produtoQuantia = int(input("Digite a quantia de Água mineral que deseja adicionar: \n"))
                    qntProduct5 += produtoQuantia
                elif produtoAdicionar == 6 and quantiaAdd >= 1:
                    produtoExtraQnt1 += int(input("Digite a quantia de {} que deseja adicionar: \n".format(produtoExtraNome1)))
                elif produtoAdicionar == 7 and quantiaAdd >= 2:
                    produtoExtraQnt1 += int(input("Digite a quantia de {} que deseja adicionar: \n".format(produtoExtraNome2)))
                elif produtoAdicionar == 8 and quantiaAdd >= 3:
                    produtoExtraQnt1 += int(input("Digite a quantia de {} que deseja adicionar: \n".format(produtoExtraNome3)))
                elif produtoAdicionar == 9 and quantiaAdd >= 4:
                    produtoExtraQnt1 += int(input("Digite a quantia de {} que deseja adicionar: \n".format(produtoExtraNome4)))
                elif produtoAdicionar == 10 and quantiaAdd >= 5:
                    produtoExtraQnt1 += int(input("Digite a quantia de {} que deseja adicionar: \n".format(produtoExtraNome5)))

                print("A máquina possui o seguinte estoque:")
                print()
                print("-----------------------------------")
                print("Número|  Bebida          | Quantidade")
                print("  1   |  Coca-Cola       |   ", qntProduct1)
                print("  2   |  Fanta Uva       |   ", qntProduct2)
                print("  3   |  Fanta Laranja   |   ", qntProduct3)
                print("  4   |  Sprite          |   ", qntProduct4)
                print("  5   |  Água mineral    |   ", qntProduct5)
                if quantiaAdd >= 1:
                    print("  6   |  {}    |   {}".format(produtoExtraNome1, produtoExtraQnt1))
                if quantiaAdd >= 2:
                    print("  7   |  {}    |   {}".format(produtoExtraNome2, produtoExtraQnt2))
                if quantiaAdd >= 3:
                    print("  8   |  {}    |   {}".format(produtoExtraNome3, produtoExtraQnt3))
                if quantiaAdd >= 4:
                    print("  9   |  {}    |   {}".format(produtoExtraNome4, produtoExtraQnt4))
                if quantiaAdd >= 5:
                    print("  10   |  {}    |   {}".format(produtoExtraNome5, produtoExtraQnt5))
                print("-----------------------------------")
                print()

                addProduto = 0

            # Dinheiro
            while addProduto == 2:

                print("---------------------------------------------")
                print(" Código               |          Moeda")
                print()
                print("  0.05                |          0,05")
                print("  0.10                |          0,10")
                print("  0.25                |          0,25")
                print("  0.50                |          0,50")
                print("  1.00                |          1,00")
                print("  2.00                |          2,00")
                print("  5.00                |          5,00")
                print("  10.00               |         10,00")
                print("  20.00               |         20,00")
                print("  50.00               |         50,00")
                print("  100.00              |        100,00")
                print("---------------------------------------------")
                print()

                notaAdicionar = float(input("Qual o valor da nota desejada ?: \n"))

                if notaAdicionar == 0.05:
                    notaQuantia = int(input("Digite a quantia de notas de 0.05: \n"))
                    qntCentavosMaquina05 += notaQuantia

                elif notaAdicionar == 0.1:
                    notaQuantia = int(input("Digite a quantia de notas de 0.10: \n"))
                    qntCentavosMaquina10 += notaQuantia

                elif notaAdicionar == 0.25:
                    notaQuantia = int(input("Digite a quantia de notas de 0.25: \n"))
                    qntCentavosMaquina25 += notaQuantia

                elif notaAdicionar == 0.50:
                    notaQuantia = int(input("Digite a quantia de notas de 0.50: \n"))
                    qntCentavosMaquina50 += notaQuantia

                elif notaAdicionar == 1:
                    notaQuantia = int(input("Digite a quantia de notas de 1: \n"))
                    qntNotaMaquina1 += notaQuantia

                elif notaAdicionar == 2:
                    notaQuantia = int(input("Digite a quantia de notas de 2: \n"))
                    qntNotaMaquina2 += notaQuantia

                elif notaAdicionar == 5:
                    notaQuantia = int(input("Digite a quantia de notas de 5: \n"))
                    qntNotaMaquina5 += notaQuantia

                elif notaAdicionar == 10:
                    notaQuantia = int(input("Digite a quantia de notas de 10: \n"))
                    qntNotaMaquina10 += notaQuantia

                elif notaAdicionar == 20:
                    notaQuantia = int(input("Digite a quantia de notas de 20: \n"))
                    qntNotaMaquina20 += notaQuantia

                elif notaAdicionar == 50:
                    notaQuantia = int(input("Digite a quantia de notas de 50: \n"))
                    qntNotaMaquina50 += notaQuantia

                elif notaAdicionar == 100:
                    notaQuantia = int(input("Digite a quantia de notas de 100: \n"))
                    qntNotaMaquina100 += notaQuantia

                if notaQuantia == 0:
                    print("O valor da nota digitada não existe, digite novamente!")
                else:
                    valorTotalMaquina = qntCentavosMaquina05 * 0.05 + qntCentavosMaquina10 * 0.1 + qntCentavosMaquina25 * 0.25 + \
                                        qntCentavosMaquina50 * 0.50 + qntNotaMaquina1 * 1 + qntNotaMaquina2 * 2 + qntNotaMaquina5 * 5 + \
                                        qntNotaMaquina10 * 10 + qntNotaMaquina20 * 20 + qntNotaMaquina50 * 50 + qntNotaMaquina100 * 100

                    print("A máquina possui o seguinte estoque:")
                    print()
                    print("-----------------------------------")
                    print("Número|  Bebida          | Quantidade")
                    print("  1   |  Coca-Cola       |   ", qntProduct1)
                    print("  2   |  Fanta Uva       |   ", qntProduct2)
                    print("  3   |  Fanta Laranja   |   ", qntProduct3)
                    print("  4   |  Sprite          |   ", qntProduct4)
                    print("  5   |  Água mineral    |   ", qntProduct5)
                    if quantiaAdd >= 1:
                        print("  6   |  {}    |   {}".format(produtoExtraNome1, produtoExtraQnt1))
                    if quantiaAdd >= 2:
                        print("  7   |  {}    |   {}".format(produtoExtraNome2, produtoExtraQnt2))
                    if quantiaAdd >= 3:
                        print("  8   |  {}    |   {}".format(produtoExtraNome3, produtoExtraQnt3))
                    if quantiaAdd >= 4:
                        print("  9   |  {}    |   {}".format(produtoExtraNome4, produtoExtraQnt4))
                    if quantiaAdd >= 5:
                        print("  10   |  {}    |   {}".format(produtoExtraNome5, produtoExtraQnt5))
                    print("-----------------------------------")
                    print()
                    print("A máquina está com as seguintes notas:")
                    print()
                    print("-----------------------------------")
                    print("Nota R$ | Quantidade | R$ Total")
                    print("  0,05  |     {}     |    {:.2f}".format(qntCentavosMaquina05, qntCentavosMaquina05 * 0.05))
                    print("  0,10  |     {}     |    {:.2f}".format(qntCentavosMaquina10, qntCentavosMaquina10 * 0.1))
                    print("  0,25  |     {}     |    {:.2f}".format(qntCentavosMaquina25, qntCentavosMaquina25 * 0.25))
                    print("  0,50  |     {}     |    {:.2f}".format(qntCentavosMaquina50, qntCentavosMaquina50 * 0.50))
                    print("  1,00  |     {}     |    {:.2f}".format(qntNotaMaquina1, qntNotaMaquina1 * 1))
                    print("  2,00  |     {}     |    {:.2f}".format(qntNotaMaquina2, qntNotaMaquina2 * 2))
                    print("  5,00  |     {}     |    {:.2f}".format(qntNotaMaquina5, qntNotaMaquina5 * 5))
                    print("  10,00 |     {}     |    {:.2f}".format(qntNotaMaquina10, qntNotaMaquina10 * 10))
                    print("  20,00 |     {}     |    {:.2f}".format(qntNotaMaquina20, qntNotaMaquina20 * 20))
                    print("  50,00 |     {}     |    {:.2f}".format(qntNotaMaquina50, qntNotaMaquina50 * 50))
                    print("  100,00|     {}     |    {:.2f}".format(qntNotaMaquina100, qntNotaMaquina100 * 100))
                    print("-----------------------------------")
                    print("A máquina possui R$ {:.2f}".format(valorTotalMaquina))
                    print()

                addProduto = 0



    elif 0 < idProduct <= (5 + quantiaAdd):
        # Converção de ID para String dos produtos e Valores
        if idProduct == 1:
            nameSelectedProduct = "Coca-Cola"
            valorBebida = 3.5
        elif idProduct == 2:
            nameSelectedProduct = "Fanta Uva"
            valorBebida = 4
        elif idProduct == 3:
            nameSelectedProduct = "Fanta Laranja"
            valorBebida = 3
        elif idProduct == 4:
            nameSelectedProduct = "Sprite"
            valorBebida = 4.5
        elif idProduct == 5:
            nameSelectedProduct = "Água Mineral"
            valorBebida = 2.5
        elif idProduct == 6 and quantiaAdd >= 1:
            nameSelectedProduct = produtoExtraNome1
            valorBebida = produtoExtraPreco1
        elif idProduct == 7 and quantiaAdd >= 2:
            nameSelectedProduct = produtoExtraNome2
            valorBebida = produtoExtraPreco2
        elif idProduct == 8 and quantiaAdd >= 3:
            nameSelectedProduct = produtoExtraNome3
            valorBebida = produtoExtraPreco3
        elif idProduct == 9 and quantiaAdd >= 4:
            nameSelectedProduct = produtoExtraNome4
            valorBebida = produtoExtraPreco4
        elif idProduct == 10 and quantiaAdd >= 5:
            nameSelectedProduct = produtoExtraNome5
            valorBebida = produtoExtraPreco5

            # Verificação se está correto
        print("Você selecionou a bebida de {}, está correto?: (S/N)".format(nameSelectedProduct))
        simOuNao = input()
        if simOuNao == "s" or simOuNao == "S":
            # Creditar notas inseridas
            while valorTotalInserido < valorBebida:

                if valorTotalInserido > 0: print(
                    "Você possui R$ {} de créditos, faltam R$ {}"
                        .format(valorTotalInserido, valorBebida - valorTotalInserido)
                )
                if valorTotalInserido == 0:
                    print("O valor total é R$ ", valorBebida)
                notaInserida = float(input("Insira o valor da nota ou moeda colocada na máquina: \n"))

                if notaInserida == 0.05:
                    qntCentavos05 += 1
                    valorTotalInserido += 0.05

                elif notaInserida == 0.1:
                    qntCentavos10 += 1
                    valorTotalInserido += 0.1

                elif notaInserida == 0.25:
                    qntCentavos25 += 1
                    valorTotalInserido += 0.25

                elif notaInserida == 0.5:
                    qntCentavos50 += 1
                    valorTotalInserido += 0.5

                elif notaInserida == 1:
                    qntNota1 += 1
                    valorTotalInserido += 1

                elif notaInserida == 2:
                    qntNota2 += 1
                    valorTotalInserido += 2

                elif notaInserida == 5:
                    qntNota5 += 1
                    valorTotalInserido += 5

                elif notaInserida == 10:
                    qntNota10 += 1
                    valorTotalInserido += 10

                elif notaInserida == 20:
                    qntNota20 += 1
                    valorTotalInserido += 20

                elif notaInserida == 50:
                    qntNota50 += 1
                    valorTotalInserido += 50

                elif notaInserida == 100:
                    qntNota100 += 1
                    valorTotalInserido += 100

                else:
                    print("\nVocê digitou o valor de uma nota inexistente, digite novamente: \n")

            if valorTotalInserido >= valorBebida:
                if credito > valorBebida:
                    valorTroco = valorTotalInserido - valorBebida - credito
                else:
                    valorTroco = valorTotalInserido - valorBebida

                # Devolver Troco
                if valorTroco > 0:
                    while valorTroco > 0:

                        if valorTotalMaquina < valorTroco:
                            # Cancelar compra por falta de troco ou não
                            print("A máquina não possui troco, escolha uma opção:")
                            print("-----------------------------------------------------")
                            print(" Opção |                 Descrição")
                            print("   1   | Cancelar a compra e receber o valor inserido")
                            print("   2   |     Comprar e deixar o troco como crédito")
                            print("-----------------------------------------------------")
                            cancelar = int(input("Digite sua escolha:\n"))
                            if cancelar == 2:
                                credito = valorTotalInserido - valorBebida
                                valorTroco = 0
                            else:
                                print("\nNão possuo troco, não será possível realizar a compra :(")
                                print("Devolvendo notas inseridas")
                                # Reset notas inseridas
                                notaTroco = 0
                                valorTroco = 0
                                valorTotalInserido = 0
                                qntCentavos05 = 0
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

                        elif valorTroco >= 100 and qntNotaMaquina100 > 0:
                            notaTroco = 100
                            valorTroco += - 100
                            qntNotaMaquina100 += -1

                        elif valorTroco >= 50 and qntNotaMaquina50 > 0:
                            notaTroco = 50
                            valorTroco += - 50
                            qntNotaMaquina50 += -1

                        elif valorTroco >= 20 and qntNotaMaquina20 > 0:
                            notaTroco = 20
                            valorTroco += - 20
                            qntNotaMaquina20 += -1

                        elif valorTroco >= 10 and qntNotaMaquina10 > 0:
                            notaTroco = 10
                            valorTroco += - 10
                            qntNotaMaquina10 += -1

                        elif valorTroco >= 5 and qntNotaMaquina5 > 0:
                            notaTroco = 5
                            valorTroco += - 5
                            qntNotaMaquina5 += -1

                        elif valorTroco >= 2 and qntNotaMaquina2 > 0:
                            notaTroco = 2
                            valorTroco += - 2
                            qntNotaMaquina2 += -1

                        elif valorTroco >= 1 and qntNotaMaquina1 > 0:
                            notaTroco = 1
                            valorTroco += - 1
                            qntNotaMaquina1 += -1

                        elif valorTroco >= 0.5 and qntCentavosMaquina50 > 0:
                            notaTroco = 0.5
                            valorTroco += - 0.5
                            qntCentavosMaquina50 += -1

                        elif valorTroco >= 0.25 and qntCentavosMaquina25 > 0:
                            notaTroco = 0.25
                            valorTroco += - 0.25
                            qntCentavosMaquina25 += -1

                        elif valorTroco >= 0.1 and qntCentavosMaquina10 > 0:
                            notaTroco = 0.1
                            valorTroco += - 0.1
                            qntCentavosMaquina10 += -1

                        elif valorTroco >= 0.05 and qntCentavosMaquina05 > 0:
                            notaTroco = 0.05
                            valorTroco += - 0.05
                            qntCentavosMaquina05 += -1

                        else:
                            # Cancelar compra por falta de troco ou não
                            print("A máquina não possui troco, escolha uma opção:")
                            print("-----------------------------------------------------")
                            print(" Opção |                 Descrição")
                            print("   1   | Cancelar a compra e receber o valor inserido")
                            print("   2   |     Comprar e deixar o troco como crédito")
                            print("-----------------------------------------------------")
                            cancelar = int(input("Digite sua escolha:\n"))
                            if cancelar == 2:
                                credito = valorTotalInserido - valorBebida
                                valorTroco = 0
                            else:
                                print("\nNão possuo troco, não será possível realizar a compra :(")
                                print("Devolvendo notas inseridas")
                                # Reset notas inseridas
                                notaTroco = 0
                                valorTroco = 0
                                valorTotalInserido = 0
                                qntCentavos05 = 0
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

                        if notaTroco > 0:
                            # Devolver nota
                            print("Devolvendo nota de R$ ", notaTroco)

                # Contabilizar venda
                if valorTroco <= 0 < valorTotalInserido:
                    # Compra realizada
                    print("Você adquiriu uma {} no valor de R$ {}".format(nameSelectedProduct, valorBebida))

                    # Atualizando estoque
                    if idProduct == 1:
                        qntProduct1 += -1
                    elif idProduct == 2:
                        qntProduct2 += -1
                    elif idProduct == 3:
                        qntProduct3 += -1
                    elif idProduct == 4:
                        qntProduct4 += -1
                    elif idProduct == 6:
                        produtoExtraQnt1 += -1
                    elif idProduct == 7:
                        produtoExtraQnt2 += -1
                    elif idProduct == 8:
                        produtoExtraQnt3 += -1
                    elif idProduct == 9:
                        produtoExtraQnt4 += -1
                    elif idProduct == 10:
                        produtoExtraQnt5 += -1

                    # Repassando notas para maquina
                    qntCentavosMaquina05 += qntCentavos05
                    qntCentavosMaquina10 += qntCentavos10
                    qntCentavosMaquina25 += qntCentavos25
                    qntCentavosMaquina50 += qntCentavos50
                    qntNotaMaquina1 += qntNota1
                    qntNotaMaquina2 += qntNota2
                    qntNotaMaquina5 += qntNota5
                    qntNotaMaquina10 += qntNota10
                    qntNotaMaquina20 += qntNota20
                    qntNotaMaquina50 += qntNota50
                    qntNotaMaquina100 += qntNota100

                    # Descontar bebida do credito
                    if credito > 0 and cancelar == 0:
                        if (valorBebida - credito) < 0:
                            credito += -valorBebida
                        else:
                            credito = 0

                    # Reset
                    cancelar = 0
                    valorTotalInserido = 0
                    qntCentavos05 = 0
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
                    valorTotalMaquina = qntCentavosMaquina05 * 0.05 + qntCentavosMaquina10 * 0.1 + qntCentavosMaquina25 * 0.25 + \
                                        qntCentavosMaquina50 * 0.50 + qntNotaMaquina1 * 1 + qntNotaMaquina2 * 2 + qntNotaMaquina5 * 5 + \
                                        qntNotaMaquina10 * 10 + qntNotaMaquina20 * 20 + qntNotaMaquina50 * 50 + qntNotaMaquina100 * 100


    else:
        # Catch error
        print("Você digitou um produto inválido, por favor, digite novamente o produto desejado:")
