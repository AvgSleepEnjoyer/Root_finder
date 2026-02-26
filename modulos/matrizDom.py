
def es_diagonalmente_dominante(A):
    # Verifica si la matriz A es diagonalmente dominante por filas.
    n = A.rows
    for i in range(n):
        suma = sum(abs(A[i, j]) for j in range(n) if j != i)
        if abs(A[i, i]) < suma:
            return False
    return True