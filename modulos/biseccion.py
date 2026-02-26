import sympy as sp      # https://docs.sympy.org/latest/guides/custom-functions.html
                        # https://docs.sympy.org/latest/explanation/glossary.html#term-sympify
import time

def biseccion(expr_str, a, b, margen_e, max_iter=100):
    # se define que x sea la variable
    x = sp.symbols('x')

    # se transforma la cadena a funcion 
    f_expr = sp.sympify(expr_str)

    # Creamos una función evaluable
    f = sp.lambdify(x, f_expr, "math")

    # Verificacion de intervalo ingresado
    if f(a) * f(b) > 0:
        raise ValueError("El intervalo no es valido: no hay cambio de signo.")
    
    print("\nIteraciones del metodo de biseccion:")
    print("Iter |   a    |   b    |   m    |  f(m)")
    print("-----------------------------------------")


    for i in range(max_iter):
        time.sleep(0.09)
        m = (a + b) / 2
        fm = f(m)
        print(f"{i+1:4d} | {a:.6f} | {b:.6f} | {m:.6f} | {fm:.6f}")


        if abs(f(m)) < margen_e or (b - a) / 2 < margen_e:
            return m
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2