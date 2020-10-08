def tabMultiplicar(numero):
    for x in range(1, 11):
        print(numero, " * ", x, " = ", numero * x)


def imprNumeros():
    for x in range(10, 21):
        print(x)


def tempCelsius():
    gCels = lambda gFaren: (gFaren - 32) / (9 / 5)
    for x in range(0, 121, 10):
        print(x, "° F  ->  ", round(gCels(x), 2), "° C", sep="")


# tabMultiplicar(10)
# imprNumeros()
# tempCelsius()
