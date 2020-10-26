import random


def tab_multiplicar(numero):
    for x in range(1, 11):
        print(numero, " * ", x, " = ", numero * x)


def impr_numeros():
    for x in range(10, 21):
        print(x)


def temp_celsius():
    gcels = lambda gfaren: (gfaren - 32) / (9 / 5)
    for x in range(0, 121, 10):
        print(x, "° F  ->  ", round(gcels(x), 2), "° C", sep="")


def ano_bisiesto(numero, saida):
    bisiesto = None
    if numero % 4 == 0:
        if numero % 100 == 0:
            if numero % 400 == 0:
                bisiesto = True
            else:
                bisiesto = False
        else:
            bisiesto = True
    else:
        bisiesto = False

    if saida:
        if bisiesto:
            print("O ano", numero, "é bisiesto")
        else:
            print("O ano", numero, "non é bisiesto")
    return bisiesto


def dias_mes(mes, saida):
    dias = 0
    nmes = None
    if mes == 1:
        dias = 31
        nmes = "Enero"
    elif mes == 2:
        dias = 28
        nmes = "Febrero"
    elif mes == 3:
        dias = 31
        nmes = "Marzo"
    elif mes == 4:
        dias = 30
        nmes = "Abril"
    elif mes == 5:
        dias = 31
        nmes = "Mayo"
    elif mes == 6:
        dias = 30
        nmes = "Junio"
    elif mes == 7:
        dias = 31
        nmes = "Julio"
    elif mes == 8:
        dias = 31
        nmes = "Agosto"
    elif mes == 9:
        dias = 30
        nmes = "Septiembre"
    elif mes == 10:
        dias = 31
        nmes = "Octubre"
    elif mes == 11:
        dias = 30
        nmes = "Noviembre"
    elif mes == 12:
        dias = 31
        nmes = "Diciembre"

    if saida:
        if nmes is None:
            print("El número introducido no se corresponde a nigún mes")
        elif mes == 2:
            print(nmes, "tiene", dias, "días (29 si el año es bisiesto)")
        else:
            print(nmes, "tiene", dias, "días")
    return dias


def data_valida(dia, mes, ano):
    valida = None
    if mes < 0 | mes > 12:
        valida = False
    else:
        if ano_bisiesto(ano, False) and mes == 2:
            if dia > 29:
                valida = False
            else:
                valida = True
        else:
            if dia > dias_mes(mes, False):
                valida = False
            else:
                valida = True

    if valida:
        print("A fecha é válida")
    else:
        print("A fecha non é válida")


def obter_iniciais(*palabras):
    iniciais = ""
    for x in palabras:
        iniciais = iniciais + x[0]
    print(iniciais)


def filtro_consonantes(palabra):
    vocales = "aeiouAEIOU"
    pfiltrada = ""
    for x in palabra:
        filtrar = None
        for y in vocales:
            if x == y:
                filtrar = True
            elif not filtrar:
                filtrar = False
        if not filtrar:
            pfiltrada = pfiltrada + x
    print(pfiltrada)


def ordear_palabras(palabra1, palabra2):
    lista_palabras = [palabra1, palabra2]
    palabras_ordeadas = sorted(lista_palabras, key=str.lower)
    print(palabras_ordeadas[0])


def comprobar_orde(tupla):
    tupla_ordeada = sorted(tupla, key=str.lower)
    if set(tupla) == set(tupla_ordeada):
        print("A tupla está ordeada de menor a maior")
    else:
        print("A tupla non está ordeada de menor a maior")


def fichas_domino(ficha1, ficha2):
    if ficha1[0] == ficha2[0] or ficha1[1] == ficha2[1] or ficha1[0] == ficha2[1] or ficha1[1] == ficha2[0]:
        print("As fichas encaixan")
    else:
        print("As fichas non encaixan")


def factoriais(lista_enteros: []):
    for x in lista_enteros:
        factorial = 1
        for y in range(1, x + 1):
            factorial = factorial * y
        print(str(x) + "! =", factorial)


def comparar(lista_enteros: [], k: int):
    lista_menores = []
    lista_maiores = []
    lista_iguais = []
    for x in lista_enteros:
        if x < k:
            lista_menores.append(x)
        elif x > k:
            lista_maiores.append(x)
        elif x == k:
            lista_iguais.append(x)
    print("Números menores ca " + str(k) + ":", lista_menores)
    print("Números maiores ca " + str(k) + ":", lista_maiores)
    print("Números iguais a " + str(k) + ":", lista_iguais)


def aparicions(cadea: str, sort: bool):
    num_aparicions = {}
    lista_palabras = cadea.lower().split()
    if sort:
        lista_palabras = sorted(lista_palabras)
    for x in lista_palabras:
        if x not in num_aparicions:
            num_aparicions[x] = 1
        else:
            num_aparicions[x] = num_aparicions[x] + 1
    print(num_aparicions)


def dados(i: int):
    resultado = ""
    for x in range(0, i):
        for y in range(0, 2):
            resultado = resultado + " " + str(random.randint(1, 6))
    print(aparicions(resultado, True))


# tab_multiplicar(10)  # 1
# impr_numeros()  # 2
# temp_celsius()  # 3
# ano_bisiesto(2020, True)  # 4
# dias_mes(2, True)  # 5
# data_valida(29, 2, 2020)  # 6
# obter_iniciais("Universal", "Serial", "Bus")  # 7
# filtro_consonantes("logaritmos")  # 8
# ordear_palabras("kde", "gnome")  # 9
# comprobar_orde(("cinnamon", "gnome", "kde"))  # 10
# fichas_domino((2, 5), (7, 2))  # 11
# factoriais([7, 12, 6, 13, 9, 15, 8])  # 12
# comparar([3, 12, 6, 8, 1, 16, 14, 34, 42, 2, 22], 14)  # 13
# aparicions("Que lindo día que fai hoxe", False)  # 14
# dados(100)  # 15
