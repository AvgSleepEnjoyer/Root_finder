import sympy as sp      # https://docs.sympy.org/latest/guides/custom-functions.html
                        # https://docs.sympy.org/latest/explanation/glossary.html#term-sympify
import time

def newthon_raphson_una_x(expr_str, x0, margen_e, max_iter=100):
    
    x = sp.symbols('x')

    f_expr = sp.sympify(expr_str)

    dx = sp.diff(f_expr, x)

    f = sp.lambdify(x, f_expr, "math")
    g = sp.lambdify(x, dx, "math")

    print("\nIteraciones del metodo de Newton-Raphson para una ecuacion y variable:")
    print("Iter |   x_0    |   x_1    |   f(x_n) |   f'(x_n)")
    print("-----------------------------------------")

    for i in range(max_iter):
        time.sleep(0.09)
        x1 = x0 - (f(x0)/g(x0))
        print(f"{i:4d} | {x0:.6f} | {x1:.6f} | {f(x0):.6f} | {g(x0):.6f}")
        
        if abs(x0-x1) < margen_e:
            return  x1
        x0 = x1


def newthon_raphsons(varis, arr, raices, margen_e, max_iter=100):
    print

    X = sp.Matrix(varis)
    F = sp.Matrix(arr)
    J = F.jacobian(X)       # https://docs.sympy.org/latest/modules/matrices/matrices.html#sympy.matrices.matrixbase.MatrixBase.jacobian


    x0 = sp.Matrix(raices)                # https://stackoverflow.com/questions/26669706/evaluating-jacobian-at-specific-points-using-sympy

    for i in range(max_iter): 
        time.sleep(0.09)                              # https://docs.sympy.org/latest/modules/matrices/matrices.html#operations-on-entries
        F_eval =  F_eval = F.subs(dict(zip(varis, x0)))     # https://www.w3schools.com/python/ref_func_zip.asp
        J_eval = J.subs(dict(zip(varis, x0)))

        x1 = x0 - J_eval.inv() * F_eval         # inv() es inversa
        
        if(x1-x0).norm() < margen_e:
            print(f"Converge en la iteracion {i+1}:\n Raiz = {x1}")
            return x1
        x0=x1
        print(f"Iteracion {i+1}: {x1}")

    print("El sistema no converge en 100 iteraciones")
    return x0

