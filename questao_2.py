def informar_numeros():
    numeros = []

    numeros.insert(0, (int(input("Informe um numero inteiro para ser o divendo: "))))
    while True:
        numeros.insert(1, int(input("Informe um numero inteiro nao nulo para ser o divisor: ")))
        if numeros[1] != 0:
            break
        print("Número informado é inválido!")
    return numeros


def verificar_negatividade_do_resultado(numeros=[]):
    resultado_positivo = False

    if (numeros[0] >= 0 and numeros[1] > 0) or (numeros[0] < 0 and numeros[1] < 0):
        resultado_positivo = True
        if numeros[0] < 0:
            numeros.insert(0, numeros[0] * (-1))
            numeros.insert(1, numeros[1] * (-1))
    else:
        resultado_positivo = False
        if numeros[0] < 0:
            numeros.insert(0, numeros[0] * (-1))
        else:
            numeros.insert(1, numeros[1] * (-1))
    return resultado_positivo


def verificar_se_dividendo_eh_menor_que_divisor(numeros=[]):
    return numeros[0] < numeros[1]


def efetuar_divisao(dividendo_eh_menor, resultado_positivo, numeros=[]):
    aux = numeros[1]
    quociente = 0

    while aux <= numeros[0]:
        quociente = quociente + 1
        aux = aux + numeros[1]

    resto = 0
    if not dividendo_eh_menor:
        resto = numeros[0] - (aux - numeros[1])

    if not resultado_positivo:
        quociente = quociente * (-1)

    return [quociente, resto]


numeros = informar_numeros()
resultado_positivo = verificar_negatividade_do_resultado(numeros)
dividendo_eh_menor = verificar_se_dividendo_eh_menor_que_divisor(numeros)
resultado = efetuar_divisao(dividendo_eh_menor, resultado_positivo, numeros)
print("Resultado da divisao:")
print(
    "Quociente =", resultado[0], "Resto =", resultado[1],
    sep=" "
)