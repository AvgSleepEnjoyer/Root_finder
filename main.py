from modulos import *

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
