# Root_finder
Codigos en python iterativos para buscar raices.

Tareas de Analisis Numerico de 5to semestre.

1. Bisex-ion

Metodo por Biseccion.
Delimitas un rango, seleccionas el valor Max y min, evaluas la funcion en esos valores y encuentras la raiz.
Pasos:

-Escoges un rango [a,b]
-Evaluas f(a) y f(b) 

si: f(a) * f(b)<0 entonces hay raiz         si no la hay, agarra otro rango de valores

-Encontrar el punto medio
m = |a-b|/2

-Evaluas f(m)   Si: f(m)=0, m es la raiz, sino...
Si f(m) tiene signo opuesto f(a) ó a f(b) se redefine el intervalo como [a,m] o [b,m]

-Repites escogiendo un punto medio para el nuevo [a,b]

-Termina las iteraciones cuando encuentre la raiz, este dentro de un margen de error seleccionado o dentro de un numero de iteraciones

2. Punto fijo

Metodo por Punto Fijo
Este metodo requiere una ecuacion x=g(x), requiere despejar en ecuaciones de grado 2

-Propones un valor inicial x=0, evaluas en g(0) = k
-Evaluas esa k en g(x) nuevamente
-Repite esto n veces necesarias o hasta cierto margen de error
-El resultado se crea una asintota en el valor de la raiz de f(x)