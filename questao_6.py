def informar_quantidade_de_nuggets():
    while True:
        valor = int(input("Informe a quantidade de nuggets que deseja comprar: "))
        if valor > 0:
            return valor
        print("Quantidade inválida!")


consegue_comprar = False
valor = informar_quantidade_de_nuggets()
for a in range((valor // 6) + 1):
    for b in range((valor // 9) + 1):
        for c in range((valor // 20) + 1):
            if (6 * a) + (9 * b) + (20 * c) == valor:
                consegue_comprar = True
                print(a, "sacos de 6 nuggets", b, "sacos de 9 nuggets", c, "sacos de 20 nuggets conseguem comprar",
                      valor, "nuggets", sep=" ")

print("Consegue comprar?", consegue_comprar, sep=" ")
