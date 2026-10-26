# Método de Gauss-Jordan para resolver un sistema de ecuaciones


def gauss_jordan(A, b):
    n = len(A)
    M = [A[i] + [b[i]] for i in range(n)]  # matriz aumentada [A | b]

    for i in range(n):
        # Si el pivote es 0, intercambiar con una fila de abajo
        if M[i][i] == 0:
            for k in range(i + 1, n):
                if M[k][i] != 0:
                    M[i], M[k] = M[k], M[i]
                    break
            else:
                print("El sistema no tiene solución única.")
                return None

        # Hacer 1 el pivote
        pivote = M[i][i]
        M[i] = [v / pivote for v in M[i]]

        # Hacer 0 el resto de la columna
        for k in range(n):
            if k != i:
                factor = M[k][i]
                M[k] = [M[k][j] - factor * M[i][j] for j in range(n + 1)]

    return [M[i][n] for i in range(n)]
