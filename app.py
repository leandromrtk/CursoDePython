from calculadora import Calculadora


while True:

    opcao = str(input("Qual operação deseja executar? \n""1 - Somar (+)\n"
                      "2 - Multiplicar (x)\n"
                      "3 - Diminuir (-)\n"
                      "4 - Dividir (%)\n"
                      "0 - Sair\n"
                      "Escolha uma :"))
    
    opcao.upper()

    if int(opcao) == 1:
        print("-> Operação de soma")
        calc = Calculadora(numero1=int(input("Digite o primeiro valor: ")),
                           numero2=int(input("Digite o segundo valor: ")))
        result = calc.somar() #calc é o objeto da classe Calculadora

    elif int(opcao) == 2:
        print("-> Operação de multiplicação")
        calc = Calculadora(numero1=int(input("Digite o primeiro valor: ")),
                           numero2=int(input("Digite o segundo valor: ")))
        result = calc.multiplicar()

    elif int(opcao) == 3:
        print("-> Operação de subutração")
        calc = Calculadora(numero1=int(input("Digite o primeiro valor: ")),
                           numero2=int(input("Digite o segundo valor: ")))
        result = calc.diminuir()

    elif int(opcao) == 4:
        print("Operação de divisão")
        calc = Calculadora(numero1=int(input("Digite o primeiro valor: ")),
                           numero2=int(input("Digite o segundo valor: ")))
        result = calc.dividir()

    elif int(opcao) == 0:
        break
    
    else:
        print("Opção invalida. Tente novamente!")    
    """  implementar exceções
    else:
        print("Opção inválida, deseja continuar? s/n")
        opcao = input()
        if opcao == "s":
            continue
        else:
            break
    """
