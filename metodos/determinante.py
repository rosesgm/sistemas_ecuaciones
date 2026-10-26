# Determinante por eliminación de Gauss:
# se triangula la matriz y se multiplica la diagonal


def determinante(A):
    n = len(A)
    M = [fila[:] for fila in A]
    signo = 1

    for i in range(n):
        if M[i][i] == 0:
            for k in range(i + 1, n):
                if M[k][i] != 0:
                    M[i], M[k] = M[k], M[i]
                    signo = -signo  # cada intercambio cambia el signo
                    break
            else:
                return 0

        for k in range(i + 1, n):
            factor = M[k][i] / M[i][i]
            M[k] = [M[k][j] - factor * M[i][j] for j in range(n)]

    det = signo
    for i in range(n):
        det *= M[i][i]
    return det
