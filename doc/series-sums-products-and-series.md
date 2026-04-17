## Sums, Products, and Series

<!-- category: Series -->
<!-- keywords: absint -->
<!-- signatures: absint(f, x, halfplane), absint(f, x), absint(f, x, a, b) -->
### Function: absint (f, x, halfplane)

`absint (f, x, halfplane)`
returns the indefinite integral of *f* with respect to
*x* in the given halfplane (`pos`, `neg`, or `both`).
*f* may contain expressions of the form
`abs (x)`, `abs (sin (x))`, `abs (a) * exp (-abs (b) * abs (x))`.


`absint (f, x)` is equivalent to
`absint (f, x, pos)`.


`absint (f, x, a, b)` returns the definite integral
of *f* with respect to *x* from *a* to *b*.

*f* may include absolute values.

<!-- category: Series -->
<!-- keywords: bashindices -->
<!-- signatures: bashindices(expr) -->
### Function: bashindices (expr)

Transforms the expression *expr* by giving each summation and product a
unique index.  This gives `changevar` greater precision when it is working
with summations or products.  The form of the unique index is
`jnumber`. The quantity *number* is determined by referring to
`gensumnum`, which can be changed by the user.  For example,
`gensumnum:0$` resets it.

<!-- category: Series -->
<!-- keywords: cauchysum -->
<!-- signatures: cauchysum -->
### Variable: cauchysum

Default value: `false`



When multiplying together sums with `inf` as their upper limit,
if `sumexpand` is `true` and `cauchysum` is `true`
then the Cauchy product will be used rather than the usual
product.
In the Cauchy product the index of the inner summation is a
function of the index of the outer one rather than varying
independently.


Example:











```maxima
maxima
(%i1) sumexpand: false$
(%i2) cauchysum: false$

(%i3) s: sum (f(i), i, 0, inf) * sum (g(j), j, 0, inf);
                      inf         inf
                      ____        ____
                      \           \
(%o3)                ( >    f(i))  >    g(j)
                      /           /
                      ----        ----
                      i = 0       j = 0

(%i4) sumexpand: true$
(%i5) cauchysum: true$

(%i6) expand(s,0,0);
                 inf     i1
                 ____   ____
                 \      \
(%o6)             >      >     g(i1 - i2) f(i2)
                 /      /
                 ----   ----
                 i1 = 0 i2 = 0
```

<!-- category: Series -->
<!-- keywords: cosnpiflag -->
<!-- signatures: cosnpiflag -->
### Variable: cosnpiflag

Default value: `true`


See `foursimp`.

<!-- category: Series -->
<!-- keywords: deftaylor -->
<!-- signatures: deftaylor(f_1(x_1), expr_1, ..., f_n(x_n), expr_n) -->
### Function: deftaylor (f_1(x_1), expr_1, ..., f_n(x_n), expr_n)

For each function *f_i* of one variable *x_i*, 
`deftaylor` defines *expr_i* as the Taylor series about zero.
*expr_i* is typically a polynomial in *x_i* or a summation;
more general expressions are accepted by `deftaylor` without complaint.


`powerseries (f_i(x_i), x_i, 0)`
returns the series defined by `deftaylor`.


`deftaylor` returns a list of the functions *f_1*, ..., *f_n*.
`deftaylor` evaluates its arguments.


Example:








```maxima
maxima

(%i1) deftaylor (f(x), x^2 + sum(x^i/(2^i*i!^2), i, 4, inf));
(%o1)                          [f]


(%i2) powerseries (f(x), x, 0);
                      inf
                      ____      i1
                      \        x         2
(%o2)                  >     -------- + x
                      /       i1    2
                      ----   2   i1!
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

Returns `true` if `equal (x, y)` otherwise `false`
(doesn’t give an error message like `equal (x, y)` would do in this case).

<!-- category: Series -->
<!-- keywords: fourcos -->
<!-- signatures: fourcos(f, x, p) -->
### Function: fourcos (f, x, p)

Returns the Fourier cosine coefficients for `f(x)` defined on
`[0, p]`.

<!-- category: Series -->
<!-- keywords: fourexpand -->
<!-- signatures: fourexpand(l, x, p, limit) -->
### Function: fourexpand (l, x, p, limit)

Constructs and returns the Fourier series from the list of Fourier coefficients
*l* up through *limit* terms (*limit* may be `inf`).  *x*
and *p* have same meaning as in `fourier`.

<!-- category: Series -->
<!-- keywords: fourier -->
<!-- signatures: fourier(f, x, p) -->
### Function: fourier (f, x, p)

Returns a list of the Fourier coefficients of `f(x)` defined
on the interval `[-p, p]`.

<!-- category: Series -->
<!-- keywords: fourint -->
<!-- signatures: fourint(f, x) -->
### Function: fourint (f, x)

Constructs and returns a list of the Fourier integral coefficients of
`f(x)` defined on `[minf, inf]`.

<!-- category: Series -->
<!-- keywords: fourintcos -->
<!-- signatures: fourintcos(f, x) -->
### Function: fourintcos (f, x)

Returns the Fourier cosine integral coefficients for `f(x)`
on `[0, inf]`.

<!-- category: Series -->
<!-- keywords: fourintsin -->
<!-- signatures: fourintsin(f, x) -->
### Function: fourintsin (f, x)

Returns the Fourier sine integral coefficients for `f(x)` on
`[0, inf]`.

<!-- category: Series -->
<!-- keywords: foursimp -->
<!-- signatures: foursimp(l) -->
### Function: foursimp (l)

Simplifies `sin (n %pi)` to 0 if `sinnpiflag` is `true` and
`cos (n %pi)` to `(-1)^n` if `cosnpiflag` is `true`.

<!-- category: Series -->
<!-- keywords: foursin -->
<!-- signatures: foursin(f, x, p) -->
### Function: foursin (f, x, p)

Returns the Fourier sine coefficients for `f(x)` defined on
`[0, p]`.

<!-- category: Series -->
<!-- keywords: funp -->
<!-- signatures: funp(f, expr), funp(f, expr, x) -->
### Function: funp (f, expr)

`funp (f, expr)`
returns `true` if *expr* contains the function *f*.


`funp (f, expr, x)`
returns `true` if *expr* contains the function *f* and the variable
*x* is somewhere in the argument of one of the instances of *f*.

<!-- category: Series -->
<!-- keywords: intopois -->
<!-- signatures: intopois(a) -->
### Function: intopois (a)

Converts *a* into a Poisson encoding.

<!-- category: Series -->
<!-- keywords: intosum -->
<!-- signatures: intosum(expr) -->
### Function: intosum (expr)

Moves multiplicative factors outside a summation to inside.
If the index is used in the
outside expression, then the function tries to find a reasonable
index, the same as it does for `sumcontract`.  This is essentially the
reverse idea of the `outative` property of summations, but note that it
does not remove this property, it only bypasses it.



In some cases, a `scanmap (multthru, expr)` may be necessary before
the `intosum`.

<!-- category: Series -->
<!-- keywords: lsum -->
<!-- signatures: lsum(expr, x, L) -->
### Function: lsum (expr, x, L)

Represents the sum of *expr* for each element *x* in *L*.
A noun form `'lsum` is returned if the argument *L* does not evaluate
to a list.


Examples:







```maxima
maxima

(%i1) lsum (x^i, i, [1, 2, 7]);
                            7    2
(%o1)                      x  + x  + x


(%i2) lsum (i^2, i, rootsof (x^3 - 1, x));
                   ____
                   \                        2
(%o2)               >                      i
                   /
                   ----
                                 3
                   i in rootsof(x  - 1, x)
```

<!-- category: Series -->
<!-- keywords: maxtayorder -->
<!-- signatures: maxtayorder -->
### Variable: maxtayorder

Default value: `true`



When `maxtayorder` is `true`, then during algebraic
manipulation of (truncated) Taylor series, `taylor` tries to retain
as many terms as are known to be correct.

<!-- category: Series -->
<!-- keywords: niceindices -->
<!-- signatures: niceindices(expr) -->
### Function: niceindices (expr)

Renames the indices of sums and products in *expr*.  `niceindices`
attempts to rename each index to the value of `niceindicespref[1]`, unless
that name appears in the summand or multiplicand, in which case
`niceindices` tries the succeeding elements of `niceindicespref` in
turn, until an unused variable is found.  If the entire list is exhausted,
additional indices are constructed by appending integers to the value of
`niceindicespref[1]`, e.g., `i0`, `i1`, `i2`, ...


`niceindices` returns an expression.
`niceindices` evaluates its argument.


Example:








```maxima
maxima

(%i1) niceindicespref;
(%o1)                  [i, j, k, l, m, n]


(%i2) product (sum (f (foo + i*j*bar), foo, 1, inf), bar, 1, inf);
                 inf    inf
                _____   ____
                |   |   \
(%o2)           |   |    >      f(bar i j + foo)
                |   |   /
                bar = 1 ----
                        foo = 1


(%i3) niceindices (%);
                     inf  inf
                    _____ ____
                    |   | \
(%o3)               |   |  >    f(i j l + k)
                    |   | /
                    l = 1 ----
                          k = 1
```

<!-- category: Series -->
<!-- keywords: niceindicespref -->
<!-- signatures: niceindicespref -->
### Variable: niceindicespref

Default value: `[i, j, k, l, m, n]`


`niceindicespref` is the list from which `niceindices`
takes the names of indices for sums and products.


The elements of `niceindicespref` are must be names of simple variables.


Example:








```maxima
maxima
(%i1) niceindicespref: [p, q, r, s, t, u]$

(%i2) product (sum (f (foo + i*j*bar), foo, 1, inf), bar, 1, inf);
                 inf    inf
                _____   ____
                |   |   \
(%o2)           |   |    >      f(bar i j + foo)
                |   |   /
                bar = 1 ----
                        foo = 1


(%i3) niceindices (%);
                     inf  inf
                    _____ ____
                    |   | \
(%o3)               |   |  >    f(i j q + p)
                    |   | /
                    q = 1 ----
                          p = 1
```

<!-- category: Series -->
<!-- keywords: nusum -->
<!-- signatures: nusum(expr, x, i_0, i_1) -->
### Function: nusum (expr, x, i_0, i_1)

Carries out indefinite hypergeometric summation of *expr* with
respect to *x* using a decision procedure due to R.W. Gosper.
*expr* and the result must be expressible as products of integer powers,
factorials, binomials, and rational functions.




The terms "definite"
and "indefinite summation" are used analogously to "definite" and
"indefinite integration".
To sum indefinitely means to give a symbolic result
for the sum over intervals of variable length, not just e.g. 0 to
inf.  Thus, since there is no formula for the general partial sum of
the binomial series, `nusum` can’t do it.


`nusum` and `unsum` know a little about sums and differences of
finite products.  See also `unsum`.


Examples:










```maxima
maxima

(%i1) nusum (n*n!, n, 0, n);
solve: dependent equations eliminated: (1)
(%o1)                     (n + 1)! - 1


(%i2) nusum (n^4*4^n/binomial(2*n,n), n, 0, n);
         n              4        3       2
      2 4  (n + 1) (63 n  + 112 n  + 18 n  - 22 n + 3)    2
(%o2) ------------------------------------------------ - ---
                    693 binomial(2 n, n)                 231


(%i3) unsum (%, n);
                              n  4
                             4  n
(%o3)                   ----------------
                        binomial(2 n, n)


(%i4) unsum (prod (i^2, i, 1, n), n);
                    n - 1
                    _____
                    |   |  2
(%o4)              (|   | i ) (n - 1) (n + 1)
                    |   |
                    i = 1


(%i5) nusum (%, n, 1, n);
solve: dependent equations eliminated: (2 3)
                            n
                          _____
                          |   |  2
(%o5)                     |   | i  - 1
                          |   |
                          i = 1
```

See also: `unsum`.

<!-- category: Series -->
<!-- keywords: outofpois -->
<!-- signatures: outofpois(a) -->
### Function: outofpois (a)

Converts *a* from Poisson encoding to general representation.  If *a* is
not in Poisson form, `outofpois` carries out the conversion,
i.e., the return value is `outofpois (intopois (a))`.
This function is thus a canonical simplifier
for sums of powers of sine and cosine terms of a particular type.

<!-- category: Series -->
<!-- keywords: pade -->
<!-- signatures: pade(taylor_series, numer_deg_bound, denom_deg_bound) -->
### Function: pade (taylor_series, numer_deg_bound, denom_deg_bound)

Returns a list of
all rational functions which have the given Taylor series expansion
where the sum of the degrees of the numerator and the denominator is
less than or equal to the truncation level of the power series, i.e.
are "best" approximants, and which additionally satisfy the specified
degree bounds.


*taylor_series* is an univariate Taylor series.
*numer_deg_bound* and *denom_deg_bound*
are positive integers specifying degree bounds on
the numerator and denominator.


*taylor_series* can also be a Laurent series, and the degree
bounds can be `inf` which causes all rational functions whose total
degree is less than or equal to the length of the power series to be
returned.  Total degree is defined as `numer_deg_bound + denom_deg_bound`.
Length of a power series is defined as
`"truncation level" + 1 - min(0, "order of series")`.













```maxima
maxima

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


There is no rational function of degree 4 numerator/denominator, with this
power series expansion.  You must in general have degree of the numerator and
degree of the denominator adding up to at least the degree of the power series,
in order to have enough unknown coefficients to solve.



```maxima
maxima
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

Differentiates *a* with respect to *b*. *b* must occur only
in the trig arguments or only in the coefficients.

<!-- category: Series -->
<!-- keywords: poisexpt -->
<!-- signatures: poisexpt(a, b) -->
### Function: poisexpt (a, b)

Functionally identical to `intopois (a^b)`.
*b* must be a positive integer.

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


`poislim` determines the domain of the coefficients in
the arguments of the trig functions.  The initial value of 5
corresponds to the interval [-2^(5-1)+1,2^(5-1)], or [-15,16], but it
can be set to [-2^(n-1)+1, 2^(n-1)].

<!-- category: Series -->
<!-- keywords: poismap -->
<!-- signatures: poismap(series, sinfn, cosfn) -->
### Function: poismap (series, sinfn, cosfn)

will map the functions *sinfn* on the sine terms and *cosfn* on the
cosine terms of the Poisson series given.  *sinfn* and *cosfn* are
functions of two arguments which are a coefficient and a trigonometric part of
a term in series respectively.

<!-- category: Series -->
<!-- keywords: poisplus -->
<!-- signatures: poisplus(a, b) -->
### Function: poisplus (a, b)

Is functionally identical to `intopois (a + b)`.

<!-- category: Series -->
<!-- keywords: poissimp -->
<!-- signatures: poissimp(a) -->
### Function: poissimp (a)

Converts *a* into a Poisson series for *a* in general
representation.

<!-- category: Series -->
<!-- keywords: poisson -->
<!-- signatures: poisson -->
### Variable: poisson

The symbol `/P/` follows the line label of Poisson series
expressions.

<!-- category: Series -->
<!-- keywords: poissubst -->
<!-- signatures: poissubst(a, b, c) -->
### Function: poissubst (a, b, c)

Substitutes *a* for *b* in *c*.  *c* is a Poisson series.


(1) Where *B* is a variable *u*, *v*, *w*, *x*, *y*,
or *z*, then *a* must be an expression linear in those variables (e.g.,
`6*u + 4*v`).


(2) Where *b* is other than those variables, then *a* must also be
free of those variables, and furthermore, free of sines or cosines.


`poissubst (a, b, c, d, n)` is a special type
of substitution which operates on *a* and *b* as in type (1) above, but
where *d* is a Poisson series, expands `cos(d)` and
`sin(d)` to order *n* so as to provide the result of substituting
`a + d` for *b* in *c*.  The idea is that *d* is an
expansion in terms of a small parameter.  For example,
`poissubst (u, v, cos(v), %e, 3)` yields
`cos(u)*(1 - %e^2/2) - sin(u)*(%e - %e^3/6)`.

<!-- category: Series -->
<!-- keywords: poistimes -->
<!-- signatures: poistimes(a, b) -->
### Function: poistimes (a, b)

Is functionally identical to `intopois (a*b)`.

<!-- category: Series -->
<!-- keywords: poistrim -->
<!-- signatures: poistrim() -->
### Function: poistrim ()

is a reserved function name which (if the user has defined
it) gets applied during Poisson multiplication.  It is a predicate
function of 6 arguments which are the coefficients of the *u*, *v*, ..., *z*
in a term.  Terms for which `poistrim` is `true` (for the coefficients of
that term) are eliminated during multiplication.

<!-- category: Series -->
<!-- keywords: powerseries -->
<!-- signatures: powerseries(expr, x, a) -->
### Function: powerseries (expr, x, a)

Returns the general form of the power series expansion for *expr* in the 
variable *x* about the point *a* (which may be `inf` for infinity):


```maxima
inf
           ====
           \               n
            >    b  (x - a)
           /      n
           ====
           n = 0
```


If `powerseries` is unable to expand *expr*,
`taylor` may give the first several terms of the series.


When `verbose` is `true`,
`powerseries` prints progress messages.







```maxima
maxima
(%i1) verbose: true$

(%i2) powerseries (log(sin(x)/x), x, 0);
trigreduce: failed to expand.

                               sin(x)
                           log(------)
                                 x

trigreduce: try again after applying rule:
                                 d   sin(x)
                               / -- (------)
                     sin(x)    | dx    x
                 log(------) = | ----------- dx
                       x       |   sin(x)
                               /   ------
                                     x


powerseries: first simplification returned 
    x
   /
   |  csc(g3955) sin(g3955) - g3955 cos(g3955) csc(g3955)
 - |  --------------------------------------------------- dg3955
   |                         g3955
   /
    0


powerseries: first simplification returned 
                       g3955 cot(g3955) - 1
                     - --------------------
                              g3955

powerseries: attempt rational function expansion of
                                1
                              -----
                              g3955
            inf
            ____        i2  2 i2 - 1             2 i2
            \      (- 1)   2         bern(2 i2) x
(%o2)        >     ----------------------------------
            /                  i2 (2 i2)!
            ----
            i2 = 1
```

<!-- category: Series -->
<!-- keywords: printpois -->
<!-- signatures: printpois(a) -->
### Function: printpois (a)

Prints a Poisson series in a readable format.  In common
with `outofpois`, it will convert *a* into a Poisson encoding first, if
necessary.

<!-- category: Series -->
<!-- keywords: product -->
<!-- signatures: product(expr, i, i_0, i_1) -->
### Function: product (expr, i, i_0, i_1)

Represents a product of the values of *expr* as
the index *i* varies from *i_0* to *i_1*.
The noun form `'product` is displayed as an uppercase letter pi.


`product` evaluates *expr* and lower and upper limits *i_0* and
*i_1*, `product` quotes (does not evaluate) the index *i*.


If the upper and lower limits differ by an integer,
*expr* is evaluated for each value of the index *i*,
and the result is an explicit product.


Otherwise, the range of the index is indefinite.
Some rules are applied to simplify the product.
When the global variable `simpproduct` is `true`, additional rules
are applied.  In some cases, simplification yields a result which is not a
product; otherwise, the result is a noun form `'product`.


See also `nouns` and `evflag`.


Examples:














```maxima
maxima

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
                           _____
                           |   |
(%o5)                      |   | a(i)
                           |   |
                           i = 1


(%i6) product (k, k, 1, n);
                               n
                             _____
                             |   |
(%o6)                        |   | k
                             |   |
                             k = 1


(%i7) product (k, k, 1, n), simpproduct;
(%o7)                          n!


(%i8) product (integrate (x^k, x, 0, 1), k, 1, n);
                             n
                           _____
                           |   |   1
(%o8)                      |   | -----
                           |   | k + 1
                           k = 1


(%i9) product (if k <= 5 then a^k else b^k, k, 1, 10);
                              15  40
(%o9)                        a   b
```

See also: `nouns`, `evflag`.

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
<!-- keywords: remfun -->
<!-- signatures: remfun(f, expr), remfun(f, expr, x) -->
### Function: remfun (f, expr)

`remfun (f, expr)` replaces all occurrences of `f (arg)` by *arg* in *expr*.


`remfun (f, expr, x)` replaces all occurrences of
`f (arg)` by *arg* in *expr* only if *arg* contains
the variable *x*.

<!-- category: Series -->
<!-- keywords: revert, revert2 -->
<!-- signatures: revert(expr, x), revert2(expr, x, n) -->
### Function: revert (expr, x)

These functions return the reversion of *expr*, a Taylor series about zero
in the variable *x*.  `revert` returns a polynomial of degree equal to
the highest power in *expr*.  `revert2` returns a polynomial of degree
*n*, which may be greater than, equal to, or less than the degree of
*expr*.


`load ("revert")` loads these functions.


Examples:












```maxima
maxima
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
<!-- keywords: simpproduct -->
<!-- signatures: simpproduct -->
### Variable: simpproduct

Default value: `false`


When `simpproduct` is `true`, the result of a `product` is simplified.
This simplification may sometimes be able to produce a closed form.  If
`simpproduct` is `false` or if the quoted form `'product` is used, the
value is a product noun form which is a representation of the pi notation used
in mathematics.

<!-- category: Series -->
<!-- keywords: simpsum -->
<!-- signatures: simpsum -->
### Variable: simpsum

Default value: `false`


When `simpsum` is `true`, the result of a `sum` is simplified.
This simplification may sometimes be able to produce a closed form.  If
`simpsum` is `false` or if the quoted form `'sum` is used, the
value is a sum noun form which is a representation of the sigma notation used
in mathematics.

<!-- category: Series -->
<!-- keywords: sinnpiflag -->
<!-- signatures: sinnpiflag -->
### Variable: sinnpiflag

Default value: `true`


See `foursimp`.

<!-- category: Series -->
<!-- keywords: sum -->
<!-- signatures: sum(expr, i, i_0, i_1) -->
### Function: sum (expr, i, i_0, i_1)

Represents a summation of the values of *expr* as
the index *i* varies from *i_0* to *i_1*.
The noun form `'sum` is displayed as an uppercase letter sigma.


`sum` evaluates its summand *expr* and lower and upper limits *i_0*
and *i_1*, `sum` quotes (does not evaluate) the index *i*.


If the upper and lower limits differ by an integer, the summand *expr* is
evaluated for each value of the summation index *i*, and the result is an
explicit sum.


Otherwise, the range of the index is indefinite.
Some rules are applied to simplify the summation.
When the global variable `simpsum` is `true`, additional rules are
applied.  In some cases, simplification yields a result which is not a
summation; otherwise, the result is a noun form `'sum`.


When the `evflag` (evaluation flag) `cauchysum` is `true`,
a product of summations is expressed as a Cauchy product,
in which the index of the inner summation is a function of the
index of the outer one, rather than varying independently.


The global variable `genindex` is the alphabetic prefix used to generate
the next index of summation, when an automatically generated index is needed.


`gensumnum` is the numeric suffix used to generate the next index of
summation, when an automatically generated index is needed.
When `gensumnum` is `false`, an automatically-generated index is only
`genindex` with no numeric suffix.


Note that `sum` is slow for symbolic sums that result in many terms,
such as `sum(x^i, i, 1, 10000)`. For such cases, using `tree_reduce`
and `makelist` is significantly faster, e.g.
`tree_reduce("+", makelist(x^i, i, 1, 10000))`.


See also `lsum`, `sumcontract`, `intosum`,
`bashindices`, `niceindices`,
`nouns`, `evflag`, and `Package-zeilberger`


Examples:

















```maxima
maxima

(%i1) sum (i^2, i, 1, 7);
(%o1)                          140


(%i2) sum (a[i], i, 1, 7);
(%o2)           a  + a  + a  + a  + a  + a  + a
                 7    6    5    4    3    2    1


(%i3) sum (a(i), i, 1, 7);
(%o3)    a(7) + a(6) + a(5) + a(4) + a(3) + a(2) + a(1)


(%i4) sum (a(i), i, 1, n);
                            n
                           ____
                           \
(%o4)                       >    a(i)
                           /
                           ----
                           i = 1


(%i5) sum (2^i + i^2, i, 0, n);
                          n
                         ____
                         \       2    i
(%o5)                     >    (i  + 2 )
                         /
                         ----
                         i = 0


(%i6) sum (2^i + i^2, i, 0, n), simpsum;
                     3      2
                  2 n  + 3 n  + n    n + 1
(%o6)             --------------- + 2      - 1
                         6


(%i7) sum (1/3^i, i, 1, inf);
                            inf
                            ____
                            \     1
(%o7)                        >    --
                            /      i
                            ----  3
                            i = 1


(%i8) sum (1/3^i, i, 1, inf), simpsum;
                                1
(%o8)                           -
                                2


(%i9) sum (i^2, i, 1, 4) * sum (1/i^2, i, 1, inf);
                              inf
                              ____
                              \     1
(%o9)                      30  >    --
                              /      2
                              ----  i
                              i = 1


(%i10) sum (i^2, i, 1, 4) * sum (1/i^2, i, 1, inf), simpsum;
                                  2
(%o10)                       5 %pi


(%i11) sum (integrate (x^k, x, 0, 1), k, 1, n);
                            n
                           ____
                           \       1
(%o11)                      >    -----
                           /     k + 1
                           ----
                           k = 1


(%i12) sum (if k <= 5 then a^k else b^k, k, 1, 10);
          10    9    8    7    6    5    4    3    2
(%o12)   b   + b  + b  + b  + b  + a  + a  + a  + a  + a
```

See also: `lsum`, `sumcontract`, `intosum`, `bashindices`, `niceindices`, `nouns`, `evflag`, `Package-zeilberger`.

<!-- category: Series -->
<!-- keywords: sumcontract -->
<!-- signatures: sumcontract(expr) -->
### Function: sumcontract (expr)

Combines all sums of an addition that have
upper and lower bounds that differ by constants.  The result is an
expression containing one summation for each set of such summations
added to all appropriate extra terms that had to be extracted to form
this sum.  `sumcontract` combines all compatible sums and uses one of
the indices from one of the sums if it can, and then try to form a
reasonable index if it cannot use any supplied.



It may be necessary to do an `intosum (expr)` before the
`sumcontract`.

<!-- category: Series -->
<!-- keywords: sumexpand -->
<!-- signatures: sumexpand -->
### Variable: sumexpand

Default value: `false`


When `sumexpand` is `true`, products of sums and
exponentiated sums simplify to nested sums.


See also `cauchysum`.


Examples:








```maxima
maxima
(%i1) sumexpand: true$

(%i2) sum (f (i), i, 0, m) * sum (g (j), j, 0, n);
                     m      n
                    ____   ____
                    \      \
(%o2)                >      >     f(i1) g(i2)
                    /      /
                    ----   ----
                    i1 = 0 i2 = 0


(%i3) sum (f (i), i, 0, m)^2;
                     m      m
                    ____   ____
                    \      \
(%o3)                >      >     f(i3) f(i4)
                    /      /
                    ----   ----
                    i3 = 0 i4 = 0
```

See also: `cauchysum`.

<!-- category: Series -->
<!-- keywords: taylor -->
<!-- signatures: taylor(expr, x, a, n), taylor(expr, [x_1, x_2, ...], a, n), taylor(expr, [x, a, n, 'asymp]), taylor(expr, [x_1, x_2, ...], [a_1, a_2, ...], [n_1, n_2, ...]), taylor(expr, [x_1, a_1, n_1], [x_2, a_2, n_2], ...) -->
### Function: taylor (expr, x, a, n)

`taylor (expr, x, a, n)` expands the expression
*expr* in a truncated Taylor or Laurent series in the variable *x*
around the point *a*,
containing terms through `(x - a)^n`.


If *expr* is of the form `f(x)/g(x)` and
`g(x)` has no terms up to degree *n* then `taylor`
attempts to expand `g(x)` up to degree `2 n`.
If there are still no nonzero terms, `taylor` doubles the degree of the
expansion of `g(x)` so long as the degree of the expansion is
less than or equal to `n 2^taylordepth`.


`taylor (expr, [x_1, x_2, ...], a, n)`
returns a truncated power series 
of degree *n* in all variables *x_1*, *x_2*, ...
about the point `(a, a, ...)`.


`taylor (expr, [x_1, a_1, n_1], [x_2, a_2, n_2], ...)` returns a truncated power series in the variables
*x_1*, *x_2*, ... about the point
`(a_1, a_2, ...)`, truncated at *n_1*, *n_2*, ...


`taylor (expr, [x_1, x_2, ...], [a_1, a_2, ...], [n_1, n_2, ...])` returns a truncated power series
in the variables *x_1*, *x_2*, ... about the point
`(a_1, a_2, ...)`, truncated at *n_1*, *n_2*, ...


`taylor (expr, [x, a, n, 'asymp])` returns an
expansion of *expr* in negative powers of `x - a`.
The highest order term is `(x - a)^-n`.


When `maxtayorder` is `true`, then during algebraic
manipulation of (truncated) Taylor series, `taylor` tries to retain
as many terms as are known to be correct.


When `psexpand` is `true`,
an extended rational function expression is displayed fully expanded.
The switch `ratexpand` has the same effect.
When `psexpand` is `false`,
a multivariate expression is displayed just as in the rational function package.
When `psexpand` is  `multi`,
then terms with the same total degree in the variables are grouped together.


See also the `taylor_logexpand` switch for controlling expansion.


Examples:






















```maxima
maxima

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
                        _____
                        |   |   i     2.5
                        |   | (x  + 1)
                        |   |
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
              3                      2
             y                      y
(%o13)/T/ (- -- + y + . . .) + (1 - -- + . . .) x
             6                      2
                    3                       2
               y   y            2      1   y            3
          + (- - + -- + . . .) x  + (- - + -- + . . .) x  + . . .
               2   12                  6   12


(%i14) taylor (sin (y + x), [x, y], 0, 3);
                      3        2      2      3
                     x  + 3 y x  + 3 y  x + y
(%o14)/T/  (y + x) - ------------------------- + . . .
                                 6


(%i15) taylor (1/sin (y + x), x, 0, 3, y, 0, 3);
           y   1               1    1
(%o15)/T/ (- + - + . . .) + (- -- + - + . . .) x
           6   y                2   6
                               y
                       1            2      1            3
                    + (-- + . . .) x  + (- -- + . . .) x  + . . .
                        3                   4
                       y                   y


(%i16) taylor (1/sin (y + x), [x, y], 0, 3);
                             3         2       2        3
            1     x + y   7 x  + 21 y x  + 21 y  x + 7 y
(%o16)/T/ ----- + ----- + ------------------------------- + . . .
          x + y     6                   360
```

See also: `taylor_logexpand`.

<!-- category: Series -->
<!-- keywords: taylor_logexpand -->
<!-- signatures: taylor_logexpand -->
### Variable: taylor_logexpand

Default value: `true`


`taylor_logexpand` controls expansions of logarithms in
`taylor` series.


When `taylor_logexpand` is `true`, all logarithms are expanded fully
so that zero-recognition problems involving logarithmic identities do not
disturb the expansion process.  However, this scheme is not always
mathematically correct since it ignores branch information.


When `taylor_logexpand` is set to `false`, then the only expansion of
logarithms that occur is that necessary to obtain a formal power series.

<!-- category: Series -->
<!-- keywords: taylor_order_coefficients -->
<!-- signatures: taylor_order_coefficients -->
### Variable: taylor_order_coefficients

Default value: `true`


`taylor_order_coefficients` controls the ordering of
coefficients in a Taylor series.


When `taylor_order_coefficients` is `true`,
coefficients of taylor series are ordered canonically.

<!-- category: Series -->
<!-- keywords: taylor_simplifier -->
<!-- signatures: taylor_simplifier(expr) -->
### Function: taylor_simplifier (expr)

Simplifies coefficients of the power series *expr*.
`taylor` calls this function.

<!-- category: Series -->
<!-- keywords: taylor_truncate_polynomials -->
<!-- signatures: taylor_truncate_polynomials -->
### Variable: taylor_truncate_polynomials

Default value: `true`



When `taylor_truncate_polynomials` is `true`,
polynomials are truncated based upon the input truncation levels.


Otherwise,
polynomials input to `taylor` are considered to have infinite precision.

<!-- category: Series -->
<!-- keywords: taylordepth -->
<!-- signatures: taylordepth -->
### Variable: taylordepth

Default value: 3



If there are still no nonzero terms, `taylor` doubles the degree of the
expansion of `g(x)` so long as the degree of the expansion is
less than or equal to `n 2^taylordepth`.

<!-- category: Series -->
<!-- keywords: taylorinfo -->
<!-- signatures: taylorinfo(expr) -->
### Function: taylorinfo (expr)

Returns information about the Taylor series *expr*.
The return value is a list of lists.
Each list comprises the name of a variable,
the point of expansion, and the degree of the expansion.


`taylorinfo` returns `false` if *expr* is not a Taylor series.


Example:







```maxima
maxima

(%i1) taylor ((1 - y^2)/(1 - x), x, 0, 3, [y, a, inf]);
                2                         2
(%o1)/T/ ((1 - a ) - 2 a (y - a) - (y - a) )
             2                       2
 + (- (y - a)  - 2 a (y - a) + (1 - a )) x
             2                       2    2
 + (- (y - a)  - 2 a (y - a) + (1 - a )) x
             2                       2    3
 + (- (y - a)  - 2 a (y - a) + (1 - a )) x  + . . .


(%i2) taylorinfo(%);
(%o2)               [[x, 0, 3], [y, a, inf]]
```

<!-- category: Series -->
<!-- keywords: taylorp -->
<!-- signatures: taylorp(expr) -->
### Function: taylorp (expr)

Returns `true` if *expr* is a Taylor series,
and `false` otherwise.

<!-- category: Series -->
<!-- keywords: taytorat -->
<!-- signatures: taytorat(expr) -->
### Function: taytorat (expr)

Converts *expr* from `taylor` form to canonical rational expression
(CRE) form.  The effect is the same as `rat (ratdisrep (expr))`, but
faster.

<!-- category: Series -->
<!-- keywords: totalfourier -->
<!-- signatures: totalfourier(f, x, p) -->
### Function: totalfourier (f, x, p)

Returns `fourexpand (foursimp (fourier (f, x, p)), x, p, 'inf)`.

<!-- category: Series -->
<!-- keywords: trunc -->
<!-- signatures: trunc(expr) -->
### Function: trunc (expr)

Annotates the internal representation of the general expression *expr*
so that it is displayed as if its sums were truncated Taylor series.
*expr* is not otherwise modified.


Example:








```maxima
maxima

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

Returns the first backward difference
`f(n) - f(n - 1)`.
Thus `unsum` in a sense is the inverse of `sum`.


See also `nusum`.


Examples:









```maxima
maxima

(%i1) g(p) := p*4^n/binomial(2*n,n);
                                     n
                                  p 4
(%o1)               g(p) := ----------------
                            binomial(2 n, n)


(%i2) g(n^4);
                              n  4
                             4  n
(%o2)                   ----------------
                        binomial(2 n, n)


(%i3) nusum (%, n, 0, n);
         n              4        3       2
      2 4  (n + 1) (63 n  + 112 n  + 18 n  - 22 n + 3)    2
(%o3) ------------------------------------------------ - ---
                    693 binomial(2 n, n)                 231


(%i4) unsum (%, n);
                              n  4
                             4  n
(%o4)                   ----------------
                        binomial(2 n, n)
```

See also: `nusum`.

<!-- category: Series -->
<!-- keywords: verbose -->
<!-- signatures: verbose -->
### Variable: verbose

Default value: `false`


When `verbose` is `true`,
`powerseries` prints progress messages.

