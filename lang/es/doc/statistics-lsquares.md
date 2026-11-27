## lsquares

<!-- category: Statistics -->
<!-- keywords: lsquares_estimates -->
<!-- signatures: lsquares_estimates(D, x, e, a), lsquares_estimates(D, x, e, a, initial=L, tol=t) -->
### Function: lsquares_estimates (D, x, e, a)

Estima los parámetros *a* que mejor se ajusten a la ecuación *e*
de variables *x* y *a* a los datos *D* por el método de los
mínimos cuadrados. La función `lsquares_estimates`
busca primero una solución exacta, y si no la encuentra, buscará
una aproximada.


El resultado es una lista de listas de ecuaciones de la forma
`[a = ..., b = ..., c = ...]`. Cada elemento de la lista es un
mínimo diferente de error cuadrático medio.


Los datos deben darse en formato matricial. Cada fila es un dato (el cual suele
denominarse ‘registro’ o ‘caso’ en ciertos contextos), y las columnas contienen los
valores para cada una de las variables. La lista de variables *x* asigna un nombre
a cada una de las columnas de *D*, incluso a aquellas que no intervienen en el
análisis. La lista *a* asigna nombres a los parámetros cuyas estimaciones se
buscan. El argumento *e* es una expresión o ecuación de variables *x* y *a*;
si *e* no es una ecuación (es decir, carece de igualdad), se trata como si 
fuese  `e = 0`.


Se pueden dar argumentos adicionales a `lsquares_estimates` en forma de ecuaciones,
las cuales se pasan tal cual a la función `lbfgs`, que es la que se encarga de
calcular las estimaciones por el método numérico cuando no encuentra una
solución exacta.


Cuando se pueda encontrar una solución exacta, mediante `solve`, los datos
en *D* pueden contener valores no numéricos. Sin embargo, cuando no exista
solución exacta, todos los elementos de *D* deben ser necesariamente
numéricos, lo cual incluye constantes numéricas tales como `%pi` o `%e`
y números literales (enteros, racionales y decimales en coma flotante, tanto los de doble 
precisión como los de precisión arbitraria).
Los cálculos numéricos se realizan en doble precisión con aritmética de
punto flotante, por lo que números de cualesquiera otro tipo son 
convenientemente convertidos antes de proceder con los cálculos.


Antes de utilizar esta función ejecútese `load("lsquares")`.


Véanse también
`lsquares_estimates_exact`,
`lsquares_estimates_approximate`,
`lsquares_mse`,
`lsquares_residuals`
y `lsquares_residual_mse`.


Ejemplos:


Un problema con solución exacta.










```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
        [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                                  [ 1  1  1 ]
                                  [         ]
                                  [ 3       ]
                                  [ -  1  2 ]
                                  [ 2       ]
                                  [         ]
(%o2)                             [ 9       ]
                                  [ -  2  1 ]
                                  [ 4       ]
                                  [         ]
                                  [ 3  2  2 ]
                                  [         ]
                                  [ 2  2  1 ]
(%i3) lsquares_estimates (
         M, [z,x,y], (z+D)^2 = A*x+B*y+C, [A,B,C,D]);
                         59        27      10921        107
(%o3)            [[A = - --, B = - --, C = -----, D = - ---]]
                         16        16      1024         32
```


un problema para el que no se encuentra solución exacta,
por lo que `lsquares_estimates` recurre a la aproximación numérica.









```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix ([1, 1], [2, 7/4], [3, 11/4], [4, 13/4]);
                                   [ 1  1  ]
                                   [       ]
                                   [    7  ]
                                   [ 2  -  ]
                                   [    4  ]
                                   [       ]
(%o2)                              [    11 ]
                                   [ 3  -- ]
                                   [    4  ]
                                   [       ]
                                   [    13 ]
                                   [ 4  -- ]
                                   [    4  ]
(%i3) lsquares_estimates (
  M, [x,y], y=a*x^b+c, [a,b,c], initial=[3,3,3], iprint=[-1,0]);
(%o3) [[a = 1.387365874920637, b = .7110956639593767, 
                                        c = - .4142705622439105]]
```

<!-- category: Statistics -->
<!-- keywords: lsquares_estimates_approximate -->
<!-- signatures: lsquares_estimates_approximate(MSE, a, initial=L, tol=t) -->
### Function: lsquares_estimates_approximate (MSE, a, initial=L, tol=t)

Estima los valores de los parámetros *a* que minimizan el error
cuadrático medio *MSE* mediante el algoritmo numérico `lbfgs`.
El error cuadrático medio es una expresión con parámetros *a*,
como los devueltos por `lsquares_mse`.


La solución devuelta por la función es un mínimo local
(posiblemente global) del error cuadrático medio.


Por consistencia con `lsquares_estimates_exact`, el valor devuelto
es una lista anidada con un único elemento, consistente en una lista
de ecuaciones de la forma `[a = ..., b = ..., c = ...]`.


Los argumentos adicionales de `lsquares_estimates_approximate`
se especifican como ecuaciones y se pasan de esta forma a la función `lbfgs`.


*MSE* debe devolver un número cuando a sus parámetros se les
asignen valores numéricos, lo cual implica que los datos a partir de los
cuales se ha generado *MSE* contengan únicamente constantes numéricas 
tales como `%pi` o `%e` y números literales (enteros, racionales y 
decimales en coma flotante, tanto los de doble 
precisión como los de precisión arbitraria).
Los cálculos numéricos se realizan en doble precisión con aritmética de
punto flotante, por lo que números de cualesquiera otro tipo son 
convenientemente convertidos antes de proceder con los cálculos.


Antes de utilizar esta función ejecútese `load("lsquares")`.


Véanse también
`lsquares_estimates`,
`lsquares_estimates_exact`,
`lsquares_mse`,
`lsquares_residuals` y `lsquares_residual_mse`.


Ejemplo:











```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]
(%i3) mse : lsquares_mse (M, [z, x, y], (z + D)^2 = A*x + B*y + C);
           5
          ====
          \                 2                         2
           >    ((D + M    )  - C - M     B - M     A)
          /            i, 1          i, 3      i, 2
          ====
          i = 1
(%o3)     ---------------------------------------------
                                5
(%i4) lsquares_estimates_approximate (
              mse, [A, B, C, D], iprint = [-1, 0]);
(%o4) [[A = - 3.67850494740174, B = - 1.683070351177813, 
                 C = 10.63469950148635, D = - 3.340357993175206]]
```

<!-- category: Statistics -->
<!-- keywords: lsquares_estimates_exact -->
<!-- signatures: lsquares_estimates_exact(MSE, a) -->
### Function: lsquares_estimates_exact (MSE, a)

Estima los valores de los parámetros *a* que minimizan el error
cuadrático medio *MSE* mediante un sistema de ecuaciones que intentará
resolver simbólicamente con `solve`. El error cuadrático medio es una
expresión con parámetros *a*, como los devueltos por `lsquares_mse`.


El valor devuelto por la función es una lista de listas de ecuaciones de la 
forma `[a = ..., b = ..., c = ...]`. El resultado puede contener cero, uno o
más elementos. Cuando la respuesta contiene más de una solución, todas ellas
representan mínimos del error cuadrático medio.


Véanse también
`lsquares_estimates`,
`lsquares_estimates_approximate`,
`lsquares_mse`,
`lsquares_residuals`
y `lsquares_residual_mse`.


Ejemplo:










```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]
(%i3) mse : lsquares_mse (M, [z, x, y], (z + D)^2 = A*x + B*y + C);
           5
          ====
          \                 2                         2
           >    ((D + M    )  - C - M     B - M     A)
          /            i, 1          i, 3      i, 2
          ====
          i = 1
(%o3)     ---------------------------------------------
                                5
(%i4) lsquares_estimates_exact (mse, [A, B, C, D]);
                  59        27      10921        107
(%o4)     [[A = - --, B = - --, C = -----, D = - ---]]
                  16        16      1024         32
```

<!-- category: Statistics -->
<!-- keywords: lsquares_mse -->
<!-- signatures: lsquares_mse(D, x, e) -->
### Function: lsquares_mse (D, x, e)

Devuelve el error medio cuadrático (MSE) para la ecuación *e*
de variables *x* respecto de los datos *D*. El resultado devuelto
es una suma, definida como



$$
{1 \over n} \, \sum_{i=1}^n \left[{\rm lhs}\left(e_i\right) - {\rm rhs}\left(e_i\right)\right]^2,
$$


```maxima
n
                   ====
               1   \                        2
               -    >    (lhs(e ) - rhs(e ))
               n   /           i         i
                   ====
                   i = 1
```



siendo *n* el número de datos y `e[i]` es la ecuación *e*
evaluada cuando a sus variables *x* se le asignan los valores asociados
al dato `i`-ésimo `D[i]`.


Antes de utilizar esta función ejecútese `load("lsquares")`.


Ejemplo:











```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]
(%i3) mse : lsquares_mse (M, [z, x, y], (z + D)^2 = A*x + B*y + C);
           5
          ====
          \                 2                         2
           >    ((D + M    )  - C - M     B - M     A)
          /            i, 1          i, 3      i, 2
          ====
          i = 1
(%o3)     ---------------------------------------------
                                5
(%i4) diff (mse, D);
         5
        ====
        \                             2
      4  >    (D + M    ) ((D + M    )  - C - M     B - M     A)
        /           i, 1         i, 1          i, 3      i, 2
        ====
        i = 1
(%o4) ----------------------------------------------------------
                                  5
(%i5) ''mse, nouns;
               2                 2         9 2               2
(%o5) (((D + 3)  - C - 2 B - 2 A)  + ((D + -)  - C - B - 2 A)
                                           4
           2               2         3 2               2
 + ((D + 2)  - C - B - 2 A)  + ((D + -)  - C - 2 B - A)
                                     2
           2             2
 + ((D + 1)  - C - B - A) )/5
```

<!-- category: Statistics -->
<!-- keywords: lsquares_residual_mse -->
<!-- signatures: lsquares_residual_mse(D, x, e, a) -->
### Function: lsquares_residual_mse (D, x, e, a)

Devuelve el residuo del error cuadrático medio (MSE) de la ecuación *e*
para los valores parámetricos *a* y datos *D*.


El residuo del error cuadrático medio (MSE) se define como



$$
{1 \over n} \, \sum_{i=1}^n \left[{\rm lhs}\left(e_i\right) - {\rm rhs}\left(e_i\right)\right]^2,
$$


```maxima
n
                   ====
               1   \                        2
               -    >    (lhs(e ) - rhs(e ))
               n   /           i         i
                   ====
                   i = 1
```



siendo `e[i]` la ecuación *e* evaluada cuando las variables *x*
toman los valores asociados al dato `i`-ésimo `D[i]`, y haciendo las
asignaciones indicadas en *a* al resto de variables.


Antes de utilizar esta función ejecútese `load("lsquares")`.


Ejemplo:












```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                           [ 1  1  1 ]
                           [         ]
                           [ 3       ]
                           [ -  1  2 ]
                           [ 2       ]
                           [         ]
(%o2)                      [ 9       ]
                           [ -  2  1 ]
                           [ 4       ]
                           [         ]
                           [ 3  2  2 ]
                           [         ]
                           [ 2  2  1 ]
(%i3) a : lsquares_estimates (
             M, [z,x,y], (z+D)^2 = A*x+B*y+C, [A,B,C,D]);

                  59        27      10921        107
(%o3)     [[A = - --, B = - --, C = -----, D = - ---]]
                  16        16      1024         32
(%i4) lsquares_residual_mse (
             M, [z,x,y], (z + D)^2 = A*x + B*y + C, first (a));
                              169
(%o4)                         ----
                              2560
```

<!-- category: Statistics -->
<!-- keywords: lsquares_residuals -->
<!-- signatures: lsquares_residuals(D, x, e, a) -->
### Function: lsquares_residuals (D, x, e, a)

Devuelve los residuos para la ecuación *e* de parámetros *a*
y datos *D*.


*D* es una matriz, *x* una lista de variables y *e* es una ecuación
o expresión general; si *e* no es una ecuación (es decir, carece de igualdad),
se trata como si fuese  `e = 0`. La lista *a* contiene ecuaciones
que especifican valores para cualesquiera parámetros de *e* que no estén en *x*.


Los residuos se definen como



$$
{\rm lhs}\left(e_i\right) - {\rm rhs}\left(e_i\right),
$$


```maxima
lhs(e ) - rhs(e )
                             i         i
```


siendo `e[i]` la ecuación *e* evaluada cuando las variables *x*
toman los valores asociados al dato `i`-ésimo `D[i]`, y haciendo las
asignaciones indicadas en *a* al resto de variables.


Antes de utilizar esta función ejecútese `load("lsquares")`.


Ejemplo:












```maxima
(%i1) load ("lsquares")$
(%i2) M : matrix (
         [1,1,1], [3/2,1,2], [9/4,2,1], [3,2,2], [2,2,1]);
                                  [ 1  1  1 ]
                                  [         ]
                                  [ 3       ]
                                  [ -  1  2 ]
                                  [ 2       ]
                                  [         ]
(%o2)                             [ 9       ]
                                  [ -  2  1 ]
                                  [ 4       ]
                                  [         ]
                                  [ 3  2  2 ]
                                  [         ]
                                  [ 2  2  1 ]
(%i3) a : lsquares_estimates (
          M, [z,x,y], (z+D)^2 = A*x+B*y+C, [A,B,C,D]);
                         59        27      10921        107
(%o3)            [[A = - --, B = - --, C = -----, D = - ---]]
                         16        16      1024         32
(%i4) lsquares_residuals (
          M, [z,x,y], (z+D)^2 = A*x+B*y+C, first(a));
                            13    13    13  13  13
(%o4)                      [--, - --, - --, --, --]
                            64    64    32  64  64
```

<!-- category: Statistics -->
<!-- keywords: plsquares -->
<!-- signatures: plsquares(Mat, VarList, depvars), plsquares(Mat, VarList, depvars, maxexpon), plsquares(Mat, VarList, depvars, maxexpon, maxdegree) -->
### Function: plsquares (Mat, VarList, depvars)

Ajuste de una función polinómica multivariante a una tabla de datos por el método
de los *mínimos cuadrados*. *Mat* es la matriz con los datos 
empíricos, *VarList* es la lista con los nombres de las variables
(una por cada columna de *Mat*, pero puede usarse `-` en lugar de los nombres de
variables para ignorar las columnas de *Mat*), *depvars* es el nombre de la
variable dependiente o una lista con uno o más nombres de variables dependientes
(cuyos nombres deben estar también en *VarList*), *maxexpon* es un argumento
opcional para indicar el máximo exponente para cada una de las variables independientes
(1 por defecto) y  *maxdegree* es otro argumento opcional para el grado del polinomio
(*maxexpon* por defecto); nótese que la suma de exponentes de cada término debe ser
igual o menor que *maxdegree*. Si `maxdgree = 0` entonces no se aplicará
ningún límite.


Si *depvars* es el nombre de una variable dependiente (no en una lista),
`plsquares` devuelve el polinomio ajustado. Si *depvars* es una lista
de una o más variables dependientes, `plsquares` devuelve una lista con
los polinomios ajustados. Los coeficientes de determinación se muestran en
su orden correspondiente para informar sobre la bondad del ajuste. Estos
valores se almacenan también en la variable global *DETCOEF* en un
formato de lista si *depvars* es a su vez una lista.


Un ejemplo sencillo de ajuste lineal multivariante:



```maxima
(%i1) load("plsquares")$

(%i2) plsquares(matrix([1,2,0],[3,5,4],[4,7,9],[5,8,10]),
                [x,y,z],z);
     Determination Coefficient for z = .9897039897039897
                       11 y - 9 x - 14
(%o2)              z = ---------------
                              3
```


El mismo ejemplo sin restricciones en el grado:



```maxima
(%i3) plsquares(matrix([1,2,0],[3,5,4],[4,7,9],[5,8,10]),
                [x,y,z],z,1,0);
     Determination Coefficient for z = 1.0
                    x y + 23 y - 29 x - 19
(%o3)           z = ----------------------
                              6
```


Cálculo del número de diagonales de un polígono de $N$ lados



```maxima
(%i4) plsquares(matrix([3,0],[4,2],[5,5],[6,9],[7,14],[8,20]),
                [N,diagonals],diagonals,5);
     Determination Coefficient for diagonals = 1.0
                                2
                               N  - 3 N
(%o4)              diagonals = --------
                                  2
(%i5) ev(%, N=9);   /* Testing for a 9 sides polygon */
(%o5)                 diagonals = 27
```


Cálculo del número de formas de colocar dos reinas en un tablero 
n x n de manera que no se amenacen.



```maxima
(%i6) plsquares(matrix([0,0],[1,0],[2,0],[3,8],[4,44]),
                [n,positions],[positions],4);
     Determination Coefficient for [positions] = [1.0]
                         4       3      2
                      3 n  - 10 n  + 9 n  - 2 n
(%o6)    [positions = -------------------------]
                                  6
(%i7) ev(%[1], n=8); /* Testing for a (8 x 8) chessboard */
(%o7)                positions = 1288
```


Un ejemplo con seis variables dependientes:



```maxima
(%i8) mtrx:matrix([0,0,0,0,0,1,1,1],[0,1,0,1,1,1,0,0],
                  [1,0,0,1,1,1,0,0],[1,1,1,1,0,0,0,1])$
(%i8) plsquares(mtrx,[a,b,_And,_Or,_Xor,_Nand,_Nor,_Nxor],
                     [_And,_Or,_Xor,_Nand,_Nor,_Nxor],1,0);
      Determination Coefficient for
[_And, _Or, _Xor, _Nand, _Nor, _Nxor] =
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
(%o2) [_And = a b, _Or = - a b + b + a,
_Xor = - 2 a b + b + a, _Nand = 1 - a b,
_Nor = a b - b - a + 1, _Nxor = 2 a b - b - a + 1]
```


Antes de hacer uso de esta función ejecútese  `load("plsquares")`.

