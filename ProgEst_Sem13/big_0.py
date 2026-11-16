
import random
import time


# EJERCICIO 1 - TRAZA DE BURBUJA
def ejercicio1():
    lista = [9, 7, 5, 3, 1]
    comparaciones = 0
    intercambios = 0

    print("Lista inicial:", lista)

    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            comparaciones += 1

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1

        print("Pasada", i + 1, ":", lista)

    print("Comparaciones:", comparaciones)
    print("Intercambios:", intercambios)
    print("Caso: Peor caso")


# EJERCICIO 2 - BURBUJA DESCENDENTE
def ejercicio2():
    lista = [5, 2, 9, 1, 7]

    print("Lista original:", lista)

    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    print("Mayor a menor:", lista)


# FUNCION BURBUJA ASCENDENTE
def burbuja(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


# FUNCION BUSQUEDA BINARIA
def busqueda_binaria(lista, dato):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == dato:
            return True

        elif lista[medio] < dato:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    return False


# EJERCICIO 3 - NOTAS Y BUSQUEDA BINARIA
def ejercicio3():
    notas = []

    for i in range(10):
        nota = float(input("Ingrese nota " + str(i + 1) + ": "))
        notas.append(nota)

    burbuja(notas)

    print("Notas ordenadas:", notas)

    dato = float(input("Nota que desea buscar: "))

    if busqueda_binaria(notas, dato):
        print("La nota existe")
    else:
        print("La nota no existe")


# EJERCICIO 4 - ORDENAR NOMBRES
def ejercicio4():
    nombres = ["Pedro", "Ana", "Luis", "Carlos", "Maria"]

    print("Nombres originales:", nombres)

    burbuja(nombres)

    print("Nombres ordenados:", nombres)
    print("Funciona porque Python permite comparar cadenas.")


# EJERCICIO 5 - MEDIR TIEMPOS
def ejercicio5():
    for cantidad in [1000, 2000, 4000]:
        numeros = []

        for i in range(cantidad):
            numeros.append(random.randint(1, 10000))

        inicio = time.perf_counter()

        burbuja(numeros)

        fin = time.perf_counter()

        tiempo = fin - inicio

        print(cantidad, "elementos:",
              round(tiempo, 4), "segundos")


# MENU PRINCIPAL
while True:
    print("\n===== PRACTICA DE ORDENAMIENTO =====")
    print("1. Traza del metodo burbuja")
    print("2. Burbuja de mayor a menor")
    print("3. Ordenar 10 notas y buscar")
    print("4. Ordenar nombres")
    print("5. Medir tiempo de burbuja")
    print("6. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        ejercicio1()

    elif opcion == "2":
        ejercicio2()

    elif opcion == "3":
        ejercicio3()

    elif opcion == "4":
        ejercicio4()

    elif opcion == "5":
        ejercicio5()

    elif opcion == "6":
        print("Programa finalizado")
        break

    else:
        print("Opcion incorrecta")
