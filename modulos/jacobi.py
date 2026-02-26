import sympy as sp      # https://docs.sympy.org/latest/guides/custom-functions.html
                        # https://docs.sympy.org/latest/explanation/glossary.html#term-sympify
import time

from .matrizDom import *


def jacobi(A, b, x0, margen_e, max_iter=100):
    n = A.rows
    x = sp.Matrix(x0)

    # Verificación de diagonalmente dominante
    if not es_diagonalmente_dominante(A):
        print("La matriz no es diagonalmente dominante. El metodo puede no converger.")

    for k in range(max_iter):
        x_new = sp.zeros(n, 1)
        for i in range(n):
            suma = sum(A[i, j] * x[j] for j in range(n) if j != i)    # hace el y1 dependiente de x, y el x2 dependiente de y
            x_new[i] = (b[i] - suma) / A[i, i]

        # criterio de parada: diferencia entre iteraciones
        if (x_new - x).norm() < margen_e:
            print(f"Convergió en iteración {k+1}: {x_new}")
            return x_new

        x = x_new
        print(f"Iteración {k+1}: {x}")
        time.sleep(0.09)

    print("No convergió en el número máximo de iteraciones")
    return x