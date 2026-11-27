## lapack

<!-- category: Numerical -->
<!-- keywords: dgeev -->
<!-- signatures: dgeev(A), dgeev(A, right_p, left_p) -->
### Function: dgeev (A)

Calcula los autovalores y, opcionalmente, también los autovectores de la matriz *A*.
Todos los elementos de *A* deben ser enteros o números decimales en coma flotante.
Además, *A* debe ser cuadrada (igual número de filas que de columnas) y puede
ser o no simétrica.


`dgeev(A)` calcula sólo los autovalores de *A*. 
`dgeev(A, right_p, left_p)` calcula los autovalores de *A*
y los autovectores por la derecha cuando $right_p = true$, y
los autovectores por la izquierda cuando $left_p = true$.


La función devuelve una lista de tres elementos.
El primer elemento es una lista con los autovalores.
El segundo elemento es `false` o la matriz de autovectores por la derecha.
El tercer elemento es `false` o la matriz de autovectores por la izquierda.


El autovector por la derecha $v(j)$ (la $j$-ésima columna de la matriz de
autovectores por la derecha) satisface


$A . v(j) = lambda(j) . v(j)$


donde $lambda(j)$ es su autovalor asociado.


El autovector por la izquierda $u(j)$ (la $j$-ésima columna de la matriz de
autovectores por la izquierda) satisface


$u(j)**H . A = lambda(j) . u(j)**H$


donde $u(j)**H$ denota la transpuesta conjugada de $u(j)$.


La función de Maxima `ctranspose` calcula la transpuesta conjugada.


Los autovectores calculados están normalizados para que su norma
euclídea valga 1 y su componente mayor tenga su parte
imaginaria igual a cero.


Ejemplo:













```maxima
(%i1) load ("lapack")$
(%i2) fpprintprec : 6;
(%o2)                           6
(%i3) M : matrix ([9.5, 1.75], [3.25, 10.45]);
                         [ 9.5   1.75  ]
(%o3)                    [             ]
                         [ 3.25  10.45 ]
(%i4) dgeev (M);
(%o4)          [[7.54331, 12.4067], false, false]
(%i5) [L, v, u] : dgeev (M, true, true);
                           [ - .666642  - .515792 ]
(%o5) [[7.54331, 12.4067], [                      ], 
                           [  .745378   - .856714 ]
                                        [ - .856714  - .745378 ]
                                        [                      ]]
                                        [  .515792   - .666642 ]
(%i6) D : apply (diag_matrix, L);
                      [ 7.54331     0    ]
(%o6)                 [                  ]
                      [    0     12.4067 ]
(%i7) M . v - v . D;
                [      0.0       - 8.88178E-16 ]
(%o7)           [                              ]
                [ - 8.88178E-16       0.0      ]
(%i8) transpose (u) . M - D . transpose (u);
                     [ 0.0  - 4.44089E-16 ]
(%o8)                [                    ]
                     [ 0.0       0.0      ]
```

<!-- category: Numerical -->
<!-- keywords: dgemm -->
<!-- signatures: dgemm(A, B), dgemm(A, B, options) -->
### Function: dgemm (A, B)

Calcula el producto de dos matrices y, opcionalmente, suma este producto
con una tercera matriz.


En su forma más simple, `dgemm(A, B)` calcula el
producto de las matrices reales *A* y *B*.


En la segunda forma, `dgemm` calcula $alpha * A * B + beta * C$, donde *A*, *B* y
*C* son matrices reales de dimensiones apropiadas, siendo *alpha* 
y *beta* números reales. De forma opcional, tanto *A* como *B*
pueden transponerse antes de calcular su producto. Los parámetros adicionales
se pueden especificar en cualquier orden, siendo su sintaxis de la forma
`clave=valor`. Las claves reconocidas son:



**C** — La matriz *C* que debe ser sumada. El valor por defecto es `false`,
lo que significa que no se sumará ninguna matriz.
**alpha** — El producto de *A* por *B* se multiplicará por este vaalor. El valor
por defecto es 1.
**beta** — Si se da la matriz *C*, se multiplicará por este valor antes de ser sumada.
El valor por defecto es 0, lo que significa que *C* no se suma, incluso estando
presente. Por lo tanto, téngase cuidado en especificar un valor no nulo para *beta*.
**transpose_a** — Si toma el valor `true`, se utilizará la transpuesta de *A*, en lugar de la 
propia matriz *A*, en el producto. El valor por defecto es `false`.
**transpose_b** — Si toma el valor `true`, se utilizará la transpuesta de *B*, en lugar de la 
propia matriz *B*, en el producto. El valor por defecto es `false`.
















```maxima
(%i1) load ("lapack")$
(%i2) A : matrix([1,2,3],[4,5,6],[7,8,9]);
                                  [ 1  2  3 ]
                                  [         ]
(%o2)                             [ 4  5  6 ]
                                  [         ]
                                  [ 7  8  9 ]
(%i3) B : matrix([-1,-2,-3],[-4,-5,-6],[-7,-8,-9]);
                               [ - 1  - 2  - 3 ]
                               [               ]
(%o3)                          [ - 4  - 5  - 6 ]
                               [               ]
                               [ - 7  - 8  - 9 ]
(%i4) C : matrix([3,2,1],[6,5,4],[9,8,7]);
                                  [ 3  2  1 ]
                                  [         ]
(%o4)                             [ 6  5  4 ]
                                  [         ]
                                  [ 9  8  7 ]
(%i5) dgemm(A,B);
                         [ - 30.0   - 36.0   - 42.0  ]
                         [                           ]
(%o5)                    [ - 66.0   - 81.0   - 96.0  ]
                         [                           ]
                         [ - 102.0  - 126.0  - 150.0 ]
(%i6) A . B;
                            [ - 30   - 36   - 42  ]
                            [                     ]
(%o6)                       [ - 66   - 81   - 96  ]
                            [                     ]
                            [ - 102  - 126  - 150 ]
(%i7) dgemm(A,B,transpose_a=true);
                         [ - 66.0  - 78.0   - 90.0  ]
                         [                          ]
(%o7)                    [ - 78.0  - 93.0   - 108.0 ]
                         [                          ]
                         [ - 90.0  - 108.0  - 126.0 ]
(%i8) transpose(A) . B;
                           [ - 66  - 78   - 90  ]
                           [                    ]
(%o8)                      [ - 78  - 93   - 108 ]
                           [                    ]
                           [ - 90  - 108  - 126 ]
(%i9) dgemm(A,B,c=C,beta=1);
                         [ - 27.0  - 34.0   - 41.0  ]
                         [                          ]
(%o9)                    [ - 60.0  - 76.0   - 92.0  ]
                         [                          ]
                         [ - 93.0  - 118.0  - 143.0 ]
(%i10) A . B + C;
                            [ - 27  - 34   - 41  ]
                            [                    ]
(%o10)                      [ - 60  - 76   - 92  ]
                            [                    ]
                            [ - 93  - 118  - 143 ]
(%i11) dgemm(A,B,c=C,beta=1, alpha=-1);
                            [ 33.0   38.0   43.0  ]
                            [                     ]
(%o11)                      [ 72.0   86.0   100.0 ]
                            [                     ]
                            [ 111.0  134.0  157.0 ]
(%i12) -A . B + C;
                               [ 33   38   43  ]
                               [               ]
(%o12)                         [ 72   86   100 ]
                               [               ]
                               [ 111  134  157 ]
```

<!-- category: Numerical -->
<!-- keywords: dgeqrf -->
<!-- signatures: dgeqrf(A) -->
### Function: dgeqrf (A)

Calcula la descomposición QR de la matriz *A*.
Todos los elementos de *A* deben ser enteros o números
reales. No es necesario que *A* tenga
el mismo número de filas que de columnas.


La función devuelve una lista con dos elementos; el primero es
la matriz cuadrada ortonormal *Q*, con el mismo número de
filas que *A*, y el segundo es la matriz triangular superior *R*,
de iguales dimensiones que *A*. El producto `Q . R`, 
siendo "." el operador de la multiplicación matricial, es igual a
*A*, ignorando errores de redondeo.











```maxima
(%i1) load ("lapack") $
(%i2) fpprintprec : 6 $
(%i3) M : matrix ([1, -3.2, 8], [-11, 2.7, 5.9]) $
(%i4) [q, r] : dgeqrf (M);
       [ - .0905357  .995893  ]
(%o4) [[                      ], 
       [  .995893    .0905357 ]
                               [ - 11.0454   2.97863   5.15148 ]
                               [                               ]]
                               [     0      - 2.94241  8.50131 ]
(%i5) q . r - M;
         [ - 7.77156E-16   1.77636E-15   - 8.88178E-16 ]
(%o5)    [                                             ]
         [      0.0       - 1.33227E-15   8.88178E-16  ]
(%i6) mat_norm (%, 1);
(%o6)                      3.10862E-15
```

<!-- category: Numerical -->
<!-- keywords: dgesv -->
<!-- signatures: dgesv(A, b) -->
### Function: dgesv (A, b)

Calcula la solución *x* de la ecuación $A x = b$,
siendo *A* una matriz cuadrada y *b* otra matriz con el mismo
número de filas que *A* y un número arbitrario de columnas. Las 
dimensiones de la solución *x* son las mismas de *b*.


Los elementos de *A* y *b* deben ser reducibles a números decimales
si se les aplica la función `float`, por lo que tales elementos
pueden en principio ser de cualquier tipo numérico, constantes numéricas
simbólicas o cualesquiera expresiones reducibles a un número decimal.
Los elementos de *x* son siempre números decimales. Todas las
operaciones aritméticas se realizan en coma flotante.


`dgesv` calcula la solución mediante la descomposición LU de *A*.


Ejemplos:


`dgesv` calcula la solución *x* de la ecuación 
$A x = b$.









```maxima
(%i1) A : matrix ([1, -2.5], [0.375, 5]);
                               [   1    - 2.5 ]
(%o1)                          [              ]
                               [ 0.375    5   ]
(%i2) b : matrix ([1.75], [-0.625]);
                                  [  1.75   ]
(%o2)                             [         ]
                                  [ - 0.625 ]
(%i3) x : dgesv (A, b);
                            [  1.210526315789474  ]
(%o3)                       [                     ]
                            [ - 0.215789473684211 ]
(%i4) dlange (inf_norm, b - A.x);
(%o4)                                 0.0
```


*b* una matriz con el mismo número de filas que *A*
y un número arbitrario de columnas. Las dimensiones de 
*x* son las mismas de *b*.









```maxima
(%o0)                                done
(%i1) A : matrix ([1, -0.15], [1.82, 2]);
                               [  1    - 0.15 ]
(%o1)                          [              ]
                               [ 1.82    2    ]
(%i2) b : matrix ([3.7, 1, 8], [-2.3, 5, -3.9]);
                              [  3.7   1    8   ]
(%o2)                         [                 ]
                              [ - 2.3  5  - 3.9 ]
(%i3) x : dgesv (A, b);
        [  3.103827540695117   1.20985481742191    6.781786185657722  ]
(%o3)   [                                                             ]
        [ - 3.974483062032557  1.399032116146062  - 8.121425428948527 ]
(%i4) dlange (inf_norm, b - A . x);
(%o4)                       1.1102230246251565E-15
```


Los elementos de *A* y *b* deben ser reducibles a números decimales.









```maxima
(%i1) A : matrix ([5, -%pi], [1b0, 11/17]);
                               [   5    - %pi ]
                               [              ]
(%o1)                          [         11   ]
                               [ 1.0b0   --   ]
                               [         17   ]
(%i2) b : matrix ([%e], [sin(1)]);
                                  [   %e   ]
(%o2)                             [        ]
                                  [ sin(1) ]
(%i3) x : dgesv (A, b);
                             [ 0.690375643155986 ]
(%o3)                        [                   ]
                             [ 0.233510982552952 ]
(%i4) dlange (inf_norm, b - A . x);
(%o4)                        2.220446049250313E-16
```

<!-- category: Numerical -->
<!-- keywords: dgesvd -->
<!-- signatures: dgesvd(A), dgesvd(A, left_p, right_p) -->
### Function: dgesvd (A)

Calcula la descomposición singular (SVD, en inglés) de la matriz *A*,
que contiene los valores singulares y, opcionalmente, los vectores singulares por
la derecha o por la izquierda. Todos los elementos de *A* deben ser enteros o 
números decimales en coma flotante. La matriz *A* puede ser cuadrada o no 
(igual número de filas que de columnas).


Sea $m$ el número de filas y $n$ el de columnas de *A*.
La descomposición singular de *A* consiste en calcular tres matrices: 
*U*, *Sigma* y *V^T*, tales que



$A = U . Sigma . V^T$


donde *U* es una matriz unitaria $m$-por-$m$,
*Sigma* es una matriz diagonal $m$-por-$n$ y
*V^T* es una matriz unitaria $n$-por-$n$.


Sea $sigma[i]$ un elemento diagonal de $Sigma$, esto es,
$Sigma[i, i] = sigma[i]$. Los elementos $sigma[i]$
se llaman valores singulares de *A*, los cuales son reales y no negativos,
siendo devueltos por la función `dgesvd` en orden descendente. 


Las primeras $min(m, n)$ columnas de *U* y *V* son los vectores
singulares izquierdo y derecho de *A*. Nótese que `dgesvd`
devuelve la transpuesta de *V*, no la propia matriz *V*.


`dgesvd(A)` calcula únicamente los valores singulares de *A*.
`dgesvd(A, left_p, right_p)` calcula los valores singulares
de *A* y los vectores sigulares por la izquierda cuando $left_p = true$,
y los vectores sigulares por la derecha cuando $right_p = true$.


La función devuelve una lista de tres elementos.
El primer elemento es una lista con los valores singulares.
El segundo elemento es `false` o la matriz de vectores singulares por la izquierda.
El tercer elemento es `false` o la matriz de vectores singulares por la derecha.


Ejemplo:


















```maxima
(%i1) load ("lapack")$
(%i2) fpprintprec : 6;
(%o2)                           6
(%i3) M: matrix([1, 2, 3], [3.5, 0.5, 8], [-1, 2, -3], [4, 9, 7]);
                        [  1    2    3  ]
                        [               ]
                        [ 3.5  0.5   8  ]
(%o3)                   [               ]
                        [ - 1   2   - 3 ]
                        [               ]
                        [  4    9    7  ]
(%i4) dgesvd (M);
(%o4)      [[14.4744, 6.38637, .452547], false, false]
(%i5) [sigma, U, VT] : dgesvd (M, true, true);
(%o5) [[14.4744, 6.38637, .452547], 
[ - .256731  .00816168   .959029    - .119523 ]
[                                             ]
[ - .526456   .672116   - .206236   - .478091 ]
[                                             ], 
[  .107997   - .532278  - .0708315  - 0.83666 ]
[                                             ]
[ - .803287  - .514659  - .180867    .239046  ]
[ - .374486  - .538209  - .755044 ]
[                                 ]
[  .130623   - .836799   0.5317   ]]
[                                 ]
[ - .917986   .100488    .383672  ]
(%i6) m : length (U);
(%o6)                           4
(%i7) n : length (VT);
(%o7)                           3
(%i8) Sigma:
        genmatrix(lambda ([i, j], if i=j then sigma[i] else 0),
                  m, n);
                  [ 14.4744     0        0    ]
                  [                           ]
                  [    0     6.38637     0    ]
(%o8)             [                           ]
                  [    0        0     .452547 ]
                  [                           ]
                  [    0        0        0    ]
(%i9) U . Sigma . VT - M;
          [  1.11022E-15        0.0       1.77636E-15 ]
          [                                           ]
          [  1.33227E-15    1.66533E-15       0.0     ]
(%o9)     [                                           ]
          [ - 4.44089E-16  - 8.88178E-16  4.44089E-16 ]
          [                                           ]
          [  8.88178E-16    1.77636E-15   8.88178E-16 ]
(%i10) transpose (U) . U;
       [     1.0      5.55112E-17    2.498E-16     2.77556E-17  ]
       [                                                        ]
       [ 5.55112E-17      1.0       5.55112E-17    4.16334E-17  ]
(%o10) [                                                        ]
       [  2.498E-16   5.55112E-17       1.0       - 2.08167E-16 ]
       [                                                        ]
       [ 2.77556E-17  4.16334E-17  - 2.08167E-16       1.0      ]
(%i11) VT . transpose (VT);
          [      1.0           0.0      - 5.55112E-17 ]
          [                                           ]
(%o11)    [      0.0           1.0       5.55112E-17  ]
          [                                           ]
          [ - 5.55112E-17  5.55112E-17       1.0      ]
```

<!-- category: Numerical -->
<!-- keywords: dlange, zlange -->
<!-- signatures: dlange(norm, A), zlange(norm, A) -->
### Function: dlange (norm, A)

Calcula una norma o seudonorma de la matriz *A*.



**max** — Calcula $max(abs(A(i, j)))$, siendo $i$ y $j$ números de filas
y columnas, respectivamente, de *A*.
Nótese que esta función no es una norma matricial.
**one_norm** — Calcula la norma $L[1]$ de *A*,
esto es, el máximo de la suma de los valores absolutos de los elementos de cada columna.
**inf_norm** — Calcula la norma $L[inf]$ de *A*,
esto es, el máximo de la suma de los valores absolutos de los elementos de cada fila.
**frobenius** — Calcula la norma de Frobenius de *A*,
esto es, la raíz cuadrada de la suma de los cuadrados de los elementos de
la matriz.

