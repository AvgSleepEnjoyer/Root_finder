import sympy as sp      # https://docs.sympy.org/latest/guides/custom-functions.html
                        # https://docs.sympy.org/latest/explanation/glossary.html#term-sympify
import time

def punto_fijo(expr_str, g_str, x0, margen_e, max_iter=50):
    x = sp.symbols('x')

    f_expr = sp.sympify(expr_str)

    g_expr = sp.sympify(g_str)

    f = sp.lambdify(x, f_expr, "math")
    g = sp.lambdify(x, g_expr, "math")

    print("\nIteraciones del metodo de punto fijo:")
    print("Iter |   x_n    |   g(x_n)   |   f(x_n)")
    print("-----------------------------------------")

    for i in range(max_iter):
        time.sleep(0.09)
        x1 = g(x0)
        print(f"{i+1:4d} | {x0:.6f} | {x1:.6f} | {f(x0):.6f}")

        if abs(x1 - x0) < margen_e:
            return x1
        x0 = x1

    return x0