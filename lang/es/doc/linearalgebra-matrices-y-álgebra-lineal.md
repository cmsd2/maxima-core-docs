## Matrices y Álgebra Lineal

<!-- category: LinearAlgebra -->
<!-- keywords: addcol -->
<!-- signatures: addcol(M, lista_1, ..., lista_n) -->
### Function: addcol (M, lista_1, ..., lista_n)

Añade la/s columna/s dada/s por la/s lista/s (o matrices) a la matriz *M*.

<!-- category: LinearAlgebra -->
<!-- keywords: addrow -->
<!-- signatures: addrow(M, lista_1, ..., lista_n) -->
### Function: addrow (M, lista_1, ..., lista_n)

Añade la/s fila/s dada/s por la/s lista/s (o matrices) a la matriz *M*.

<!-- category: LinearAlgebra -->
<!-- keywords: adjoint -->
<!-- signatures: adjoint(M) -->
### Function: adjoint (M)

Devuelve el adjunto de la matriz *M*.
La matriz adjunta es la transpuesta de la matriz de cofactores de *M*.

<!-- category: LinearAlgebra -->
<!-- keywords: augcoefmatrix -->
<!-- signatures: augcoefmatrix([eqn_1, ..., eqn_m], [x_1, ..., x_n]) -->
### Function: augcoefmatrix ([eqn_1, ..., eqn_m], [x_1, ..., x_n])

Devuelve la matriz aumentada de coeficientes del sistema de ecuaciones lineales 
*eqn_1*, ..., *eqn_m* de variables *x_1*, ..., *x_n*. Se trata de la
matriz de coeficientes con una columna adicional para los términos constantes de cada
ecuación, es decir, aquellos términos que no dependen de las variables
*x_1*, ..., *x_n*.



```maxima
(%i1) m: [2*x - (a - 1)*y = 5*b, c + b*y + a*x = 0]$
(%i2) augcoefmatrix (m, [x, y]);
                       [ 2  1 - a  - 5 b ]
(%o2)                  [                 ]
                       [ a    b      c   ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: cauchy_matrix -->
<!-- signatures: cauchy_matrix([x_1, x_2, ..., x_m], [y_1, y_2, ..., y_n]), cauchy_matrix([x_1, x_2, ..., x_n]) -->
### Function: cauchy_matrix ([x_1, x_2, ..., x_m], [y_1, y_2, ..., y_n])

Devuelve una matriz de Cauchy *n* by *m* de elementos
*a[i,j]* = 1/(*x_i*+*y_i*).
El segundo elemento de `cauchy_matrix` es opcional, y en caso
de no estar presente, los elementos serán de la forma
*a[i,j]* = 1/(*x_i*+*x_j*).


Observación: en la literatura, la matriz de Cauchy se define a veces
con sus elementos de la forma *a[i,j]* = 1/(*x_i*-*y_i*).


Ejemplos:







```maxima
(%i1) cauchy_matrix([x1,x2],[y1,y2]);
                      [    1        1    ]
                      [ -------  ------- ]
                      [ y1 + x1  y2 + x1 ]
(%o1)                 [                  ]
                      [    1        1    ]
                      [ -------  ------- ]
                      [ y1 + x2  y2 + x2 ]

(%i2) cauchy_matrix([x1,x2]);
                      [   1         1    ]
                      [  ----    ------- ]
                      [  2 x1    x2 + x1 ]
(%o2)                 [                  ]
                      [    1       1     ]
                      [ -------   ----   ]
                      [ x2 + x1   2 x2   ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: charpoly -->
<!-- signatures: charpoly(M, x) -->
### Function: charpoly (M, x)

Calcula el polinomio característico de la matriz *M*
respecto de la variable *x*. Esto es, 
`determinant (M - diagmatrix (length (M), x))`.



```maxima
(%i1) a: matrix ([3, 1], [2, 4]);
                            [ 3  1 ]
(%o1)                       [      ]
                            [ 2  4 ]
(%i2) expand (charpoly (a, lambda));
                           2
(%o2)                lambda  - 7 lambda + 10
(%i3) (programmode: true, solve (%));
(%o3)               [lambda = 5, lambda = 2]
(%i4) matrix ([x1], [x2]);
                             [ x1 ]
(%o4)                        [    ]
                             [ x2 ]
(%i5) ev (a . % - lambda*%, %th(2)[1]);
                          [ x2 - 2 x1 ]
(%o5)                     [           ]
                          [ 2 x1 - x2 ]
(%i6) %[1, 1] = 0;
(%o6)                     x2 - 2 x1 = 0
(%i7) x2^2 + x1^2 = 1;
                            2     2
(%o7)                     x2  + x1  = 1
(%i8) solve ([%th(2), %], [x1, x2]);
                  1               2
(%o8) [[x1 = - -------, x2 = - -------], 
               sqrt(5)         sqrt(5)

                                             1             2
                                    [x1 = -------, x2 = -------]]
                                          sqrt(5)       sqrt(5)
```

<!-- category: LinearAlgebra -->
<!-- keywords: coefmatrix -->
<!-- signatures: coefmatrix([eqn_1, ..., eqn_m], [x_1, ..., x_n]) -->
### Function: coefmatrix ([eqn_1, ..., eqn_m], [x_1, ..., x_n])

Devuelve la matriz de coeficientes para las variables *x_1*, ..., *x_n*
del sistema de ecuaciones lineales *eqn_1*, ..., *eqn_m*.



```maxima
(%i1) coefmatrix([2*x-(a-1)*y+5*b = 0, b*y+a*x = 3], [x,y]);
                                 [ 2  1 - a ]
(%o1)                            [          ]
                                 [ a    b   ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: col -->
<!-- signatures: col(M, i) -->
### Function: col (M, i)

Devuelve la *i*-ésima columna de la matriz *M*.
El resultado es una matriz de una sola columna.

<!-- category: LinearAlgebra -->
<!-- keywords: columnvector, covect -->
<!-- signatures: columnvector(L), covect(L) -->
### Function: columnvector (L)

Devuelve una matriz con una columna  y `length (L)` filas,
conteniendo los elementos de la lista *L*.


La llamada `covect` es un sinónimo de `columnvector`.


Es necesario cargar la función haciendo `load ("eigen")`.



Ejemplo:





```maxima
(%i1) load ("eigen")$
Warning - you are redefining the Macsyma function eigenvalues
Warning - you are redefining the Macsyma function eigenvectors
(%i2) columnvector ([aa, bb, cc, dd]);
                             [ aa ]
                             [    ]
                             [ bb ]
(%o2)                        [    ]
                             [ cc ]
                             [    ]
                             [ dd ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: copymatrix -->
<!-- signatures: copymatrix(M) -->
### Function: copymatrix (M)

Devuelve una copia de la matriz *M*. Esta es la única
manera de obtener una réplica de *M* además de la de
copiar elemento a elemento.


Nótese que una asignación de una matriz a otra, como en `m2: m1`,
no hace una copia de `m1`. Asignaciones del tipo `m2 [i,j]: x` o
`setelmx (x, i, j, m2` también modifica `m1 [i,j]`. Si se crea una copia 
con `copymatrix` y luego se hacen asignaciones se tendrá una copia separada y
modificada.

<!-- category: LinearAlgebra -->
<!-- keywords: determinant -->
<!-- signatures: determinant(M) -->
### Function: determinant (M)

Calcula el determinante de  *M* por un método similar al
de eliminación de Gauss



La forma del resultado depende del valor asignado
a `ratmx`.



Existe una rutina especial para calcular determinantes de matrices con elementos dispersas, la cual
será invocada cuando las variables `ratmx` y `sparse` valgan ambas
`true`.

<!-- category: LinearAlgebra -->
<!-- keywords: detout -->
<!-- signatures: detout -->
### Variable: detout

Valor por defecto: `false`


Cuando `detout` vale `true`, el determinante de la matriz 
cuya inversa se calcula aparece como un factor fuera de la matriz.


Para que esta variable surta efecto, `doallmxops` y `doscmxops` deberían tener
el valor `false` (véanse sus descripciones). Alternativamente, esta 
variable puede ser suministrada a `ev`.


Ejemplo:



```maxima
(%i1) m: matrix ([a, b], [c, d]);
                            [ a  b ]
(%o1)                       [      ]
                            [ c  d ]
(%i2) detout: true$
(%i3) doallmxops: false$
(%i4) doscmxops: false$
(%i5) invert (m);
                          [  d   - b ]
                          [          ]
                          [ - c   a  ]
(%o5)                     ------------
                           a d - b c
```

<!-- category: LinearAlgebra -->
<!-- keywords: diagmatrix -->
<!-- signatures: diagmatrix(n, x) -->
### Function: diagmatrix (n, x)

Devuelve una matriz diagonal de orden *n* 
con los elementos de la diagonal todos ellos iguales a *x*. La llamada
`diagmatrix (n, 1)` devuelve una matriz identidad
(igual que `ident (n)`).


La variable *n* debe ser un número entero, en caso contrario `diagmatrix` envía un mensaje de error.


*x* puede ser cualquier tipo de expresión, incluso otra matriz.
Si *x* es una matriz, no se copia; todos los elementos de la diagonal son iguales a *x*.

<!-- category: LinearAlgebra -->
<!-- keywords: doallmxops -->
<!-- signatures: doallmxops -->
### Variable: doallmxops

Valor por defecto: `true`


Cuando `doallmxops` vale `true`,
todas las operaciones relacionadas con matrices son
llevadas a cabo. Cuando es `false`, entonces las
selecciones para `dot` controlan las operaciones a ejecutar.

<!-- category: LinearAlgebra -->
<!-- keywords: domxexpt -->
<!-- signatures: domxexpt -->
### Variable: domxexpt

Valor por defecto: `true`


Cuando `domxexpt` vale `true`,
un exponente matricial, como `exp (M)` donde *M* es
una matriz, se interpreta como una matriz cuyo elemento `[i,j` es
igual a `exp (m[i,j])`. En otro caso, `exp (M)` se
evalúa como `exp (ev(M))`.


La variable `domxexpt` afecta a todas las expresiones de la forma `base^exponente`
donde *base* es una expresión escalar o constante y *exponente* es una
lista o matriz.


Ejemplo:



```maxima
(%i1) m: matrix ([1, %i], [a+b, %pi]);
                         [   1    %i  ]
(%o1)                    [            ]
                         [ b + a  %pi ]
(%i2) domxexpt: false$
(%i3) (1 - c)^m;
                             [   1    %i  ]
                             [            ]
                             [ b + a  %pi ]
(%o3)                 (1 - c)
(%i4) domxexpt: true$
(%i5) (1 - c)^m;
                  [                      %i  ]
                  [    1 - c      (1 - c)    ]
(%o5)             [                          ]
                  [        b + a         %pi ]
                  [ (1 - c)       (1 - c)    ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: domxmxops -->
<!-- signatures: domxmxops -->
### Variable: domxmxops

Valor por defecto: `true`


Cuando `domxmxops` vale `true`, se realizan todas las operaciones entre
matrices o entre matrices y listas (pero no las operaciones 
entre matrices y escalares); si esta variable es `false` tales
operaciones no se realizan.

<!-- category: LinearAlgebra -->
<!-- keywords: domxnctimes -->
<!-- signatures: domxnctimes -->
### Variable: domxnctimes

Valor por defecto: `false`


Cuando `domxnctimes` vale `true`, se calculan los productos
no conmutativos entre matrices.

<!-- category: LinearAlgebra -->
<!-- keywords: dontfactor -->
<!-- signatures: dontfactor -->
### Variable: dontfactor

Valor por defecto: `[]`


En `dontfactor` puede guardarse una lista de variables respecto de
las cuales no se realizarán factorizaciones. Inicialmente, la lista
está vacía.

<!-- category: LinearAlgebra -->
<!-- keywords: doscmxops -->
<!-- signatures: doscmxops -->
### Variable: doscmxops

Valor por defecto: `false`


Cuando `doscmxops` vale `true`, se realizan las operaciones entre escalares y 
matrices.

<!-- category: LinearAlgebra -->
<!-- keywords: doscmxplus -->
<!-- signatures: doscmxplus -->
### Variable: doscmxplus

Valor por defecto: `false`


Cuando `doscmxplus` vale `true`, las operaciones entre
escalares y matrices dan como resultado una matriz.

<!-- category: LinearAlgebra -->
<!-- keywords: dot0nscsimp -->
<!-- signatures: dot0nscsimp -->
### Variable: dot0nscsimp

Valor por defecto: `true`



(Esta descripción no está clara en la versión inglesa original.)

<!-- category: LinearAlgebra -->
<!-- keywords: dotassoc -->
<!-- signatures: dotassoc -->
### Variable: dotassoc

Valor por defecto: `true`


Cuando `dotassoc` vale `true`, una expresión como `(A.B).C` se transforma en
`A.(B.C)`.

<!-- category: LinearAlgebra -->
<!-- keywords: dotconstrules -->
<!-- signatures: dotconstrules -->
### Variable: dotconstrules

Valor por defecto: `true`


Cuando `dotconstrules` vale `true`, un producto no conmutativo de una
constante con otro término se transforma en un producto conmutativo.

<!-- category: LinearAlgebra -->
<!-- keywords: dotdistrib -->
<!-- signatures: dotdistrib -->
### Variable: dotdistrib

Valor por defecto: `false`


Cuando `dotdistrib` vale `true`, una expresión como `A.(B + C)` se transforma en `A.B + A.C`.

<!-- category: LinearAlgebra -->
<!-- keywords: dotexptsimp -->
<!-- signatures: dotexptsimp -->
### Variable: dotexptsimp

Valor por defecto: `true`


Cuando `dotexptsimp` vale `true`, una expresión como `A.A` se transforma en `A^^2`.

<!-- category: LinearAlgebra -->
<!-- keywords: dotident -->
<!-- signatures: dotident -->
### Variable: dotident

Valor por defecto: 1


El valor de la variable `dotident` es el resultado devuelto por `X^^0`.

<!-- category: LinearAlgebra -->
<!-- keywords: dotscrules -->
<!-- signatures: dotscrules -->
### Variable: dotscrules

Valor por defecto: `false`


Cuando `dotscrules` vale `true`, una expresión como `A.SC` o `SC.A` se transforma 
en `SC*A` y `A.(SC*B)` en `SC*(A.B)`.

<!-- category: LinearAlgebra -->
<!-- keywords: echelon -->
<!-- signatures: echelon(M) -->
### Function: echelon (M)

Devuelve la forma escalonada de la matriz *M*, obtenida por eliminación gaussiana.
La forma escalonada se calcula a partir de *M* mediante operaciones elementales con sus filas,
de tal manera que el primer elemento no nulo de cada fila en la matriz 
resultado es la unidad y que cada elemento de la columna por debajo del primer uno de cada
fila sean todos ceros.


La función `triangularize` también lleva a cabo la eliminación gaussiana, pero no 
normaliza el primer elemento no nulo de cada fila.


Otras funciones, como `lu_factor` y `cholesky`, también dan como resultados
matrices triangularizadas.







```maxima
(%i1) M: matrix ([3, 7, aa, bb], [-1, 8, 5, 2], [9, 2, 11, 4]);
                       [  3   7  aa  bb ]
                       [                ]
(%o1)                  [ - 1  8  5   2  ]
                       [                ]
                       [  9   2  11  4  ]
(%i2) echelon (M);
                  [ 1  - 8  - 5      - 2     ]
                  [                          ]
                  [         28       11      ]
                  [ 0   1   --       --      ]
(%o2)             [         37       37      ]
                  [                          ]
                  [              37 bb - 119 ]
                  [ 0   0    1   ----------- ]
                  [              37 aa - 313 ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: eigenvalues, eivals -->
<!-- signatures: eigenvalues(M), eivals(M) -->
### Function: eigenvalues (M)

Devuelve una lista con dos sublistas. La primera sublista la forman los
valores propios de la matriz *M* y la segunda sus multiplicidades correspondientes.


El nombre `eivals` es un sinónimo de `eigenvalues`.


La función `eigenvalues` llama a la función `solve` para calcular las raíces
del polinomio característico de la matriz. En ocasiones, `solve` no
podrá encontrar dichas raíces, en cuyo caso otras funciones de este paquete
no trabajarán correctamente, a excepción de `innerproduct`,
`unitvector`, `columnvector` y `gramschmidt`.





En algunos casos los valores propios encontrados por `solve` serán
expresiones complicadas, las cuales se podrán simplificar haciendo uso
de otras funciones.



El paquete `eigen.mac` se carga en memoria de forma automática cuando
se invocan `eigenvalues` o `eigenvectors`. Si `eigen.mac` no
está ya cargado, `load ("eigen")` lo carga. Tras la carga, todas las
funciones y variables del paquete estarán activas.

<!-- category: LinearAlgebra -->
<!-- keywords: eigenvectors, eivects -->
<!-- signatures: eigenvectors(M), eivects(M) -->
### Function: eigenvectors (M)

Calcula los vectores propios de la matriz *M*.
El resultado devuelto es una lista con dos elementos;
el primero está formado por dos listas, la primera con los valores propios
de *M* y la segunda con sus respectivas multiplicidades, el segundo
elemento es una lista de listas de vectores propios, una por
cada valor propio, pudiendo haber uno o más vectores propios en cada lista.


Tomando la matriz *M* como argumento, devuelve una lista de listas,
la primera de las cuales es la salida de `eigenvalues` y las 
siguientes son los vectorios propios de la matriz asociados a los
valores propios correspondientes. Los vectores propios calculados son los 
vectores propios por la derecha.


El nombre `eivects` es un sinónimo de `eigenvectors`.


El paquete `eigen.mac` se carga en memoria de forma automática cuando
se invocan `eigenvalues` o `eigenvectors`. Si `eigen.mac` no
está ya cargado, `load ("eigen")` lo carga. Tras la carga, todas las
funciones y variables del paquete estarán activas.


Las variables que afectan a esta función son: 


`nondiagonalizable` toma el valor `true` o `false` dependiendo
de si la matriz no es diagonalizable o diagonalizable tras la ejecución de
`eigenvectors`.


`hermitianmatrix`, si vale `true`, entonces los vectores propios 
degenerados de la matriz hermítica son ortogonalizados mediante el
algoritmo de Gram-Schmidt.


`knowneigvals`, si vale `true`, entonces el paquete `eigen` da por
sentado que los valores propios de la matriz son conocidos por el usuario y 
almacenados en la variable global `listeigvals`.  `listeigvals` debería
ser similar a la salida de `eigenvalues`.


La función `algsys` se utiliza aquí para calcular los vectores propios. A
veces, `algsys` no podrá calcular una solución. En algunos casos, será posible
simplificar los valores propios calculándolos en primer lugar con `eigenvalues` y
luego utilizando otras funciones para simplificarlos. Tras la simplificación, 
`eigenvectors` podrá ser llamada otra vez con la variable `knowneigvals`
ajustada al valor `true`.


Véase también `eigenvalues`.


Ejemplos:


Una matriz con un único vector propio por cada valor propio.









```maxima
(%i1) M1 : matrix ([11, -1], [1, 7]);
                           [ 11  - 1 ]
(%o1)                      [         ]
                           [ 1    7  ]
(%i2) [vals, vecs] : eigenvectors (M1);
(%o2) [[[9 - sqrt(3), sqrt(3) + 9], [1, 1]], 
                        [[[1, sqrt(3) + 2]], [[1, 2 - sqrt(3)]]]]
(%i3) for i thru length (vals[1]) do disp (val[i] = vals[1][i],
  mult[i] = vals[2][i], vec[i] = vecs[i]);
                       val  = 9 - sqrt(3)
                          1

                            mult  = 1
                                1

                    vec  = [[1, sqrt(3) + 2]]
                       1

                       val  = sqrt(3) + 9
                          2

                            mult  = 1
                                2

                    vec  = [[1, 2 - sqrt(3)]]
                       2

(%o3)                         done
```


Una matriz con dos vectores propios para uno de los valores propios.









```maxima
(%i1) M1 : matrix ([0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]);
                         [ 0  1  0  0 ]
                         [            ]
                         [ 0  0  0  0 ]
(%o1)                    [            ]
                         [ 0  0  2  0 ]
                         [            ]
                         [ 0  0  0  2 ]
(%i2) [vals, vecs] : eigenvectors (M1);
(%o2) [[[0, 2], [2, 2]], [[[1, 0, 0, 0]],
                                   [[0, 0, 1, 0], [0, 0, 0, 1]]]]
(%i3) for i thru length (vals[1]) do disp (val[i] = vals[1][i],
  mult[i] = vals[2][i], vec[i] = vecs[i]);
                            val  = 0
                               1

                            mult  = 2
                                1

                      vec  = [[1, 0, 0, 0]]
                         1

                            val  = 2
                               2

                            mult  = 2
                                2

               vec  = [[0, 0, 1, 0], [0, 0, 0, 1]]
                  2

(%o3)                         done
```

<!-- category: LinearAlgebra -->
<!-- keywords: ematrix -->
<!-- signatures: ematrix(m, n, x, i, j) -->
### Function: ematrix (m, n, x, i, j)

Devuelve una matriz de orden *m* por *n*, con todos sus elementos 
nulos, excepto el que ocupa la posición `[i, j]`, que
es igual a *x*.

<!-- category: LinearAlgebra -->
<!-- keywords: entermatrix -->
<!-- signatures: entermatrix(m, n) -->
### Function: entermatrix (m, n)

Devuelve una matriz de orden *m* por *n*, cuyos elementos
son leidos de forma interactiva.


Si *n* es igual a *m*, Maxima pregunta por el tipo de
matriz (diagonal, simétrica, antisimétrica o general) y luego por
cada elemento. Cada respuesta introducida por el usuario debe terminar
con un punto y coma `;` o con un signo de dólar `$`.


Si *n* y *m* no son iguales, Maxima pregunta
por el valor de cada elemento.


Los elementos de la matriz pueden ser cualquier tipo de 
expresión, que en todo caso será evaluada.
`entermatrix` evalúa sus argumentos.



```maxima
(%i1) n: 3$
(%i2) m: entermatrix (n, n)$

Is the matrix  1. Diagonal  2. Symmetric  3. Antisymmetric  
   4. General
Answer 1, 2, 3 or 4 : 
1$
Row 1 Column 1: 
(a+b)^n$
Row 2 Column 2: 
(a+b)^(n+1)$
Row 3 Column 3: 
(a+b)^(n+2)$

Matrix entered.
(%i3) m;
                [        3                     ]
                [ (b + a)      0         0     ]
                [                              ]
(%o3)           [                  4           ]
                [    0      (b + a)      0     ]
                [                              ]
                [                            5 ]
                [    0         0      (b + a)  ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: genmatrix -->
<!-- signatures: genmatrix(a, i_2, j_2, i_1, j_1), genmatrix(a, i_2, j_2, i_1), genmatrix(a, i_2, j_2) -->
### Function: genmatrix (a, i_2, j_2, i_1, j_1)

Devuelve una matriz generada a partir de *a*, siendo `a[i_1,j_1]` el elemento superior izquierdo y `a[i_2,j_2]` el inferior derecho de la matriz. 
Aquí *a* se declara como una arreglo (creado por `array`,
pero no por `make_array`), o un array no declarado, o una función array, o una
expresión lambda de dos argumentos.
(An array function is created like other functions with `:=` or `define`,
but arguments are enclosed in square brackets instead of parentheses.)


Si se omite *j_1*, entonces se le asigna el valor *i_1*. Si tanto *j_1* como *i_1* se omiten, a las dos variables se le asigna el valor 1.


Si un elemento `i,j` del arreglo no está definido, se le asignará el elemento simbólico `a[i,j]`.













```maxima
(%i1) h [i, j] := 1 / (i + j - 1);
                                    1
(%o1)                  h     := ---------
                        i, j    i + j - 1
(%i2) genmatrix (h, 3, 3);
                           [    1  1 ]
                           [ 1  -  - ]
                           [    2  3 ]
                           [         ]
                           [ 1  1  1 ]
(%o2)                      [ -  -  - ]
                           [ 2  3  4 ]
                           [         ]
                           [ 1  1  1 ]
                           [ -  -  - ]
                           [ 3  4  5 ]
(%i3) array (a, fixnum, 2, 2);
(%o3)                           a
(%i4) a [1, 1] : %e;
(%o4)                          %e
(%i5) a [2, 2] : %pi;
(%o5)                          %pi
(%i6) genmatrix (a, 2, 2);
                           [ %e   0  ]
(%o6)                      [         ]
                           [ 0   %pi ]
(%i7) genmatrix (lambda ([i, j], j - i), 3, 3);
                         [  0    1   2 ]
                         [             ]
(%o7)                    [ - 1   0   1 ]
                         [             ]
                         [ - 2  - 1  0 ]
(%i8) genmatrix (B, 2, 2);
                        [ B      B     ]
                        [  1, 1   1, 2 ]
(%o8)                   [              ]
                        [ B      B     ]
                        [  2, 1   2, 2 ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: gramschmidt -->
<!-- signatures: gramschmidt(x), gramschmidt(x, F) -->
### Function: gramschmidt (x)

Ejecuta el algoritmo de ortogonalización de Gram-Schmidt sobre *x*,
que puede ser una matriz o una lista de listas. La función 
`gramschmidt` no altera el valor de *x*.
El producto interno por defecto empleado en `gramschmidt` es
`innerproduct`, o *F*, si se ha hecho uso de esta opción.


Si *x* es una matriz, el algoritmo se aplica a las filas de *x*. Si
*x* es una lista de listas, el algoritmo se aplica a las sublistas,
las cuales deben tener el mismo número de miembros. En cualquier caso,
el valor devuelto es una lista de listas, cuyas sublistas son ortogonales.



La función `factor` es invocada  en cada paso del algoritmo para 
simplificar resultados intermedios. Como consecuencia, el valor retornado 
puede contener enteros factorizados.


El nombre `gschmit` es sinónimo de `gramschmidt`.


Es necesario cargar la función haciendo `load ("eigen")`.


Ejemplo:


Algoritmo de Gram-Schmidt utilizando el producto interno por defecto.









```maxima
(%i1) load ("eigen")$
(%i2) x: matrix ([1, 2, 3], [9, 18, 30], [12, 48, 60]);
                         [ 1   2   3  ]
                         [            ]
(%o2)                    [ 9   18  30 ]
                         [            ]
                         [ 12  48  60 ]
(%i3) y: gramschmidt (x);
                       2      2            4     3
                      3      3   3 5      2  3  2  3
(%o3)  [[1, 2, 3], [- ---, - --, ---], [- ----, ----, 0]]
                      2 7    7   2 7       5     5
(%i4) map (innerproduct, [y[1], y[2], y[3]], [y[2], y[3], y[1]]);
(%o4)                       [0, 0, 0]
```


Algoritmo de Gram-Schmidt utilizando un producto interno especificado
por el usuario.









```maxima
(%i1) load ("eigen")$
(%i2) ip (f, g) := integrate (f * g, u, a, b);
(%o2)          ip(f, g) := integrate(f g, u, a, b)
(%i3) y : gramschmidt ([1, sin(u), cos(u)], ip), a= -%pi/2, b=%pi/2;
                               %pi cos(u) - 2
(%o3)              [1, sin(u), --------------]
                                    %pi
(%i4) map (ip, [y[1], y[2], y[3]], [y[2], y[3], y[1]]), a= -%pi/2, b=%pi/2;
(%o4)                       [0, 0, 0]
```

<!-- category: LinearAlgebra -->
<!-- keywords: ident -->
<!-- signatures: ident(n) -->
### Function: ident (n)

Devuelve la matriz identidad de orden *n*.

<!-- category: LinearAlgebra -->
<!-- keywords: innerproduct, inprod -->
<!-- signatures: innerproduct(x, y), inprod(x, y) -->
### Function: innerproduct (x, y)

Devuelve el producto interior o escalar de *x* por *y*, que deben ser listas de igual longitud, o ambas matrices columa o fila de igual longitud. El valor devuelto es `conjugate (x) . y`, donde `.` es el operador de multiplicación no conmutativa.


Es necesario cargar la función haciendo `load ("eigen")`.


El nombre `inprod` es sinónimo de `innerproduct`.

<!-- category: LinearAlgebra -->
<!-- keywords: invert -->
<!-- signatures: invert(M) -->
### Function: invert (M)

Devuelve la inversa de la matriz *M*, calculada por el método del adjunto.


La implementación actual no es eficiente para matrices de orden grande.


Cuando `detout` vale `true`, el determinante se deja
 fuera de la inversa a modo de factor escalar.


Los elementos de la matriz inversa no se expanden. Si *M* tiene elementos
polinómicos, se puede mejorar el aspecto del resultado haciendo 
`expand (invert (m)), detout`.


Véase la descripción de `^^` (exponente no conmutativo) para 
información sobre otro método para invertir matrices.

<!-- category: LinearAlgebra -->
<!-- keywords: list_matrix_entries -->
<!-- signatures: list_matrix_entries(M) -->
### Function: list_matrix_entries (M)

Devuelve una lista con todos los elementos de la matriz *M*.


Ejemplo:






```maxima
(%i1) list_matrix_entries(matrix([a,b],[c,d]));
(%o1)                     [a, b, c, d]
```

<!-- category: LinearAlgebra -->
<!-- keywords: lmxchar -->
<!-- signatures: lmxchar -->
### Variable: lmxchar

Valor por defecto: `[`


La variable `lmxchar` guarda el carácter a mostrar como delimitador izquierdo de la matriz.
Véase también `rmxchar`.


Ejemplo:



```maxima
(%i1) lmxchar: "|"$
(%i2) matrix ([a, b, c], [d, e, f], [g, h, i]);
                           | a  b  c ]
                           |         ]
(%o2)                      | d  e  f ]
                           |         ]
                           | g  h  i ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: matrix -->
<!-- signatures: matrix(fila_1, ..., fila_n) -->
### Function: matrix (fila_1, ..., fila_n)

Devuelve una matriz rectangular con las filas  *fila_1*, ..., *fila_n*. Cada fila es una lista de expresiones. Todas las filas deben tener el mismo número de miembros.


Las operaciones `+` (suma), `-` (resta), `*` (multiplicación) y `/` (división), se llevan a cabo elemento a elemento cuando los operandos son dos matrices, un escalar y una matriz o una matriz con un escalar. La operación `^` (exponenciación, equivalente a `**`) se lleva cabo también elemento a elemento si los operandos son un escalr y una matriz o uma matriz y un escalar, pero no si los operandos son dos matrices.


El producto matricial se representa con el operador de multiplicación no conmutativa `.`. El correspondiente operador de exponenciación no conmutativa es `^^`. Dada la matriz `A`, `A.A = A^^2` y `A^^-1` es la inversa de *A*, si existe.


Algunas variables controlan la simplificación de expresiones que incluyan estas operaciones: `doallmxops`, `domxexpt`, `domxmxops`, `doscmxops` y `doscmxplus`.



Hay otras opciones adicionales relacionadas con matrices:
`lmxchar`, `rmxchar`, `ratmx`, `listarith`, `detout`,
`scalarmatrix` y `sparse`.



Hay también algunas funciones que admiten matrices como argumentos o que devuelven resultados matriciales: `eigenvalues`, `eigenvectors`,
`determinant`,
`charpoly`, `genmatrix`, `addcol`, `addrow`, 
`copymatrix`, `transpose`, `echelon` y `rank`.



Ejemplos:



- *
Construcción de matrices a partir de listas.


```maxima
(%i1) x: matrix ([17, 3], [-8, 11]);
                           [ 17   3  ]
(%o1)                      [         ]
                           [ - 8  11 ]
(%i2) y: matrix ([%pi, %e], [a, b]);
                           [ %pi  %e ]
(%o2)                      [         ]
                           [  a   b  ]
```


- *
Suma elemento a elemento.


```maxima
(%i3) x + y;
                      [ %pi + 17  %e + 3 ]
(%o3)                 [                  ]
                      [  a - 8    b + 11 ]
```


- *
Resta elemento a elemento.


```maxima
(%i4) x - y;
                      [ 17 - %pi  3 - %e ]
(%o4)                 [                  ]
                      [ - a - 8   11 - b ]
```


- *
Multiplicación elemento a elemento.


```maxima
(%i5) x * y;
                        [ 17 %pi  3 %e ]
(%o5)                   [              ]
                        [ - 8 a   11 b ]
```


- *
División elemento a elemento.


```maxima
(%i6) x / y;
                        [ 17       - 1 ]
                        [ ---  3 %e    ]
                        [ %pi          ]
(%o6)                   [              ]
                        [   8    11    ]
                        [ - -    --    ]
                        [   a    b     ]
```


- *
Matriz elevada a un exponente escalar, operación elemento a elemento.


```maxima
(%i7) x ^ 3;
                         [ 4913    27  ]
(%o7)                    [             ]
                         [ - 512  1331 ]
```


- *
Base escalar y exponente matricial, operación elemento a elemento.


```maxima
(%i8) exp(y); 
                         [   %pi    %e ]
                         [ %e     %e   ]
(%o8)                    [             ]
                         [    a     b  ]
                         [  %e    %e   ]
```


- *
Base y exponente matriciales. Esta operación no se realiza elemento a elemento.


```maxima
(%i9) x ^ y;
                                [ %pi  %e ]
                                [         ]
                                [  a   b  ]
                     [ 17   3  ]
(%o9)                [         ]
                     [ - 8  11 ]
```


- *
Multiplicación matricial no conmutativa.


```maxima
(%i10) x . y;
                  [ 3 a + 17 %pi  3 b + 17 %e ]
(%o10)            [                           ]
                  [ 11 a - 8 %pi  11 b - 8 %e ]
(%i11) y . x;
                [ 17 %pi - 8 %e  3 %pi + 11 %e ]
(%o11)          [                              ]
                [  17 a - 8 b     11 b + 3 a   ]
```


- *
Exponenciación matricial no conmutativa. Una base escalar *b* elevada a un exponente matricial *M* se lleva a cabo elemento a elemento y por lo tanto `b^^m` equivale a `b^m`.


```maxima
(%i12) x ^^ 3;
                        [  3833   1719 ]
(%o12)                  [              ]
                        [ - 4584  395  ]
(%i13) %e ^^ y;
                         [   %pi    %e ]
                         [ %e     %e   ]
(%o13)                   [             ]
                         [    a     b  ]
                         [  %e    %e   ]
```


- *
Una matriz elevada al exponente -1 con el operador de exponenciación no conmutativa equivale a la matriz inversa, si existe.


```maxima
(%i14) x ^^ -1;
                         [ 11      3  ]
                         [ ---  - --- ]
                         [ 211    211 ]
(%o14)                   [            ]
                         [  8    17   ]
                         [ ---   ---  ]
                         [ 211   211  ]
(%i15) x . (x ^^ -1);
                            [ 1  0 ]
(%o15)                      [      ]
                            [ 0  1 ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: matrix_element_add -->
<!-- signatures: matrix_element_add -->
### Variable: matrix_element_add

Valor por defecto: `+`


La variable `matrix_element_add` guarda el símbolo del operador a ejecutar en lugar de la suma en el producto matricial; a `matrix_element_add` se le puede asignar cualquier operador n-ario (esto es, una función que admite cualquier número de argumentos). El valor asignado puede ser el nombre de un operador encerrado entre apóstrofos, el nombre de una función o una expresión lambda.


Véanse también `matrix_element_mult` y `matrix_element_transpose`.


Ejemplo:



```maxima
(%i1) matrix_element_add: "*"$
(%i2) matrix_element_mult: "^"$
(%i3) aa: matrix ([a, b, c], [d, e, f]);
                           [ a  b  c ]
(%o3)                      [         ]
                           [ d  e  f ]
(%i4) bb: matrix ([u, v, w], [x, y, z]);
                           [ u  v  w ]
(%o4)                      [         ]
                           [ x  y  z ]
(%i5) aa . transpose (bb);
                     [  u  v  w   x  y  z ]
                     [ a  b  c   a  b  c  ]
(%o5)                [                    ]
                     [  u  v  w   x  y  z ]
                     [ d  e  f   d  e  f  ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: matrix_element_mult -->
<!-- signatures: matrix_element_mult -->
### Variable: matrix_element_mult

Valor por defecto: `*`


La variable `matrix_element_mult` guarda el símbolo del operador a ejecutar en lugar de la multiplicación en el producto matricial; a `matrix_element_mult` se le puede asignar cualquier operador binario. El valor asignado puede ser el nombre de un operador encerrado entre apóstrofos, el nombre de una función o una expresión lambda.


El operador `.` puede ser una opción útil en determinados contextos.


Véanse también `matrix_element_add` y `matrix_element_transpose`.


Ejemplo:



```maxima
(%i1) matrix_element_add: lambda ([[x]], sqrt (apply ("+", x)))$
(%i2) matrix_element_mult: lambda ([x, y], (x - y)^2)$
(%i3) [a, b, c] . [x, y, z];
                          2          2          2
(%o3)         sqrt((c - z)  + (b - y)  + (a - x) )
(%i4) aa: matrix ([a, b, c], [d, e, f]);
                           [ a  b  c ]
(%o4)                      [         ]
                           [ d  e  f ]
(%i5) bb: matrix ([u, v, w], [x, y, z]);
                           [ u  v  w ]
(%o5)                      [         ]
                           [ x  y  z ]
(%i6) aa . transpose (bb);
               [             2          2          2  ]
               [ sqrt((c - w)  + (b - v)  + (a - u) ) ]
(%o6)  Col 1 = [                                      ]
               [             2          2          2  ]
               [ sqrt((f - w)  + (e - v)  + (d - u) ) ]

                         [             2          2          2  ]
                         [ sqrt((c - z)  + (b - y)  + (a - x) ) ]
                 Col 2 = [                                      ]
                         [             2          2          2  ]
                         [ sqrt((f - z)  + (e - y)  + (d - x) ) ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: matrix_element_transpose -->
<!-- signatures: matrix_element_transpose -->
### Variable: matrix_element_transpose

Valor por defecto: `false`


La variable `matrix_element_transpose` es una operación que se aplica a cada elemento de una matriz a la que se le calcula la transpuesta. A `matrix_element_mult` se le puede asignar cualquier operador unitario. El valor asignado puede ser el nombre de un operador encerrador entre apóstrofos, el nombre de una función o una expresión lambda.


Cuando `matrix_element_transpose` es igual a `transpose`, la función `transpose` se aplica a cada elemento. Cuando  `matrix_element_transpose` es igual  a `nonscalars`, la función `transpose` se aplica a todos los elementos no escalares. Si alguno de los elementos es un átomo, la opción `nonscalars` se aplica 
`transpose` sólo si el átomo se declara no escalar, mientras que la opción `transpose` siempre aplica  `transpose`.


La opción por defecto, `false`, significa que no se aplica ninguna operación.


Véanse también `matrix_element_add` y `matrix_element_mult`.


Ejemplos:



```maxima
(%i1) declare (a, nonscalar)$
(%i2) transpose ([a, b]);
                        [ transpose(a) ]
(%o2)                   [              ]
                        [      b       ]
(%i3) matrix_element_transpose: nonscalars$
(%i4) transpose ([a, b]);
                        [ transpose(a) ]
(%o4)                   [              ]
                        [      b       ]
(%i5) matrix_element_transpose: transpose$
(%i6) transpose ([a, b]);
                        [ transpose(a) ]
(%o6)                   [              ]
                        [ transpose(b) ]
(%i7) matrix_element_transpose: 
           lambda ([x], realpart(x) - %i*imagpart(x))$
(%i8) m: matrix ([1 + 5*%i, 3 - 2*%i], [7*%i, 11]);
                     [ 5 %i + 1  3 - 2 %i ]
(%o8)                [                    ]
                     [   7 %i       11    ]
(%i9) transpose (m);
                      [ 1 - 5 %i  - 7 %i ]
(%o9)                 [                  ]
                      [ 2 %i + 3    11   ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: matrixmap -->
<!-- signatures: matrixmap(f, M) -->
### Function: matrixmap (f, M)

Devuelve una matriz con el elemento `i,j` igual a `f(M[i,j])`.


Véanse también `map`, `fullmap`, `fullmapl` y `apply`.

<!-- category: LinearAlgebra -->
<!-- keywords: matrixp -->
<!-- signatures: matrixp(expr) -->
### Function: matrixp (expr)

Devuelve `true` si *expr* es una matriz, en caso contrario `false`.

<!-- category: LinearAlgebra -->
<!-- keywords: mattrace -->
<!-- signatures: mattrace(M) -->
### Function: mattrace (M)

Devuelve la traza (esto es, la suma de los elementos de la diagonal principal) de la matriz cuadrada *M*.  


Para disponer de esta función es necesario cargar el paquete haciendo `load ("nchrpl")`.

<!-- category: LinearAlgebra -->
<!-- keywords: minor -->
<!-- signatures: minor(M, i, j) -->
### Function: minor (M, i, j)

Devuelve el menor `(i, j)` de la matriz *M*.  Esto es, la propia matriz *M*, una vez extraídas la fila *i* y la columna *j*.

<!-- category: LinearAlgebra -->
<!-- keywords: ncharpoly -->
<!-- signatures: ncharpoly(M, x) -->
### Function: ncharpoly (M, x)

Devuelve el polinomio característico de la matriz *M* respecto de la variable *x*. Es una alternativa a la función `charpoly` de Maxima.


La función `ncharpoly` opera calculando trazas de las potencias de la matriz dada, que son iguales a las sumas de las potencias de las raíces del polinomio característico. A partir de estas cantidades se pueden calcular las funciones simétricas de las raíces, que no son otra cosa sino los coeficientes del polinomio característico. La función   `charpoly` opera calculando el determinante de  by `x * ident [n] - a`. La función `ncharpoly` es m’as eficiente en el caso de matrices grandes y densas.


Para disponer de esta función es necesario cargar el paquete haciendo `load ("nchrpl")`.

<!-- category: LinearAlgebra -->
<!-- keywords: newdet -->
<!-- signatures: newdet(M) -->
### Function: newdet (M)

Calcula el determinante de la matriz *M* por el algoritmo del árbol menor
de Johnson-Gentleman. El resultado devuelto por `newdet` tiene formato CRE.

<!-- category: LinearAlgebra -->
<!-- keywords: permanent -->
<!-- signatures: permanent(M) -->
### Function: permanent (M)

Calcula la permanente de la matriz *M* por el algoritmo del árbol menor de
Johnson-Gentleman. La permanente es como un determinante pero sin cambios de signo.
El resultado devuelto por `permanent` tiene formato CRE.


Véase también `newdet`.

<!-- category: LinearAlgebra -->
<!-- keywords: rank -->
<!-- signatures: rank(M) -->
### Function: rank (M)

Calcula el rango de la matriz *M*.  Esto es, el orden del mayor subdeterminante no singular de *M*.



La función *rango* puede retornar una respuesta errónea si no detecta que un elemento de la matriz equivalente a cero lo es.

<!-- category: LinearAlgebra -->
<!-- keywords: ratmx -->
<!-- signatures: ratmx -->
### Variable: ratmx

Valor por defecto: `false`


Si `ratmx` vale `false`, el determinante y la suma, resta y producto matriciales se calculan cuando las matrices se expresan en términos de sus elementos, pero no se calcula la inversión matricial en su representación general.


Si `ratmx` vale `true`, las cuatro operaciones citadas más arriba se calculan en el formato CRE y el resultado de la matriz inversa también se da en formato CRE. Esto puede hacer que se expandan los elementos de la matriz, dependiendo del valor de `ratfac`, lo que quizás no sea siempre deseable.

<!-- category: LinearAlgebra -->
<!-- keywords: rmxchar -->
<!-- signatures: rmxchar -->
### Variable: rmxchar

Valor por defecto: `]`


La variable `rmxchar` es el carácter que se dibuja al lado derecho de una matriz.


Véase también `lmxchar`.

<!-- category: LinearAlgebra -->
<!-- keywords: row -->
<!-- signatures: row(M, i) -->
### Function: row (M, i)

Devuelve la *i*-ésima fila de la matriz *M*. El valor que devuelve tiene formato de matriz.

<!-- category: LinearAlgebra -->
<!-- keywords: scalarmatrixp -->
<!-- signatures: scalarmatrixp -->
### Variable: scalarmatrixp

Valor por defecto: `true`


Si `scalarmatrixp` vale `true`, entonces siempre que una matriz 1 x 1 se produce como resultado del cálculo del producto no conmutativo de matrices se cambia al formato escalar.


Si `scalarmatrixp` vale `all`, entonces todas las matrices 1 x 1 se simplifican a escalares.


Si `scalarmatrixp` vale `false`, las matrices 1 x 1 no se convierten en escalares.

<!-- category: LinearAlgebra -->
<!-- keywords: setelmx -->
<!-- signatures: setelmx(x, i, j, M) -->
### Function: setelmx (x, i, j, M)

Asigna el valor *x* al (*i*, *j*)-ésimo elemento de la matriz *M* y devuelve la matriz actualizada.


La llamada `M [i, j]: x` hace lo mismo, pero devuelve  *x* en lugar de *M*.

<!-- category: LinearAlgebra -->
<!-- keywords: similaritytransform, simtran -->
<!-- signatures: similaritytransform(M), simtran(M) -->
### Function: similaritytransform (M)

La función `similaritytransform` calcula la transformada de similitud de la matriz `M`. Devuelve una lista que es la salida de la instrucción `uniteigenvectors`. Además, si la variable `nondiagonalizable` vale `false` entonces se calculan dos matrices globales `leftmatrix` y `rightmatrix`. Estas matrices tienen la propiedad de que `leftmatrix . M . rightmatrix` es una matriz diagonal con los valores propios de *M* en su diagonal.  Si `nondiagonalizable` vale `true` entonces no se calculan estas matrices.


Si la variable `hermitianmatrix` vale `true` entonces `leftmatrix` es el conjugado complejo de la transpuesta de `rightmatrix`.  En otro caso `leftmatrix` es la inversa de `rightmatrix`.


Las columnas de la matriz `rightmatrix` son los vectores propios de *M*.  Las otras variables (véanse `eigenvalues` y `eigenvectors`) tienen el mismo efecto, puesto que `similaritytransform` llama a las otras funciones del paquete para poder formar `rightmatrix`.


Estas funciones se cargan con `load ("eigen")`.


El nombre `simtran` es sinónimo de `similaritytransform`.

<!-- category: LinearAlgebra -->
<!-- keywords: sparse -->
<!-- signatures: sparse -->
### Variable: sparse

Valor por defecto: `false`


Si `sparse` vale `true` y si `ratmx` vale `true`, entonces `determinant`
utilizará rutinas especiales para calcular determinantes dispersos.

<!-- category: LinearAlgebra -->
<!-- keywords: submatrix -->
<!-- signatures: submatrix(i_1, ..., i_m, M, j_1, ..., j_n), submatrix(i_1, ..., i_m, M), submatrix(M, j_1, ..., j_n) -->
### Function: submatrix (i_1, ..., i_m, M, j_1, ..., j_n)

Devuelve una nueva matriz formada a partir de la matriz *M* pero cuyas filas *i_1*, ..., *i_m* y columnas  *j_1*, ..., *j_n* han sido eliminadas.

<!-- category: LinearAlgebra -->
<!-- keywords: transpose -->
<!-- signatures: transpose(M) -->
### Function: transpose (M)

Calcula la transpuesta de *M*.


Si *M* es una matriz, el valor devuelto es otra matriz *N* tal que `N[i,j] = M[j,i]`.


Si *M* es una lista, el valor devuelto es una matriz *N* de `length (m)` filas y 1 columna, tal que `N[i,1] = M[i]`.


En caso de no ser *M* ni matriz ni lista, se devuelve la
expresión nominal `'transpose (M)`.

<!-- category: LinearAlgebra -->
<!-- keywords: triangularize -->
<!-- signatures: triangularize(M) -->
### Function: triangularize (M)

Devuelve la forma triangular superior de la matriz `M`, obtenida por eliminación gaussiana.
El resultado es el mismo que el devuelto por `echelon`, con la salvedad de que el primer elemento no nulo de cada fila no se normaliza a 1.


Las funciones `lu_factor` y `cholesky` también triangularizan matrices.







```maxima
(%i1) M: matrix ([3, 7, aa, bb], [-1, 8, 5, 2], [9, 2, 11, 4]);
                       [  3   7  aa  bb ]
                       [                ]
(%o1)                  [ - 1  8  5   2  ]
                       [                ]
                       [  9   2  11  4  ]
(%i2) triangularize (M);
             [ - 1   8         5            2      ]
             [                                     ]
(%o2)        [  0   - 74     - 56         - 22     ]
             [                                     ]
             [  0    0    626 - 74 aa  238 - 74 bb ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: uniteigenvectors, ueivects -->
<!-- signatures: uniteigenvectors(M), ueivects(M) -->
### Function: uniteigenvectors (M)

Calcula los vectores propios unitarios de la matriz *M*. El valor que devuelve es una lista de listas, la primera de las cuales es la salida de la función `eigenvalues` y el resto de sublistas son los vectores propios unitarios de la matriz correspondiente a esos valores propios, respectivamente.


Las variables citadas en la descripción de la función `eigenvectors` tienen los mismos efectos en `uniteigenvectors`.


Si `knowneigvects` vale `true`, el paquete `eigen` da por supuesto que el usuario conoce los vectores propios de la matriz y que están guardados en la variable global `listeigvects`, en tal caso el contenido de  `listeigvects` debe ser una lista de estructura similar a la que devuelve la función `eigenvectors`.



Si `knowneigvects` vale `true` y la lista de vectores propios está en la variable `listeigvects`, el valor de la variable `nondiagonalizable` puede que no sea el correcto. Si tal es el caso, debe asignarsele el valor correcto. 


Para utilizar esta fucnión es necesario cargarla haciendo `load ("eigen")`.


El nombre `ueivects` es sinónimo de `uniteigenvectors`.

<!-- category: LinearAlgebra -->
<!-- keywords: unitvector, uvect -->
<!-- signatures: unitvector(x), uvect(x) -->
### Function: unitvector (x)

Devuelve $x/norm(x)$, esto es, el vector unitario de igual dirección y sentido que *x*.


`load ("eigen")` loads this function.


Para utilizar esta fucnión es necesario cargarla haciendo `load ("eigen")`.


El nombre `uvect` es sinónimo de `unitvector`.

<!-- category: LinearAlgebra -->
<!-- keywords: vectorpotential -->
<!-- signatures: vectorpotential(givencurl) -->
### Function: vectorpotential (givencurl)

Devuelve el vector potencial de un vector rotacional en el sistema
de coordenadas actual. 
`potentialzeroloc` tiene un rol similar al de `potential`, 
pero el orden del miembro izquierdo de las ecuaciones debe ser una
permutación cíclica de las coordenadas.

<!-- category: LinearAlgebra -->
<!-- keywords: vectorsimp -->
<!-- signatures: vectorsimp(expr) -->
### Function: vectorsimp (expr)

Realiza simplificaciones y expansiones de acuerdo con los valores de las siguientes variables globales:


`expandall`, `expanddot`, `expanddotplus`, `expandcross`, `expandcrossplus`,
`expandcrosscross`, `expandgrad`, `expandgradplus`, `expandgradprod`,
`expanddiv`, `expanddivplus`, `expanddivprod`, `expandcurl`, `expandcurlplus`,
`expandcurlcurl`, `expandlaplacian`, `expandlaplacianplus` y `expandlaplacianprod`.


Todas estas variables tienen por defecto el valor `false`. El sufijo `plus` se refiere al uso de la suma o la distributividad.  El sufijo `prod` se refiere a la expansión de operadores que realizan cualquier tipo de producto.



**expandcrosscross** — Simplifica $p ~ (q ~ r)$ en $(p . r)*q - (p . q)*r$.
**expandcurlcurl** — Simplifica $curl curl p$ en $grad div p + div grad p$.
**expandlaplaciantodivgrad** — Simplifica $laplacian p$ en $div grad p$.
**expandcross** — Activa `expandcrossplus` y `expandcrosscross`.
**expandplus** — Activa `expanddotplus`, `expandcrossplus`, `expandgradplus`,
`expanddivplus`, `expandcurlplus` y `expandlaplacianplus`.
**expandprod** — Activa `expandgradprod`, `expanddivprod` y `expandlaplacianprod`.



Estas variables están declaradas como `evflag`.

<!-- category: LinearAlgebra -->
<!-- keywords: zeromatrix -->
<!-- signatures: zeromatrix(m, n) -->
### Function: zeromatrix (m, n)

Devuelve una matriz rectangular *m* por *n* con todos sus elementos iguales a cero.

