## simplex

<!-- category: Numerical -->
<!-- keywords: epsilon_lp -->
<!-- signatures: epsilon_lp -->
### Variable: epsilon_lp

Valor por defecto: `10^-8`


Error epsilon utilizado en los cálculos numéricos de `linear_program`.


Véase también `linear_program`.

<!-- category: Numerical -->
<!-- keywords: linear_program -->
<!-- signatures: linear_program(A, b, c) -->
### Function: linear_program (A, b, c)

La función `linear_program` es una implementación del algoritmo
simplex. La instrucción `linear_program(A, b, c)` calcula un 
vector *x* tal que minimiza `c.x` bajo las restricciones `A.x = b`
y `x >= 0`. El argumento *A* es una matriz y los argumentos *b* y
*c* son listas.


La función `linear_program` devuelve una lista que contiene el vector
solución *x* y el valor mínimo de `c.x`.
Si el problema no está acotado, devuelve el mensaje "Problem not bounded!"
y si el problema no es factible, devuelve el mensaje "Problem not feasible!".


Para usar esta función, cárguese primero el paquete con la
instrucción `load("simplex");`.


Ejemplo:










```maxima
(%i2) A: matrix([1,1,-1,0], [2,-3,0,-1], [4,-5,0,0])$
(%i3) b: [1,1,6]$
(%i4) c: [1,-2,0,0]$
(%i5) linear_program(A, b, c);
                   13     19        3
(%o5)            [[--, 4, --, 0], - -]
                   2      2         2
```


Véanse también `minimize_lp`, `scale_lp` y `epsilon_lp`.

<!-- category: Numerical -->
<!-- keywords: maximize_lp -->
<!-- signatures: maximize_lp(obj, cond, [pos]) -->
### Function: maximize_lp (obj, cond, [pos])

Maximiza la función objetivo lineal *obj* sujeta a ciertas restricciones
lineales *cond*. Véase `minimize_lp` para una descripción detallada
de los argumentos y de la respuesta dada por esta función.

<!-- category: Numerical -->
<!-- keywords: minimize_lp -->
<!-- signatures: minimize_lp(obj, cond, [pos]) -->
### Function: minimize_lp (obj, cond, [pos])

Minimiza la función objetivo lineal *obj* sujeta a ciertas restricciones
lineales *cond*, siendo ésta una lista de ecuaciones o inecuaciones lineales.
En las inecuaciones estrictas se reemplaza `>` por `>=` y `<`
por `<=`. El argumento opcional *pos* es una lista de variables de
decisión que se suponen positivas.


Si el mínimo existe, `minimize_lp` devuelve una lista que
contiene el valor mínimo de la función objetivo y una lista 
de valores para las variables de decisión con los que se alcanza el 
mínimo. 
Si el problema no está acotado, devuelve el mensaje "Problem not bounded!"
y si el problema no es factible, devuelve el mensaje "Problem not feasible!".


Las variables de decisión no se suponen no negativas. Si todas las 
variables de decisión son no negativas, asígnese el valor
`true` a la variable `nonegative_lp`. Si sólo algunas de las
variables de decisión son positivas, lístense
en el argumento opcional *pos*, lo cual es más eficiente que 
añadir restricciones.


La función `minimize_lp` utiliza el algoritmo simplex implementado
en la función `linear_program` de Maxima.


Para usar esta función, cárguese primero el paquete con la
instrucción `load("simplex");`.


Ejemplos:









```maxima
(%i1) minimize_lp(x+y, [3*x+y=0, x+2*y>2]);
                      4       6        2
(%o1)                [-, [y = -, x = - -]]
                      5       5        5
(%i2) minimize_lp(x+y, [3*x+y>0, x+2*y>2]), nonegative_lp=true;
(%o2)                [1, [y = 1, x = 0]]
(%i3) minimize_lp(x+y, [3*x+y=0, x+2*y>2]), nonegative_lp=true;
(%o3)                Problem not feasible!
(%i4) minimize_lp(x+y, [3*x+y>0]);
(%o4)                Problem not bounded!
```



Véanse también `maximize_lp`, `nonegative_lp` y `epsilon_lp`.

<!-- category: Numerical -->
<!-- keywords: nonegative_lp -->
<!-- signatures: nonegative_lp -->
### Variable: nonegative_lp

Valor por defecto: `false`


Si `nonegative_lp` vale `true` todas las variables de decisión
pasadas a `minimize_lp` y a `maximize_lp` se suponen positivas.


Véase también `minimize_lp`.

