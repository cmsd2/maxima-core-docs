## linearalgebra

<!-- category: LinearAlgebra -->
<!-- keywords: addmatrices -->
<!-- signatures: addmatrices(f, M_1, ..., M_n) -->
### Function: addmatrices (f, M_1, ..., M_n)

Utiliza la función *f* como una función aditiva, devolviendo la
suma de las matrices *M_1*, ..., *M_n*. La función *f* debe
ser tal que acepte un número arbitrario de argumentos; en otras palabras,
será una función n-aria de Maxima.


Ejemplos:









```maxima
(%i1) m1 : matrix([1,2],[3,4])$
(%i2) m2 : matrix([7,8],[9,10])$
(%i3) addmatrices('max,m1,m2);
(%o3) matrix([7,8],[9,10])
(%i4) addmatrices('max,m1,m2,5*m1);
(%o4) matrix([7,10],[15,20])
```

<!-- category: LinearAlgebra -->
<!-- keywords: blockmatrixp -->
<!-- signatures: blockmatrixp(M) -->
### Function: blockmatrixp (M)

Devuelve el valor `true` si y solo si *M* es una matriz
cuyos elementos son a su vez matrices.

<!-- category: LinearAlgebra -->
<!-- keywords: cholesky -->
<!-- signatures: cholesky(M), cholesky(M, field) -->
### Function: cholesky (M)

Devuelve la factorización de Cholesky de la matriz autoadjunta 
(o hermítica) *M*. El valor por defecto del segundo argumento
es `generalring`. Para una descripción de los posibles valores para
*field*, véase `lu_factor`.

<!-- category: LinearAlgebra -->
<!-- keywords: columnop -->
<!-- signatures: columnop(M, i, j, theta) -->
### Function: columnop (M, i, j, theta)

Si *M* es una matriz, devuelve la matriz que resulta de hacer la
operación columna `C_i <- C_i - theta * C_j`. Si *M*
carece de cualquiera de las filas *i* o *j*, devuelve un mensaje
de error.

<!-- category: LinearAlgebra -->
<!-- keywords: columnspace -->
<!-- signatures: columnspace(M) -->
### Function: columnspace (M)

Si *M* es una matriz, devuelve `span (v_1, ..., v_n)`, donde
el conjunto `{v_1, ..., v_n}` es la base del espacio generado por
las columnas de *M*.

<!-- category: LinearAlgebra -->
<!-- keywords: columnswap -->
<!-- signatures: columnswap(M, i, j) -->
### Function: columnswap (M, i, j)

Si *M* es una matriz, intercambia las columnas *i* y *j*.
Si *M* carece de cualquiera de las filas *i* o *j*, devuelve 
un mensaje de error.

<!-- category: LinearAlgebra -->
<!-- keywords: copy -->
<!-- signatures: copy(e) -->
### Function: copy (e)

Devuelve una copia de la expresión *e* de Maxima. Aunque *e*
puede ser cualquier expresión de Maxima, la función `copy` es
especialmente útil cuando *e* es una lista o una matriz. 
Considérese el siguiente ejemplo:










```maxima
(%i1) m : [1,[2,3]]$
(%i2) mm : m$
(%i3) mm[2][1] : x$
(%i4) m;
(%o4)                      [1,[x,3]]
(%i5) mm;
(%o5)                      [1,[x,3]]
```

Veamos el mismo ejemplo siendo ahora *mm* una copia de *m*









```maxima
(%i6) m : [1,[2,3]]$
(%i7) mm : copy(m)$
(%i8) mm[2][1] : x$
(%i9) m;
(%o9)                     [1,[2,3]]
(%i10) mm;
(%o10)                    [1,[x,3]]
```

En esta ocasión, la asignación a *mm* no cambia el valor de *m*.

<!-- category: LinearAlgebra -->
<!-- keywords: ctranspose -->
<!-- signatures: ctranspose(M) -->
### Function: ctranspose (M)

Devuelve la transpuesta compleja conjugada de la matriz *M*. La función
`ctranspose` utiliza `matrix_element_transpose` para transponer
cada elemento de la matriz.

<!-- category: LinearAlgebra -->
<!-- keywords: diag_matrix -->
<!-- signatures: diag_matrix(d_1, d_2, ..., d_n) -->
### Function: diag_matrix (d_1, d_2, ..., d_n)

Devuelve una matriz diagonal con los elementos de la diagonal iguales a
*d_1*, *d_2*, ..., *d_n*; cuando éstos son matrices, los
elementos nulos de la matriz devuelta son matrices nulas de tamaño 
apropiado. Por ejemplo:







```maxima
(%i1) diag_matrix(diag_matrix(1,2),diag_matrix(3,4));

                            [ [ 1  0 ]  [ 0  0 ] ]
                            [ [      ]  [      ] ]
                            [ [ 0  2 ]  [ 0  0 ] ]
(%o1)                       [                    ]
                            [ [ 0  0 ]  [ 3  0 ] ]
                            [ [      ]  [      ] ]
                            [ [ 0  0 ]  [ 0  4 ] ]
(%i2) diag_matrix(p,q);

                                   [ p  0 ]
(%o2)                              [      ]
                                   [ 0  q ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: dotproduct -->
<!-- signatures: dotproduct(u, v) -->
### Function: dotproduct (u, v)

Devuelve el producto escalar de los vectores *u* y *v*. Equivale
a `conjugate (transpose (u)) . v`. Los argumentos *u* y *v*
deben ser vectores columna.

<!-- category: LinearAlgebra -->
<!-- keywords: eigens_by_jacobi -->
<!-- signatures: eigens_by_jacobi(A), eigens_by_jacobi(A, field_type) -->
### Function: eigens_by_jacobi (A)

Calcula los valores y vectores propios de *A* por el método de
las rotaciones de Jacobi. *A* debe ser una matriz simétrica
(aunque no necesariamente definida o semidefinida positiva).
El argumento *field_type* indica el tipo numérico sobre el
que se realizan los cálculos, que puede ser tanto `floatfield`
como `bigfloatfield`. En caso de que no se especifique *field_type*,
su valor por defecto será `floatfield`.


Los elementos de *A* deben ser números o expresiones reducibles
a números mediante la ejecución de `float` o `bfloat`,
según sea el valor de *field_type*.


Ejemplos:











```maxima
(%i1) S : matrix ([1/sqrt(2), 1/sqrt(2)], [- 1/sqrt(2), 1/sqrt(2)]);
                     [     1         1    ]
                     [  -------   ------- ]
                     [  sqrt(2)   sqrt(2) ]
(%o1)                [                    ]
                     [      1        1    ]
                     [ - -------  ------- ]
                     [   sqrt(2)  sqrt(2) ]
(%i2) L : matrix ([sqrt(3), 0], [0, sqrt(5)]);
                      [ sqrt(3)     0    ]
(%o2)                 [                  ]
                      [    0     sqrt(5) ]
(%i3) M : S . L . transpose (S);
            [ sqrt(5)   sqrt(3)  sqrt(5)   sqrt(3) ]
            [ ------- + -------  ------- - ------- ]
            [    2         2        2         2    ]
(%o3)       [                                      ]
            [ sqrt(5)   sqrt(3)  sqrt(5)   sqrt(3) ]
            [ ------- - -------  ------- + ------- ]
            [    2         2        2         2    ]
(%i4) eigens_by_jacobi (M);
The largest percent change was 0.1454972243679
The largest percent change was 0.0
number of sweeps: 2
number of rotations: 1
(%o4) [[1.732050807568877, 2.23606797749979], 
                        [  0.70710678118655   0.70710678118655 ]
                        [                                      ]]
                        [ - 0.70710678118655  0.70710678118655 ]
(%i5) float ([[sqrt(3), sqrt(5)], S]);
(%o5) [[1.732050807568877, 2.23606797749979], 
                        [  0.70710678118655   0.70710678118655 ]
                        [                                      ]]
                        [ - 0.70710678118655  0.70710678118655 ]
(%i6) eigens_by_jacobi (M, bigfloatfield);
The largest percent change was 1.454972243679028b-1
The largest percent change was 0.0b0
number of sweeps: 2
number of rotations: 1
(%o6) [[1.732050807568877b0, 2.23606797749979b0], 
                [  7.071067811865475b-1   7.071067811865475b-1 ]
                [                                              ]]
                [ - 7.071067811865475b-1  7.071067811865475b-1 ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: get_lu_factors -->
<!-- signatures: get_lu_factors(x) -->
### Function: get_lu_factors (x)

Cuando `x = lu_factor (A)`, entonces `get_lu_factors`
devuelve una lista de la forma `[P, L, U]`, donde *P* es una matriz
permutación, *L* es triangular inferior con unos en la diagonal y *U*
es triangular superior, verificándose que `A = P L U`.

<!-- category: LinearAlgebra -->
<!-- keywords: hankel -->
<!-- signatures: hankel(col), hankel(col, row) -->
### Function: hankel (col)

Devuelve la matriz de Hankel *H*. La primera columna de *H* coincide
con *col*, excepto en el primer elemento, la última fila de *H* es
*row*. El valor por defecto para *row* es el vector nulo con igual
número de elementos que *col*.

<!-- category: LinearAlgebra -->
<!-- keywords: hessian -->
<!-- signatures: hessian(f, x) -->
### Function: hessian (f, x)

Devuelve la matriz hessiana de *f* con respecto de la lista de variables
*x*. El elemento `(i, j)`-ésimo de la matriz
hessiana es `diff(f, x[i], 1, x[j], 1)`.


Ejemplos:








```maxima
(%i1) hessian (x * sin (y), [x, y]);
                     [   0       cos(y)   ]
(%o1)                [                    ]
                     [ cos(y)  - x sin(y) ]
(%i2) depends (F, [a, b]);
(%o2)                       [F(a, b)]
(%i3) hessian (F, [a, b]);
                        [   2      2   ]
                        [  d F    d F  ]
                        [  ---   ----- ]
                        [    2   da db ]
                        [  da          ]
(%o3)                   [              ]
                        [   2      2   ]
                        [  d F    d F  ]
                        [ -----   ---  ]
                        [ da db     2  ]
                        [         db   ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: hilbert_matrix -->
<!-- signatures: hilbert_matrix(n) -->
### Function: hilbert_matrix (n)

Devuelve la matriz de Hilbert *n* por *n*. Si *n* no es
un entero positivo, emite un mensaje de error.

<!-- category: LinearAlgebra -->
<!-- keywords: identfor -->
<!-- signatures: identfor(M), identfor(M, fld) -->
### Function: identfor (M)

Devuelve una matriz identidad con la misma forma que la matriz
*M*. Los elementos de la diagonal de la matriz identidad son
la identidad multiplicativa del campo *fld*; el valor por
defecto para *fld* es *generalring*.


El primer argumento *M* debe ser una matriz cuadrada o no ser
matriz en absoluto. Si *M* es una matriz, sus elementos pueden
ser matrices cuadradas. La matriz puede tener bloques a cualquier nivel
finito de profundidad.


Véase también `zerofor`

<!-- category: LinearAlgebra -->
<!-- keywords: invert_by_lu -->
<!-- signatures: invert_by_lu(M, (rng generalring)) -->
### Function: invert_by_lu (M, (rng generalring))

Invierte la matriz *M* mediante la factorización LU, la cual
se hace utilizando el anillo *rng*.

<!-- category: LinearAlgebra -->
<!-- keywords: jacobian -->
<!-- signatures: jacobian(f, x) -->
### Function: jacobian (f, x)

Devuelve la matriz jacobiana de la lista de funciones *f* respecto
de la lista de variables *x*. El elemento `(i, j)`-ésimo de
la matriz jacobiana es `diff(f[i], x[j])`.


Ejemplos:








```maxima
(%i1) jacobian ([sin (u - v), sin (u * v)], [u, v]);
                  [ cos(v - u)  - cos(v - u) ]
(%o1)             [                          ]
                  [ v cos(u v)   u cos(u v)  ]
(%i2) depends ([F, G], [y, z]);
(%o2)                  [F(y, z), G(y, z)]
(%i3) jacobian ([F, G], [y, z]);
                           [ dF  dF ]
                           [ --  -- ]
                           [ dy  dz ]
(%o3)                      [        ]
                           [ dG  dG ]
                           [ --  -- ]
                           [ dy  dz ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: kronecker_product -->
<!-- signatures: kronecker_product(A, B) -->
### Function: kronecker_product (A, B)

Devuelve el producto de Kroneckerde las matrices *A* y *B*.

<!-- category: LinearAlgebra -->
<!-- keywords: locate_matrix_entry -->
<!-- signatures: locate_matrix_entry(M, r_1, c_1, r_2, c_2, f, rel) -->
### Function: locate_matrix_entry (M, r_1, c_1, r_2, c_2, f, rel)

El primer argumento debe ser una matriz, mientras que los argumentos
desde *r_1* hasta *c_2* determinan la submatriz de *M* tomando
las filas desde *r_1* hasta *r_2* y las columnas desde *c_1*
hasta *c_2*.


La función `locate_matrix_entry` busca en la submatriz de *M*
un elemento que satisfaga cierta propiedad. hay tres posibilidades:


(1) `rel = 'bool` y *f* es un predicado: 


Rastrea la submatriz de izquierda a derecha y de arriba hacia abajo,
devolviendo el índice del primer elemento que 
satisface el predicado *f*; si ningún elemento lo satisface,
el resultado es `false`.


(2) `rel = 'max` y *f* una función real:


Rastrea la submatriz buscando el elemento que maximice *f*,
devolviendo el índice correspondiente.


(3) `rel = 'min` y *f* una función real:


Rastrea la submatriz buscando el elemento que minimice *f*,
devolviendo el índice correspondiente.

<!-- category: LinearAlgebra -->
<!-- keywords: lu_backsub -->
<!-- signatures: lu_backsub(M, b) -->
### Function: lu_backsub (M, b)

Si `M = lu_factor (A, field)`, entonces
`lu_backsub (M, b)` resuelve el sistema de ecuaciones
lineales `A x = b`.

<!-- category: LinearAlgebra -->
<!-- keywords: lu_factor -->
<!-- signatures: lu_factor(M, field) -->
### Function: lu_factor (M, field)

Devuelve una lista de la forma `[LU, perm, fld]`,
o `[LU, perm, fld, lower-cnd upper-cnd]`, donde




- *
La matriz *LU* contiene la factorización de *M* de forma empaquetada, lo
que significa tres cosas. En primer lugar, que las filas de *LU* están permutadas de
acuerdo con la lista *perm*; por ejemplo, si *perm* es la lista `[3,2,1]`,
la primera fila de la factorización *LU* es la tercera fila de la matriz *LU*.
En segundo lugar, el factor triangular inferior de *M* es la parte triangular inferior
de *LU* con los elementos de la diagonal sustituidos por unos. Por último, el factor
triangular superior de *M* es la parte triangular superior de *LU*.
- *
Si el campo es `floatfield` o `complexfield`, los números *lower-cnd* y
*upper-cnd* son las cotas inferior y superior del número de condición de la norma
infinita de *M*. El número de condición no se puede estimar para todos los campos,
en cuyo caso `lu_factor` devuelve una lista de dos elementos. Tanto la cota inferior
como la superior pueden diferir de sus valores verdaderos. Véase también `mat_cond`.


El argumento *M* debe ser una matriz cuadrada.


El argumento opcional *fld* debe ser un símbolo que determine un anillo o
un campo. Los anillos y campos predefinidos son:



1. `generalring` – el anillo de las expresiones de Maxima
2. `floatfield` – el campo de los números decimales en coma flotante de doble precisión
3. `complexfield` – el campo de los números complejos decimales en coma flotante de doble precisión
4. `crering`  – el anillo de las expresiones canónicas racionales (*Canonical Rational Expression* o CRE) de Maxima
5. `rationalfield` – el campo de los números racionales
6. `runningerror` – controla los errores de redondeo de las operaciones en coma flotante
7. `noncommutingring` – el anillo de las expresiones de Maxima en las que el producto es el operador no conmutativo "."


Si el campo es `floatfield`, `complexfield` o `runningerror`,
el algoritmo utiliza pivoteo parcial; para los demás campos, las filas se cambian 
cuando se necesita evitar pivotes nulos.


La suma aritmética en coma flotante no es asociativa, por lo que el
significado de ’campo’ no coincide exactamente con su definición matemática.


Un elemento del campo `runningerror` consiste en una lista de Maxima
de la forma `[x,n]`, donde *x* es un número decimal en coma flotante 
y `n` un enetro. La diferencia relativa entre el valor real de `x` y 
`x` está aproximadamente acotado por el valor epsilon de la máquina 
multiplicado por `n`. 


No es posible la definición de un nuevo campo por parte del usuario, a menos
que éste tenga conocimientos de Common Lisp. Para hacerlo, el usuario debe
definir funciones para las operaciones aritméticas y para convertir de la
representación del campo a Maxima y al revés. Además, en los campos ordenados,
donde se hace uso del pivoteo parcial, el usuario debe definir funciones para el 
módulo y para comparar números del campo. Después de lo anterior, tan solo queda
definir una estructura Common Lisp `mring`. El fichero `mring` tiene
muchos ejemplos.


Para calcular la factorización, la primera tarea consiste en convertir cada elemento
de la matriz a un elemento del campo especificado. Si la conversión no es posible,
la factorización se detiene con un mensaje de error. Los elementos del campo
no necesitan ser expresiones de Maxima; por ejemplo, los elementos de `complexfield`
son números complejos de Common Lisp. Tras la factorización, los elementos de la
matriz deben convertirse nuevamente a expresiones de Maxima.


Véase también  `get_lu_factors`.



Ejemplos:















```maxima
(%i1) w[i,j] := random (1.0) + %i * random (1.0);
(%o1)          w     := random(1.) + %i random(1.)
                i, j
(%i2) showtime : true$
Evaluation took 0.00 seconds (0.00 elapsed)
(%i3) M : genmatrix (w, 100, 100)$
Evaluation took 7.40 seconds (8.23 elapsed)
(%i4) lu_factor (M, complexfield)$
Evaluation took 28.71 seconds (35.00 elapsed)
(%i5) lu_factor (M, generalring)$
Evaluation took 109.24 seconds (152.10 elapsed)
(%i6) showtime : false$

(%i7) M : matrix ([1 - z, 3], [3, 8 - z]); 
                        [ 1 - z    3   ]
(%o7)                   [              ]
                        [   3    8 - z ]
(%i8) lu_factor (M, generalring);
          [ 1 - z         3        ]
          [                        ]
(%o8)    [[   3            9       ], [1, 2], generalring]
          [ -----  - z - ----- + 8 ]
          [ 1 - z        1 - z     ]
(%i9) get_lu_factors (%);
                  [   1    0 ]  [ 1 - z         3        ]
        [ 1  0 ]  [          ]  [                        ]
(%o9)  [[      ], [   3      ], [                9       ]]
        [ 0  1 ]  [ -----  1 ]  [   0    - z - ----- + 8 ]
                  [ 1 - z    ]  [              1 - z     ]
(%i10) %[1] . %[2] . %[3];
                        [ 1 - z    3   ]
(%o10)                  [              ]
                        [   3    8 - z ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: mat_cond -->
<!-- signatures: mat_cond(M, 1), mat_cond(M, inf) -->
### Function: mat_cond (M, 1)

Devuelve el número de condición de la *p*-norma de la matriz
*M*. Los valores admisibles para  *p* son 1 y *inf*. Esta
función utiliza la factorización LU para invertir la matriz *M*,
por lo que el tiempo de ejecución de `mat_cond` es proporcional al
cubo del tamaño de la matriz; `lu_factor` determina las cotas inferior
y superior para el número de condición de la norma infinita en un tiempo
proporcional al cuadrado del tamaño de la matriz.

<!-- category: LinearAlgebra -->
<!-- keywords: mat_fullunblocker -->
<!-- signatures: mat_fullunblocker(M) -->
### Function: mat_fullunblocker (M)

Si *M* es una matriz de bloques, transforma la matriz llevando todos
los elementos de los bloques al primer nivel. Si *M* es una matriz,
devuelve *M*; en cualquier otro caso, envía un mensaje de error.

<!-- category: LinearAlgebra -->
<!-- keywords: mat_norm -->
<!-- signatures: mat_norm(M, 1), mat_norm(M, inf), mat_norm(M, frobenius) -->
### Function: mat_norm (M, 1)

Devuelve la *p*-norma de la matriz *M*. Los valores admisibles
para *p* son 1, `inf` y `frobenius` (la norma matricial de Frobenius).
La matriz *M* no debe contener bloques.

<!-- category: LinearAlgebra -->
<!-- keywords: mat_trace -->
<!-- signatures: mat_trace(M) -->
### Function: mat_trace (M)

Calcula la traza de la matriz *M*. Si *M* no es una matriz, devuelve
una forma nominal. Si *M* es una matriz de bloques, `mat_trace(M)`
calcula el mismo valor que `mat_trace(mat_unblocker(m))`.

<!-- category: LinearAlgebra -->
<!-- keywords: mat_unblocker -->
<!-- signatures: mat_unblocker(M) -->
### Function: mat_unblocker (M)

Si *M* es una matriz de bloques, deshace los bloques de un nivel. Si *M*
es una matriz, `mat_unblocker (M)` devuelve *M*; en cualquier otro caso, 
envía un mensaje de error.


Si todos los elementos de *M* son matrices, `mat_unblocker (M)` devuelve
una matriz sin bloques, pero si los elementos de *M* son a su vez matrices de
bloques, `mat_unblocker (M)` devuelve una matriz con el nivel de bloques
disminuido en uno.


En caso de trabajar con matrices de bloques, quizás sea conveniente darle a
`matrix_element_mult` el valor `"."` y a `matrix_element_transpose`
el valor `'transpose`. Véase también `mat_fullunblocker`.


Ejemplo:









```maxima
(%i1) A : matrix ([1, 2], [3, 4]);
                            [ 1  2 ]
(%o1)                       [      ]
                            [ 3  4 ]
(%i2) B : matrix ([7, 8], [9, 10]);
                            [ 7  8  ]
(%o2)                       [       ]
                            [ 9  10 ]
(%i3) matrix ([A, B]);

                     [ [ 1  2 ]  [ 7  8  ] ]
(%o3)                [ [      ]  [       ] ]
                     [ [ 3  4 ]  [ 9  10 ] ]

(%i4) mat_unblocker (%);
                         [ 1  2  7  8  ]
(%o4)                    [             ]
                         [ 3  4  9  10 ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: matrix_size -->
<!-- signatures: matrix_size(M) -->
### Function: matrix_size (M)

Devuelve una lista con el número de filas y columnas de la matriz *M*.

<!-- category: LinearAlgebra -->
<!-- keywords: nullity -->
<!-- signatures: nullity(M) -->
### Function: nullity (M)

Si *M* es una matriz, devuelve la dimensión del espacio nulo de *M*.

<!-- category: LinearAlgebra -->
<!-- keywords: nullspace -->
<!-- signatures: nullspace(M) -->
### Function: nullspace (M)

Si *M* es una matriz, devuelve `span (v_1, ..., v_n)`, siendo 
`{v_1, ..., v_n}` la base del espacio nulo de *M*. Si el 
espacio nulo contiene un único elemento, devuelve `span ()`.

<!-- category: LinearAlgebra -->
<!-- keywords: orthogonal_complement -->
<!-- signatures: orthogonal_complement(v_1, ..., v_n) -->
### Function: orthogonal_complement (v_1, ..., v_n)

Devuelve `span (u_1, ..., u_m)`, siendo `{u_1, ..., u_m}` la base
del complemento ortogonal del conjunto `(v_1, ..., v_n)`, cuyos elementos
deben ser vectores columna.

<!-- category: LinearAlgebra -->
<!-- keywords: polynomialp -->
<!-- signatures: polynomialp(p, L, coeffp, exponp), polynomialp(p, L, coeffp), polynomialp(p, L) -->
### Function: polynomialp (p, L, coeffp, exponp)

Devuelve `true` si *p* es un polinomio cuyas variables son las
de la lista *L*, el predicado *coeffp* toma el valor `true` al
aplicarlo a cada coeficiente y el predicado *exponp* también alcanza el
valor `true` al ser aplicado a los exponentes de las variables listadas en
*L*. En caso de necesitar que *exponp* no sea un predicado por defecto,
se deberá especificar también el predicado *coeffp*, aunque aquí
se desee su comportamiento por defecto.



La instrucción `polynomialp (p, L, coeffp)` equivale a
`polynomialp (p, L, coeffp, 'nonnegintegerp)`, al tiempo que
`polynomialp (p, L)` equivale a
`polynomialp (p, L, 'constantp, 'nonnegintegerp)`.


No es necesario expandir el polinomio:







```maxima
(%i1) polynomialp ((x + 1)*(x + 2), [x]);
(%o1)                         true
(%i2) polynomialp ((x + 1)*(x + 2)^a, [x]);
(%o2)                         false
```


Un ejemplo utilizando valores distintos a los utilizados por defecto en 
*coeffp* y en *exponp*:









```maxima
(%i1) polynomialp ((x + 1)*(x + 2)^(3/2), [x],
                   numberp, numberp);
(%o1)                         true
(%i2) polynomialp ((x^(1/2) + 1)*(x + 2)^(3/2), [x],
                   numberp, numberp);
(%o2)                         true
```


Polinomios con dos variables:







```maxima
(%i1) polynomialp (x^2 + 5*x*y + y^2, [x]);
(%o1)                         false
(%i2) polynomialp (x^2 + 5*x*y + y^2, [x, y]);
(%o2)                         true
```

<!-- category: LinearAlgebra -->
<!-- keywords: polytocompanion -->
<!-- signatures: polytocompanion(p, x) -->
### Function: polytocompanion (p, x)

Si *p* es un polinomio en *x*, devuelve la matriz compañera de *p*. Para
un polinomio mónico *p* de grado *n* se tiene
`p = (-1)^n charpoly (polytocompanion (p, x))`.


Si *p* no es un polinomio en  *x*, se devuelve un mensaje de error.

<!-- category: LinearAlgebra -->
<!-- keywords: ptriangularize -->
<!-- signatures: ptriangularize(M, v) -->
### Function: ptriangularize (M, v)

Si *M* es una matriz en la que sus elementos son polinomios en *v*,
devuelve una matriz *M2* tal que



1. *M2* es triangular superior,
2. `M2 = E_n ... E_1 M`, donde *E_1*, ...,
*E_n* son matrices elementales cuyos elementos son polinomios en *v*,
3. `|det (M)| = |det (M2)|`,


Nota: esta función no comprueba si los elementos de la matriz son
polinomios en *v*.

<!-- category: LinearAlgebra -->
<!-- keywords: rowop -->
<!-- signatures: rowop(M, i, j, theta) -->
### Function: rowop (M, i, j, theta)

Si *M* es una matriz, devuelve la matriz que resulta de relizar la
transformación `R_i <- R_i - theta * R_j` con las filas `R_i` y 
`R_j`. Si *M* no tiene estas filas, devuelve un mensaje de error.

<!-- category: LinearAlgebra -->
<!-- keywords: rowswap -->
<!-- signatures: rowswap(M, i, j) -->
### Function: rowswap (M, i, j)

Si *M* es una matriz, intercambia las filas  *i* y *j*. Si *M*
carece de estas filas, devuelve un mensaje de error.

<!-- category: LinearAlgebra -->
<!-- keywords: toeplitz -->
<!-- signatures: toeplitz(col), toeplitz(col, row) -->
### Function: toeplitz (col)

Devuelve una  matriz de Toeplitz *T*. La primera columna de *T* es *col*,
excepto su primer elemento. La primera fila de *T* es *row*. El valor por
defecto para *row* es el complejo conjugado de *col*. Ejemplo:






```maxima
(%i1)  toeplitz([1,2,3],[x,y,z]);

                                  [ 1  y  z ]
                                  [         ]
(%o1)                             [ 2  1  y ]
                                  [         ]
                                  [ 3  2  1 ]

(%i2)  toeplitz([1,1+%i]);


                              [   1     1 - %I ]
(%o2)                         [                ]
                              [ %I + 1    1    ]
```

<!-- category: LinearAlgebra -->
<!-- keywords: vandermonde_matrix -->
<!-- signatures: vandermonde_matrix([x_1, ..., x_n]) -->
### Function: vandermonde_matrix ([x_1, ..., x_n])

Devuelve una matriz *n* por *n*, cuya *i*-ésima fila es
`[1, x_i, x_i^2, ... x_i^(n-1)]`.

<!-- category: LinearAlgebra -->
<!-- keywords: zerofor -->
<!-- signatures: zerofor(M), zerofor(M, fld) -->
### Function: zerofor (M)

Devuelve la matriz nula con la misma estructura que la matriz *M*.
Cada elemento de la matriz nula es la identidad aditiva del campo *fld*;
el valor por defecto de *fld* es *generalring*.


El primer argumento de *M* debe ser una matriz cuadrada o no ser matriz en
absoluto. Si *M* es una matriz, cada uno de sus elementos puede ser una 
matriz cuadrada, por lo que *M* puede ser una matriz de Maxima definida por
bloques.


Véase también `identfor`.

<!-- category: LinearAlgebra -->
<!-- keywords: zeromatrixp -->
<!-- signatures: zeromatrixp(M) -->
### Function: zeromatrixp (M)

Si *M* no es una matriz definida por bloques, devuelve `true` si
 `is (equal (e, 0))` es verdadero para todo elemento *e* de
*M*. Si *M* es una matriz por bloques, devuelve `true` si
`zeromatrixp` devuelve a su vez `true` para cada elemento de *e*.

