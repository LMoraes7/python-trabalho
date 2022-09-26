def informar_operacao():
    while True:
        operacao = int(input("1 - Somar; 2 - Subtrair; 3 - Dividir; 4 - Multiplicar; 5 - Sair: "))
        if operacao == 5:
            print("Saindo do programa!")
            exit(0)
        if 4 >= operacao >= 1:
            informar_numeros(operacao)
        else:
            print("Número informado é inválido!")


def informar_numeros(operacao):
    primeiro_numero = int(input("Informe o primeiro número: "))
    segundo_numero = int(input("Informe o segundo número: "))

    if operacao == 1:
        print("resultado da soma =", (primeiro_numero + segundo_numero), sep=" ")
    if operacao == 2:
        print("resultado da subtração =", (primeiro_numero - segundo_numero), sep=" ")
    if operacao == 3:
        if segundo_numero == 0:
            print("divisão por zero é inválido")
        else:
            print("resultado da subtração =", (primeiro_numero / segundo_numero), sep=" ")
    if operacao == 4:
        print("resultado da multiplicação =", (primeiro_numero * segundo_numero), sep=" ")

informar_operacao()