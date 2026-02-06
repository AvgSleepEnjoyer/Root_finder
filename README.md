# Root_finder
Códigos en Python iterativos para buscar raíces reales en ℝ².

Tareas de Análisis Numérico de 5.º semestre.

# Reglas:
- Las ecuaciones tienen que tener una o más raíces reales. 
- Las ecuaciones deberán tener de variable a x. 
- La forma para resolver ecuaciones con igualdad a 0 es introducir su función de una de las siguientes maneras:  
  2*x**2 - x - 2  
  (x**2 - x - 2)/2  
  x*exp(x) - 2*x  

---

## 1. Bisección

Método por Bisección.  
Delimitas un rango, seleccionas el valor máximo y mínimo, evalúas la función en esos valores y encuentras la raíz.  

**Pasos:**
- Escoges un rango [a, b].  
- Evalúas f(a) y f(b).  

Si: f(a) * f(b) < 0 entonces hay raíz.  
Si no la hay, selecciona otro rango de valores.  

- Encuentras el punto medio:  
  m = |a - b| / 2  

- Evalúas f(m).  
  Si f(m) = 0, m es la raíz.  
  Si no, y f(m) tiene signo opuesto a f(a) o a f(b), se redefine el intervalo como [a, m] o [b, m].  

- Repites escogiendo un punto medio para el nuevo [a, b].  

- Terminas las iteraciones cuando se encuentre la raíz, esté dentro de un margen de error seleccionado o dentro de un número máximo de iteraciones.  

---

## 2. Punto Fijo

Método por Punto Fijo.  
Este método requiere una ecuación de la forma x = g(x), normalmente despejada a partir de ecuaciones de grado 2.  

**Pasos:**
- Propones un valor inicial, por ejemplo x = 0, y evalúas g(0) = k.  
- Evalúas esa k en g(x) nuevamente.  
- Repites este proceso n veces o hasta alcanzar un margen de error deseado.  
- El resultado converge hacia un valor que corresponde a la raíz de f(x).  

---

## 3. Newton-Raphson (una variable, una ecuación)

Método por Newton-Raphson.  
Este método sirve para encontrar raíces de una sola ecuación con una sola variable. Se basa en aproximaciones sucesivas usando la derivada de la función.  

**Pasos:**
- Defines la función f(x).  
- Calculas su derivada f'(x).  
- Propones un valor inicial x0.  
- Iteras con la fórmula:  
- x1 = x0 - f(x0)/f'(x0)  
- Repites el proceso hasta que la diferencia |x1 - x0| sea menor que el margen de error seleccionado o hasta llegar al número máximo de iteraciones.  
- El resultado converge hacia la raíz de f(x).
