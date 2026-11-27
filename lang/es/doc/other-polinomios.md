## Polinomios

<!-- category: Other -->
<!-- keywords: algebraic -->
<!-- signatures: algebraic -->
### Variable: algebraic

Valor por defecto: `false`


La variable `algebraic` debe valer `true` para que se pueda hacer la simplificación de enteros algebraicos.

<!-- category: Other -->
<!-- keywords: berlefact -->
<!-- signatures: berlefact -->
### Variable: berlefact

Valor por defecto: `true`


Si `berlefact` vale `false` entonces se utiliza el algoritmo de factorización de Kronecker, en caso contrario se utilizará el algoritmo de Berlekamp, que es el que se aplica por defecto.

<!-- category: Other -->
<!-- keywords: bezout -->
<!-- signatures: bezout(p1, p2, x) -->
### Function: bezout (p1, p2, x)

Es una alternativa a la función `resultant`.  Devuelve una matriz.



```maxima
(%i1) bezout(a*x+b, c*x^2+d, x);
                         [ b c  - a d ]
(%o1)                    [            ]
                         [  a     b   ]
(%i2) determinant(%);
                            2      2
(%o2)                      a  d + b  c
(%i3) resultant(a*x+b, c*x^2+d, x);
                            2      2
(%o3)                      a  d + b  c
```

<!-- category: Other -->
<!-- keywords: bothcoef -->
<!-- signatures: bothcoef(expr, x) -->
### Function: bothcoef (expr, x)

Devuelve una lista cuyo primer miembro es el coeficiente de *x* en *expr* (que coincide con el que devuelve `ratcoef` si *expr* está en formato CRE, o el que devuelve `coeff` si no está en este formato) y cuyo segundo miembro es la parte restante de *expr*. Esto es, `[A, B]` donde `expr = A*x + B`.


Ejemplo:








```maxima
(%i1) islinear (expr, x) := block ([c],
        c: bothcoef (rat (expr, x), x),
        is (freeof (x, c) and c[1] # 0))$
(%i2) islinear ((r^2 - (x - r)^2)/x, x);
(%o2)                         true
```

<!-- category: Other -->
<!-- keywords: coeff -->
<!-- signatures: coeff(expr, x, n), coeff(expr, x) -->
### Function: coeff (expr, x, n)

Devuelve el coeficiente de `x^n` en *expr*,
donde *expr* es un polinomio o monomio en *x*.


`coeff(expr, x^n)` es equivalente a
`coeff(expr, x, n)`.
`coeff(expr, x, 0)` devuelve el resto de *expr*,
el cual no contiene a *x*. En caso de omisión, se entiende
que *n* es igual a 1.


*x* puede ser tanto el nombre de una variable simple como el
de una variable con subíndice, o también una
subexpresión de *expr* que contenga un operador junto con
todos sus argumentos.


En ocasiones, es posible calcular los coeficientes de expresiones
equivalentes a *expr* aplicando `expand` o `factor`.
`coeff` no aplica ni `expand`, ni `factor`, ni ninguna otra
función.


`coeff` se distribuye sobre listas, matrices y ecuaciones.


Ejemplos:


`coeff` devuelve el coeficiente de `x^n` en *expr*.






```maxima
(%i1) coeff (b^3*a^3 + b^2*a^2 + b*a + 1, a^3);
                                3
(%o1)                          b
```


`coeff(expr, x^n)` es equivalente
a `coeff(expr, x, n)`.







```maxima
(%i1) coeff (c[4]*z^4 - c[3]*z^3 - c[2]*z^2 + c[1]*z, z, 3);
(%o1)                         - c
                                 3
(%i2) coeff (c[4]*z^4 - c[3]*z^3 - c[2]*z^2 + c[1]*z, z^3);
(%o2)                         - c
                                 3
```


`coeff(expr, x, 0)` devuelve el resto de *expr*,
el cual no contiene a *x*.






```maxima
(%i1) coeff (a*u + b^2*u^2 + c^3*u^3, b, 0);
                            3  3
(%o1)                      c  u  + a u
```


*x* puede ser tanto el nombre de una variable simple como el
de una variable con subíndice, o también una
subexpresión de *expr* que contenga un operador junto con
todos sus argumentos.









```maxima
(%i1) coeff (h^4 - 2*%pi*h^2 + 1, h, 2);
(%o1)                        - 2 %pi
(%i2) coeff (v[1]^4 - 2*%pi*v[1]^2 + 1, v[1], 2);
(%o2)                        - 2 %pi
(%i3) coeff (sin(1 + x)*sin(x) + sin(1 + x)^3*sin(x)^3, sin(1 + x)^3);
                                3
(%o3)                        sin (x)
(%i4) coeff ((d - a)^2*(b + c)^3 + (a + b)^4*(c - d), a + b, 4);
(%o4)                         c - d
```


`coeff` no aplica ni `expand`, ni `factor`, ni ninguna otra
función.











```maxima
(%i1) coeff (c*(a + b)^3, a);
(%o1)                           0
(%i2) expand (c*(a + b)^3);
                 3          2        2        3
(%o2)           b  c + 3 a b  c + 3 a  b c + a  c
(%i3) coeff (%, a);
                                2
(%o3)                        3 b  c
(%i4) coeff (b^3*c + 3*a*b^2*c + 3*a^2*b*c + a^3*c, (a + b)^3);
(%o4)                           0
(%i5) factor (b^3*c + 3*a*b^2*c + 3*a^2*b*c + a^3*c);
                                  3
(%o5)                      (b + a)  c
(%i6) coeff (%, (a + b)^3);
(%o6)                           c
```


`coeff` se distribuye sobre listas, matrices y ecuaciones.








```maxima
(%i1) coeff ([4*a, -3*a, 2*a], a);
(%o1)                      [4, - 3, 2]
(%i2) coeff (matrix ([a*x, b*x], [-c*x, -d*x]), x);

                          [  a    b  ]
(%o2)                     [          ]
                          [ - c  - d ]

(%i3) coeff (a*u - b*v = 7*u + 3*v, u);
(%o3)                         a = 7
```

<!-- category: Other -->
<!-- keywords: content -->
<!-- signatures: content(p_1, x_1, ..., x_n) -->
### Function: content (p_1, x_1, ..., x_n)

Devuelve una lista cuyo primer miembro es el máximo común divisor de los coeficientes de los términos del polinomio *p_1* de variable *x_n* (este es el contenido) y cuyo segundo miembro es el polinomio *p_1* dividido por el contenido.




Ejemplos:





```maxima
(%i1) content (2*x*y + 4*x^2*y^2, y);
                                   2
(%o1)                   [2 x, 2 x y  + y]
```

<!-- category: Other -->
<!-- keywords: denom -->
<!-- signatures: denom(expr) -->
### Function: denom (expr)

Devuelve el denominador de la expresión racional *expr*.

<!-- category: Other -->
<!-- keywords: divide -->
<!-- signatures: divide(p_1, p_2, x_1, ..., x_n) -->
### Function: divide (p_1, p_2, x_1, ..., x_n)

Calcula el cociente y el resto del polinomio *p_1* dividido por el polinomio *p_2*, siendo la variable principal *x_n*.

Las otras funciones son como en la función `ratvars`. El resultado es una lista cuyo primer miembro es el cociente y el segundo miembro el resto.


Ejemplos:






```maxima
(%i1) divide (x + y, x - y, x);
(%o1)                       [1, 2 y]
(%i2) divide (x + y, x - y);
(%o2)                      [- 1, 2 x]
```



Nótese que `y` es la variable principal en el segundo ejemplo.

<!-- category: Other -->
<!-- keywords: eliminate -->
<!-- signatures: eliminate([eqn_1, ..., eqn_n], [x_1, ..., x_k]) -->
### Function: eliminate ([eqn_1, ..., eqn_n], [x_1, ..., x_k])

Elimina variables de ecuaciones (o de expresiones que se supone valen cero) tomando resultantes sucesivas. Devuelve una lista con `n - k` expresiones y *k* variables *x_1*, ..., *x_k* eliminadas.  Primero se elimina  *x_1* dando `n - 1` expresiones, después se elimina `x_2`, etc.  Si `k = n` entonces se devuelve una lista con una única expresión, libre de las variables *x_1*, ..., *x_k*. En este caso se llama a `solve` para resolver la última resultante para la última variable.


Ejemplo:








```maxima
(%i1) expr1: 2*x^2 + y*x + z;
                                      2
(%o1)                    z + x y + 2 x
(%i2) expr2: 3*x + 5*y - z - 1;
(%o2)                  - z + 5 y + 3 x - 1
(%i3) expr3: z^2 + x - y^2 + 5;
                          2    2
(%o3)                    z  - y  + x + 5
(%i4) eliminate ([expr3, expr2, expr1], [y, z]);
             8         7         6          5          4
(%o4) [7425 x  - 1170 x  + 1299 x  + 12076 x  + 22887 x

                                    3         2
                            - 5154 x  - 1291 x  + 7688 x + 15376]
```

<!-- category: Other -->
<!-- keywords: ezgcd -->
<!-- signatures: ezgcd(p_1, p_2, p_3, ...) -->
### Function: ezgcd (p_1, p_2, p_3, ...)

Devuelve una lista cuyo primer elemento es el máximo común divisor (mcd)
de los polinomios *p_1*, *p_2*, *p_3*, ...,  siendo los 
miembros restantes los mismos polinomios divididos por el mcd. 
Se utiliza siempre el algoritmo `ezgcd`.


Véanse también `gcd`, `gcdex`, `gcdivide` y `poly_gcd`.


Ejemplos:


Los tres polinomios tiene como máximo común divisor `2*x-3`,
el cual se calcula primero con la función `gcd` y luego con
`ezgcd`.



```maxima
(%i1) p1 : 6*x^3-17*x^2+14*x-3;
                        3       2
(%o1)                6 x  - 17 x  + 14 x - 3
(%i2) p2 : 4*x^4-14*x^3+12*x^2+2*x-3;
                    4       3       2
(%o2)            4 x  - 14 x  + 12 x  + 2 x - 3
(%i3) p3 : -8*x^3+14*x^2-x-3;
                          3       2
(%o3)                - 8 x  + 14 x  - x - 3

(%i4) gcd(p1, gcd(p2, p3));
(%o4)                        2 x - 3

(%i5) ezgcd(p1, p2, p3);
                   2               3      2           2
(%o5) [2 x - 3, 3 x  - 4 x + 1, 2 x  - 4 x  + 1, - 4 x  + x + 1]
```

<!-- category: Other -->
<!-- keywords: facexpand -->
<!-- signatures: facexpand -->
### Variable: facexpand

Valor por defecto: `true`


La variable `facexpand` controla si los factores irreducibles devueltos por `factor` están en formato expandido (por defecto) o recursivo  (CRE normal).

<!-- category: Other -->
<!-- keywords: factor -->
<!-- signatures: factor(expr), factor(expr, p) -->
### Function: factor (expr)

Factoriza la expresión *expr*, que puede contener
cualquier número de variables o funciones, en factores 
irreducibles respecto de los enteros. La llamada 
`factor (expr, p)` factoriza *expr* 
en el campo de los racionales con un elemento añadido cuyo 
polinomio mínimo es *p*.


La función `factor` utiliza a `ifactors` 
para factorizar enteros.


Si la variable `factorflag` vale `false` suprime 
la factorización de los factores enteros en las expresiones racionales.


La variable `dontfactor` puede contener una lista 
de variables con respecto a las cuales no se factorizará 
(inicialmente está vacía). Tampoco se 
factorizará respecto de cualesquiera otra variables que sean menos importantes (según la ordenación que se sigue en el formato CRE) que aquellas que se encuentran en la lista `dontfactor`.


Si la variable `savefactors` vale `true`, los 
factores de una expresión en forma de producto se guardarán 
por ciertas funciones a fin de acelerar posteriores factorizaciones 
de expresiones que contengan algunos de estos mismos factores.


Si `berlefact` vale `false` entonces se utiliza el 
algoritmo de factorización de Kronecker, en caso contrario se 
utilizará el algoritmo de Berlekamp, que es el que se aplica por defecto.


Si la variable `intfaclim` vale `true`, Maxima desistirá de
factorizar enteros si no encuentra ningún factor después de las
divisiones tentativas y de aplicar el método rho de Pollard. Si vale
`false` (este es el caso cuando el usuario invoca explícitamente
a `factor`), se intentará la factorización completa del entero. El valor
asignado a `intfaclim` se utiliza en llamadas internas a `factor`. Así,
se puede cambiar el valor de `intfaclim` para evitar que Maxima dedique
un tiempo prohibitivo a factorizar números enteros grandes.


Ejemplos:




















```maxima
(%i1) factor (2^63 - 1);
                    2
(%o1)              7  73 127 337 92737 649657
(%i2) factor (-8*y - 4*x + z^2*(2*y + x));
(%o2)               (2 y + x) (z - 2) (z + 2)
(%i3) -1 - 2*x - x^2 + y^2 + 2*x*y^2 + x^2*y^2;
                2  2        2    2    2
(%o3)          x  y  + 2 x y  + y  - x  - 2 x - 1
(%i4) block ([dontfactor: [x]], factor (%/36/(1 + 2*y + y^2)));
                       2
                     (x  + 2 x + 1) (y - 1)
(%o4)                ----------------------
                           36 (y + 1)
(%i5) factor (1 + %e^(3*x));
                      x         2 x     x
(%o5)              (%e  + 1) (%e    - %e  + 1)
(%i6) factor (1 + x^4, a^2 - 2);
                    2              2
(%o6)             (x  - a x + 1) (x  + a x + 1)
(%i7) factor (-y^2*z^2 - x*z^2 + x^2*y^2 + x^3);
                       2
(%o7)              - (y  + x) (z - x) (z + x)
(%i8) (2 + x)/(3 + x)/(b + x)/(c + x)^2;
                             x + 2
(%o8)               ------------------------
                                           2
                    (x + 3) (x + b) (x + c)
(%i9) ratsimp (%);
                4                  3
(%o9) (x + 2)/(x  + (2 c + b + 3) x

     2                       2             2                   2
 + (c  + (2 b + 6) c + 3 b) x  + ((b + 3) c  + 6 b c) x + 3 b c )
(%i10) partfrac (%, x);
           2                   4                3
(%o10) - (c  - 4 c - b + 6)/((c  + (- 2 b - 6) c

     2              2         2                2
 + (b  + 12 b + 9) c  + (- 6 b  - 18 b) c + 9 b ) (x + c))

                 c - 2
 - ---------------------------------
     2                             2
   (c  + (- b - 3) c + 3 b) (x + c)

                         b - 2
 + -------------------------------------------------
             2             2       3      2
   ((b - 3) c  + (6 b - 2 b ) c + b  - 3 b ) (x + b)

                         1
 - ----------------------------------------------
             2
   ((b - 3) c  + (18 - 6 b) c + 9 b - 27) (x + 3)
(%i11) map ('factor, %);
              2
             c  - 4 c - b + 6                 c - 2
(%o11) - ------------------------- - ------------------------
                2        2                                  2
         (c - 3)  (c - b)  (x + c)   (c - 3) (c - b) (x + c)

                       b - 2                        1
            + ------------------------ - ------------------------
                             2                          2
              (b - 3) (c - b)  (x + b)   (b - 3) (c - 3)  (x + 3)
(%i12) ratsimp ((x^5 - 1)/(x - 1));
                       4    3    2
(%o12)                x  + x  + x  + x + 1
(%i13) subst (a, x, %);
                       4    3    2
(%o13)                a  + a  + a  + a + 1
(%i14) factor (%th(2), %);
                       2        3        3    2
(%o14)   (x - a) (x - a ) (x - a ) (x + a  + a  + a + 1)
(%i15) factor (1 + x^12);
                       4        8    4
(%o15)               (x  + 1) (x  - x  + 1)
(%i16) factor (1 + x^99);
                 2            6    3
(%o16) (x + 1) (x  - x + 1) (x  - x  + 1)

   10    9    8    7    6    5    4    3    2
 (x   - x  + x  - x  + x  - x  + x  - x  + x  - x + 1)

   20    19    17    16    14    13    11    10    9    7    6
 (x   + x   - x   - x   + x   + x   - x   - x   - x  + x  + x

    4    3            60    57    51    48    42    39    33
 - x  - x  + x + 1) (x   + x   - x   - x   + x   + x   - x

    30    27    21    18    12    9    3
 - x   - x   + x   + x   - x   - x  + x  + 1)
```

<!-- category: Other -->
<!-- keywords: factorflag -->
<!-- signatures: factorflag -->
### Variable: factorflag

Valor por defecto: `false`



Si `factorflag` vale `false` se evita la factorización de factores enteros de expresiones racionales.

<!-- category: Other -->
<!-- keywords: factorout -->
<!-- signatures: factorout(expr, x_1, x_2, ...) -->
### Function: factorout (expr, x_1, x_2, ...)

Reorganiza la suma *expr* como una suma de términos de la forma 
`f (x_1, x_2, ...)*g`, donde `g` es un producto 
de expresiones que no contienen ningún *x_i* y `f` se factoriza.


Nótese que `factorout` ignora la variable opcional `keepfloat`.


Ejemplo:







```maxima
(%i1) expand (a*(x+1)*(x-1)*(u+1)^2);
             2  2          2      2      2
(%o1)     a u  x  + 2 a u x  + a x  - a u  - 2 a u - a
(%i2) factorout(%,x);
         2
(%o2) a u  (x - 1) (x + 1) + 2 a u (x - 1) (x + 1)
                                              + a (x - 1) (x + 1)
```

<!-- category: Other -->
<!-- keywords: factorsum -->
<!-- signatures: factorsum(expr) -->
### Function: factorsum (expr)

Intenta agrupar términos en los factores de *expr* que son sumas en grupos de términos tales que su suma sea factorizable. La función `factorsum` puede restablecer el recuperar de `expand ((x + y)^2 + (z + w)^2)` pero no puede recuperar `expand ((x + 1)^2 + (x + y)^2)` porque los términos tienen variables comunes.


Ejemplo:






```maxima
(%i1) expand ((x + 1)*((u + v)^2 + a*(w + z)^2));
           2      2                            2      2
(%o1) a x z  + a z  + 2 a w x z + 2 a w z + a w  x + v  x

                                     2        2    2            2
                        + 2 u v x + u  x + a w  + v  + 2 u v + u
(%i2) factorsum (%);
                                   2          2
(%o2)            (x + 1) (a (z + w)  + (v + u) )
```

<!-- category: Other -->
<!-- keywords: fasttimes -->
<!-- signatures: fasttimes(p_1, p_2) -->
### Function: fasttimes (p_1, p_2)

Calcula el producto de los polinomios *p_1* y *p_2* utilizando un algoritmo especial. Los polinomios `p_1` y `p_2` deben ser multivariantes, densos y aproximadamente del mismo tamaño. La multiplicación clásica es de orden `n_1 n_2` donde `n_1` es el grado de  `p_1` y  `n_2` el grado de `p_2`. La función `fasttimes` es de orden `max (n_1, n_2)^1.585`.

<!-- category: Other -->
<!-- keywords: fullratsimp -->
<!-- signatures: fullratsimp(expr) -->
### Function: fullratsimp (expr)

Aplica repetidamente `ratsimp` a una expresión, seguida de simplificaciones no racionales, hasta que no se obtienen más transformaciones; entonces devuelve el resultado.


En presencia de expresiones no racionales, una llamada a `ratsimp` seguida de una simplificación no racional ("general") puede no ser suficiente para conseguir un resultado simplificado. En ocasiones serán necesarias más de una llamada a `ratsimp`, que es lo que hace precisamente `fullratsimp`.


Ejemplo:








```maxima
(%i1) expr: (x^(a/2) + 1)^2*(x^(a/2) - 1)^2/(x^a - 1);
                       a/2     2   a/2     2
                     (x    - 1)  (x    + 1)
(%o1)                -----------------------
                              a
                             x  - 1
(%i2) ratsimp (expr);
                          2 a      a
                         x    - 2 x  + 1
(%o2)                    ---------------
                              a
                             x  - 1
(%i3) fullratsimp (expr);
                              a
(%o3)                        x  - 1
(%i4) rat (expr);
                       a/2 4       a/2 2
                     (x   )  - 2 (x   )  + 1
(%o4)/R/             -----------------------
                              a
                             x  - 1
```

<!-- category: Other -->
<!-- keywords: fullratsubst -->
<!-- signatures: fullratsubst(a, b, c) -->
### Function: fullratsubst (a, b, c)

Similar a `ratsubst` excepto por el hecho de que se llama a í misma recursivamente hasta que el resultado deja de cambiar. Esta función es útil cuando la expresión a sustituir y la que la sustituye tienen variables comunes.


La función `fullratsubst` también acepta sus argumentos en el formato de `lratsubst`.


Es necesario ejecutar `load ("lrats")` para cargar `fullratsubst` y `lratsubst`.


Ejemplos:














```maxima
(%i1) load ("lrats")$
```


- *
`subst` puede hacer sustituciones múltiples;
`lratsubst` es análoga a `subst`.


```maxima
(%i2) subst ([a = b, c = d], a + c);
(%o2)                         d + b
(%i3) lratsubst ([a^2 = b, c^2 = d], (a + e)*c*(a + c));
(%o3)                (d + a c) e + a d + b c
```


- *
Si sólo se quiere una sustitución, entonces se puede dar una única ecuación como primer argumento.


```maxima
(%i4) lratsubst (a^2 = b, a^3);
(%o4)                          a b
```


- *
`fullratsubst` equivale a `ratsubst`, 
excepto por el hecho de que se llama a í misma recursivamente hasta que el resultado deja de cambiar.


```maxima
(%i5) ratsubst (b*a, a^2, a^3);
                               2
(%o5)                         a  b
(%i6) fullratsubst (b*a, a^2, a^3);
                                 2
(%o6)                         a b
```


- *
`fullratsubst` también acepta una lista de ecuaciones o una sóla ecuación como primer argumento.


```maxima
(%i7) fullratsubst ([a^2 = b, b^2 = c, c^2 = a], a^3*b*c);
(%o7)                           b
(%i8) fullratsubst (a^2 = b*a, a^3);
                                 2
(%o8)                         a b
```


- *
`fullratsubst` puede caer en una recursión infinita.


```maxima
(%i9) errcatch (fullratsubst (b*a^2, a^2, a^3));

*** - Lisp stack overflow. RESET
```

<!-- category: Other -->
<!-- keywords: gcd -->
<!-- signatures: gcd(p_1, p_2, x_1, ...) -->
### Function: gcd (p_1, p_2, x_1, ...)

Devuelve el máximo común divisor de *p_1* y *p_2*.
La variable `gcd` determiona qué algoritmo se va a utilizar.
Asignándole a `gcd` los valores `ez`, `subres`, `red`
o `spmod`, se seleccionan los algoritmos `ezgcd`, 
subresultante `prs`, reducido o modular, respectivamente.
Si `gcd` vale `false` entonces `gcd(p_1, p_2, x)` devolverá siempre 1 para cualquier *x*.
Muchas funciones (por ejemplo,  `ratsimp`, `factor`, etc.)
hacen uso de `gcd` implícitamente.  
En caso de polinomios homogéneos se recomienda darle a 
`gcd` el valor `subres`.  Para calcular un máximo 
común divisor en presencia de raíces, como en
 `gcd (x^2 - 2*sqrt(2)*x + 2, x - sqrt(2))`,
la variable `algebraic` debe igualarse
a `true` y `gcd` no puede ser `ez`.


Se recomienda utilizar el algoritmo `subres` en lugar de `red`,
por ser aquél más moderno.


Si la variable `gcd`, cuyo valor por defecto es `spmod`,
vale `false`, no se calculará el máximo común divisor 
cuando las expresiones se conviertan a su forma canónica (CRE),
lo que redundará en ocasiones en mayor rapidez de cálculo.

<!-- category: Other -->
<!-- keywords: gcdex -->
<!-- signatures: gcdex(f, g), gcdex(f, g, x) -->
### Function: gcdex (f, g)

Devuelve una lista `[a, b, u]` en la que *u* es el máximo común divisor (mcd) de *f* y *g*, e igual a `a f + b g`.
Los argumentos *f* y *g* deben ser polinomios univariantes, o indicarles la variable principal *x* en caso de ser multivariantes. 


La función `gcdex` implementa el algoritmo de Euclides, en el que tenemos una secuencia de `L[i]: [a[i], b[i], r[i]]` todos ellos ortogonales a `[f, g, -1]` siendo el siguiente calculado a partir de `q = quotient(r[i]/r[i+1])` y `L[i+2]: L[i] - q L[i+1]`; el proceso termina en `L[i+1]` cuando el resto `r[i+2]` se anula.







```maxima
(%i1) gcdex (x^2 + 1, x^3 + 4);
                       2
                      x  + 4 x - 1  x + 4
(%o1)/R/           [- ------------, -----, 1]
                           17        17
(%i2) % . [x^2 + 1, x^3 + 4, -1];
(%o2)/R/                        0
```

<!-- category: Other -->
<!-- keywords: gcfactor -->
<!-- signatures: gcfactor(n) -->
### Function: gcfactor (n)

Factoriza el entero gaussiano *n* como producto, a su vez, de enteros gaussianos, (un entero gaussiano es de la forma`a + b %i` donde *a* y *b* son números enteros). Los factores se normalizan de manera que tanto la parte real como imaginaria sean no negativas.

<!-- category: Other -->
<!-- keywords: gfactor -->
<!-- signatures: gfactor(expr) -->
### Function: gfactor (expr)

Factoriza el polinomio *expr* sobre los enteros gaussianos (un entero gaussiano es de la forma`a + b %i` donde *a* y *b* son números enteros).

Es como `factor (expr, a^2+1)` donde *a* vale `%i`.


Ejemplo:





```maxima
(%i1) gfactor (x^4 - 1);
(%o1)           (x - 1) (x + 1) (x - %i) (x + %i)
```

<!-- category: Other -->
<!-- keywords: gfactorsum -->
<!-- signatures: gfactorsum(expr) -->
### Function: gfactorsum (expr)

Esta función es similar a `factorsum` pero aplica `gfactor` en lugar de `factor`.

<!-- category: Other -->
<!-- keywords: hipow -->
<!-- signatures: hipow(expr, x) -->
### Function: hipow (expr, x)

Devuelve el mayor exponente explícito de  *x* en *expr*.
El argumento*x* puede ser una variable o una expresión general.
Si *x* no aparece en *expr*, `hipow` devuelve `0`.


La función `hipow` no tiene en cuenta expresiones equivalentes a `expr`.
En particular, `hipow` no expande `expr`, de manera que `hipow (expr, x)` y `hipow (expand (expr, x))` pueden dar resultados diferentes.


Ejemplos:



```maxima
(%i1) hipow (y^3 * x^2 + x * y^4, x);
(%o1)                           2
(%i2) hipow ((x + y)^5, x);
(%o2)                           1
(%i3) hipow (expand ((x + y)^5), x);
(%o3)                           5
(%i4) hipow ((x + y)^5, x + y);
(%o4)                           5
(%i5) hipow (expand ((x + y)^5), x + y);
(%o5)                           0
```

<!-- category: Other -->
<!-- keywords: intfaclim -->
<!-- signatures: intfaclim -->
### Variable: intfaclim

Valor por defecto: `true`


Si vale `true`, Maxima  desistirá de
factorizar enteros si no encuentra ningún factor después de las
divisiones tentativas y de aplicar el método rho de Pollard, por lo que 
la factorización puede quedar incompleta.


Si vale `false` (este es el caso cuando el usuario invoca explícitamente
a `factor`), se intentará la factorización completa del entero. El valor
asignado a `intfaclim` se utiliza en llamadas internas a `factor`. A la variable
`intfaclim` se le asigna el valor `false` cuando se calculan factores desde las
funciones `divisors`, `divsum` y `totient`.




Las llamadas internas a `factor` respetan el valor dado por el usuario a `intfaclim`.
Asignando a `intfaclim` el valor `true` se puede reducir  el tiempo que Maxima dedica a
factorizar enteros grandes.

<!-- category: Other -->
<!-- keywords: keepfloat -->
<!-- signatures: keepfloat -->
### Variable: keepfloat

Valor por defecto: `false`


Si `keepfloat` vale `true`, los números decimales en coma flotante no se racionalizan cuando las expresiones que los contienen se convierten al formato canónico racional (CRE).


Nótese que la función `solve` y todas aquellas otras que la
invocan (por ejemplo, `eigenvalues`) ignoran esta variable, por
lo que hacen la conversión de los números decimales.


Ejemplos:







```maxima
(%i1) rat(x/2.0);

`rat' replaced 0.5 by 1/2 = 0.5
                                       x
(%o1)/R/                               -
                                       2
(%i2) rat(x/2.0), keepfloat;

(%o2)/R/                             0.5 x
```


`solve` ignora `keepfloat`:






```maxima
(%i3) solve(1.0-x,x), keepfloat;

`rat' replaced 1.0 by 1/1 = 1.0
(%o3)                               [x = 1]
```

<!-- category: Other -->
<!-- keywords: lopow -->
<!-- signatures: lopow(expr, x) -->
### Function: lopow (expr, x)

Devuelve el menor exponente de *x* que aparece explícitamente
en *expr*.



```maxima
(%i1) lopow ((x+y)^2 + (x+y)^a, x+y);
(%o1)                       min(a, 2)
```

<!-- category: Other -->
<!-- keywords: lratsubst -->
<!-- signatures: lratsubst(L, expr) -->
### Function: lratsubst (L, expr)

Esta función es similar a `subst (L, expr)`, excepto por el hecho de que utiliza `ratsubst` en lugar de `subst`.


El primer argumento de `lratsubst` es una ecuación o lista de ecuaciones idénticas en formato a las aceptadas por `subst`.  Las sustituciones se hacen en el orden dado por la lista de ecuaciones, esto es, de izquierda a derecha.


La instrucción `load ("lrats")` carga `fullratsubst` y `lratsubst`.


Ejemplos:









```maxima
(%i1) load ("lrats")$
```


- *
`subst` can carry out multiple substitutions.
`lratsubst` is analogous to `subst`.


```maxima
(%i2) subst ([a = b, c = d], a + c);
(%o2)                         d + b
(%i3) lratsubst ([a^2 = b, c^2 = d], (a + e)*c*(a + c));
(%o3)                (d + a c) e + a d + b c
```


- *
If only one substitution is desired, then a single
equation may be given as first argument.


```maxima
(%i4) lratsubst (a^2 = b, a^3);
(%o4)                          a b
```

<!-- category: Other -->
<!-- keywords: modulus -->
<!-- signatures: modulus -->
### Variable: modulus

Valor por defecto: `false`


Si `modulus` es un número positivo *p*, las operaciones con números racionales
(como los devueltos por `rat` y funciones relacionadas) se realizan módulo *p*,
utilizando el llamado sistema de módulo balanceado, en el que `n módulo p`
se define como un entero *k* de `[-(p-1)/2, ..., 0, ..., (p-1)/2]`
si *p* es impar, o de `[-(p/2 - 1), ..., 0, ...., p/2]` si *p* es par,
de tal manera que `a p + k` es igual a *n* para algún entero *a*.


Normalmente a `modulus` se le asigna un número primo. Se acepta que a `modulus`
se le asigne un entero positivo no primo, pero se obtendrá un mensaje de aviso. Maxima 
responderá con un mensaje de error cuando se le asigne a `modulus` cero o un número
negativo.


Ejemplos:



```maxima
(%i1) modulus:7;
(%o1)                           7
(%i2) polymod([0,1,2,3,4,5,6,7]);
(%o2)            [0, 1, 2, 3, - 3, - 2, - 1, 0]
(%i3) modulus:false;
(%o3)                         false
(%i4) poly:x^6+x^2+1;
                            6    2
(%o4)                      x  + x  + 1
(%i5) factor(poly);
                            6    2
(%o5)                      x  + x  + 1
(%i6) modulus:13;
(%o6)                          13
(%i7) factor(poly);
                      2        4      2
(%o7)               (x  + 6) (x  - 6 x  - 2)
(%i8) polymod(%);
                            6    2
(%o8)                      x  + x  + 1
```

<!-- category: Other -->
<!-- keywords: num -->
<!-- signatures: num(expr) -->
### Function: num (expr)

Devuelve el numerador de *expr* si se trata de una fracción. Si *expr* no es una fracción, se devuelve *expr*.


La función `num` evalúa su argumento.

<!-- category: Other -->
<!-- keywords: polydecomp -->
<!-- signatures: polydecomp(p, x) -->
### Function: polydecomp (p, x)

Descompone el polinomio *p* de variable *x* en una composición funcional de polinomios en *x*. 
La función `polydecomp` devuelve una lista `[p_1, ..., p_n]` tal que 



```maxima
lambda([x],p_1)(lambda ([x],p_2)(...(lambda([x],p_n)(x))...))
```


es igual a  *p*.
El grado de *p_i* es mayor que 1 para *i* menor que *n*.


Esta descomposición no es única.


Ejemplos:








```maxima
(%i1) polydecomp (x^210, x);
                          7   5   3   2
(%o1)                   [x , x , x , x ]
(%i2) p : expand (subst (x^3 - x - 1, x, x^2 - a));
                6      4      3    2
(%o2)          x  - 2 x  - 2 x  + x  + 2 x - a + 1
(%i3) polydecomp (p, x);
                        2       3
(%o3)                 [x  - a, x  - x - 1]
```


La siguiente función compone `L = [e_1, ..., e_n]` como funciones de `x`;
se trata de la inversa de `polydecomp`:







```maxima
compose (L, x) :=
  block ([r : x], for e in L do r : subst (e, x, r), r) $
```


Se vuelve a obtener el resultado del ejemplo de más arriba haciendo uso de `compose`:






```maxima
(%i3) polydecomp (compose ([x^2 - a, x^3 - x - 1], x), x);
                        2       3
(%o3)                 [x  - a, x  - x - 1]
```


Nótese que aunque `compose (polydecomp (p, x), x)`
devuelve siempre *p* (sin expandir),
`polydecomp (compose ([p_1, ..., p_n], x), x)`  *no*
devuelve necesariamente `[p_1, ..., p_n]`:







```maxima
(%i4) polydecomp (compose ([x^2 + 2*x + 3, x^2], x), x);
                          2       2
(%o4)                   [x  + 2, x  + 1]
(%i5) polydecomp (compose ([x^2 + x + 1, x^2 + x + 1], x), x);
                      2       2
                     x  + 3  x  + 5
(%o5)               [------, ------, 2 x + 1]
                       4       2
```

<!-- category: Other -->
<!-- keywords: polymod -->
<!-- signatures: polymod(p), polymod(p, m) -->
### Function: polymod (p)

Convierte el polinomio *p* a una representación modular respecto del módulo actual, que es el valor almacenado en la variable `modulus`.  


La llamada `polymod (p, m)` especifica un módulo *m* para ser utilizado en lugar de valor almacenado en `modulus`.


Véase `modulus`.

<!-- category: Other -->
<!-- keywords: powers -->
<!-- signatures: powers(expr, x) -->
### Function: powers (expr, x)

Devuelve las potencias de *x* dentro de *expr*.


La instrucción `load ("powers")` carga esta función.

<!-- category: Other -->
<!-- keywords: quotient -->
<!-- signatures: quotient(p_1, p_2), quotient(p_1, p_2, x_1, ..., x_n) -->
### Function: quotient (p_1, p_2)

Devuelve el polinomio *p_1* dividido por el polinomio *p_2*. Los argumentos *x_1*, ..., *x_n* se interpretan como en la función `ratvars`.


La función `quotient` devuelve el primer elemento de la lista devuelta por `divide`.

<!-- category: Other -->
<!-- keywords: radsubstflag -->
<!-- signatures: radsubstflag -->
### Variable: radsubstflag

Valor por defecto: `false`


Si `radsubstflag` vale `true` se permite a `ratsubst` hacer la sustitución `u` por `sqrt (x)` in `x`.

<!-- category: Other -->
<!-- keywords: rat -->
<!-- signatures: rat(expr), rat(expr, x_1, ..., x_n) -->
### Function: rat (expr)

Convierte *expr* al formato canónico racional (canonical rational expression o CRE) expandiendo y combinando todos los términos sobre un denominador común y cancelando el máximo común divisor del numerador y denominador, así como convirtiendo números decimales en coma flotante a números racionales dentro de la tolerancia indicada por `ratepsilon`. Las variables se ordenan de acuerdo a *x_1*, ..., *x_n* si se han especificado, como en la función `ratvars`.


En general, `rat` no simplifica otras funciones que no sean la suma `+`, resta `-`, multiplicación `*`, división `/` y exponenciación de exponente entero, mientras que `ratsimp` sí lo hace.
Nótese que los átomos (números y variables) en expresiones en formato CRE no son los mismos que en el formato general.
Por ejemplo, `rat(x)- x` devuelve `rat(0)`, que tiene una representación interna diferente de 0.




Si `ratprint` vale `false` no aparecerán mensajes informando al usuario sobre la conversión de números decimales en coma flotante a números racionales.


Si `keepfloat` vale `true` no se convertirán números decimales en coma flotante a números racionales.


Véanse también `ratexpand` y  `ratsimp`.


Ejemplos:







```maxima
(%i1) ((x - 2*y)^4/(x^2 - 4*y^2)^2 + 1)*(y + a)*(2*y + x)
         / (4*y^2 + x^2);
                                           4
                                  (x - 2 y)
              (y + a) (2 y + x) (------------ + 1)
                                   2      2 2
                                 (x  - 4 y )
(%o1)         ------------------------------------
                              2    2
                           4 y  + x
(%i2) rat (%, y, a, x);
                            2 a + 2 y
(%o2)/R/                    ---------
                             x + 2 y
```

<!-- category: Other -->
<!-- keywords: ratalgdenom -->
<!-- signatures: ratalgdenom -->
### Variable: ratalgdenom

Valor por defecto: `true`


Si `ratalgdenom` vale `true`, se permite la racionalización de denominadores eliminando radicales.
La variable `ratalgdenom` sólo tiene efecto cuando expresiones en formato canónico (CRE) están siendo utilizadas en modo algebraico.

<!-- category: Other -->
<!-- keywords: ratcoef -->
<!-- signatures: ratcoef(expr, x, n), ratcoef(expr, x) -->
### Function: ratcoef (expr, x, n)

Devuelve el coeficiente de la expresión `x^n` dentro de la expresión *expr*. Si se omite, *n* se considera igual a 1.


El valor devuelto está libre de las variables en *x*, excepto quizás en un sentido no racional. Si no existe un coeficiente de este tipo se devuelve 0.


La función `ratcoef` expande y simplifica racionalmente su primer argumento, por lo que puede dar una respuesta diferente a la dada por la función `coeff`, la cual tiene un carácter puramente sintáctico.
Así, `ratcoef ((x + 1)/y + x, x)` devuelve `(y + 1)/y`, 
mientras que `coeff` devuelve 1.


La llamada `ratcoef (expr, x, 0)`, siendo *expr* una suma, devuelve una suma formada por los términos que no contienen *x*.


Puesto que *expr* se simplifica racionalmente antes de ser examinada, algunos coeficientes puede que no aparezcan como en la expresión original.


Ejemplo:






```maxima
(%i1) s: a*x + b*x + 5$
(%i2) ratcoef (s, a + b);
(%o2)                           x
```

<!-- category: Other -->
<!-- keywords: ratdenom -->
<!-- signatures: ratdenom(expr) -->
### Function: ratdenom (expr)

Devuelve el denominador de *expr*, después de transformar *expr* al formato canónico (CRE). El valor retornado está también en formato CRE.



El argumento *expr* se transforma al formato CRE por la función `rat`, a menos que ya esté en este formato.
Esta conversión puede cambiar la forma de *expr* colocando todos sus términos sobre un denominador común.


La función `denom` es parecida, pero devuelve una expresión general en lugar de una CRE. Tampoco `denom` intenta colocar todos sus términos sobre un denominador común, de manera que algunas expresiones que son consideradas como divisiones por `ratdenom`, no son tales para `denom`.

<!-- category: Other -->
<!-- keywords: ratdenomdivide -->
<!-- signatures: ratdenomdivide -->
### Variable: ratdenomdivide

Valor por defecto: `true`


Si `ratdenomdivide` vale `true`, la función `ratexpand` expande una fracción en la que el numerador es una suma en una suma de divisiones. En otro caso, `ratexpand` reduce una suma de divisiones a una única fracción, cuyo numerador es la suma de los denominadores de cada fracción.


Ejemplos:



```maxima
(%i1) expr: (x^2 + x + 1)/(y^2 + 7);
                            2
                           x  + x + 1
(%o1)                      ----------
                              2
                             y  + 7
(%i2) ratdenomdivide: true$
(%i3) ratexpand (expr);
                       2
                      x        x        1
(%o3)               ------ + ------ + ------
                     2        2        2
                    y  + 7   y  + 7   y  + 7
(%i4) ratdenomdivide: false$
(%i5) ratexpand (expr);

                            2
                           x  + x + 1
(%o5)                      ----------
                              2
                             y  + 7

(%i6) expr2: a^2/(b^2 + 3) + b/(b^2 + 3);
                                     2
                           b        a
(%o6)                    ------ + ------
                          2        2
                         b  + 3   b  + 3
(%i7) ratexpand (expr2);
                                  2
                             b + a
(%o7)                        ------
                              2
                             b  + 3
```

<!-- category: Other -->
<!-- keywords: ratdiff -->
<!-- signatures: ratdiff(expr, x) -->
### Function: ratdiff (expr, x)

Deriva la expresión racional *expr* con respecto a *x*.
El argumento *expr* debe ser una fracción algebraica o un polinomio en *x*.
El argumento *x* puede ser una variable o una subexpresión de *expr*.





El resultado equivale al devuelto por `diff`, aunque es posible que se obtenga en una forma diferente.
La función `ratdiff` puede ser más rápida que `diff` en expresiones racionales.


La función `ratdiff` devuelve una expresión en formato canónico o CRE si `expr` es también una expresión CRE. En otro caso, `ratdiff` devuelve una expresión general.


La función `ratdiff` considera únicamente la dependencia de *expr* respecto de *x*, ignorando cualquier dependencia establecida por `depends`.


Ejemplo:










```maxima
(%i1) expr: (4*x^3 + 10*x - 11)/(x^5 + 5);
                           3
                        4 x  + 10 x - 11
(%o1)                   ----------------
                              5
                             x  + 5
(%i2) ratdiff (expr, x);
                    7       5       4       2
                 8 x  + 40 x  - 55 x  - 60 x  - 50
(%o2)          - ---------------------------------
                          10       5
                         x   + 10 x  + 25
(%i3) expr: f(x)^3 - f(x)^2 + 7;
                         3       2
(%o3)                   f (x) - f (x) + 7
(%i4) ratdiff (expr, f(x));
                           2
(%o4)                   3 f (x) - 2 f(x)
(%i5) expr: (a + b)^3 + (a + b)^2;
                              3          2
(%o5)                  (b + a)  + (b + a)
(%i6) ratdiff (expr, a + b);
                    2                    2
(%o6)            3 b  + (6 a + 2) b + 3 a  + 2 a
```

<!-- category: Other -->
<!-- keywords: ratdisrep -->
<!-- signatures: ratdisrep(expr) -->
### Function: ratdisrep (expr)

Devuelve su argumento como una expresión general.
Si *expr* es una expresión general, se devuelve sin cambios.


Normalmente se invoca a `ratdisrep` a fin de convertir una expresión en formato canónico (CRE) al formato general, lo que puede ser utilizado si se quiere parar el contagio que produce el formato CRE, o para utilizar funciones racionales en contextos no racionales.


Véase también `totaldisrep`.

<!-- category: Other -->
<!-- keywords: ratexpand -->
<!-- signatures: ratexpand(expr) -->
### Function: ratexpand (expr)

Expande *expr* multiplicando productos de sumas y sumas con exponentes, combinando fracciones con común denominador, cancelando el máximo común divisor del numerador y del denominador y luego dividiendo los sumandos del numerador por el denominador.


El valor que devuelve `ratexpand` es una expresión general, incluso cuando *expr* está en formato canónico o CRE.


Si la variable `ratexpand` vale `true` hará que las expresiones CRE se expandan completamente cuando se conviertan al formato general o se muestren en el terminal, mientras que si vale `false` se mostrarán de forma recursiva. Véase también `ratsimp`.


Si `ratdenomdivide` vale `true`,
`ratexpand` expande una fracción en la que el numerador es una suma en una suma de fracciones, todas ellas con denominador común. En otro caso, `ratexpand` reduce una suma de fracciones en una única fracción, cuyo numerador es la suma de los numeradores de cada fracción.


Si `keepfloat` vale `true`, los números decimales en coma flotante no se racionalizan cuando las expresiones que los contienen se convierten al formato canónico racional (CRE).


Ejemplos:








```maxima
(%i1) ratexpand ((2*x - 3*y)^3);
                     3         2       2        3
(%o1)          - 27 y  + 54 x y  - 36 x  y + 8 x
(%i2) expr: (x - 1)/(x + 1)^2 + 1/(x - 1);
                         x - 1       1
(%o2)                   -------- + -----
                               2   x - 1
                        (x + 1)
(%i3) expand (expr);
                    x              1           1
(%o3)          ------------ - ------------ + -----
                2              2             x - 1
               x  + 2 x + 1   x  + 2 x + 1
(%i4) ratexpand (expr);
                        2
                     2 x                 2
(%o4)           --------------- + ---------------
                 3    2            3    2
                x  + x  - x - 1   x  + x  - x - 1
```

<!-- category: Other -->
<!-- keywords: ratfac -->
<!-- signatures: ratfac -->
### Variable: ratfac

Valor por defecto: `false`


Si `ratfac` vale `true`, las expresiones canónicas (CRE) se manipulan en una forma parcialmente factorizada.


Durante las operaciones racionales, las expresiones se mantienen completamente factorizadas tanto como sea posible sin llamar a `factor`. Esto debería ahorrar espacio y tiempo en algunos cálculos. El numerador y denominador se hacen primos relativos, por ejemplo `rat ((x^2 - 1)^4/(x + 1)^2)` devuelve `(x - 1)^4 (x + 1)^2)`, pero los factores dentro de cada parte pueden no ser primos relativos.


En el paquete `ctensr` sobre manipulación de tensores por componentes, los tensores de Ricci, Einstein, Riemann y Weyl y la curvatura escalar se factorizan automáticamente si `ratfac` vale `true`; 
*`ratfac` debe activarse únicamente en aquellos casos en los que se sabe que el número de términos de las componentes tensoriales es pequño.*


Nota: Los esquemas de comportamiento basados en `ratfac` y `ratweight` son incompatibles y no se debe  pretender usarlos al mismo tiempo.

<!-- category: Other -->
<!-- keywords: ratnumer -->
<!-- signatures: ratnumer(expr) -->
### Function: ratnumer (expr)

Devuelve el numerador de *expr*, después de reducir *expr* a su forma canónica (CRE).
El valor retornado está también en formato CRE.



El argumento *expr* se transforma al formato CRE por la función `rat`, a menos que ya esté en este formato.
Esta conversión puede cambiar la forma de *expr* colocando todos sus términos sobre un denominador común.


Es parecida a la función `num`, pero devuelve una expresión general en lugar de una CRE.
Además, `num` no intenta colocar todos los términos sobre un denominador común, de manera que algunas expresiones que son consideradas fracciones por `ratnumer` no se consideran como tales por `num`.

<!-- category: Other -->
<!-- keywords: ratp -->
<!-- signatures: ratp(expr) -->
### Function: ratp (expr)

Devuelve `true` si *expr* es una expresión canónica racional (canonical rational expression o CRE) o una CRE extendida, en caso contrario devuelve `false`.


Las expresiones CRE son creadas por `rat` y funciones asociadas. Las CRE extendidas son creadas por `taylor` y funciones asociadas.

<!-- category: Other -->
<!-- keywords: ratprint -->
<!-- signatures: ratprint -->
### Variable: ratprint

Valor por defecto: `true`


Si `ratprint` vale `true`, se muestra al usuario un mensaje dando cuenta de la conversión de números decimales en coma flotante a formato racional.

<!-- category: Other -->
<!-- keywords: ratsimp -->
<!-- signatures: ratsimp(expr), ratsimp(expr, x_1, ..., x_n) -->
### Function: ratsimp (expr)

Simplifica la expresión *expr* y todas sus subexpresiones, incluyendo los argumentos de funciones no racionales. El resultado es un cociente de dos polinomios en una forma recursiva, esto es, los coeficientes de la variable principal son polinomios respecto de las otras variables. Las variables pueden incluir funciones no racionales, como `sin (x^2 + 1)`, y los argumentos de tales funciones son también racionalmente simplificados.


La llamada `ratsimp (expr, x_1, ..., x_n)` permite la simplificación racional con la especificación del orden de las variables, como en `ratvars`.


Si `ratsimpexpons` vale `true`, `ratsimp` se aplica a los exponentes de las expresiones durante la simplificación.


Véase también `ratexpand`. Nótese que `ratsimp` se ve afectada por algunas de las variables globales que controlan a `ratexpand`.


Ejemplos:









```maxima
(%i1) sin (x/(x^2 + x)) = exp ((log(x) + 1)^2 - log(x)^2);
                                         2      2
                   x         (log(x) + 1)  - log (x)
(%o1)        sin(------) = %e
                  2
                 x  + x
(%i2) ratsimp (%);
                             1          2
(%o2)                  sin(-----) = %e x
                           x + 1
(%i3) ((x - 1)^(3/2) - (x + 1)*sqrt(x - 1))/sqrt((x - 1)*(x + 1));
                       3/2
                (x - 1)    - sqrt(x - 1) (x + 1)
(%o3)           --------------------------------
                     sqrt((x - 1) (x + 1))
(%i4) ratsimp (%);
                           2 sqrt(x - 1)
(%o4)                    - -------------
                                 2
                           sqrt(x  - 1)
(%i5) x^(a + 1/a), ratsimpexpons: true;
                               2
                              a  + 1
                              ------
                                a
(%o5)                        x
```

<!-- category: Other -->
<!-- keywords: ratsimpexpons -->
<!-- signatures: ratsimpexpons -->
### Variable: ratsimpexpons

Valor por defecto: `false`


Si `ratsimpexpons` vale `true`, `ratsimp` se aplica a los exponentes de las expresiones durante la simplificación.

<!-- category: Other -->
<!-- keywords: ratsubst -->
<!-- signatures: ratsubst(a, b, c) -->
### Function: ratsubst (a, b, c)

Sustituye *b* por *a* en *c* y devuelve la expresión resultante.

El argumento *b* puede ser una suma, un producto, una potencia, etc.



La función `ratsubst` reconoce el significado de las expresiones, mientras que `subst` tan solo realiza sustituciones sintácticas. Así por ejemplo, `subst (a, x + y, x + y + z)` devuelve `x + y + z`
cuando `ratsubst` devuelve `z + a`.


Si `radsubstflag` vale `true`,
`ratsubst` sustituye radicales en expresiones que no los contienen explícitamente.


`ratsubst` ignora el valor `true` de la variable 
opcional `keepfloat`.


Ejemplos:













```maxima
(%i1) ratsubst (a, x*y^2, x^4*y^3 + x^4*y^8);
                              3      4
(%o1)                      a x  y + a
(%i2) cos(x)^4 + cos(x)^3 + cos(x)^2 + cos(x) + 1;
               4         3         2
(%o2)       cos (x) + cos (x) + cos (x) + cos(x) + 1
(%i3) ratsubst (1 - sin(x)^2, cos(x)^2, %);
            4           2                     2
(%o3)    sin (x) - 3 sin (x) + cos(x) (2 - sin (x)) + 3
(%i4) ratsubst (1 - cos(x)^2, sin(x)^2, sin(x)^4);
                        4           2
(%o4)                cos (x) - 2 cos (x) + 1
(%i5) radsubstflag: false$
(%i6) ratsubst (u, sqrt(x), x);
(%o6)                           x
(%i7) radsubstflag: true$
(%i8) ratsubst (u, sqrt(x), x);
                                2
(%o8)                          u
```

<!-- category: Other -->
<!-- keywords: ratvars -->
<!-- signatures: ratvars(x_1, ..., x_n), ratvars() -->
### Function: ratvars (x_1, ..., x_n)

Declara como variables principales *x_1*, ..., *x_n* en expresiones racionales. Si *x_n* está presente en una expresión racional, se considerará como variable principal. Si no está presente, entonces se considerará principal a la variable *x_[n-1]* si aparece en la expresión, se continúa así hasta *x_1*, que se considerará como variable principal sólo si ninguna de las variables que le siguen está presente en la expresión.


Si una variable de la expresión racional no está presente en la lista `ratvars`, se le dará una prioridad inferior a la de *x_1*.


Los argumentos de `ratvars` pueden ser tanto variables como funciones no racionales como `sin(x)`.


La variable `ratvars` es una lista que contiene los argumentos pasados a la función `ratvars` la última vez que fue invocada. Cada llamada a la función `ratvars` reinicializa la lista. La llamada `ratvars ()` vacía la lista.

<!-- category: Other -->
<!-- keywords: ratvarswitch -->
<!-- signatures: ratvarswitch -->
### Variable: ratvarswitch

Valor por defecto: `true`


Maxima almacena una lista interna en la variable Lisp `VARLIST` cuyo
contenido son las variables principales de las expresiones racionales. Cuando `ratvarswitch`
vale `true`, su valor por defecto, cada evaluación comienza con la lista
`VARLIST` vacía. En caso contrario, las variables principales
de las expresiones anteriores se mantienen en la lista `VARLIST`.


Las variables principales declaradas con la función `ratvars` no se
ven afectadas por la opción `ratvarswitch`.


Ejemplos:


Cuando `ratvarswitch` vale `true`, su valor por defecto, cada 
evaluación comienza con la lista `VARLIST` vacía.










```maxima
(%i1) ratvarswitch:true$

(%i2) rat(2*x+y^2);
                             2
(%o2)/R/                    y  + 2 x
(%i3) :lisp varlist
($X $Y)

(%i3) rat(2*a+b^2);
                             2
(%o3)/R/                    b  + 2 a

(%i4) :lisp varlist
($A $B)
```


Cuando `ratvarswitch` vale `false`, las variables principales
de las expresiones anteriores se mantienen en lista `VARLIST`.










```maxima
(%i4) ratvarswitch:false$

(%i5) rat(2*x+y^2);
                             2
(%o5)/R/                    y  + 2 x
(%i6) :lisp varlist
($X $Y)

(%i6) rat(2*a+b^2);
                             2
(%o6)/R/                    b  + 2 a

(%i7) :lisp varlist
($A $B $X $Y)
```

<!-- category: Other -->
<!-- keywords: ratweight -->
<!-- signatures: ratweight(x_1, w_1, ..., x_n, w_n), ratweight() -->
### Function: ratweight (x_1, w_1, ..., x_n, w_n)

Asigna un peso *w_i* a la variable *x_i*. Un término será reemplazado por 0 si su peso excede el valor de la variable `ratwtlvl` (por defecto no se realiza el truncamiento). El peso de un término es la suma de los productos de los pesos de las variables que lo forman multiplicados por sus exponentes. Por ejemplo, el peso de `3 x_1^2 x_2` es `2 w_1 + w_2`. El truncamiento basado en `ratwtlvl` solamente se lleva a cabo cuando se multiplican o se elevan a potencias expresiones canónicas (CRE).


La llamada `ratweight ()` devuelve la lista acumulada de asignaciones de pesos.


Nota: Los esquemas de comportamiento basados en `ratfac` y `ratweight` son incompatibles y no se debe  pretender usarlos al mismo tiempo.


Ejemplos:









```maxima
(%i1) ratweight (a, 1, b, 1);
(%o1)                     [a, 1, b, 1]
(%i2) expr1: rat(a + b + 1)$
(%i3) expr1^2;
                  2                  2
(%o3)/R/         b  + (2 a + 2) b + a  + 2 a + 1
(%i4) ratwtlvl: 1$
(%i5) expr1^2;
(%o5)/R/                  2 b + 2 a + 1
```

<!-- category: Other -->
<!-- keywords: ratweights -->
<!-- signatures: ratweights -->
### Variable: ratweights

Valor por defecto: `[]`


La variable `ratweights` es una lista que contiene los pesos asignados por `ratweight`.
Las lista es acumulativa, en el sentido de que cada llamada a `ratweight` añade nuevos elementos a la lista.

<!-- category: Other -->
<!-- keywords: ratwtlvl -->
<!-- signatures: ratwtlvl -->
### Variable: ratwtlvl

Valor por defecto: `false`


La variable `ratwtlvl` se utiliza en combinación con la función `ratweight` para controlar el truncamiento de expresiones racionales canónicas (CRE). Con el valor por defecto, `false`, no se produce truncamiento alguno.

<!-- category: Other -->
<!-- keywords: remainder -->
<!-- signatures: remainder(p_1, p_2), remainder(p_1, p_2, x_1, ..., x_n) -->
### Function: remainder (p_1, p_2)

Devuelve el resto de la división del polinomio *p_1* entre *p_2*. Los argumentos *x_1*, ..., *x_n* se interpretan como en `ratvars`.


La función `remainder` devuelve el segundo elemento de la lista retornada por `divide`.

<!-- category: Other -->
<!-- keywords: resultant -->
<!-- signatures: resultant(p_1, p_2, x) -->
### Function: resultant (p_1, p_2, x)

Calcula la resultante de los dos polinomios *p_1* y *p_2*, eliminando
la variable *x*. La resultante es un determinante de los coeficientes de *x*
en *p_1* y *p_2*, que es igual a cero si sólo si *p_1* y *p_2*
tienen un factor común no constante.


Si *p_1* o *p_2* pueden ser factorizados, puede ser necesario llamar a 
`factor` antes que invocar a `resultant`.


La variable opcional `resultant` controla qué algoritmo será utilizado para calcular la resultante.
Véanse `option_resultant` y `resultant`.


La función `bezout` toma los mismos argumentos que `resultant` y devuelve una matriz.
El determinante del valor retornado es la resultante buscada.


Ejemplos:



```maxima
(%i1) resultant(2*x^2+3*x+1, 2*x^2+x+1, x);
(%o1)                           8
(%i2) resultant(x+1, x+1, x);
(%o2)                           0
(%i3) resultant((x+1)*x, (x+1), x);
(%o3)                           0
(%i4) resultant(a*x^2+b*x+1, c*x + 2, x);
                         2
(%o4)                   c  - 2 b c + 4 a

(%i5) bezout(a*x^2+b*x+1, c*x+2, x);

                        [ 2 a  2 b - c ]
(%o5)                   [              ]
                        [  c      2    ]

(%i6) determinant(%);
(%o6)                   4 a - (2 b - c) c
```

<!-- category: Other -->
<!-- keywords: savefactors -->
<!-- signatures: savefactors -->
### Variable: savefactors

Valor por defecto: `false`



Si `savefactors` vale `true`, los factores de una expresión producto se almacenan por ciertas funciones a fin de acelerar posteriores factorizaciones de expresiones que contengan algunos de estos factores.

<!-- category: Other -->
<!-- keywords: showratvars -->
<!-- signatures: showratvars(expr) -->
### Function: showratvars (expr)

Devuelve una lista de las variables de expresiones canónicas racionales (CRE) en la expresión `expr`.


Véase también `ratvars`.

<!-- category: Other -->
<!-- keywords: tellrat -->
<!-- signatures: tellrat(p_1, ..., p_n), tellrat() -->
### Function: tellrat (p_1, ..., p_n)

Añade al anillo de enteros algebraicos conocidos por Maxima los elementos que son soluciones de los polinomios *p_1*, ..., *p_n*. Cada argumento *p_i* es un polinomio de coeficientes enteros.


La llamada `tellrat (x)` hace que se sustituya 0 por *x* en las funciones racionales.


La llamada `tellrat ()` devuelve una lista con las sustituciones actuales.


A la variable `algebraic` se le debe asignar el valor `true` a fin de poder realizar la simplificación de enteros algebraicos.


Maxima reconoce la unidad imaginaria `%i` y todas las raíces de los enteros.


La instrucción `untellrat` borra todas las propiedades de `tellrat`.


Es ambiguo aplicar `tellrat` a un polinomio multivariante tal como `tellrat (x^2 - y^2)`, pues no se sabe si sustituir `y^2` por `x^2` o al revés. Maxima sigue un cierto orden, pero si el usuario quiere especificar uno en concreto, puede hacerlo mediante la sintaxis `tellrat (y^2 = x^2)`, que indica que se ponga `x^2` en lugar de `y^2`.


Ejemplos:










```maxima
(%i1) 10*(%i + 1)/(%i + 3^(1/3));
                           10 (%i + 1)
(%o1)                      -----------
                                  1/3
                            %i + 3
(%i2) ev (ratdisrep (rat(%)), algebraic);
             2/3      1/3              2/3      1/3
(%o2)    (4 3    - 2 3    - 4) %i + 2 3    + 4 3    - 2
(%i3) tellrat (1 + a + a^2);
                            2
(%o3)                     [a  + a + 1]
(%i4) 1/(a*sqrt(2) - 1) + a/(sqrt(3) + sqrt(2));
                      1                 a
(%o4)           ------------- + -----------------
                sqrt(2) a - 1   sqrt(3) + sqrt(2)
(%i5) ev (ratdisrep (rat(%)), algebraic);
         (7 sqrt(3) - 10 sqrt(2) + 2) a - 2 sqrt(2) - 1
(%o5)    ----------------------------------------------
                               7
(%i6) tellrat (y^2 = x^2);
                        2    2   2
(%o6)                 [y  - x , a  + a + 1]
```

<!-- category: Other -->
<!-- keywords: totaldisrep -->
<!-- signatures: totaldisrep(expr) -->
### Function: totaldisrep (expr)

Convierte cada subexpresión  de *expr* del formato canónico (CRE) al general y devuelve el resultado.
Si *expr* está en formato CRE entonces `totaldisrep` es idéntico a `ratdisrep`.


La función `totaldisrep` puede ser útil para modificar expresiones como las ecuaciones, listas, matrices, etc., que tienen algunas subexpresiones en formato CRE.

<!-- category: Other -->
<!-- keywords: untellrat -->
<!-- signatures: untellrat(x_1, ..., x_n) -->
### Function: untellrat (x_1, ..., x_n)

Elimina de *x_1*, ..., *x_n* las propiedades relacionadas con `tellrat`.

