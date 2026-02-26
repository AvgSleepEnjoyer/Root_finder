import sympy as sp      # https://docs.sympy.org/latest/guides/custom-functions.html
                        # https://docs.sympy.org/latest/explanation/glossary.html#term-sympify
import time

from .matrizDom import *

def gauss_seidel(A, b, x0, margen_e, max_iter=100):
    n = A.rows
    x = sp.Matrix(x0)

    if not es_diagonalmente_dominante(A):
        print("La matriz no es diagonalmente dominante. El metodo puede no converger.")

    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            suma = sum(A[i, j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - suma) / A[i, i]

        if (x_new - x).norm() < margen_e:
            print(f"Convergió en iteración {k+1}: {x_new}")
            return x_new

        x = x_new
        print(f"Iteración {k+1}: {x}")
        time.sleep(0.09)

    print("No convergió en el número máximo de iteraciones")
    return x
