# Método de suma y resta para un sistema de 2 ecuaciones:
#   a1*x + b1*y = c1
#   a2*x + b2*y = c2


def suma_y_resta(a1, b1, c1, a2, b2, c2):
    # Multiplicar para igualar los coeficientes de x y restar
    coef_y = b1 * a2 - b2 * a1
    termino = c1 * a2 - c2 * a1

    if coef_y == 0:
        print("El sistema no tiene solución única.")
        return None

    y = termino / coef_y

    # Sustituir y para encontrar x
    if a1 != 0:
        x = (c1 - b1 * y) / a1
    else:
        x = (c2 - b2 * y) / a2
    return x, y
