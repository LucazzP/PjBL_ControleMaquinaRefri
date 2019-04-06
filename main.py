##### Variáveis #####
#renan teste#
#renan teste#

isRunning = True
idProduct = 0
qntProduct1 = 10
qntProduct2 = 10
qntProduct3 = 10
qntProduct4 = 10
qntProduct5 = 10
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
qntNotaMaquina5 = 0
qntNotaMaquina10 = 0
qntNotaMaquina20 = 0
qntNotaMaquina50 = 0
qntNotaMaquina100 = 0
valorTotalMaquina = qntCentavosMaquina05 * 0.05 + qntCentavosMaquina10 * 0.1 + qntCentavosMaquina25 * 0.25 + \
                    qntCentavosMaquina50 * 0.50 + qntNotaMaquina1 * 1 + qntNotaMaquina2 * 2 + qntNotaMaquina5 * 5 + \
                    qntNota10 * 10 + qntNotaMaquina20 * 20 + qntNotaMaquina50 * 50 + qntNotaMaquina100 * 100

##### Início #####

# Selecionar Bebida

while isRunning:

    print("")
    print("-----------------------------------")
    print("Número|  Bebida          | Valor")
    print("  1   |  Coca-Cola       | R$ 3.50")
    print("  2   |  Fanta Uva       | R$ 4.00")
    print("  3   |  Fanta Laranja   | R$ 3.00")
    print("  4   |  Sprite          | R$ 4.50")
    print("  5   |  Água mineral    | R$ 2.50")
    print("-----------------------------------")
    print("")
    idProduct = input("Digite o número da bebida desejada: \n")


    # Verificar se é numero
    if idProduct is 1 or 2 or 3 or 4 or 5 or 996:
        idProduct = int(idProduct)
    else:
        idProduct = 404

    if idProduct == 996: # 996 = admPassword
        # Área do admnistrador
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

    elif 0 < idProduct <= 5:
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

            # Verificação se está correto
        print("Você selecionou a bebida de {}, está correto?: (S/N)".format(nameSelectedProduct))
        simOuNao = input()
        if simOuNao == "s" or simOuNao == "S":
            # Creditar notas inseridas
            while valorTotalInserido < valorBebida:

                if valorTotalInserido > 0 : print(
                    "Você possui R$ {} de créditos, faltam R$ {}"
                        .format(valorTotalInserido, valorBebida - valorTotalInserido)
                )
                if valorTotalInserido == 0 : print("O valor total é R$ ", valorBebida)
                notaInserida = float(input("Insira o valor da nota ou moeda colocada na máquina: \n"))

                if notaInserida == 0.05:
                    qntCentavos05+= 1
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

                else : print("\nVocê digitou o valor de uma nota inexistente, digite novamente: \n")

            if valorTotalInserido >= valorBebida:
                valorTroco = valorTotalInserido - valorBebida

                # Devolver Troco
                if valorTroco > 0:
                    while valorTroco > 0:

                        if valorTroco == 0.05 and qntCentavosMaquina05 > 0:
                            notaTroco = 0.05
                            valorTroco += -0.05
                            qntCentavosMaquina05 += -1

                        elif valorTroco == 0.1 and qntCentavosMaquina10 > 0:
                            notaTroco = 0.1
                            valorTroco += -0.1
                            qntCentavosMaquina10 += -1

                        elif valorTroco == 0.25 and qntCentavosMaquina25 > 0:
                            notaTroco = 0.25
                            valorTroco += -0.25
                            qntCentavosMaquina25 += -1

                        elif valorTroco == 0.5 and qntCentavosMaquina50 > 0:
                            notaTroco = 0.5
                            valorTroco += -0.5
                            qntCentavosMaquina50 += -1

                        elif valorTroco == 1 and qntNotaMaquina1 > 0:
                            notaTroco = 1
                            valorTroco += -1
                            qntNotaMaquina1 += -1

                        elif valorTroco == 2 and qntNotaMaquina2 > 0:
                            notaTroco = 2
                            valorTroco += -2
                            qntNotaMaquina2 += -1

                        # Verificação complexa
                        elif 2 < valorTroco < 5 and qntNotaMaquina2 > 0:
                            notaTroco = 2
                            valorTroco += -2
                            qntNotaMaquina2 += -1
                        # Fim da Verificação complexa

                        elif valorTroco == 5 and qntNotaMaquina5 > 0:
                            notaTroco = 5
                            valorTroco += -5
                            qntNotaMaquina5 += -1

                        elif valorTroco == 10 and qntNotaMaquina10 > 0:
                            notaTroco = 10
                            valorTroco += -10
                            qntNotaMaquina10 += -1

                        elif valorTroco == 20 and qntNotaMaquina20 > 0:
                            notaTroco = 20
                            valorTroco += -20
                            qntNotaMaquina20 += -1

                        elif valorTroco == 50 and qntNotaMaquina50 > 0:
                            notaTroco = 50
                            valorTroco += -50
                            qntNotaMaquina50 += -1

                        elif valorTroco == 100 and qntNotaMaquina100 > 0:
                            notaTroco = 100
                            valorTroco += -100
                            qntNotaMaquina100 += -1

                        else:
                            print("\nNão possuo troco na máquina, não será possível realizar a compra :(")
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
                if valorTroco == 0 and valorTotalInserido > 0:
                    # Compra realizada
                    print("Você adquiriu uma {} no valor de R$ {}".format(nameSelectedProduct, valorBebida))

                    #Atualizando estoque
                    if idProduct == 1:
                        qntProduct1 += -1
                    elif idProduct == 2:
                        qntProduct2 += -1
                    elif idProduct == 3:
                        qntProduct3 += -1
                    elif idProduct == 4:
                        qntProduct4 += -1
                    elif idProduct == 5:
                        qntProduct5 += -1

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

                    # Reset
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
                                        qntNota10 * 10 + qntNotaMaquina20 * 20 + qntNotaMaquina50 * 50 + qntNotaMaquina100 * 100


    else:
        # Catch error
        print("Você digitou um produto inválido, por favor, digite novamente o produto desejado:")