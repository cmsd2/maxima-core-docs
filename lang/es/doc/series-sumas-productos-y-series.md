## Sumas productos y series

<!-- category: Series -->
<!-- keywords: absint -->
<!-- signatures: absint(f, x, halfplane), absint(f, x), absint(f, x, a, b) -->
### Function: absint (f, x, halfplane)

La llamada `absint (f, x, halfplane)` devuelve la integral indefinida de *f* con respecto a 
*x* en el semiplano dado (`pos`, `neg` o `both`). La función *f* puede contener expresiones de la forma `abs (x)`, `abs (sin (x))`, `abs (a) * exp (-abs (b) * abs (x))`.


La llamada `absint (f, x)` equivale a `absint (f, x, pos)`.


La llamada `absint (f, x, a, b)` devuelve la integral definida de *f* con respecto a  *x* de *a* a *b*.

<!-- category: Series -->
<!-- keywords: bashindices -->
<!-- signatures: bashindices(expr) -->
### Function: bashindices (expr)

Transforma la expresión *expr* dándole a cada sumatorio y producto un
único índice. Esto le da a `changevar` mayor precisión 
cuando opera con sumas y productos. La forma del único índice es 
`jnumber`. La cantidad *number* se determina en función de 
`gensumnum`, valor que puede cambiar el usuario. Por ejemplo, haciendo `gensumnum:0$`.

<!-- category: Series -->
<!-- keywords: cauchysum -->
<!-- signatures: cauchysum -->
### Variable: cauchysum

Valor por defecto: `false`


Cuando se multiplican sumatorios infinitos, si `sumexpand` vale `true` y `cauchysum` vale `true`, entonces se utilizará el producto  de Cauchy en lugar del usual. En el producto de Cauchy  el índice de la suma interna es función del índice de la exterior en lugar de variar de forma independiente. Un ejemplo aclara esta idea:



```maxima
(%i1) sumexpand: false$
(%i2) cauchysum: false$
(%i3) s: sum (f(i), i, 0, inf) * sum (g(j), j, 0, inf);
                      inf         inf
                      ====        ====
                      \           \
(%o3)                ( >    f(i))  >    g(j)
                      /           /
                      ====        ====
                      i = 0       j = 0
(%i4) sumexpand: true$
(%i5) cauchysum: true$
(%i6) ''s;
                 inf     i1
                 ====   ====
                 \      \
(%o6)             >      >     g(i1 - i2) f(i2)
                 /      /
                 ====   ====
                 i1 = 0 i2 = 0
```

<!-- category: Series -->
<!-- keywords: cosnpiflag -->
<!-- signatures: cosnpiflag -->
### Variable: cosnpiflag

Valor por defecto: `true`


Véase `foursimp`.

<!-- category: Series -->
<!-- keywords: deftaylor -->
<!-- signatures: deftaylor(f_1(x_1), expr_1, ..., f_n(x_n), expr_n) -->
### Function: deftaylor (f_1(x_1), expr_1, ..., f_n(x_n), expr_n)

Para cada función *f_i* de variable *x_i*,  `deftaylor` define *expr_i* como una serie de Taylor alrededor de cero. La expresión *expr_i* será un polinomio en  *x_i* o una suma; `deftaylor` admite también expresiones más generales.


La llamada `powerseries (f_i(x_i), x_i, 0)` devuelve la serie definida por  `deftaylor`.


La función `deftaylor` evalúa sus argumentos y devuelve la lista de las funciones *f_1*, ..., *f_n*. 


Ejemplo:



```maxima
(%i1) deftaylor (f(x), x^2 + sum(x^i/(2^i*i!^2), i, 4, inf));
(%o1)                          [f]
(%i2) powerseries (f(x), x, 0);
                      inf
                      ====      i1
                      \        x         2
(%o2)                  >     -------- + x
                      /       i1    2
                      ====   2   i1!
                      i1 = 4
(%i3) taylor (exp (sqrt (f(x))), x, 0, 4);
                      2         3          4
                     x    3073 x    12817 x
(%o3)/T/     1 + x + -- + ------- + -------- + . . .
                     2     18432     307200
```

<!-- category: Series -->
<!-- keywords: equalp -->
<!-- signatures: equalp(x, y) -->
### Function: equalp (x, y)

Devuelve `true` si `equal (x, y)`, en otro caso devuelve `false`. No devuelve el mensaje de error que se obtiene de  `equal (x, y)` en un caso como éste.

<!-- category: Series -->
<!-- keywords: fourcos -->
<!-- signatures: fourcos(f, x, p) -->
### Function: fourcos (f, x, p)

Devuelve los coeficientes de los cosenos de Fourier de `f(x)` definida en `[0, p]`.

<!-- category: Series -->
<!-- keywords: fourexpand -->
<!-- signatures: fourexpand(l, x, p, limit) -->
### Function: fourexpand (l, x, p, limit)

Calcula y devuelve la serie de Fourier a partir de la lista de los coeficientes de Fourier *l* hasta el término *limit* (*limit* puede ser `inf`). Los argumentos *x* y *p* tienen el mismo significado que en
`fourier`.

<!-- category: Series -->
<!-- keywords: fourier -->
<!-- signatures: fourier(f, x, p) -->
### Function: fourier (f, x, p)

Devuelve una lista con los coeficientes de Fourier de 
`f(x)` definida en el intervalo `[-p, p]`.

<!-- category: Series -->
<!-- keywords: fourint -->
<!-- signatures: fourint(f, x) -->
### Function: fourint (f, x)

Calcula y devuelve la lista de los coeficientes integrales de Fourier de `f(x)` definida en `[minf, inf]`.

<!-- category: Series -->
<!-- keywords: fourintcos -->
<!-- signatures: fourintcos(f, x) -->
### Function: fourintcos (f, x)

Devuelve los coeficientes integrales de los cosenos  `f(x)` en `[0, inf]`.

<!-- category: Series -->
<!-- keywords: fourintsin -->
<!-- signatures: fourintsin(f, x) -->
### Function: fourintsin (f, x)

Devuelve los coeficientes integrales de los senos  `f(x)` en `[0, inf]`.

<!-- category: Series -->
<!-- keywords: foursimp -->
<!-- signatures: foursimp(l) -->
### Function: foursimp (l)

Simplifica `sin (n %pi)` a 0 si `sinnpiflag` vale `true` y
`cos (n %pi)` a `(-1)^n` si `cosnpiflag` vale `true`.

<!-- category: Series -->
<!-- keywords: foursin -->
<!-- signatures: foursin(f, x, p) -->
### Function: foursin (f, x, p)

Devuelve los coeficientes de los senos de Fourier de `f(x)` definida en `[0, p]`.

<!-- category: Series -->
<!-- keywords: funp -->
<!-- signatures: funp(f, expr), funp(f, expr, x) -->
### Function: funp (f, expr)

La llamada `funp (f, expr)` devuelve `true` si *expr* contiene la función *f*.


La llamada `funp (f, expr, x)` devuelve `true` si *expr* contiene la función *f* y la variable *x* está presente en el argumento de alguna de las presencias de *f*.

<!-- category: Series -->
<!-- keywords: intopois -->
<!-- signatures: intopois(a) -->
### Function: intopois (a)

Convierte *a* en un codificado Poisson.

<!-- category: Series -->
<!-- keywords: intosum -->
<!-- signatures: intosum(expr) -->
### Function: intosum (expr)

Mueve los factores multiplicativos que están fuera de un sumatorio hacia dentro
de éste. Si el índice del sumatorio aparece en la expresión exterior,
entonces `intosum` busca un índice razonable, lo mismo que hace con 
`sumcontract`. Se trata de la operación contraria a extraer factores comunes de los sumatorios.


En algunos caos puede ser necesario hacer `scanmap (multthru, expr)` antes que `intosum`.



Ejemplo:



```maxima
(%i1) sum(2*x^2*n^k, k , 0, inf);
                               inf
                               ====
                             2 \      k
(%o1)                     2 x   >    n
                               /
                               ====
                               k = 0


(%i2) intosum(%);
                          inf
                          ====
                          \        k  2
(%o2)                      >    2 n  x
                          /
                          ====
                          k = 0
```

<!-- category: Series -->
<!-- keywords: lsum -->
<!-- signatures: lsum(expr, x, L) -->
### Function: lsum (expr, x, L)

Representa la suma de *expr* para cada elemento *x* en *L*.


Se retornará la forma nominal `'lsum` si el argumento *L* no es una lista.


Ejemplos:







```maxima
(%i1) lsum (x^i, i, [1, 2, 7]);
                            7    2
(%o1)                      x  + x  + x
(%i2) lsum (i^2, i, rootsof (x^3 - 1, x));
                     ====
                     \      2
(%o2)                 >    i
                     /
                     ====
                                   3
                     i in rootsof(x  - 1, x)
```

<!-- category: Series -->
<!-- keywords: maxtayorder -->
<!-- signatures: maxtayorder -->
### Variable: maxtayorder

Valor por defecto: `true`


Si `maxtayorder` vale `true`, entonces durante la manipulación algebraica de series truncadas de Taylor, la función `taylor` trata de retener tantos términos correctos como sea posible.

<!-- category: Series -->
<!-- keywords: niceindices -->
<!-- signatures: niceindices(expr) -->
### Function: niceindices (expr)

Cambia las etiquetas de los índices de sumas y productos de *expr*. La función `niceindices` trata de cambiar cada índice al valor de `niceindicespref[1]`, a menos que esa etiqueta aparezca ya en el sumando o factor, en cuyo caso  `niceindices` realiza intentos con los siguientes elementos de  `niceindicespref`, hasta que encuentre una variable que que no esté en uso. Si todas las variables de la lista han sido ya revisadas, se formarán nuevos ínices añadiendo números enteros al valor de `niceindicespref[1]`, como `i0`, `i1`, `i2`, ....


La función `niceindices` evalúa sus argumentos y devuelve una expresión.


Ejemplo:



```maxima
(%i1) niceindicespref;
(%o1)                  [i, j, k, l, m, n]
(%i2) product (sum (f (foo + i*j*bar), foo, 1, inf), bar, 1, inf);
                 inf    inf
                /===\   ====
                 ! !    \
(%o2)            ! !     >      f(bar i j + foo)
                 ! !    /
                bar = 1 ====
                        foo = 1
(%i3) niceindices (%);
                     inf  inf
                    /===\ ====
                     ! !  \
(%o3)                ! !   >    f(i j l + k)
                     ! !  /
                    l = 1 ====
                          k = 1
```

<!-- category: Series -->
<!-- keywords: niceindicespref -->
<!-- signatures: niceindicespref -->
### Variable: niceindicespref

Valor por defecto: `[i, j, k, l, m, n]`


La variable `niceindicespref` es la lista de la que la función `niceindices` va tomando nombres de etiquetas para índices de sumatorios y productos.


En `niceindicespref` se guardan normalmente nombres de variables.


Ejemplo:



```maxima
(%i1) niceindicespref: [p, q, r, s, t, u]$
(%i2) product (sum (f (foo + i*j*bar), foo, 1, inf), bar, 1, inf);
                 inf    inf
                /===\   ====
                 ! !    \
(%o2)            ! !     >      f(bar i j + foo)
                 ! !    /
                bar = 1 ====
                        foo = 1
(%i3) niceindices (%);
                     inf  inf
                    /===\ ====
                     ! !  \
(%o3)                ! !   >    f(i j q + p)
                     ! !  /
                    q = 1 ====
                          p = 1
```

<!-- category: Series -->
<!-- keywords: nusum -->
<!-- signatures: nusum(expr, x, i_0, i_1) -->
### Function: nusum (expr, x, i_0, i_1)

Calcula la suma hipergeométrica indefinida de  *expr* con respecto a la variable  *x* utilizando una procedimiento de decisión debido a R.W. Gosper. La expresión *expr* y el resultado deben poder ser escritos como productos de potencias enteras, factoriales, coeficientes binomiales y funciones racionales.




Los términos suma "definida" e "indefinida" se usan de forma análoga a integración "definida" e "indefinida". La suma indefinida significa dar un resultado simbólico.


Las funciones `nusum` y `unsum` disponen de cierta información sobre sumas y diferencias de productos finitos. Véase también `unsum`.


Ejemplos:



```maxima
(%i1) nusum (n*n!, n, 0, n);

Dependent equations eliminated:  (1)
(%o1)                     (n + 1)! - 1
(%i2) nusum (n^4*4^n/binomial(2*n,n), n, 0, n);
                     4        3       2              n
      2 (n + 1) (63 n  + 112 n  + 18 n  - 22 n + 3) 4      2
(%o2) ------------------------------------------------ - ------
                    693 binomial(2 n, n)                 3 11 7
(%i3) unsum (%, n);
                              4  n
                             n  4
(%o3)                   ----------------
                        binomial(2 n, n)
(%i4) unsum (prod (i^2, i, 1, n), n);
                    n - 1
                    /===\
                     ! !   2
(%o4)              ( ! !  i ) (n - 1) (n + 1)
                     ! !
                    i = 1
(%i5) nusum (%, n, 1, n);

Dependent equations eliminated:  (2 3)
                            n
                          /===\
                           ! !   2
(%o5)                      ! !  i  - 1
                           ! !
                          i = 1
```

<!-- category: Series -->
<!-- keywords: outofpois -->
<!-- signatures: outofpois(a) -->
### Function: outofpois (a)

Convierte *a* desde codificado de Poisson a una representación general.  Si *a* no está en forma de Poisson, `outofpois` hace la conversión, siendo entonces el valor retornado `outofpois (intopois (a))`. Esta función es un simplificador canónico para sumas de potencias de senos y cosenos.

<!-- category: Series -->
<!-- keywords: pade -->
<!-- signatures: pade(taylor_series, numer_deg_bound, denom_deg_bound) -->
### Function: pade (taylor_series, numer_deg_bound, denom_deg_bound)

Devuelve la lista de todas las funciones racionales que tienen el desarrollo de Taylor dado, en las que la suma de los grados del numerador y denominador es menor o igual que el nivel de truncamiento de la serie de potencias.


La expresión *taylor_series* es una serie de Taylor univariante. Los argumentos *numer_deg_bound* y *denom_deg_bound* son enteros positivos que indican las cotas para numerador y denominador.


La expresión *taylor_series* también puede ser una serie de Laurent, y las cotas de los grados pueden ser `inf`. El grado total se define como `numer_deg_bound + denom_deg_bound`. La longitud de una serie de potencias se define como `"truncation level" + 1 - min(0, "order of series")`.



```maxima
(%i1) taylor (1 + x + x^2 + x^3, x, 0, 3);
                              2    3
(%o1)/T/             1 + x + x  + x  + . . .
(%i2) pade (%, 1, 1);
                                 1
(%o2)                       [- -----]
                               x - 1
(%i3) t: taylor(-(83787*x^10 - 45552*x^9 - 187296*x^8
                   + 387072*x^7 + 86016*x^6 - 1507328*x^5
                   + 1966080*x^4 + 4194304*x^3 - 25165824*x^2
                   + 67108864*x - 134217728)
       /134217728, x, 0, 10);
                    2    3       4       5       6        7
             x   3 x    x    15 x    23 x    21 x    189 x
(%o3)/T/ 1 - - + ---- - -- - ----- + ----- - ----- - ------
             2    16    32   1024    2048    32768   65536

                                  8         9          10
                            5853 x    2847 x    83787 x
                          + ------- + ------- - --------- + . . .
                            4194304   8388608   134217728
(%i4) pade (t, 4, 4);
(%o4)                          []
```


No hay ninguna función racional de grado 4 en numerador y denominador con este desarrollo en serie de potencias. Es necesario dar un número de grados al numerador y denominador cuya suma sea al menos el grado del desarrollo de la serie, a fin de disponer de un número suficiente de coeficientes desconocidos para calcular.



```maxima
(%i5) pade (t, 5, 5);
                     5                4                 3
(%o5) [- (520256329 x  - 96719020632 x  - 489651410240 x

                  2
 - 1619100813312 x  - 2176885157888 x - 2386516803584)

               5                 4                  3
/(47041365435 x  + 381702613848 x  + 1360678489152 x

                  2
 + 2856700692480 x  + 3370143559680 x + 2386516803584)]
```

<!-- category: Series -->
<!-- keywords: poisdiff -->
<!-- signatures: poisdiff(a, b) -->
### Function: poisdiff (a, b)

Deriva *a* con respecto a *b*. El argumento *b* debe aparecer sólo en los argumentos trigonométricos o sólo en los coeficientes.

<!-- category: Series -->
<!-- keywords: poisexpt -->
<!-- signatures: poisexpt(a, b) -->
### Function: poisexpt (a, b)

Idéntico a `intopois (a^b)`. El argumento *b* debe ser un entero positivo.

<!-- category: Series -->
<!-- keywords: poisint -->
<!-- signatures: poisint(a, b) -->
### Function: poisint (a, b)

Integra en un sentido restringido similar a `poisdiff`.

<!-- category: Series -->
<!-- keywords: poislim -->
<!-- signatures: poislim -->
### Variable: poislim

Valor por defecto: 5


La variable `poislim` determina el dominio de los coeficientes en los argumentos de las funciones trigonométricas.  El valor por defecto 5 corresponde al intervalo [-2^(5-1)+1,2^(5-1)], o [-15,16], pero puede reasignarse para  [-2^(n-1)+1, 2^(n-1)].

<!-- category: Series -->
<!-- keywords: poismap -->
<!-- signatures: poismap(series, sinfn, cosfn) -->
### Function: poismap (series, sinfn, cosfn)

Aplica las funciones *sinfn* a los términos sinusoidales y
las funciones *cosfn* a los cosenoidales de la serie de Poisson
dada. Tanto *sinfn* como *cosfn* son funciones de dos
argumentos, los cuales son un coeficiente y una parte trigonométrica
de un término de la serie.

<!-- category: Series -->
<!-- keywords: poisplus -->
<!-- signatures: poisplus(a, b) -->
### Function: poisplus (a, b)

Idéntico a `intopois (a + b)`.

<!-- category: Series -->
<!-- keywords: poissimp -->
<!-- signatures: poissimp(a) -->
### Function: poissimp (a)

Convierte *a* en una serie de Poisson para *a* en su representación general.

<!-- category: Series -->
<!-- keywords: poisson -->
<!-- signatures: poisson -->
### Variable: poisson

El símbolo `/P/` sigue a la etiqueta de las líneas que contienen expresiones que son series de Poisson.

<!-- category: Series -->
<!-- keywords: poissubst -->
<!-- signatures: poissubst(a, b, c) -->
### Function: poissubst (a, b, c)

Sustituye *b* por *a* en *c*, donde  *c* es una serie de Poisson.


(1) Si *b* es una de las variables *u*, *v*, *w*, *x*, *y* o *z*, entonces *a* debe ser una expresión lineal en esas variables (por ejemplo, `6*u + 4*v`).


(2) Si *b* no es ninguna de esas variables, entonces *a* no puede contener tampoco a ninguna de ellas, ni senos, ni cosenos.

<!-- category: Series -->
<!-- keywords: poistimes -->
<!-- signatures: poistimes(a, b) -->
### Function: poistimes (a, b)

Idéntico a `intopois (a*b)`.

<!-- category: Series -->
<!-- keywords: powerseries -->
<!-- signatures: powerseries(expr, x, a) -->
### Function: powerseries (expr, x, a)

Devuelve la forma general del desarrollo en serie de potencias 
de *expr* para la variable *x* alrededor del punto 
*a* (que puede ser `inf`, de infinito):


```maxima
inf
           ====
           \               n
            >    b  (x - a)
           /      n
           ====
           n = 0
```


Si `powerseries` no es capaz de desarrollar *expr*,
la función `taylor` puede calcular los primeros términos de la serie.


Si `verbose` vale `true`, `powerseries` va 
mostrando mensajes mientras progresa el cálculo. 



```maxima
(%i1) verbose: true$
(%i2) powerseries (log(sin(x)/x), x, 0);
can't expand 
                                 log(sin(x))
so we'll try again after applying the rule:
                                        d
                                      / -- (sin(x))
                                      [ dx
                        log(sin(x)) = i ----------- dx
                                      ]   sin(x)
                                      /
in the first simplification we have returned:
                             /
                             [
                             i cot(x) dx - log(x)
                             ]
                             /
                    inf
                    ====        i1  2 i1             2 i1
                    \      (- 1)   2     bern(2 i1) x
                     >     ------------------------------
                    /                i1 (2 i1)!
                    ====
                    i1 = 1
(%o2)                -------------------------------------
                                      2
```

<!-- category: Series -->
<!-- keywords: printpois -->
<!-- signatures: printpois(a) -->
### Function: printpois (a)

Presenta una serie de Poisson en un formato legible.  Conjuntamente con `outofpois`, si es necesario convertirá *a* primero en una codificación de Poisson.

<!-- category: Series -->
<!-- keywords: product -->
<!-- signatures: product(expr, i, i_0, i_1) -->
### Function: product (expr, i, i_0, i_1)

Representa el producto de los valores de `expr` según el índice *i* varía de *i_0* hasta *i_1*.
La forma nominal `'product` se presenta en forma de letra pi mayúscula.


La función `product` evalúa *expr* y los límites inferior y superior, *i_0* y *i_1*, pero no evalúa el índice *i*.


Si la diferencia entre los límites superior e inferior es un número entero, la expresión *expr* se evalúa para cada valor del índice *i*, siendo el resultado un producto en forma explícita.


En caso contrario, el rango del índice no está definido, aplicándose entonces algunas reglas que permitan simplificar el producto.
Cuando la variable global `simpproduct` valga `true`, se aplicarán reglas adicionales.
En ciertos casos, la simplificación dará lugar a un resultado que ya no tenga el formato del producto; en caso contrario se devolverá una forma nominal `'product`.


Véanse también `nouns` y `evflag`.



Ejemplos:















```maxima
(%i1) product (x + i*(i+1)/2, i, 1, 4);
(%o1)           (x + 1) (x + 3) (x + 6) (x + 10)
(%i2) product (i^2, i, 1, 7);
(%o2)                       25401600
(%i3) product (a[i], i, 1, 7);
(%o3)                 a  a  a  a  a  a  a
                       1  2  3  4  5  6  7
(%i4) product (a(i), i, 1, 7);
(%o4)          a(1) a(2) a(3) a(4) a(5) a(6) a(7)
(%i5) product (a(i), i, 1, n);
                             n
                           /===\
                            ! !
(%o5)                       ! !  a(i)
                            ! !
                           i = 1
(%i6) product (k, k, 1, n);
                               n
                             /===\
                              ! !
(%o6)                         ! !  k
                              ! !
                             k = 1
(%i7) product (k, k, 1, n), simpproduct;
(%o7)                          n!
(%i8) product (integrate (x^k, x, 0, 1), k, 1, n);
                             n
                           /===\
                            ! !    1
(%o8)                       ! !  -----
                            ! !  k + 1
                           k = 1
(%i9) product (if k <= 5 then a^k else b^k, k, 1, 10);
                              15  40
(%o9)                        a   b
```

<!-- category: Series -->
<!-- keywords: psexpand -->
<!-- signatures: psexpand -->
### Variable: psexpand

Valor por defecto: `false`


Si `psexpand` vale `true`, toda expresi’on racional se muestra completamente expandida. La variable `ratexpand` tiene el mismo efecto.



Si `psexpand` vale `false`, las expresines multivariantes se presentan tal como lo hace el paquete de funciones racionales.



Si `psexpand` vale  `multi`, los términos de igual grado son agrupados.

<!-- category: Series -->
<!-- keywords: remfun -->
<!-- signatures: remfun(f, expr), remfun(f, expr, x) -->
### Function: remfun (f, expr)

La llamada `remfun (f, expr)` reemplaza todas las subexpresiones `f (arg)` por *arg* en *expr*.


La llamada `remfun (f, expr, x)` reemplaza todas las subexpresiones `f (arg)` por *arg* en *expr* sólo si *arg* contiene a la variable *x*.

<!-- category: Series -->
<!-- keywords: revert, revert2 -->
<!-- signatures: revert(expr, x), revert2(expr, x, n) -->
### Function: revert (expr, x)

Estas funciones devuelven el recíproco de *expr* en forma de desarrollo de Taylor alrededor de cero respecto de la variable *x*. La función `revert` devuelve un polinomio de grado igual a la mayor potencia en *expr*.
La función `revert2` devuelve un polinomio de grado *n*, el cual puede ser mayor, igual o menor que el grado de  *expr*.


Para utilizar estas funciones es necesario cargarlas en memoria mediante `load ("revert")`.


Ejemplos:



```maxima
(%i1) load ("revert")$
(%i2) t: taylor (exp(x) - 1, x, 0, 6);
                   2    3    4    5     6
                  x    x    x    x     x
(%o2)/T/      x + -- + -- + -- + --- + --- + . . .
                  2    6    24   120   720
(%i3) revert (t, x);
               6       5       4       3       2
           10 x  - 12 x  + 15 x  - 20 x  + 30 x  - 60 x
(%o3)/R/ - --------------------------------------------
                                60
(%i4) ratexpand (%);
                     6    5    4    3    2
                    x    x    x    x    x
(%o4)             - -- + -- - -- + -- - -- + x
                    6    5    4    3    2
(%i5) taylor (log(x+1), x, 0, 6);
                    2    3    4    5    6
                   x    x    x    x    x
(%o5)/T/       x - -- + -- - -- + -- - -- + . . .
                   2    3    4    5    6
(%i6) ratsimp (revert (t, x) - taylor (log(x+1), x, 0, 6));
(%o6)                           0
(%i7) revert2 (t, x, 4);
                          4    3    2
                         x    x    x
(%o7)                  - -- + -- - -- + x
                         4    3    2
```

<!-- category: Series -->
<!-- keywords: simpsum -->
<!-- signatures: simpsum -->
### Variable: simpsum

Valor por defecto: `false`


Si `simpsum` vale `true`, se simplifica el resultado de un sumatorio `sum`.
Esta simplificación podrá producir en ocasiones una expresión compacta. Si 
`simpsum` vale `false` o si se utiliza la forma apostrofada `'sum`,
el valor es una forma nominal que representa la notación sigma habitual en matemáticas.

<!-- category: Series -->
<!-- keywords: sinnpiflag -->
<!-- signatures: sinnpiflag -->
### Variable: sinnpiflag

Valor por defecto: `true`


Véase `foursimp`.

<!-- category: Series -->
<!-- keywords: sum -->
<!-- signatures: sum(expr, i, i_0, i_1) -->
### Function: sum (expr, i, i_0, i_1)

Representa la suma de los valores de `expr` según el índice *i* varía de *i_0* hasta *i_1*.
La forma nominal `'sum` se presenta en forma de letra sigma mayúscula.


La función `sum` evalúa su sumando *expr* y los límites inferior y superior, *i_0* y *i_1*, pero no evalúa el índice *i*.


Si la diferencia entre los límites superior e inferior es un número entero, el sumando *expr* se evalúa para cada valor del índice *i*, siendo el resultado una suma en forma explícita.


En caso contrario, el rango del índice no está definido, aplicándose entonces algunas reglas que permitan simplificar la suma.
Cuando la variable global `simpsum` valga `true`, se aplicarán reglas adicionales.
En ciertos casos, la simplificación dará lugar a un resultado que ya no tenga el formato del sumatorio; en caso contrario se devolverá una forma nominal `'product`.


Cuando `cauchysum` vale `true`, el producto de sumatorios se expresa como un producto de Cauchy, en cuyo caso el índice del sumatorio interior es función del índice del exterior, en lugar de variar independientemente.


La variable global `genindex` guarda el prefijo alfabético a utilizar cuando sea necesario generar automáticamente el siguiente índice de sumatorio.


La variable global `gensumnum` guarda el sufijo numérico a utilizar cuando sea necesario generar automáticamente el siguiente índice de sumatorio. Si `gensumnum` vale `false`, un índice generado automáticamente constará sólo de `genindex`, sin sufijo numérico.


Véanse también `sumcontract`, `intosum`,
`bashindices`, `niceindices`,
`nouns` y `evflag`.


Ejemplos:


















```maxima
(%i1) sum (i^2, i, 1, 7);
(%o1)                          140
(%i2) sum (a[i], i, 1, 7);
(%o2)           a  + a  + a  + a  + a  + a  + a
                 7    6    5    4    3    2    1
(%i3) sum (a(i), i, 1, 7);
(%o3)    a(7) + a(6) + a(5) + a(4) + a(3) + a(2) + a(1)
(%i4) sum (a(i), i, 1, n);
                            n
                           ====
                           \
(%o4)                       >    a(i)
                           /
                           ====
                           i = 1
(%i5) sum (2^i + i^2, i, 0, n);
                          n
                         ====
                         \       i    2
(%o5)                     >    (2  + i )
                         /
                         ====
                         i = 0
(%i6) sum (2^i + i^2, i, 0, n), simpsum;
                              3      2
                   n + 1   2 n  + 3 n  + n
(%o6)             2      + --------------- - 1
                                  6
(%i7) sum (1/3^i, i, 1, inf);
                            inf
                            ====
                            \     1
(%o7)                        >    --
                            /      i
                            ====  3
                            i = 1
(%i8) sum (1/3^i, i, 1, inf), simpsum;
                                1
(%o8)                           -
                                2
(%i9) sum (i^2, i, 1, 4) * sum (1/i^2, i, 1, inf);
                              inf
                              ====
                              \     1
(%o9)                      30  >    --
                              /      2
                              ====  i
                              i = 1
(%i10) sum (i^2, i, 1, 4) * sum (1/i^2, i, 1, inf), simpsum;
                                  2
(%o10)                       5 %pi
(%i11) sum (integrate (x^k, x, 0, 1), k, 1, n);
                            n
                           ====
                           \       1
(%o11)                      >    -----
                           /     k + 1
                           ====
                           k = 1
(%i12) sum (if k <= 5 then a^k else b^k, k, 1, 10));
          10    9    8    7    6    5    4    3    2
(%o12)   b   + b  + b  + b  + b  + a  + a  + a  + a  + a
```

<!-- category: Series -->
<!-- keywords: sumcontract -->
<!-- signatures: sumcontract(expr) -->
### Function: sumcontract (expr)

Combina todos los sumatorios de una suma cuyos límites inferiores y 
superiores difieren por constantes. El resultado es una expresión que contiene 
un sumatorio por cada conjunto de tales sumatorios, más todos los demás
términos adicionales que tuvieron que extraerse para formar la suma. La función 
`sumcontract` combina todos los sumatorios compatibles y utiliza uno de los
índices de uno de los sumatorios si puede, si no formará un 
índice que sea razonable.


Puede ser necesario hacer `intosum (expr)` antes que `sumcontract`.



Ejemplo:



```maxima
(%i1) 'sum(1/l,l,1,n)+'sum(k,k,1,n+2);

                         n        n + 2
                        ====      ====
                        \     1   \
(%o1)                    >    - +  >    k
                        /     l   /
                        ====      ====
                        l = 1     k = 1

(%i2) sumcontract(%);

                            n
                           ====
                           \          1
(%o2)                2 n +  >    (l + -) + 3
                           /          l
                           ====
                           l = 1
```

<!-- category: Series -->
<!-- keywords: sumexpand -->
<!-- signatures: sumexpand -->
### Variable: sumexpand

Valor por defecto: `false`


Si `sumexpand` vale `true`, productos de sumatorios y de sumatorios con exponentes se 
reducen a sumatorios anidados.


Véase también `cauchysum`.


Ejemplos:



```maxima
(%i1) sumexpand: true$
(%i2) sum (f (i), i, 0, m) * sum (g (j), j, 0, n);

                     m      n
                    ====   ====
                    \      \
(%o2)                >      >     f(i1) g(i2)
                    /      /
                    ====   ====
                    i1 = 0 i2 = 0

(%i3) sum (f (i), i, 0, m)^2;
                     m      m
                    ====   ====
                    \      \
(%o3)                >      >     f(i3) f(i4)
                    /      /
                    ====   ====
                    i3 = 0 i4 = 0
```

<!-- category: Series -->
<!-- keywords: taylor -->
<!-- signatures: taylor(expr, x, a, n), taylor(expr, [x_1, x_2, ...], a, n), taylor(expr, [x, a, n, 'asymp]), taylor(expr, [x_1, x_2, ...], [a_1, a_2, ...], [n_1, n_2, ...]), taylor(expr, [x_1, a_1, n_1], [x_2, a_2, n_2], ...) -->
### Function: taylor (expr, x, a, n)

La llamada `taylor (expr, x, a, n)` expande la expresión *expr* en un desarrollo  de 
 Taylor o de  Laurent respecto de la variable *x* alrededor del punto *a*, con términos hasta `(x - a)^n`.


Si *expr* es de la forma `f(x)/g(x)` y `g(x)` no tiene términos hasta de grado *n*, entonces `taylor` intenta expandir `g(x)` hasta el grado  `2 n`. Si aún así no hay términos no nulos, `taylor` dobla el grado de la expansión de `g(x)` hasta que el grado de la expansión sea menor o igual que `n 2^taylordepth`.


La llamada `taylor (expr, [x_1, x_2, ...], a, n)` devuelve la serie en potencias truncada de grado  *n* en todas las variables *x_1*, *x_2*, ... alrededor del punto `(a, a, ...)`.


La llamada `taylor (expr, [x_1, a_1, n_1], [x_2, a_2, n_2], ...)`
devuelve la serie en potencias truncada en las variables *x_1*, *x_2*, ... alrededor del punto `(a_1, a_2, ...)`; el truncamiento se realiza, respectivamente, en los grados *n_1*, *n_2*, ....


La llamada `taylor (expr, [x_1, x_2, ...], [a_1, a_2, ...], [n_1, n_2, ...])`
devuelve la serie en potencias truncada en las variables *x_1*, *x_2*, ... alrededor del punto `(a_1, a_2, ...)`, el truncamiento se realiza, respectivamente, en los grados *n_1*, *n_2*, ....


La llamada `taylor (expr, [x, a, n, 'asymp])` devuelve el desarrollo de  *expr* en potencias negativas de `x - a`. El término de mayor orden es `(x - a)^-n`.


Si `maxtayorder` vale `true`, entonces durante la manipulación algebraica de las series (truncadas) de Taylor, la función `taylor` intenta mantener tantos términos correctos como sea posible.


Si `psexpand` vale `true`, una expresión racional desarrollada se muestra completamente expandida. La variable  `ratexpand` tiene el mismo efecto. Si `psexpand` vale `false`, una expresión multivariante se mostrará tal como lo hace el paquete de funciones racionales. Si  `psexpand` vale  `multi`, los términos del mismo grado 
son agrupados.


Véase también la variable `taylor_logexpand` para el control del desarrollo.


Ejemplos:




















```maxima
(%i1) taylor (sqrt (sin(x) + a*x + 1), x, 0, 3);
                           2             2
             (a + 1) x   (a  + 2 a + 1) x
(%o1)/T/ 1 + --------- - -----------------
                 2               8

                                   3      2             3
                               (3 a  + 9 a  + 9 a - 1) x
                             + -------------------------- + . . .
                                           48
(%i2) %^2;
                                    3
                                   x
(%o2)/T/           1 + (a + 1) x - -- + . . .
                                   6
(%i3) taylor (sqrt (x + 1), x, 0, 5);
                       2    3      4      5
                  x   x    x    5 x    7 x
(%o3)/T/      1 + - - -- + -- - ---- + ---- + . . .
                  2   8    16   128    256
(%i4) %^2;
(%o4)/T/                  1 + x + . . .
(%i5) product ((1 + x^i)^2.5, i, 1, inf)/(1 + x^2);
                         inf
                        /===\
                         ! !    i     2.5
                         ! !  (x  + 1)
                         ! !
                        i = 1
(%o5)                   -----------------
                              2
                             x  + 1
(%i6) ev (taylor(%, x,  0, 3), keepfloat);
                               2           3
(%o6)/T/    1 + 2.5 x + 3.375 x  + 6.5625 x  + . . .
(%i7) taylor (1/log (x + 1), x, 0, 3);
                               2       3
                 1   1   x    x    19 x
(%o7)/T/         - + - - -- + -- - ----- + . . .
                 x   2   12   24    720
(%i8) taylor (cos(x) - sec(x), x, 0, 5);
                                4
                           2   x
(%o8)/T/                - x  - -- + . . .
                               6
(%i9) taylor ((cos(x) - sec(x))^3, x, 0, 5);
(%o9)/T/                    0 + . . .
(%i10) taylor (1/(cos(x) - sec(x))^3, x, 0, 5);
                                               2          4
            1     1       11      347    6767 x    15377 x
(%o10)/T/ - -- + ---- + ------ - ----- - ------- - --------
             6      4        2   15120   604800    7983360
            x    2 x    120 x

                                                          + . . .
(%i11) taylor (sqrt (1 - k^2*sin(x)^2), x, 0, 6);
               2  2       4      2   4
              k  x    (3 k  - 4 k ) x
(%o11)/T/ 1 - ----- - ----------------
                2            24

                                    6       4       2   6
                               (45 k  - 60 k  + 16 k ) x
                             - -------------------------- + . . .
                                          720
(%i12) taylor ((x + 1)^n, x, 0, 4);
                      2       2     3      2         3
                    (n  - n) x    (n  - 3 n  + 2 n) x
(%o12)/T/ 1 + n x + ----------- + --------------------
                         2                 6

                               4      3       2         4
                             (n  - 6 n  + 11 n  - 6 n) x
                           + ---------------------------- + . . .
                                          24
(%i13) taylor (sin (y + x), x, 0, 3, y, 0, 3);
               3                 2
              y                 y
(%o13)/T/ y - -- + . . . + (1 - -- + . . .) x
              6                 2

                    3                       2
               y   y            2      1   y            3
          + (- - + -- + . . .) x  + (- - + -- + . . .) x  + . . .
               2   12                  6   12
(%i14) taylor (sin (y + x), [x, y], 0, 3);
                     3        2      2      3
                    x  + 3 y x  + 3 y  x + y
(%o14)/T/   y + x - ------------------------- + . . .
                                6
(%i15) taylor (1/sin (y + x), x, 0, 3, y, 0, 3);
          1   y              1    1               1            2
(%o15)/T/ - + - + . . . + (- -- + - + . . .) x + (-- + . . .) x
          y   6               2   6                3
                             y                    y

                                           1            3
                                      + (- -- + . . .) x  + . . .
                                            4
                                           y
(%i16) taylor (1/sin (y + x), [x, y], 0, 3);
                             3         2       2        3
            1     x + y   7 x  + 21 y x  + 21 y  x + 7 y
(%o16)/T/ ----- + ----- + ------------------------------- + . . .
          x + y     6                   360
```

<!-- category: Series -->
<!-- keywords: taylor_logexpand -->
<!-- signatures: taylor_logexpand -->
### Variable: taylor_logexpand

Valor por defecto: `true`


La variable `taylor_logexpand` controla los desarrollos de logaritmos en la función `taylor`.


Si `taylor_logexpand` vale `true`, todos los logaritmos se expanden completamente de manera que algunos problemas que se plantean debido a ciertas identidades logarítmicas no interfieran con el proceso del cálculo del desarrollo de Taylor. Sin embargo, este proceder no es del todo correcto.

<!-- category: Series -->
<!-- keywords: taylor_order_coefficients -->
<!-- signatures: taylor_order_coefficients -->
### Variable: taylor_order_coefficients

Valor por defecto: `true`


La variable `taylor_order_coefficients` controla la ordenación de los coeficientes en un desarrollo de Taylor.


Si `taylor_order_coefficients` vale `true`, los coeficientes del desarrollo de Taylor se ordenan de la forma canónica.

<!-- category: Series -->
<!-- keywords: taylor_simplifier -->
<!-- signatures: taylor_simplifier(expr) -->
### Function: taylor_simplifier (expr)

Simplifica los coeficientes de la serie de potencias *expr*. Esta función es llamada desde la función `taylor`.

<!-- category: Series -->
<!-- keywords: taylor_truncate_polynomials -->
<!-- signatures: taylor_truncate_polynomials -->
### Variable: taylor_truncate_polynomials

Valor por defecto: `true`



Si `taylor_truncate_polynomials` vale `true`, los polinomios quedan truncados en base a los niveles de truncamiento de entrada.


En otro caso, aquellos polinomios que se utilicen como entrada a la función  `taylor` se consideran que tienen precisión infinita.

<!-- category: Series -->
<!-- keywords: taylordepth -->
<!-- signatures: taylordepth -->
### Variable: taylordepth

Valor por defecto: 3



Si todavía no hay términos no nulos, la función `taylor` dobla el grado del desarrollo de `g(x)`
tantas veces como sea necesario para que el grado del desarrollo sea menor o igual que `n 2^taylordepth`.

<!-- category: Series -->
<!-- keywords: taylorinfo -->
<!-- signatures: taylorinfo(expr) -->
### Function: taylorinfo (expr)

Devuelve información sobre el desarrollo de Taylor *expr*. El valor devuelto por esta función es una lista de listas. Cada lista contiene el nombre de una variable, el punto de expansión y el grado del desarrollo.


La función `taylorinfo` devuelve `false` si *expr* no es un desarrollo de Taylor.


Ejemplo:



```maxima
(%i1) taylor ((1 - y^2)/(1 - x), x, 0, 3, [y, a, inf]);
                  2                       2
(%o1)/T/ - (y - a)  - 2 a (y - a) + (1 - a )

         2                        2
 + (1 - a  - 2 a (y - a) - (y - a) ) x

         2                        2   2
 + (1 - a  - 2 a (y - a) - (y - a) ) x

         2                        2   3
 + (1 - a  - 2 a (y - a) - (y - a) ) x  + . . .
(%i2) taylorinfo(%);
(%o2)               [[y, a, inf], [x, 0, 3]]
```

<!-- category: Series -->
<!-- keywords: taylorp -->
<!-- signatures: taylorp(expr) -->
### Function: taylorp (expr)

Devuelve `true` si *expr* es un desarrollo de Taylor y `false` en caso contrario.

<!-- category: Series -->
<!-- keywords: taytorat -->
<!-- signatures: taytorat(expr) -->
### Function: taytorat (expr)

Convierte *expr* del formato de `taylor` al formato CRE (Canonical Rational Expression). El efecto es el mismo que haciendo  `rat (ratdisrep (expr))`, pero más rápido.

<!-- category: Series -->
<!-- keywords: totalfourier -->
<!-- signatures: totalfourier(f, x, p) -->
### Function: totalfourier (f, x, p)

Devuelve `fourexpand (foursimp (fourier (f, x, p)), x, p, 'inf)`.

<!-- category: Series -->
<!-- keywords: trunc -->
<!-- signatures: trunc(expr) -->
### Function: trunc (expr)

Devuelve la representación interna de la expresión *expr* de tal forma como si sus sumas fuesen una serie truncada de Taylor. La expresión *expr* no sufre ninguna otra modificación.


Ejemplo:



```maxima
(%i1) expr: x^2 + x + 1;
                            2
(%o1)                      x  + x + 1
(%i2) trunc (expr);
                                2
(%o2)                  1 + x + x  + . . .
(%i3) is (expr = trunc (expr));
(%o3)                         true
```

<!-- category: Series -->
<!-- keywords: unsum -->
<!-- signatures: unsum(f, n) -->
### Function: unsum (f, n)

Devuelve la diferencia `f(n) - f(n - 1)`. En cierto sentido `unsum` es la inversa de `sum`.


Véase también `nusum`.


Ejemplos:








```maxima
(%i1) g(p) := p*4^n/binomial(2*n,n);
                                     n
                                  p 4
(%o1)               g(p) := ----------------
                            binomial(2 n, n)
(%i2) g(n^4);
                              4  n
                             n  4
(%o2)                   ----------------
                        binomial(2 n, n)
(%i3) nusum (%, n, 0, n);
                     4        3       2              n
      2 (n + 1) (63 n  + 112 n  + 18 n  - 22 n + 3) 4      2
(%o3) ------------------------------------------------ - ------
                    693 binomial(2 n, n)                 3 11 7
(%i4) unsum (%, n);
                              4  n
                             n  4
(%o4)                   ----------------
                        binomial(2 n, n)
```

<!-- category: Series -->
<!-- keywords: verbose -->
<!-- signatures: verbose -->
### Variable: verbose

Valor por defecto: `false`


Si `verbose` vale `true`, la función `powerseries` va imprimiendo mensajes durante su ejecución.

