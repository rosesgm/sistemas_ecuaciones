# Eliminación gaussiana + sustitución hacia atrás


def eliminacion_sustitucion(A, b):
    n = len(A)
    M = [A[i] + [b[i]] for i in range(n)]  # matriz aumentada [A | b]

    # Eliminación: dejar la matriz triangular superior
    for i in range(n):
        if M[i][i] == 0:
            for k in range(i + 1, n):
                if M[k][i] != 0:
                    M[i], M[k] = M[k], M[i]
                    break
            else:
                print("El sistema no tiene solución única.")
                return None

        for k in range(i + 1, n):
            factor = M[k][i] / M[i][i]
            M[k] = [M[k][j] - factor * M[i][j] for j in range(n + 1)]

    # Sustitución hacia atrás
    x = [0] * n
    for i in range(n - 1, -1, -1):
        suma = sum(M[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (M[i][n] - suma) / M[i][i]
    return x
