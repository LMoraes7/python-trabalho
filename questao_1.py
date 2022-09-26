def informar_quantidade_de_numeros():
    return int(input("Quantos números você quer deseja informar: "))


def informar_numeros_desejados(quantidade_de_numeros):
    numeros = []

    for i in range(quantidade_de_numeros):
        numeros.append(int(input("Informe um número: ")))
    return numeros


def calcular_soma_dos_quadrados(numeros=[]):
    soma = 0
    for x in numeros:
        soma += (x ** 2)
    return soma


print(
    "A soma total dos quadrados dos números informados é:",
    calcular_soma_dos_quadrados(informar_numeros_desejados(informar_quantidade_de_numeros())),
    sep=" "
)
