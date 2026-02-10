import sympy as sp      # https://docs.sympy.org/latest/guides/custom-functions.html
                        # https://docs.sympy.org/latest/explanation/glossary.html#term-sympify
import os
import time

    # sympify transforma un tipo de dato valido a una funcion o expresion usable para sympy  

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


def es_diagonalmente_dominante(A):
    # Verifica si la matriz A es diagonalmente dominante por filas.
    n = A.rows
    for i in range(n):
        suma = sum(abs(A[i, j]) for j in range(n) if j != i)
        if abs(A[i, i]) < suma:
            return False
    return True


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


def gauss_seidel(A, b, x, margen_e, max_iter=100):
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



# Menu
os.system("cls");

print("Que metodo de busqueda de raices necesita:")
print("1. Biseccion")
print("2. Punto fijo")
print("3. Newton-Raphson para una variable")
print("4. Newton-Raphson para sistema de ecuaciones")
print("5. Método de Jacobi")
print("6. Método de Gauss-Seidel")
opcion = int(input("\n"))

match opcion:
    case 1:
        
        funcion = input("Ingresa una funcion en x (ejemplo: x**2 - 3): ")
        a = float(input("Ingresa el extremo izquierdo del intervalo: "))
        b = float(input("Ingresa el extremo derecho del intervalo: "))
        margen_e = float(input("Ingresa el margen de error aceptable (ejemplo: 0.0001): "))

        try:
            raiz = biseccion(funcion, a, b, margen_e)
            print("Raiz aproximada:", raiz)
        except ValueError as e:
            print(e)

    case 2:
        funcion = input("Ingresa la funcion f(x) (ejemplo: x**2 - x - 2): ")
        g_funcion = input("Ingresa la funcion g(x) para la iteración (ejemplo: sqrt(x+2)): ")
        x0 = float(input("Ingresa el valor inicial x0: "))
        margen_e = float(input("Ingresa el margen de error (ejemplo: 0.0001): "))

        raiz = punto_fijo(funcion, g_funcion, x0, margen_e)
        print("\nRaiz aproximada:", raiz)

    case 3:
        funcion = input("Ingresa la funcion f(x) (ejemplo: exp(x) - pi*x): ")
        x0 = float(input("Ingrese un valor inicial x0 (ejemplo: 0): "))
        margen_e = float(input("Ingresa el margen de error (ejemplo: 0.0001): "))

        raiz = newthon_raphson_una_x(funcion, x0, margen_e)
        print("\nRaiz aproximada es:", raiz)

    case 4:
        n_funciones = int(input("Newton-Raphson consiste en encontrar las intersecciones entre n cantidad de ecuaciones\n\nNumero de funciones: "))
        varis = []
        arr = []
        raices = []

        for i in range (n_funciones):
            varis.append(input(f"Variable {i+1}: "))

        print("ejemplo1: (x-2)**2 + (y-1)**2 + x*y -3\nejemplo2: x*exp(x+y) + y -3")
        for i in range (n_funciones):
            arr.append(sp.sympify(input(f"Ingresa la funcion: ")))

        for i in range(n_funciones):
            raices.append(float(input(f"Raiz aproximada de la funcion {i+1}: ")))

        margen_e = float(input("Ingresa el margen de error (ejemplo: 0.0001): "))
        raiz= newthon_raphsons(varis, arr, raices, margen_e)

    case 5:
        n = int(input("Numero de variables: "))
        A = []
        b = []

        print("Introduce la matriz A fila por fila:\nEjemplo: 5 1\n1 4")
        for i in range(n):
            fila = list(map(float, input(f"Fila {i+1}: ").split()))
            A.append(fila)

        print("Introduce el vector b:\nEjemplo: 7\n5")
        for i in range(n):
            bi = float(input(f"b[{i+1}]: "))
            b.append(bi)

        x0 = list(map(float, input("Vector inicial (separado por espacios)\nEjemplo 0 0\n: ").split()))

        A = sp.Matrix(A)
        b = sp.Matrix(b)

        margen_e = float(input("Ingresa el margen de error (ejemplo: 0.0001): "))

        sol = jacobi(A, b, x0, margen_e)
        print("Solucion aproximada:", sol)

    case 6:

        n = int(input("Número de variables: "))
        A = []
        b = []

        print("Introduce la matriz A fila por fila:\nEjemplo: 5 1\n1 4")
        for i in range(n):
            fila = list(map(float, input(f"Fila {i+1}: ").split()))
            A.append(fila)

        print("Introduce el vector b:\nEjemplo: 7\n5")
        for i in range(n):
            bi = float(input(f"b[{i+1}]: "))
            b.append(bi)

        x0 = list(map(float, input("Vector inicial (separado por espacios)\nEjemplo 0 0\n: ").split()))

        A = sp.Matrix(A)
        b = sp.Matrix(b)

        margen_e = float(input("Ingresa el margen de error (ejemplo: 0.0001): "))

        sol = gauss_seidel(A, b, x0, margen_e)
        print("Solucion aproximada:", sol)
