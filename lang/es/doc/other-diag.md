## diag

<!-- category: Other -->
<!-- keywords: diag -->
<!-- signatures: diag(lm) -->
### Function: diag (lm)

Genera una matriz cuadrada con las matrices de *lm*
en la diagonal, siendo *lm* una lista de matrices o de
escalares.


Ejemplo:


```maxima
(%i1) load("diag")$

(%i2) a1:matrix([1,2,3],[0,4,5],[0,0,6])$

(%i3) a2:matrix([1,1],[1,0])$

(%i4) diag([a1,x,a2]);
                   [ 1  2  3  0  0  0 ]
                   [                  ]
                   [ 0  4  5  0  0  0 ]
                   [                  ]
                   [ 0  0  6  0  0  0 ]
(%o4)              [                  ]
                   [ 0  0  0  x  0  0 ]
                   [                  ]
                   [ 0  0  0  0  1  1 ]
                   [                  ]
                   [ 0  0  0  0  1  0 ]
```


Antes de hacer uso de esta función ejecútese  `load("diag")`.

<!-- category: Other -->
<!-- keywords: dispJordan -->
<!-- signatures: dispJordan(l) -->
### Function: dispJordan (l)

Devuelve la matriz de Jordan asociada a la codificación
dada por la lista *l*, que habitualmente será la salida
de la función `jordan`.


Ejemplo:


```maxima
(%i1) load("diag")$

(%i2) b1:matrix([0,0,1,1,1],
                [0,0,0,1,1],
                [0,0,0,0,1],
                [0,0,0,0,0],
                [0,0,0,0,0])$

(%i3) jordan(b1);
(%o3)                  [[0, 3, 2]]
(%i4) dispJordan(%);
                    [ 0  1  0  0  0 ]
                    [               ]
                    [ 0  0  1  0  0 ]
                    [               ]
(%o4)               [ 0  0  0  0  0 ]
                    [               ]
                    [ 0  0  0  0  1 ]
                    [               ]
                    [ 0  0  0  0  0 ]
```


Antes de hacer uso de esta función ejecútese  `load("diag")`.
Véanse también `jordan` y `minimalPoly`.

<!-- category: Other -->
<!-- keywords: JF -->
<!-- signatures: JF(lambda, n) -->
### Function: JF (lambda, n)

Devuelve la célula de Jordan de orden  *n* con
valor propio *lambda*.


Ejemplo:


```maxima
(%i1) load("diag")$

(%i2) JF(2,5);
                    [ 2  1  0  0  0 ]
                    [               ]
                    [ 0  2  1  0  0 ]
                    [               ]
(%o2)               [ 0  0  2  1  0 ]
                    [               ]
                    [ 0  0  0  2  1 ]
                    [               ]
                    [ 0  0  0  0  2 ]
(%i3) JF(3,2);
                         [ 3  1 ]
(%o3)                    [      ]
                         [ 0  3 ]
```


Antes de hacer uso de esta función ejecútese  `load("diag")`.

<!-- category: Other -->
<!-- keywords: jordan -->
<!-- signatures: jordan(mat) -->
### Function: jordan (mat)

Devuelve la forma de Jordan de la matriz *mat*, pero
en formato de lista de Maxima. Para obtener la matriz
correspondiente, llámese a la función `dispJordan`
utilizando como argumento la salida de `jordan`.


Ejemplo:


```maxima
(%i1) load("diag")$

(%i3) a:matrix([2,0,0,0,0,0,0,0],
               [1,2,0,0,0,0,0,0],
               [-4,1,2,0,0,0,0,0],
               [2,0,0,2,0,0,0,0],
               [-7,2,0,0,2,0,0,0],
               [9,0,-2,0,1,2,0,0],
               [-34,7,1,-2,-1,1,2,0],
               [145,-17,-16,3,9,-2,0,3])$

(%i34) jordan(a);
(%o4)             [[2, 3, 3, 1], [3, 1]]
(%i5) dispJordan(%);
                [ 2  1  0  0  0  0  0  0 ]
                [                        ]
                [ 0  2  1  0  0  0  0  0 ]
                [                        ]
                [ 0  0  2  0  0  0  0  0 ]
                [                        ]
                [ 0  0  0  2  1  0  0  0 ]
(%o5)           [                        ]
                [ 0  0  0  0  2  1  0  0 ]
                [                        ]
                [ 0  0  0  0  0  2  0  0 ]
                [                        ]
                [ 0  0  0  0  0  0  2  0 ]
                [                        ]
                [ 0  0  0  0  0  0  0  3 ]
```


Antes de hacer uso de esta función ejecútese  `load("diag")`.
Véanse también `dispJordan` y `minimalPoly`.

<!-- category: Other -->
<!-- keywords: mat_function -->
<!-- signatures: mat_function(f, mat) -->
### Function: mat_function (f, mat)

Devuelve  $f(mat)$, siendo *f* una función analítica
y *mat* una matriz. Este cálculo se basa en la fórmula integral
de Cauchy, que establece que si `f(x)` es analítica y


```maxima
mat=diag([JF(m1,n1),...,JF(mk,nk)]),
```


entonces



```maxima
f(mat)=ModeMatrix*diag([f(JF(m1,n1)),...,f(JF(mk,nk))])
          * ModeMatrix^^(-1)
```


Nótese que hay otros métodos alternativos para
realizar este cálculo.


Se presentan algunos ejemplos.


Ejemplo 1:


```maxima
(%i1) load("diag")$

(%i2) b2:matrix([0,1,0], [0,0,1], [-1,-3,-3])$

(%i3) mat_function(exp,t*b2);
               2   - t
              t  %e          - t     - t
(%o3) matrix([-------- + t %e    + %e   ,
                 2
        - t     - t                           - t
 2    %e      %e        - t           - t   %e
t  (- ----- - ----- + %e   ) + t (2 %e    - -----)
        t       2                             t
               t
                         - t          - t     - t
       - t       - t   %e        2  %e      %e
 + 2 %e   , t (%e    - -----) + t  (----- - -----)
                         t            2       t
               2   - t            - t     - t
     - t      t  %e        2    %e      %e        - t
 + %e   ], [- --------, - t  (- ----- - ----- + %e   ),
                 2                t       2
                                         t
        - t     - t      2   - t
   2  %e      %e        t  %e          - t
- t  (----- - -----)], [-------- - t %e   ,
        2       t          2
        - t     - t                           - t
 2    %e      %e        - t           - t   %e
t  (- ----- - ----- + %e   ) - t (2 %e    - -----),
        t       2                             t
               t
      - t     - t                 - t
 2  %e      %e            - t   %e
t  (----- - -----) - t (%e    - -----)])
      2       t                   t
(%i4) ratsimp(%);
               [   2              - t ]
               [ (t  + 2 t + 2) %e    ]
               [ -------------------- ]
               [          2           ]
               [                      ]
               [         2   - t      ]
(%o4)  Col 1 = [        t  %e         ]
               [      - --------      ]
               [           2          ]
               [                      ]
               [     2          - t   ]
               [   (t  - 2 t) %e      ]
               [   ----------------   ]
               [          2           ]
         [      2        - t    ]
         [    (t  + t) %e       ]
         [                      ]
 Col 2 = [     2            - t ]
         [ - (t  - t - 1) %e    ]
         [                      ]
         [     2          - t   ]
         [   (t  - 3 t) %e      ]
         [        2   - t       ]
         [       t  %e          ]
         [       --------       ]
         [          2           ]
         [                      ]
         [      2          - t  ]
 Col 3 = [    (t  - 2 t) %e     ]
         [  - ----------------  ]
         [           2          ]
         [                      ]
         [   2              - t ]
         [ (t  - 4 t + 2) %e    ]
         [ -------------------- ]
         [          2           ]
```



Ejemplo 2:


```maxima
(%i5) b1:matrix([0,0,1,1,1],
                [0,0,0,1,1],
                [0,0,0,0,1],
                [0,0,0,0,0],
                [0,0,0,0,0])$

(%i6) mat_function(exp,t*b1);
                  [              2     ]
                  [             t      ]
                  [ 1  0  t  t  -- + t ]
                  [             2      ]
                  [                    ]
(%o6)             [ 0  1  0  t    t    ]
                  [                    ]
                  [ 0  0  1  0    t    ]
                  [                    ]
                  [ 0  0  0  1    0    ]
                  [                    ]
                  [ 0  0  0  0    1    ]
(%i7) minimalPoly(jordan(b1));
                             3
(%o7)                       x
(%i8) ident(5)+t*b1+1/2*(t^2)*b1^^2;
                  [              2     ]
                  [             t      ]
                  [ 1  0  t  t  -- + t ]
                  [             2      ]
                  [                    ]
(%o8)             [ 0  1  0  t    t    ]
                  [                    ]
                  [ 0  0  1  0    t    ]
                  [                    ]
                  [ 0  0  0  1    0    ]
                  [                    ]
                  [ 0  0  0  0    1    ]
(%i9) mat_function(exp,%i*t*b1);
             [                           2 ]
             [                          t  ]
             [ 1  0  %i t  %i t  %i t - -- ]
             [                          2  ]
             [                             ]
(%o9)        [ 0  1   0    %i t    %i t    ]
             [                             ]
             [ 0  0   1     0      %i t    ]
             [                             ]
             [ 0  0   0     1        0     ]
             [                             ]
             [ 0  0   0     0        1     ]
(%i10) mat_function(cos,t*b1)+%i*mat_function(sin,t*b1);
              [                           2 ]
              [                          t  ]
              [ 1  0  %i t  %i t  %i t - -- ]
              [                          2  ]
              [                             ]
(%o10)        [ 0  1   0    %i t    %i t    ]
              [                             ]
              [ 0  0   1     0      %i t    ]
              [                             ]
              [ 0  0   0     1        0     ]
              [                             ]
              [ 0  0   0     0        1     ]
```


Ejemplo 3:


```maxima
(%i11) a1:matrix([2,1,0,0,0,0],
                 [-1,4,0,0,0,0],
                 [-1,1,2,1,0,0],
                 [-1,1,-1,4,0,0],
                 [-1,1,-1,1,3,0],
                 [-1,1,-1,1,1,2])$

(%i12) fpow(x):=block([k],declare(k,integer),x^k)$

(%i13) mat_function(fpow,a1);
                [  k      k - 1 ]         [      k - 1    ]
                [ 3  - k 3      ]         [   k 3         ]
                [               ]         [               ]
                [       k - 1   ]         [  k      k - 1 ]
                [  - k 3        ]         [ 3  + k 3      ]
                [               ]         [               ]
                [       k - 1   ]         [      k - 1    ]
                [  - k 3        ]         [   k 3         ]
(%o13)  Col 1 = [               ] Col 2 = [               ]
                [       k - 1   ]         [      k - 1    ]
                [  - k 3        ]         [   k 3         ]
                [               ]         [               ]
                [       k - 1   ]         [      k - 1    ]
                [  - k 3        ]         [   k 3         ]
                [               ]         [               ]
                [       k - 1   ]         [      k - 1    ]
                [  - k 3        ]         [   k 3         ]
         [       0       ]         [       0       ]
         [               ]         [               ]
         [       0       ]         [       0       ]
         [               ]         [               ]
         [  k      k - 1 ]         [      k - 1    ]
         [ 3  - k 3      ]         [   k 3         ]
         [               ]         [               ]
 Col 3 = [       k - 1   ] Col 4 = [  k      k - 1 ]
         [  - k 3        ]         [ 3  + k 3      ]
         [               ]         [               ]
         [       k - 1   ]         [      k - 1    ]
         [  - k 3        ]         [   k 3         ]
         [               ]         [               ]
         [       k - 1   ]         [      k - 1    ]
         [  - k 3        ]         [   k 3         ]
         [    0    ]
         [         ]         [ 0  ]
         [    0    ]         [    ]
         [         ]         [ 0  ]
         [    0    ]         [    ]
         [         ]         [ 0  ]
 Col 5 = [    0    ] Col 6 = [    ]
         [         ]         [ 0  ]
         [    k    ]         [    ]
         [   3     ]         [ 0  ]
         [         ]         [    ]
         [  k    k ]         [  k ]
         [ 3  - 2  ]         [ 2  ]
```


Antes de hacer uso de esta función ejecútese  `load("diag")`.

<!-- category: Other -->
<!-- keywords: minimalPoly -->
<!-- signatures: minimalPoly(l) -->
### Function: minimalPoly (l)

Devuelve el polinomio mínimo asociado a la
codificación dada por la lista *l*, que habitualmente
será la salida de la función `jordan`.


Ejemplo:


```maxima
(%i1) load("diag")$

(%i2) a:matrix([2,1,2,0],
               [-2,2,1,2],
               [-2,-1,-1,1],
               [3,1,2,-1])$

(%i3) jordan(a);
(%o3)               [[- 1, 1], [1, 3]]
(%i4) minimalPoly(%);
                            3
(%o4)                (x - 1)  (x + 1)
```


Antes de hacer uso de esta función ejecútese  `load("diag")`.
Véanse también `jordan` y `dispJordan`.

<!-- category: Other -->
<!-- keywords: ModeMatrix -->
<!-- signatures: ModeMatrix(A, l) -->
### Function: ModeMatrix (A, l)

Devuelve la matriz *M* tal que $(M^^-1).A.M=J$, 
donde *J* es la forma de Jordan de *A*. La lista *l* 
es la forma codificada de la forma de Jordan tal como la
devuelve la función `jordan`.


Ejemplo:


```maxima
(%i1) load("diag")$

(%i2) a:matrix([2,1,2,0],
          [-2,2,1,2],
          [-2,-1,-1,1],
          [3,1,2,-1])$

(%i3) jordan(a);
(%o3)               [[- 1, 1], [1, 3]]
(%i4) M: ModeMatrix(a,%);
                  [  1    - 1   1   1 ]
                  [                   ]
                  [   1               ]
                  [ - -   - 1   0   0 ]
                  [   9               ]
                  [                   ]
(%o4)             [   13              ]
                  [ - --   1   - 1  0 ]
                  [   9               ]
                  [                   ]
                  [  17               ]
                  [  --   - 1   1   1 ]
                  [  9                ]
(%i5) is(  (M^^-1).a.M = dispJordan(%o3)  );
(%o5)                      true
```

Nótese que `dispJordan(%o3)` es la forma de Jordan de la matriz `a`.


Antes de hacer uso de esta función ejecútese  `load("diag")`.
Véanse también `jordan` y `dispJordan`.

