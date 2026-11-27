## Summen, Produkte und Reihen

<!-- category: Series -->
<!-- keywords: bashindices -->
<!-- signatures: bashindices(expr) -->
### Function: bashindices (expr)

Transformiert einen Ausdruck *expr*, der mehrere Summen oder Produkte
enthalt so, dass alle Summen und Produkte einen unterschiedlichen Index haben.
Dies erleichtert zum Beispiel Substitutionen mit der Funktion
`changevar`.  Die neuen Indizes werden mit `jnummer`
bezeichnet, wobei die Zahl *nummer* der Wert der Optionsvariablen
`gensumnum` ist.


Beispiel:



```maxima
(%i1) sum(1/k^2,k,0,inf)+sum(1/k,k,0,inf);
                       inf       inf
                       ====      ====
                       \     1   \     1
(%o1)                   >    - +  >    --
                       /     k   /      2
                       ====      ====  k
                       k = 0     k = 0
(%i2) bashindices(%);
                     inf         inf
                     ====        ====
                     \      1    \       1
(%o2)                 >     -- +  >     ---
                     /      j2   /        2
                     ====        ====   j1
                     j2 = 0      j1 = 0
```

See also: `changevar`, `gensumnum`.

<!-- category: Series -->
<!-- keywords: cauchysum -->
<!-- signatures: cauchysum -->
### Variable: cauchysum

Standardwert: `false`


Werden zwei Reihen miteinander multipliziert und die Optionsvariablen
`sumexpand` sowie `cauchysum` haben beide den Wert `true`, dann 
wird die Cauchy-Produktformel angewendet.


Beispiele:



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

See also: `sumexpand`.

<!-- category: Series -->
<!-- keywords: cf -->
<!-- signatures: cf(expr) -->
### Function: cf (expr)

Converts *expr* into a continued fraction. *expr* is an expression
comprising continued fractions and square roots of integers. Operands in the 
expression may be combined with arithmetic operators. Aside from continued 
fractions and square roots, factors in the expression must be integer or 
rational numbers. Maxima does not know about operations on continued fractions 
outside of `cf`.


`cf` evaluates its arguments after binding `listarith` to 
`false`. `cf` returns a continued fraction, represented as a list.


A continued fraction `a + 1/(b + 1/(c + ...))` is represented by the list 
`[a, b, c, ...]`. The list elements `a`, `b`, `c`, ...
must evaluate to integers. *expr* may also contain `sqrt (n)` where
`n` is an integer. In this case `cf` will give as many terms of the
continued fraction as the value of the variable `cflength` times the
period.


A continued fraction can be evaluated to a number by evaluating the arithmetic 
representation returned by `cfdisrep`. See also `cfexpand` for another 
way to evaluate a continued fraction.


See also `cfdisrep`, `cfexpand`, and `cflength`.


Examples:



- *
*expr* is an expression comprising continued fractions and square roots of integers.

```maxima
(%i1) cf ([5, 3, 1]*[11, 9, 7] + [3, 7]/[4, 3, 2]);
(%o1)               [59, 17, 2, 1, 1, 1, 27]
(%i2) cf ((3/17)*[1, -2, 5]/sqrt(11) + (8/13));
(%o2)        [0, 1, 1, 1, 3, 2, 1, 4, 1, 9, 1, 9, 2]
```
- *
`cflength` controls how many periods of the continued fraction
are computed for algebraic, irrational numbers.

```maxima
(%i1) cflength: 1$
(%i2) cf ((1 + sqrt(5))/2);
(%o2)                    [1, 1, 1, 1, 2]
(%i3) cflength: 2$
(%i4) cf ((1 + sqrt(5))/2);
(%o4)               [1, 1, 1, 1, 1, 1, 1, 2]
(%i5) cflength: 3$
(%i6) cf ((1 + sqrt(5))/2);
(%o6)           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
```
- *
A continued fraction can be evaluated by evaluating the arithmetic representation
returned by `cfdisrep`.

```maxima
(%i1) cflength: 3$
(%i2) cfdisrep (cf (sqrt (3)))$
(%i3) ev (%, numer);
(%o3)                   1.731707317073171
```
- *
Maxima does not know about operations on continued fractions outside of `cf`.

```maxima
(%i1) cf ([1,1,1,1,1,2] * 3);
(%o1)                     [4, 1, 5, 2]
(%i2) cf ([1,1,1,1,1,2]) * 3;
(%o2)                  [3, 3, 3, 3, 3, 6]
```

<!-- category: Series -->
<!-- keywords: cfdisrep -->
<!-- signatures: cfdisrep(list) -->
### Function: cfdisrep (list)

Constructs and returns an ordinary arithmetic expression
of the form `a + 1/(b + 1/(c + ...))`
from the list representation of a continued fraction `[a, b, c, ...]`.



```maxima
(%i1) cf ([1, 2, -3] + [1, -2, 1]);
(%o1)                     [1, 1, 1, 2]
(%i2) cfdisrep (%);
                                  1
(%o2)                     1 + ---------
                                    1
                              1 + -----
                                      1
                                  1 + -
                                      2
```

<!-- category: Series -->
<!-- keywords: cfexpand -->
<!-- signatures: cfexpand(x) -->
### Function: cfexpand (x)

Returns a matrix of the numerators and denominators of the
last (column 1) and next-to-last (column 2) convergents of the continued fraction *x*.



```maxima
(%i1) cf (rat (ev (%pi, numer)));

`rat' replaced 3.141592653589793 by 103993/33102 =3.141592653011902
(%o1)                  [3, 7, 15, 1, 292]
(%i2) cfexpand (%); 
                         [ 103993  355 ]
(%o2)                    [             ]
                         [ 33102   113 ]
(%i3) %[1,1]/%[2,1], numer;
(%o3)                   3.141592653011902
```

<!-- category: Series -->
<!-- keywords: cflength -->
<!-- signatures: cflength -->
### Variable: cflength

Default value: 1


`cflength` controls the number of terms of the continued
fraction the function `cf` will give, as the value `cflength` times the
period.  Thus the default is to give one period.



```maxima
(%i1) cflength: 1$
(%i2) cf ((1 + sqrt(5))/2);
(%o2)                    [1, 1, 1, 1, 2]
(%i3) cflength: 2$
(%i4) cf ((1 + sqrt(5))/2);
(%o4)               [1, 1, 1, 1, 1, 1, 1, 2]
(%i5) cflength: 3$
(%i6) cf ((1 + sqrt(5))/2);
(%o6)           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
```

<!-- category: Series -->
<!-- keywords: deftaylor -->
<!-- signatures: deftaylor(f_1(x_1), expr_1, ..., f_n(x_n), expr_n) -->
### Function: deftaylor (f_1(x_1), expr_1, ..., f_n(x_n), expr_n)

Fur eine Funktion *f_i* einer Variablen *x_i* definiert 
`deftaylor` den Ausdruck *expr_i* als die Taylorreihe um den Nullpunkt.
*expr_i* ist typischerweise ein Polynom in der Variablen *x_i* oder eine
Summe.  `deftaylor` akzeptiert aber auch allgemeinere Ausdrucke.


`powerseries(f_i(x_i), x_i, 0)` gibt die Reihe zuruck, 
die mit `deftaylor` definiert wurde.


`deftaylor` gibt eine Liste der Funktionen *f_1*, ..., *f_n* 
zuruck.  `deftaylor` wertet die Argumente aus.


Siehe auch `taylor` und `powerseries`.


Beispiele:



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

See also: `taylor`, `powerseries`.

<!-- category: Series -->
<!-- keywords: genindex -->
<!-- signatures: genindex -->
### Variable: genindex

Standardwert: `i`


`genindex` enthalt das Zeichen fur den Prafix, der verwendet wird, um
einen neuen Index fur eine Summe oder ein Produkt zu generieren.  Siehe auch
`gensumnum`.

See also: `gensumnum`.

<!-- category: Series -->
<!-- keywords: gensumnum -->
<!-- signatures: gensumnum -->
### Variable: gensumnum

Standardwert: 0


`gensumnum` enthalt die Nummer, die an den Prafix `genindex`
angehangt wird, um den nachsten Index fur eine Summe oder ein Produkt zu 
generieren.  Hat `gensumnum` den Wert `false`, wird der Index nur aus 
dem Zeichen `genindex` gebildet.  Siehe auch `genindex`.

See also: `genindex`.

<!-- category: Series -->
<!-- keywords: intopois -->
<!-- signatures: intopois(a) -->
### Function: intopois (a)

Converts *a* into a Poisson encoding.

<!-- category: Series -->
<!-- keywords: intosum -->
<!-- signatures: intosum(expr) -->
### Function: intosum (expr)

Multipliziert Faktoren in eine Summe herein.  Tritt der Index der Summe als ein
Faktor außerhalb der Summe auf, wird von der Funktion `intosum` ein 
neuer Index gebildet.  Summen haben die Eigenschaft `outative`, so dass 
Faktoren bei der Vereinfachung aus der Summe herausgezogen werden.  Mit der
Funktion `intosum` wird diese Vereinfachung ruckgangig gemacht.


Beispiel:



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

See also: `outative`.

<!-- category: Series -->
<!-- keywords: lsum -->
<!-- signatures: lsum(expr, i, L) -->
### Function: lsum (expr, i, L)

Bildet die Summe fur den Ausdruck *expr* zum Index *i* fur alle 
Elemente der Liste *L*.  Kann das Argument *L* nicht zu einer Liste 
ausgewertet werden, wird eine Substantivform zuruckgegeben.  Siehe auch
`sum`.


Beispiele:



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

See also: `sum`.

<!-- category: Series -->
<!-- keywords: maxtayorder -->
<!-- signatures: maxtayorder -->
### Variable: maxtayorder

Standardwert: `true`


Hat `maxtayorder` den Wert `true`, werden bei der algebraischen
Manipulation von Taylor-Reihen, von der Funktion `taylor` so viele
Terme wie moglich mitgefuhrt.

See also: `taylor`.

<!-- category: Series -->
<!-- keywords: niceindices -->
<!-- signatures: niceindices(expr) -->
### Function: niceindices (expr)

Gibt den Indizes von Summen und Produkten im Ausdruck *expr* einen neuen
Namen.  `niceindices` benennt die Indizes nacheinander mit den Namen, die
in der Liste der Optionsvariablen `niceindicespref` enthalten sind.  Die 
Standardnamen sind `[i, j, k, l, m, n]`.  Sind nicht genugend Namen in 
der Liste vorhanden, werden weitere Indizes durch das Anhangen einer Nummer
gebildet.


`niceindices` wertet das Argument aus.


Beispiele:



```maxima
(%i1) product (sum (f (foo + i*j*bar), foo, 1, inf), bar, 1, inf);
                 inf    inf
                /===\   ====
                 ! !    \
(%o1)            ! !     >      f(bar i j + foo)
                 ! !    /
                bar = 1 ====
                        foo = 1


(%i2) niceindices (%);
                     inf  inf
                    /===\ ====
                     ! !  \
(%o2)                ! !   >    f(i j l + k)
                     ! !  /
                    l = 1 ====
                          k = 1
```

See also: `niceindicespref`.

<!-- category: Series -->
<!-- keywords: niceindicespref -->
<!-- signatures: niceindicespref -->
### Variable: niceindicespref

Standardwert: `[i, j, k, l, m, n]`


`niceindicespref` ist die Liste mit den Namen, die die Funktion 
`niceindices` nutzt, um die Indizes von Summen und Produkte umzubenennen.


Beispiele:



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

See also: `niceindices`.

<!-- category: Series -->
<!-- keywords: nusum -->
<!-- signatures: nusum(expr, i, i_0, i_1) -->
### Function: nusum (expr, i, i_0, i_1)

Wendet den Gosper-Algorithmus der unbestimmten Summation fur den Ausdruck 
*expr* und dem Index *i* an.  Der Index *i* lauft von *i_0* 
bis *i_1*.  Der Ausdruck *expr* und das Ergebnis der Summation mussen 
als Produkte von ganzzahligen Exponentiationen, Fakultaten, Binomialen und
rationalen Funktionen darstellbar sein.


Die Funktionen `nusum` und `unsum` wenden einige Regeln fur die
Vereinfachung von Summen und Differenzen von endlichen Produkten an.  Siehe 
auch `unsum`.


Beispiele:



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

See also: `unsum`.

<!-- category: Series -->
<!-- keywords: outofpois -->
<!-- signatures: outofpois(a) -->
### Function: outofpois (a)

Converts *a* from Poisson encoding to general representation.  If *a* 
is not in Poisson form, `outofpois` carries out the conversion, i.e., 
the return value is `outofpois (intopois (a))`. This function is 
thus a canonical simplifier for sums of powers of sine and cosine terms of a 
particular type.

<!-- category: Series -->
<!-- keywords: pade -->
<!-- signatures: pade(taylor_series, numer_deg_bound, denom_deg_bound) -->
### Function: pade (taylor_series, numer_deg_bound, denom_deg_bound)

Gibt eine Liste aller rationalen Funktionen zuruck, die die angegebene
Taylor-Reihenentwicklung haben und deren Summe des Nennergrads und des
Zahlergrads kleiner oder gleich des Grads der Reihenentwicklung ist.


Das Argument *taylor_series* ist eine Taylor-Reihe in einer Variablen.
Die Argumente *numer_deg_bound* und *denom_deg_bound* sind positive
ganze Zahlen, die eine Grenze fur den Nennergrad und den Zahlergrad der
rationalen Funktion angeben.


Die Taylor-Reihe kann auch eine Laurent-Reihe sein und die Grenzen fur den 
Grad konnen `inf` sein.


Siehe auch `taylor`.


Beispiele:



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


Es gibt keine rationale Funktion des Grads 4 im Zahler und Nenner fur die
oben angegebene Taylor-Reihenentwicklung.  Die Summe des Zahlergrads und des 
Nennergrads mussen mindestens gleich dem Grad der Reihenentwicklung sein.
In diesem Fall ist der Grad der Taylor-Reihenentwicklung `10`.



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

See also: `taylor`.

<!-- category: Series -->
<!-- keywords: poisdiff -->
<!-- signatures: poisdiff(a, b) -->
### Function: poisdiff (a, b)

Differentiates *a* with respect to *b*. *b* must occur only
in the trig arguments or only in the coefficients.

<!-- category: Series -->
<!-- keywords: poisexpt -->
<!-- signatures: poisexpt(a, b) -->
### Function: poisexpt (a, b)

Functionally identical to `intopois (a^b)`. *b* must be a
positive integer.

<!-- category: Series -->
<!-- keywords: poisint -->
<!-- signatures: poisint(a, b) -->
### Function: poisint (a, b)

Integrates in a similarly restricted sense (to `poisdiff`).  Non-periodic 
terms in *b* are dropped if *b* is in the trig arguments.

<!-- category: Series -->
<!-- keywords: poislim -->
<!-- signatures: poislim -->
### Variable: poislim

Default value: 5


`poislim` determines the domain of the coefficients in the arguments of 
the trig functions.  The initial value of 5 corresponds to the interval 
[-2^(5-1)+1,2^(5-1)], or [-15,16], but it can be set to [-2^(n-1)+1, 2^(n-1)].

<!-- category: Series -->
<!-- keywords: poismap -->
<!-- signatures: poismap(series, sinfn, cosfn) -->
### Function: poismap (series, sinfn, cosfn)

will map the functions *sinfn* on the sine terms and *cosfn* on the 
cosine terms of the Poisson series given. *sinfn* and *cosfn* are 
functions of two arguments which are a coefficient and a trigonometric part 
of a term in series respectively.

<!-- category: Series -->
<!-- keywords: poisplus -->
<!-- signatures: poisplus(a, b) -->
### Function: poisplus (a, b)

Is functionally identical to `intopois (a + b)`.

<!-- category: Series -->
<!-- keywords: poissimp -->
<!-- signatures: poissimp(a) -->
### Function: poissimp (a)

Converts *a* into a Poisson series for *a* in general representation.

<!-- category: Series -->
<!-- keywords: poisson -->
<!-- signatures: poisson -->
### Variable: poisson

The symbol `/P/` follows the line label of Poisson series expressions.

<!-- category: Series -->
<!-- keywords: poissubst -->
<!-- signatures: poissubst(a, b, c) -->
### Function: poissubst (a, b, c)

Substitutes *a* for *b* in *c*.  *c* is a Poisson series.


(1) Where *B* is a variable *u*, *v*, *w*, *x*, *y*, or 
*z*, then *a* must be an expression linear in those variables (e.g., 
`6*u + 4*v`).


(2) Where *b* is other than those variables, then *a* must also be
free of those variables, and furthermore, free of sines or cosines.


`poissubst (a, b, c, d, n)` is a special 
type of substitution which operates on *a* and *b* as in type (1) above,
but where *d* is a Poisson series, expands `cos(d)` and 
`sin(d)` to order *n* so as to provide the result of substituting
`a + d` for *b* in *c*.  The idea is that *d* is an
expansion in terms of a small parameter.  For example,
`poissubst (u, v, cos(v), %e, 3)` yields `cos(u)*(1 - %e^2/2) - sin(u)*(%e - %e^3/6)`.

<!-- category: Series -->
<!-- keywords: poistimes -->
<!-- signatures: poistimes(a, b) -->
### Function: poistimes (a, b)

Is functionally identical to `intopois (a*b)`.

<!-- category: Series -->
<!-- keywords: poistrim -->
<!-- signatures: poistrim() -->
### Function: poistrim ()

is a reserved function name which (if the user has defined it) gets applied 
during Poisson multiplication.  It is a predicate function of 6 arguments which 
are the coefficients of the *u*, *v*, ..., *z* in a term.  Terms
for which `poistrim` is `true` (for the coefficients of that term) 
are eliminated during multiplication.

<!-- category: Series -->
<!-- keywords: powerseries -->
<!-- signatures: powerseries(expr, x, a) -->
### Function: powerseries (expr, x, a)

Gibt eine geschlossene Form fur die Reihenentwicklung des Ausdrucks *expr*
in der Variablen *x* um den Punkt *a* zuruck.  Das Argument *a* 
kann die Werte `inf` oder `infinity` haben.  Die Reihenentwicklung 
fur eine Funktion `f(x)` hat die allgemeine Form:


```maxima
inf
                  ====
                  \               n
       f(x) =      >    b  (x - a)
                  /      n
                  ====
                  n = 0
```


$$
f\left(x\right)=\sum_{n=0}^{\infty }{b_{n}\,\left(x-a\right)^{n}}
$$


Mit den Koeffzienten:


```maxima
!
            d        !
            -- (f(x))!
            dn       !
                     !x = a
       b  = ---------------
        n         n!
```


$$
b_{n}={{\left.{{d}\over{d\,n}}\,f\left(x\right)\right|_{x=a}}\over{n!}}
$$


Kann die Funktion `powerseries` keine Reihenentwicklung fur den Ausdruck
*expr* finden, konnen moglicherweise mit der Funktion `taylor` die
ersten Terme der Reihenentwicklung berechnet werden.


Hat die Optionsvariable `verbose` den Wert `true`, werden Meldungen
zu den verwendeten Algorithmen von der Funktion `powerseries` angezeigt.


Beispiel:



```maxima
(%i1) verbose: true$

(%i2) powerseries (log(sin(x)/x), x, 0);
trigreduce: can't expand                            
                 log(sin(x))

trigreduce: try again after applying the rule:
                                 d
                               / -- (sin(x))
                               [ dx
                 log(sin(x)) = I ----------- dx
                               ]   sin(x)
                               /


powerseries: first simplification returned

                                /
                                [
                     - log(x) + I cot(x) dx
                                ]
                                /


           inf
           ====        i1  - 1 + 2 i1             2 i1
           \      (- 1)   2           bern(2 i1) x
(%o2)       >     ------------------------------------
           /                   i1 (2 i1)!
           ====
           i1 = 1
```

See also: `taylor`, `verbose`.

<!-- category: Series -->
<!-- keywords: printpois -->
<!-- signatures: printpois(a) -->
### Function: printpois (a)

Prints a Poisson series in a readable format.  In common with `outofpois`, 
it will convert *a* into a Poisson encoding first, if necessary.

<!-- category: Series -->
<!-- keywords: product -->
<!-- signatures: product(expr, i, i_0, i_1) -->
### Function: product (expr, i, i_0, i_1)

Bildet das Produkt des Ausdrucks *expr* zum Index *i* in den Grenzen
*i_0* bis *i_1*.  `product` wertet *expr* sowie die untere 
Grenze *i_0* und obere Grenze *i_1* aus.  Der Index *i* wird nicht 
ausgewertet.


Ist die Differenz der oberen und unteren Grenze eine ganze Zahl, wird *expr*
fur jeden Wert des Index *i* ausgewertet.  Das Ergebnis ist ein explizites
Produkt.  Andernfalls ist der Bereich des Index unbestimmt.  Maxima wendet 
einige einfache Regeln an, um das Produkt zu vereinfachen.  Hat die 
Optionsvariable `simpproduct` den Wert `true`, wendet Maxima weitere 
Regeln an, um Produkte zu vereinfachen.


Siehe auch `nouns` und `evflag` fur die Auswertung von Ausdrucken,
die die Substantivform eines Produktes enthalten.


Beispiele:



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

See also: `simpproduct`, `nouns`, `evflag`.

<!-- category: Series -->
<!-- keywords: psexpand -->
<!-- signatures: psexpand -->
### Variable: psexpand

Default value: `false`




When `psexpand` is `true`,
an extended rational function expression is displayed fully expanded.
The switch `ratexpand` has the same effect.



When `psexpand` is `false`,
a multivariate expression is displayed just as in the rational function package.



When `psexpand` is  `multi`,
then terms with the same total degree in the variables are grouped together.

<!-- category: Series -->
<!-- keywords: revert, revert2 -->
<!-- signatures: revert(expr, x), revert2(expr, x, n) -->
### Function: revert (expr, x)

Die Funktion `revert` berechnet eine Taylorreihe in der Variablen *x*
um den Entwicklungspunkt Null, die der Taylorreihe der inversen Funktion 
entspricht, die von der Taylorreihe *expr* reprasentiert wird.  Das
Ergebnis ist ein Polynom in einer CRE-Darstellung mit dem Grad der hochsten
Potenz im Ausdruck *expr*.


Die Funktion `revert2` entspricht der Funktion `revert` mit dem
Unterschied, dass mit dem dritten Argument *n* der Grad der neuen
Taylorreihe explizit angegeben werden kann.  Dieser kann kleiner oder
großer als der Grad der Taylorreihe *expr* sein.


Mit dem Kommando `load("revert")` werden die Funktionen geladen.


Siehe auch die Funktion `taylor`.


Beispiel:


Die Inverse der Funktion `exp(x) - 1` ist die Funktion `log(x+1)`.
Mit dem Kommando `revert(taylor(exp(x) - 1, x, 0, 6), x)` wird die
Taylorreihe der Inversen `log(x+1)` berechnet.



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

See also: `taylor`.

<!-- category: Series -->
<!-- keywords: simpproduct -->
<!-- signatures: simpproduct -->
### Variable: simpproduct

Standardwert: `false`


Hat `simpproduct` den Wert `true`, versucht Maxima ein Produkt weiter 
zu vereinfachen.  Die Vereinfachung kann eine geschlossene Form liefern.  Hat
`simpproduct` den Wert `false` oder wird das Produkt als
Substantivform `'product` definiert, werden nur einige einfache Regeln von
Maxima fur die Vereinfachung angewendet.  `simpproduct` ist auch ein
Auswertungsschalter.  Siehe `evflag`.


Siehe auch `product` fur ein Beispiel.

See also: `evflag`, `product`.

<!-- category: Series -->
<!-- keywords: simpsum -->
<!-- signatures: simpsum -->
### Variable: simpsum

Standardwert: `false`


Hat `simpsum` den Wert `true`, versucht Maxima eine Summe oder Reihe 
weiter zu vereinfachen.  Die Vereinfachung kann eine geschlossene Form liefern.
Hat `simpsum` den Wert `false` oder die Summe oder Reihe liegt als
Substantivform `'sum` vor, werden nur einige einfache Regeln von Maxima 
fur die Vereinfachung angewendet.  `simpsum` ist auch ein
Auswertungsschalter.  Siehe `evflag`.


Siehe auch `sum` fur ein Beispiel.

See also: `evflag`, `sum`.

<!-- category: Series -->
<!-- keywords: sum -->
<!-- signatures: sum(expr, i, i_0, i_1) -->
### Function: sum (expr, i, i_0, i_1)

Bildet die Summe des Ausdrucks *expr* zum Index *i* in den Grenzen
*i_0* bis *i_1*.  Die Funktion `sum` wertet *expr* sowie die 
untere Grenze *i_0* und obere Grenze *i_1* aus.  Der Index *i* wird 
nicht ausgewertet.


Ist die Differenz der oberen und unteren Grenze eine ganze Zahl, wird *expr*
fur jeden Wert des Index *i* ausgewertet.  Das Ergebnis ist eine explizite
Summe.  Andernfalls ist der Bereich des Index unbestimmt.  Maxima wendet einige 
einfache Regeln an, um die Summe zu vereinfachen.  Hat die Optionsvariable 
`simpsum` den Wert `true`, wendet Maxima weitere Regeln an, um Summen
zu vereinfachen.


Werden zwei unendliche Reihen miteinander multipliziert und die Optionsvariablen
`sumexpand` sowie `cauchysum` haben beide den Wert `true`, dann 
wird die Cauchy-Produktformel angewendet.


Die Optionsvariable `genindex` enthalt das Zeichen, das der Prafix 
eines automatisch generierten Index ist.  `gensumnum` enthalt eine ganze 
Zahl, die an den Prafix `genindex` angehangt wird, um einen 
automatischen Index zu generieren.  `gensumnum` wird von Maxima automatisch
erhoht.  Hat `gensumnum` den Wert `false`, wird keine Zahl an den 
Prafix angehangt.


Das Paket `simplify_sum` enthalt die Funktion 
`simplify_sum`, mit der Summen zu einer geschlossenen Form vereinfacht
werden konnen.


Es ist zu beachten, dass `sum` bei symbolischen Summen, die viele Terme
ergeben, langsam ist, z. B. `sum(x^i, i, 1, 10000)`. In solchen Fallen
ist die Verwendung von `makelist` und `tree_reduce` signifikant
schneller, z. B. `tree_reduce("+", makelist(x^i, i, 1, 10000))`.


Siehe auch `sumcontract`,  `sumexpand`,
`intosum`, `bashindices`, `niceindices`,
`cauchysum` und `zeilberger`.


Beispiele:



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
(%i12) sum (if k <= 5 then a^k else b^k, k, 1, 10);
          10    9    8    7    6    5    4    3    2
(%o12)   b   + b  + b  + b  + b  + a  + a  + a  + a  + a
```

See also: `simpsum`, `sumexpand`, `cauchysum`, `genindex`, `gensumnum`, `simplify_sum`, `sumcontract`, `intosum`, `bashindices`, `niceindices`, `zeilberger`.

<!-- category: Series -->
<!-- keywords: sumcontract -->
<!-- signatures: sumcontract(expr) -->
### Function: sumcontract (expr)

Fasst alle Summen in dem Ausdruck *expr* zusammen, die sich in ihrem oberen
und unterem Index nur um eine Konstante voneinander unterscheiden.  Das Ergebnis
ist eine Ausdruck mit einer Summe, fur die Summen, die zusammengefasst werden 
konnen und weiteren Termen, die hinzu addiert werden mussen, um einen
aquivalenten Ausdruck zu erhalten.


Es kann notwendig sein zunachst das Kommando `intosum(expr)` 
auszufuhren.  Siehe `intosum`.


Beispiel:



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

See also: `intosum`.

<!-- category: Series -->
<!-- keywords: sumexpand -->
<!-- signatures: sumexpand -->
### Variable: sumexpand

Standardwert: `false`


Hat die Optionsvariable `sumexpand` den Wert `true`, werden Produkte
von Summen und Potenzen von Summen zu verschachtelten Summen vereinfacht.  Siehe
auch `cauchysum`.


Beispiele:



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

See also: `cauchysum`.

<!-- category: Series -->
<!-- keywords: taylor -->
<!-- signatures: taylor(expr, x, a, n), taylor(expr, [x_1, x_2, ...], a, n), taylor(expr, [x, a, n, 'asymp]), taylor(expr, [x_1, x_2, ...], [a_1, a_2, ...], [n_1, n_2, ...]), taylor(expr, [x_1, a_1, n_1], [x_2, a_2, n_2], ...) -->
### Function: taylor (expr, x, a, n)

`taylor(expr, x, a, n)` entwickelt den Ausdruck
*expr* in eine Taylor- oder Laurent-Reihenwicklung in der Variablen *x*
um den Punkt *a*, die die Terme bis zur Ordnung `(x - a)^n` enthalt.


Hat der Ausdruck *expr* die Form `f(x)/g(x)`
und hat `g(x)` keine Terme bis zur Ordnung *n*, dann 
versucht `taylor` den Ausdruck `g(x)` bis zur Ordnung
`2 n` zu entwickeln.  Treten in der Entwicklung weiterhin keine
von Null verschiedenen Terme auf, verdoppelt `taylor` die Ordnung der
Entwicklung fur `g(x)` so lange, wie die Ordnung kleiner 
oder gleich `n 2^taylordepth` ist.  Siehe auch `taylordepth`.


`taylor(expr, [x_1, x_2, ...], a, n)` gibt
die Reihenentwicklung der Ordnung *n* in allen Variablen *x_1*,
*x_2*, ... um den Punkt *a* zuruck.


Die beiden folgenden aquivalenten Kommandos `taylor(expr, [x_1, a_1, n_1], [x_2, a_2, n_2], ...)` und 
`taylor(expr, [x_1, x_2, ...], [a_1, a_2, ...], [n_1, n_2, ...])` geben eine Reihenentwicklung 
fur die Variablen *x_1*, *x_2*, ... um den Punkt `(a_1, a_2, ...)` mit den Ordnungen *n_1*, *n_2*, ... zuruck.


`taylor(expr, [x, a, n, 'asymp])` entwickelt den 
Ausdruck *expr* in negativen Potenzen von `x - a`.  Der
Term mit der großten Ordnung ist `(x - a)^-n`.


Folgende Optionsvariablen kontrollieren die Berechnung einer Taylorreihe:



**maxtayorder** — Hat `maxtayorder` den Wert `true`, werden bei der algebraischen
Manipulation von Taylor-Reihen, von der Funktion `taylor` so viele
Terme wie moglich mitgefuhrt.
**taylordepth** — Findet `taylor` keine von Null verschiedenen Terme in der
Reihenentwicklung, wird die Ordnung der Entwicklung solange erhoht wie sie
kleiner oder gleich `2^taylordepth` ist.
**taylor_logexpand** — Die Optionsvariable `taylor_logexpand` kontrolliert die Entwicklung von
Logarithmusfunktionen, die bei der Reihenentwicklung auftreten.  Der 
Standardwert ist `true` und die Logarithmusfunktionen in einer 
Reihenentwicklung werden vollstandig entwickelt.
**taylor_order_coefficients** — Die Optionsvariable `taylor_order_coefficients` kontrolliert die Anordung
von Termen in einer Reihenentwicklung.  Der Standardwert ist `true` und
die Anordung entspricht der kanonischen Darstellung eines Ausdrucks.
**taylor_truncate_polynomials** — Hat die Optionsvariable `taylor_truncate_polynomials` den Wert
`false`, wird das Ergebnis der Reihenentwicklung eines Polynoms als exakt
angenommen.
**taylor_simplifier** — Die Funktion zur Vereinfachung der Koeffizienten einer Entwicklung ist in der Optionsvariablen `taylor_simplifier` enthalten.  Der Standardwert ist
`simplify`.  Der Variablen kann eine nutzerdefinierte Funktion zugewiesen
werden.











Mit der Funktion `taylorp` kann getestet werden, ob ein Ausdruck eine
Taylorreihe reprasentiert.  Die Funktion `taylorinfo` gibt Informationen
zu einer Taylorreihe aus.  Die spezielle CRE-Form einer Taylorreihe wird mit der
Funktion `taytorat` in eine Standardform gebracht. 
Mit den Funktionen `revert` und `revert2` kann die Taylorreihe einer
inversen Funktion berechnet werden.


Beispiele:



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

See also: `taylordepth`, `maxtayorder`, `taylor_logexpand`, `taylor_order_coefficients`, `taylor_truncate_polynomials`, `taylor_simplifier`, `taylorp`, `taylorinfo`, `taytorat`, `revert`, `revert2`.

<!-- category: Series -->
<!-- keywords: taylor_logexpand -->
<!-- signatures: taylor_logexpand -->
### Variable: taylor_logexpand

Standardwert: `true`













`taylor_logexpand` kontrolliert die Entwicklung von Logarithmen in einer
Taylorreihe.  Der Standardwert ist `true` und die Logarithmusfunktionen in
einer Reihenentwicklung werden vollstandig entwickelt.  Ansonsten werden
Logarithmusfunktionen so weit entwickelt, wie es notwendig ist, um eine formale
Reihenentwicklung zu erhalten.

<!-- category: Series -->
<!-- keywords: taylor_order_coefficients -->
<!-- signatures: taylor_order_coefficients -->
### Variable: taylor_order_coefficients

Standardwert: `true`









Die Optionsvariable `taylor_order_coefficients` kontrolliert die Ordnung
der Koeffizienten einer Taylorreihenentwicklung.
Hat `taylor_order_coefficients` den Wert `true`, werden die
Koeffizienten kanonisch angeordnet.

<!-- category: Series -->
<!-- keywords: taylor_simplifier -->
<!-- signatures: taylor_simplifier -->
### Variable: taylor_simplifier

Standardwert: `SIMPLIFY`






Die Optionsvariable `taylor_simplifier` enthalt den Namen der Funktion,
die fur die Vereinfachung der Koeffizienten einer Taylorreihenentwicklung
von `taylor` aufgerufen wird.  Der Standardwert ist die Lisp-Funktion
`SIMPLIFY`.

See also: `taylor`.

<!-- category: Series -->
<!-- keywords: taylor_truncate_polynomials -->
<!-- signatures: taylor_truncate_polynomials -->
### Variable: taylor_truncate_polynomials

Standardwert: `true`










Hat die Optionsvariable `taylor_truncate_polynomials` den Wert
`false`, wird das Ergebnis der Reihenentwicklung eines Polynoms als exakt
angenommen.


Beispiel:



```maxima
(%i1) taylor(x^6+x^4+x^2,x,0,4),taylor_truncate_polynomials:true;
                          2    4
(%o1)/T/                 x  + x  + . . .
(%i2) taylor(x^6+x^4+x^2,x,0,4),taylor_truncate_polynomials:false;
                              2    4
(%o2)/T/                     x  + x
```

<!-- category: Series -->
<!-- keywords: taylordepth -->
<!-- signatures: taylordepth -->
### Variable: taylordepth

Standardwert: 3


Findet die Funktion `taylor` keine von Null verschiedenen Terme in der
Reihenentwicklung, wird die Ordnung der Entwicklung solange erhoht wie sie
kleiner oder gleich `2^taylordepth` ist.


Siehe auch `taylor`.

See also: `taylor`.

<!-- category: Series -->
<!-- keywords: taylorinfo -->
<!-- signatures: taylorinfo(expr) -->
### Function: taylorinfo (expr)

Gibt Informationen uber die Taylorreihe *expr* zuruck.  Die Ruckgabe
ist eine Liste, die Listen mit den Namen der Variablen, den Entwicklungspunkten
und den Ordnungen der Entwicklung enthalten.


Ist *expr* keine Taylorreihe, ist die Ruckgabe `false`.


Beispiele:



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

Hat den Ruckgabewert `true`, wenn das Argument *expr* eine
Taylorreihe ist.  Ansonsten ist der Ruckgabewert `false`.

<!-- category: Series -->
<!-- keywords: taytorat -->
<!-- signatures: taytorat(expr) -->
### Function: taytorat (expr)

Konvertiert den Ausdruck *expr* von der speziellen Darstellung einer
Taylorreihenentwicklung in eine CRE-Form.


Beispiel:



```maxima
(%i1) taylor(atan(x),x,0,5);
                            3    5
                           x    x
(%o1)/T/               x - -- + -- + . . .
                           3    5
(%i2) taytorat(%);

                          5      3
                       3 x  - 5 x  + 15 x
(%o2)/R/               ------------------
                               15
```

<!-- category: Series -->
<!-- keywords: trunc -->
<!-- signatures: trunc(expr) -->
### Function: trunc (expr)

Die Ruckgabe der Funktion `trunc` ist ein Ausdruck, der das Argument
*expr* in der Ausgabe wie eine Taylorreihenentwicklung anzeigt.  Der
Ausdruck *expr* wird ansonsten nicht modifiziert.


Beispiel:



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

Gibt die erste Ruckwartsdifferenz `f(n) - f(n-1)` zuruck.  Siehe auch `nusum`.


Beispiele:



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

See also: `nusum`.

<!-- category: Series -->
<!-- keywords: verbose -->
<!-- signatures: verbose -->
### Variable: verbose

Standardwert: `false`


Hat die Optionsvariable `verbose` den Wert `true`, werden von der
Funktion `powerseries` Meldungen uber die verwendeten Algorithmen 
ausgegeben.

See also: `powerseries`.

