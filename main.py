from metodos.gauss_jordan import gauss_jordan
from metodos.eliminacion_sustitucion import eliminacion_sustitucion
from metodos.suma_y_resta import suma_y_resta
from metodos.determinante import determinante


def leer_sistema():
    n = int(input("Número de ecuaciones: "))
    A, b = [], []
    for i in range(n):
        A.append([float(v) for v in input(f"Coeficientes de la ecuación {i + 1}: ").split()])
        b.append(float(input(f"Resultado de la ecuación {i + 1}: ")))
    return A, b


def mostrar(x):
    if x:
        for i, v in enumerate(x):
            print(f"x{i + 1} = {v:.4f}")


while True:
    print("\n1. Gauss-Jordan")
    print("2. Eliminación y sustitución")
    print("3. Suma y resta (2x2)")
    print("4. Determinante")
    print("0. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        A, b = leer_sistema()
        mostrar(gauss_jordan(A, b))

    elif opcion == "2":
        A, b = leer_sistema()
        mostrar(eliminacion_sustitucion(A, b))

    elif opcion == "3":
        a1, b1, c1 = [float(v) for v in input("Ecuación 1 (a1 b1 c1): ").split()]
        a2, b2, c2 = [float(v) for v in input("Ecuación 2 (a2 b2 c2): ").split()]
        r = suma_y_resta(a1, b1, c1, a2, b2, c2)
        if r:
            print(f"x = {r[0]:.4f}, y = {r[1]:.4f}")

    elif opcion == "4":
        n = int(input("Tamaño de la matriz: "))
        A = [[float(v) for v in input(f"Fila {i + 1}: ").split()] for i in range(n)]
        print(f"Determinante = {determinante(A):.4f}")

    elif opcion == "0":
        break
