## Polynomials

### Variable: algebraic

Default value: `false`


`algebraic` must be set to `true` in order for the simplification of
algebraic integers to take effect.

### Function: algfac (f, p)

Returns the factorization of *f* in the field $K[a]$. Does the same
as `factor(f, p)` which in fact calls `algfac`. One can also
specify the variable *a* as in `algfac(f, p, a)`.


Examples:



```maxima
(%i1) algfac(x^4 + 1, a^2 - 2);
                           2              2
(%o1)                    (x  - a x + 1) (x  + a x + 1)
(%i2) algfac(x^4 - t*x^2 + 1, a^2 - t - 2, a);
                           2              2
(%o2)                    (x  - a x + 1) (x  + a x + 1)
```


In the second example note that $a = sqrt(2 + t)$.

### Function: algnorm (f, p, a)

Returns the norm of the polynomial $f(a)$ in the extension
obtained by a root *a* of polynomial *p*. The coefficients of
*f* may depend on other variables.


Examples:



```maxima
(%i1) algnorm(x*a^2 + y*a + z,a^2 - 2, a);
                            2              2      2
(%o1)/R/                   z  + 4 x z - 2 y  + 4 x
```


The norm is also the resultant of polynomials *f* and *p*, and the product
of the differences of the roots of *f* and *p*.

### Function: algtrace (f, p, a)

Returns the trace of the polynomial $f(a)$ in the extension
obtained by a root *a* of polynomial *p*. The coefficients of
*f* may depend on other variables which remain “inert”.


Example:



```maxima
(%i1) algtrace(x*a^5 + y*a^3 + z + 1, a^2 + a + 1, a);
(%o1)/R/                       2 z + 2 y - x + 2
```

### Function: assoc_legendre_p (n, m, x)

The associated Legendre function of the first kind of degree $n$ and
order $m$, 
$P_{n}^{m}(z),$
is a solution of the differential equation:



$$(1-z^2){d^2 w\over dz^2} - 2z{dw\over dz} + \left[n(n+1)-{m^2\over 1-z^2}\right] w = 0$$


$$(1-z^2){d^2 w\over dz^2} - 2z{dw\over dz} + \left[n(n+1)-{m^2\over 1-z^2}\right] w = 0$$



This is related to the Legendre polynomial, 
$P_n(x)$
via



$$P_n^m(x) = (-1)^m\left(1-x^2\right)^{m/2} {d^m\over dx^m} P_n(x)$$


$$P_n^m(x) = (-1)^m\left(1-x^2\right)^{m/2} {d^m\over dx^m} P_n(x)$$



Reference: [https://personal.math.ubc.ca/~cbm/aands/page_779.htmA&S eqn 22.5.37](), [https://personal.math.ubc.ca/~cbm/aands/page_334.htmA&S eqn 8.6.6](), and [https://personal.math.ubc.ca/~cbm/aands/page_333.htmA&S eqn 8.2.5]().


Some examples:









```maxima
(%i1) assoc_legendre_p(2,0,x);
                                                 2
                                        3 (1 - x)
(%o1)                   (- 3 (1 - x)) + ---------- + 1
                                            2
(%i2) factor(%);
                                      2
                                   3 x  - 1
(%o2)                              --------
                                      2
(%i3) factor(assoc_legendre_p(2,1,x));
                                              2
(%o3)                         - 3 x sqrt(1 - x )

(%i4) (-1)^1*(1-x^2)^(1/2)*diff(legendre_p(2,x),x);
                                                    2
(%o4)                   - (3 - 3 (1 - x)) sqrt(1 - x )

(%i5) factor(%);
                                              2
(%o5)                         - 3 x sqrt(1 - x )
```


See also `orthopoly_returns_intervals` for how numerical results
are returned.

See also: `orthopoly_returns_intervals`.

### Function: assoc_legendre_q (n, m, x)

The associated Legendre function of the second kind of degree $n$
and order $m$, 
$Q_{n}^{m}(z),$
is a solution of the differential equation:



$$(1-z^2){d^2 w\over dz^2} - 2z{dw\over dz} + \left[n(n+1)-{m^2\over 1-z^2}\right] w = 0$$


$$(1-z^2){d^2 w\over dz^2} - 2z{dw\over dz} + \left[n(n+1)-{m^2\over 1-z^2}\right] w = 0$$



Reference: Abramowitz and Stegun, equation 8.5.3 and 8.1.8.


Some examples:







```maxima
(%i1) assoc_legendre_q(0,0,x);
                                       x + 1
                                 log(- -----)
                                       x - 1
(%o1)                            ------------
                                      2
(%i2) assoc_legendre_q(1,0,x);
                                    x + 1
                              log(- -----) x - 2
                                    x - 1
(%o2)/R/                      ------------------
                                      2
(%i3) assoc_legendre_q(1,1,x);
(%o3)/R/ 
          x + 1            2   2               2            x + 1            2
    log(- -----) sqrt(1 - x ) x  - 2 sqrt(1 - x ) x - log(- -----) sqrt(1 - x )
          x - 1                                             x - 1
  - ---------------------------------------------------------------------------
                                        2
                                     2 x  - 2
```

### Function: bdiscr (args)

Computes the discriminant of a basis $x_i$ in $K[a]$ as
the determinant of the matrix of elements $trace(x_i*x_j)$.
The args are the elements of the basis followed by the minimal
polynomial.


Example:



```maxima
(%i1) bdiscr(1, x, x^2, x^3 - 2);
(%o1)/R/                             - 108
(%i2) poly_discriminant(x^3 - 2, x);
(%o2)                                - 108
```


A standard base in an extension of degree n is $1, x, ..., x^{n - 1}$.
In this case it is known that the discriminant of this base is the discriminant
of the minimal polynomial. This is checked in (%o2) above.

### Variable: berlefact

Default value: `true`


When `berlefact` is `false` then the Kronecker factoring
algorithm will be used otherwise the Berlekamp algorithm, which is the
default, will be used.

### Function: bezout (p1, p2, x)

an alternative to the `resultant` command.  It
returns a matrix.  `determinant` of this matrix is the desired resultant.


Examples:








```maxima
maxima

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

See also: `resultant`.

### Function: bothcoef (expr, x)

Returns a list whose first member is the coefficient of *x* in *expr*
(as found by `ratcoef` if *expr* is in CRE form
otherwise by `coeff`) and whose second member is the remaining part of
*expr*.  That is, `[A, B]` where `expr = A*x + B`.


Example:









```maxima
maxima

(%i1) islinear (expr, x) := block ([c],
        c: bothcoef (rat (expr, x), x),
        is (freeof (x, c) and c[1] # 0))$


(%i2) islinear ((r^2 - (x - r)^2)/x, x);
(%o2)                         true
```

### Function: chebyshev_t (n, x)

The Chebyshev polynomial of the first kind of degree $n$, 
$T_n(x).$


Reference: [https://personal.math.ubc.ca/~cbm/aands/page_779.htmA&S eqn 22.5.47]().


The polynomials 
$T_n(x)$
can be written in terms of a hypergeometric function:



$$T_n(x) = {_{2}}F_{1}\left(-n, n; {1\over 2}; {1-x\over 2}\right)$$


$$T_n(x) = {_{2}}F_{1}\left(-n, n; {1\over 2}; {1-x\over 2}\right)$$



The polynomials can also be defined in terms of the sum



$$T_n(x) = {n\over 2} \sum_{r=0}^{\lfloor {n/2}\rfloor} {(-1)^r\over n-r} {n-r\choose k}(2x)^{n-2r}$$


$$T_n(x) = {n\over 2} \sum_{r=0}^{\lfloor {n/2}\rfloor} {(-1)^r\over n-r} {n-r\choose k}(2x)^{n-2r}$$



or the Rodrigues formula



$$T_n(x) = {1\over \kappa_n w(x)} {d^n\over dx^n}\left(w(x)(1-x^2)^n\right)$$


$$T_n(x) = {1\over \kappa_n  w(x)} {d^n\over dx^n}\left(w(x)(1-x^2)^n\right)$$



where



$$\eqalign{ w(x) &= 1/\sqrt{1-x^2} \cr \kappa_n &= (-2)^n\left(1\over 2\right)_n }$$


$$\eqalign{
w(x) &= 1/\sqrt{1-x^2} \cr
\kappa_n &= (-2)^n\left(1\over 2\right)_n
}$$



Some examples:








```maxima
(%i1) chebyshev_t(2,x);
                                                 2
(%o1)                   (- 4 (1 - x)) + 2 (1 - x)  + 1
(%i2) factor(%);
                                      2
(%o2)                              2 x  - 1
(%i3) factor(chebyshev_t(3,x));
                                       2
(%o3)                            x (4 x  - 3)
(%i4) factor(hgfred([-3,3],[1/2],(1-x)/2));
                                       2
(%o4)                            x (4 x  - 3)
```


See also `orthopoly_returns_intervals` for how numerical results
are returned.

See also: `orthopoly_returns_intervals`.

### Function: chebyshev_u (n, x)

The Chebyshev polynomial of the second kind of degree $n$, 
$U_n(x).$


Reference: [https://personal.math.ubc.ca/~cbm/aands/page_779.htmA&S eqn 22.5.48]().


The polynomials 
$U_n(x)$
can be written in terms of a hypergeometric function:



$$U_n(x) = (n+1)\; {_{2}F_{1}}\left(-n, n+2; {3\over 2}; {1-x\over 2}\right)$$


$$U_n(x) = (n+1)\; {_{2}F_{1}}\left(-n, n+2; {3\over 2}; {1-x\over 2}\right)$$



The polynomials can also be defined in terms of the sum



$$U_n(x) = \sum_{r=0}^{\lfloor n/2 \rfloor} (-1)^r {n-r \choose r} (2x)^{n-2r}$$


$$U_n(x) = \sum_{r=0}^{\lfloor n/2 \rfloor} (-1)^r {n-r \choose r} (2x)^{n-2r}$$



or the Rodrigues formula



$$U_n(x) = {1\over \kappa_n w(x)} {d^n\over dx^n}\left(w(x)(1-x^2)^n\right)$$


$$U_n(x) = {1\over \kappa_n  w(x)} {d^n\over dx^n}\left(w(x)(1-x^2)^n\right)$$



where



$$\eqalign{ w(x) &= \sqrt{1-x^2} \cr \kappa_n &= {(-2)^n\left({3\over 2}\right)_n \over n+1} }$$


$$\eqalign{
w(x) &= \sqrt{1-x^2} \cr
\kappa_n &= {(-2)^n\left({3\over 2}\right)_n \over n+1}
}$$

.









```maxima
(%i1) chebyshev_u(2,x);
                                                  2
                            8 (1 - x)    4 (1 - x)
(%o1)                 3 ((- ---------) + ---------- + 1)
                                3            3
(%i2) expand(%);
                                      2
(%o2)                              4 x  - 1
(%i3) expand(chebyshev_u(3,x));
                                     3
(%o3)                             8 x  - 4 x
(%i4) expand(4*hgfred([-3,5],[3/2],(1-x)/2));
                                     3
(%o4)                             8 x  - 4 x
```


See also `orthopoly_returns_intervals` for how numerical results
are returned.

See also: `orthopoly_returns_intervals`.

### Function: coeff (coeff, expr, x, n, coeff, expr, x)

Returns the coefficient of `x^n` in *expr*,
where *expr* is a polynomial or a monomial term in *x*.
Other than `ratcoef` `coeff` is a strictly syntactical
operation and will only find literal instances of
`x^n` in the internal representation of *expr*.


`coeff(expr, x^n)` is equivalent
to `coeff(expr, x, n)`.
`coeff(expr, x, 0)` returns the remainder of *expr*
which is free of *x*.
If omitted, *n* is assumed to be 1.


*x* may be a simple variable or a subscripted variable,
or a subexpression of *expr* which
comprises an operator and all of its arguments.


It may be possible to compute coefficients of expressions which are equivalent
to *expr* by applying `expand` or `factor`.  `coeff` itself
does not apply `expand` or `factor` or any other function.


`coeff` distributes over lists, matrices, and equations.


See also `ratcoef`.


Examples:


`coeff` returns the coefficient `x^n` in *expr*.






```maxima
maxima

(%i1) coeff (b^3*a^3 + b^2*a^2 + b*a + 1, a^3);
                                3
(%o1)                          b
```


`coeff(expr, x^n)` is equivalent
to `coeff(expr, x, n)`.







```maxima
maxima

(%i1) coeff (c[4]*z^4 - c[3]*z^3 - c[2]*z^2 + c[1]*z, z, 3);
(%o1)                         - c
                                 3


(%i2) coeff (c[4]*z^4 - c[3]*z^3 - c[2]*z^2 + c[1]*z, z^3);
(%o2)                         - c
                                 3
```


`coeff(expr, x, 0)` returns the remainder of *expr*
which is free of *x*.






```maxima
maxima

(%i1) coeff (a*u + b^2*u^2 + c^3*u^3, b, 0);
                            3  3
(%o1)                      c  u  + a u
```


*x* may be a simple variable or a subscripted variable,
or a subexpression of *expr* which
comprises an operator and all of its arguments.









```maxima
maxima

(%i1) coeff (h^4 - 2*%pi*h^2 + 1, h, 2);
(%o1)                        - 2 %pi


(%i2) coeff (v[1]^4 - 2*%pi*v[1]^2 + 1, v[1], 2);
(%o2)                        - 2 %pi


(%i3) coeff (sin(1+x)*sin(x) + sin(1+x)^3*sin(x)^3, sin(1+x)^3);
                                3
(%o3)                        sin (x)


(%i4) coeff ((d - a)^2*(b + c)^3 + (a + b)^4*(c - d), a + b, 4);
(%o4)                         c - d
```


`coeff` itself does not apply `expand` or `factor` or any other
function.











```maxima
maxima

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


`coeff` distributes over lists, matrices, and equations.








```maxima
maxima

(%i1) coeff ([4*a, -3*a, 2*a], a);
(%o1)                      [4, - 3, 2]


(%i2) coeff (matrix ([a*x, b*x], [-c*x, -d*x]), x);
                          [  a    b  ]
(%o2)                     [          ]
                          [ - c  - d ]


(%i3) coeff (a*u - b*v = 7*u + 3*v, u);
(%o3)                         a = 7
```

See also: `ratcoef`.

### Function: content (p_1, x_1, ..., x_n)

Returns a list whose first element is
the greatest common divisor of the coefficients of the terms of the
polynomial *p_1* in the variable *x_n* (this is the content) and whose
second element is the polynomial *p_1* divided by the content.




Examples:






```maxima
maxima

(%i1) content (2*x*y + 4*x^2*y^2, y);
                                   2
(%o1)                   [2 x, 2 x y  + y]
```

### Function: denom (expr)

Returns the denominator of the rational expression *expr*.


See also `num`









```maxima
maxima

(%i1) g1:(x+2)*(x+1)/((x+3)^2);
                         (x + 1) (x + 2)
(%o1)                    ---------------
                                   2
                            (x + 3)


(%i2) denom(g1);
                                   2
(%o2)                       (x + 3)


(%i3) g2:sin(x)/10*cos(x)/y;
                          cos(x) sin(x)
(%o3)                     -------------
                              10 y


(%i4) denom(g2);
(%o4)                         10 y
```

See also: `num`.

### Function: divide (p_1, p_2, x_1, ..., x_n)

computes the quotient and remainder
of the polynomial *p_1* divided by the polynomial *p_2*, in a main
polynomial variable, *x_n*.

The other variables are as in the `ratvars` function.
The result is a list whose first element is the quotient
and whose second element is the remainder.


Examples:







```maxima
maxima

(%i1) divide (x + y, x - y, x);
(%o1)                       [1, 2 y]


(%i2) divide (x + y, x - y);
(%o2)                      [- 1, 2 x]
```



Note that `y` is the main variable in the second example.

### Function: eliminate (eqn_1, ..., eqn_n, x_1, ..., x_k)

Eliminates variables from equations (or expressions assumed equal to zero) by
taking successive resultants. This returns a list of `n - k`
expressions with the *k* variables *x_1*, ..., *x_k* eliminated.
First *x_1* is eliminated yielding `n - 1` expressions, then
`x_2` is eliminated, etc.  If `k = n` then a single
expression in a list is returned free of the variables *x_1*, ...,
*x_k*.  In this case `solve` is called to solve the last resultant for
the last variable.


Example:









```maxima
maxima

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

### Function: ezgcd (p_1, p_2, p_3, ...)

Returns a list whose first element is the greatest common divisor of the
polynomials *p_1*, *p_2*, *p_3*, ... and whose remaining
elements are the polynomials divided by the greatest common divisor.  This
always uses the `ezgcd` algorithm.


See also `gcd`, `gcdex`, `gcdivide`, and
`poly_005fgcd`.


Examples:


The three polynomials have the greatest common divisor `2*x-3`.  The
gcd is first calculated with the function `gcd` and then with the function
`ezgcd`.










```maxima
maxima

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

See also: `gcd`, `gcdex`, `gcdivide`, `poly_gcd`.

### Variable: facexpand

Default value: `true`


`facexpand` controls whether the irreducible factors returned by
`factor` are in expanded (the default) or recursive (normal CRE) form.

### Function: factor (factor, expr, factor, expr, p)

Factors the expression *expr*, containing any number of variables or 
functions, into factors irreducible over the integers.
`factor (expr, p)` factors *expr* over the field of 
rationals with an element adjoined whose minimum polynomial is *p*.


`factor` uses `ifactors` function for factoring integers.


`factorflag` if `false` suppresses the factoring of integer factors
of rational expressions.


`dontfactor` may be set to a list of variables with respect to which
factoring is not to occur.  (It is initially empty).  Factoring also
will not take place with respect to any variables which are less
important (using the variable ordering assumed for CRE form) than
those on the `dontfactor` list.


`savefactors` if `true` causes the factors of an expression which
is a product of factors to be saved by certain functions in order to
speed up later factorizations of expressions containing some of the
same factors.


`berlefact` if `false` then the Kronecker factoring algorithm will
be used otherwise the Berlekamp algorithm, which is the default, will
be used.


`intfaclim` if `true` maxima will give up factorization of
integers if no factor is found after trial divisions and Pollard’s rho
method.  If set to `false` (this is the case when the user calls
`factor` explicitly), complete factorization of the integer will be
attempted.  The user’s setting of `intfaclim` is used for internal
calls to `factor`.  Thus, `intfaclim` may be reset to prevent
Maxima from taking an inordinately long time factoring large integers.


`factor_max_degree` if set to a positive integer `n` will
prevent certain polynomials from being factored if their degree in any
variable exceeds `n`.


See also `collectterms` and `sqfr`


Examples:





















```maxima
maxima

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

See also: `ifactors`, `factorflag`, `dontfactor`, `savefactors`, `berlefact`, `intfaclim`, `factor_max_degree`, `collectterms`, `sqfr`.

### Variable: factor_max_degree

Default value: `1000`


When `factor_max_degree` is set to a positive integer `n`, it will prevent
Maxima from attempting to factor certain polynomials whose degree in any
variable exceeds `n`. If `factor_max_degree_print_warning` is true,
a warning message will be printed. `factor_max_degree` can be used to
prevent excessive memory usage and/or computation time and stack overflows.
Note that "obvious" factoring of polynomials such as `x^2000+x^2001` to
`x^2000*(x+1)` will still take place. To disable this behavior, set
`factor_max_degree` to `0`.


Example:







```maxima
maxima
(%i1) factor_max_degree : 100$

(%i2) factor(x^100-1);
                        2        4    3    2
(%o2) (x - 1) (x + 1) (x  + 1) (x  - x  + x  - x + 1)
   4    3    2            8    6    4    2
 (x  + x  + x  + x + 1) (x  - x  + x  - x  + 1)
   20    15    10    5        20    15    10    5
 (x   - x   + x   - x  + 1) (x   + x   + x   + x  + 1)
   40    30    20    10
 (x   - x   + x   - x   + 1)


(%i3) factor(x^101-1);
                               101
Refusing to factor polynomial x    - 1
               because its degree exceeds factor_max_degree (100)
                             101
(%o3)                       x    - 1
```


See also: `factor_max_degree_print_warning`

See also: `factor_max_degree_print_warning`.

### Variable: factor_max_degree_print_warning

Default value: `true`


When factor_max_degree_print_warning is true, then Maxima will print a
warning message when the factoring of a polynomial is prevented because
its degree exceeds the value of factor_max_degree.


See also: `factor_max_degree`

See also: `factor_max_degree`.

### Variable: factorflag

Default value: `false`



When `factorflag` is `false`, suppresses the factoring of
integer factors of rational expressions.

### Function: factorout (expr, x_1, x_2, ...)

Rearranges the sum *expr* into a sum of terms of the form 
`f (x_1, x_2, ...)*g` where `g` is a product of 
expressions not containing any *x_i* and `f` is factored.


Note that the option variable `keepfloat` is ignored by `factorout`.


Example:







```maxima
maxima

(%i1) expand (a*(x+1)*(x-1)*(u+1)^2);
             2  2          2      2      2
(%o1)     a u  x  + 2 a u x  + a x  - a u  - 2 a u - a


(%i2) factorout(%,x);
         2
(%o2) a u  (x - 1) (x + 1) + 2 a u (x - 1) (x + 1)
                                              + a (x - 1) (x + 1)
```

### Function: factorsum (expr)

Tries to group terms in factors of *expr* which are sums into groups of
terms such that their sum is factorable.  `factorsum` can recover the
result of `expand ((x + y)^2 + (z + w)^2)` but it can’t recover
`expand ((x + 1)^2 + (x + y)^2)` because the terms have variables in
common.


Example:







```maxima
maxima

(%i1) expand ((x + 1)*((u + v)^2 + a*(w + z)^2));
           2      2                            2      2
(%o1) a x z  + a z  + 2 a w x z + 2 a w z + a w  x + v  x
                                     2        2    2            2
                        + 2 u v x + u  x + a w  + v  + 2 u v + u


(%i2) factorsum (%);
                                   2          2
(%o2)            (x + 1) (a (z + w)  + (v + u) )
```

### Function: fasttimes (p_1, p_2)

Returns the product of the polynomials *p_1* and *p_2* by using a
special algorithm for multiplication of polynomials.  `p_1` and `p_2`
should be multivariate, dense, and nearly the same size.  Classical
multiplication is of order `n_1 n_2` where
`n_1` is the degree of `p_1`
and `n_2` is the degree of `p_2`.
`fasttimes` is of order `max (n_1, n_2)^1.585`.

### Function: fullratsimp (expr)

`fullratsimp` repeatedly
applies `ratsimp` followed by non-rational simplification to an
expression until no further change occurs,
and returns the result.


When non-rational expressions are involved, one call
to `ratsimp` followed as is usual by non-rational ("general")
simplification may not be sufficient to return a simplified result.
Sometimes, more than one such call may be necessary.
`fullratsimp` makes this process convenient.


`fullratsimp (expr, x_1, ..., x_n)` takes one or more
arguments similar to `ratsimp` and `rat`.


Example:









```maxima
maxima

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

### Function: fullratsubst (new, old, expr, fullratsubst, old = new, expr, fullratsubst, [ old_1 = new_1, ..., old_n = new_n ], expr)

`fullratsubst` applies `lratsubst` repeatedly until *expr*
stops changing (or `lrats_max_iter` is reached). This function is
useful when the replacement expression and the replaced expression have
one or more variables in common.


`fullratsubst` accepts its arguments in the format of
`ratsubst` or `lratsubst`.




Examples:



- *
`subst` can carry out multiple substitutions.
`lratsubst` is analogous to `subst`.






```maxima
maxima

(%i1) subst ([a = b, c = d], a + c);
(%o1)                         d + b


(%i2) lratsubst ([a^2 = b, c^2 = d], (a + e)*c*(a + c));
(%o2)                (d + a c) e + a d + b c
```


- *
If only one substitution is desired, then a single
equation may be given as first argument.





```maxima
maxima

(%i1) lratsubst (a^2 = b, a^3);
(%o1)                          a b
```


- *
`fullratsubst` is equivalent to `ratsubst`
except that it recurses until its result stops changing.






```maxima
maxima

(%i1) ratsubst (b*a, a^2, a^3);
                               2
(%o1)                         a  b


(%i2) fullratsubst (b*a, a^2, a^3);
                                 2
(%o2)                         a b
```


- *
`fullratsubst` also accepts a list of equations or a single
equation as first argument.






```maxima
maxima

(%i1) fullratsubst ([a^2 = b, b^2 = c, c^2 = a], a^3*b*c);
(%o1)                           b


(%i2) fullratsubst (a^2 = b*a, a^3);
                                 2
(%o2)                         a b
```


- *
`fullratsubst` catches potential infinite recursions. `lrats_005fmax_005fiter`.




Warning: fullratsubst2(listofeqns,expr): reached maximum iterations of 15 . Increase ‘lrats_max_iter’ to increase this limit.


```maxima
maxima

(%i1) fullratsubst (b*a^2, a^2, a^3), lrats_max_iter=15;
                              3  15
(%o1)                        a  b
```


See also `lrats_max_iter` and `fullratsubstflag`.

See also: `lratsubst`, `lrats_max_iter`, `ratsubst`, `fullratsubstflag`.

### Variable: fullratsubstflag

Default value: `false`


An option variable that is set to `true` in `fullratsubst`.

See also: `fullratsubst`.

### Function: gcd (p_1, p_2, x_1, ...)

Returns the greatest common divisor of *p_1* and *p_2*.  The flag
`gcd` determines which algorithm is employed.  Setting `gcd` to
`ez`, `subres`, `red`, or `spmod` selects the `ezgcd`,
subresultant `prs`, reduced, or modular algorithm, respectively.  If
`gcd` `false` then `gcd (p_1, p_2, x)` always
returns 1 for all *x*.  Many functions (e.g. `ratsimp`,
`factor`, etc.) cause gcd’s to be taken implicitly.  For homogeneous
polynomials it is recommended that `gcd` equal to `subres` be used.
To take the gcd when an algebraic is present, e.g.,
`gcd (x^2 - 2*sqrt(2)* x + 2, x - sqrt(2))`, the option
variable `algebraic` must be `true` and `gcd` must not be
`ez`.


The `gcd` flag, default: `spmod`, if `false` will also prevent
the greatest common divisor from being taken when expressions are converted to
canonical rational expression (CRE) form.  This will sometimes speed the
calculation if gcds are not required.


See also `ezgcd`, `gcdex`, `gcdivide`, and
`poly_005fgcd`.


Example:










```maxima
maxima

(%i1) p1:6*x^3+19*x^2+19*x+6;
                        3       2
(%o1)                6 x  + 19 x  + 19 x + 6


(%i2) p2:6*x^5+13*x^4+12*x^3+13*x^2+6*x;
                  5       4       3       2
(%o2)          6 x  + 13 x  + 12 x  + 13 x  + 6 x


(%i3) gcd(p1, p2);
                            2
(%o3)                    6 x  + 13 x + 6


(%i4) p1/gcd(p1, p2), ratsimp;
(%o4)                         x + 1


(%i5) p2/gcd(p1, p2), ratsimp;
                              3
(%o5)                        x  + x
```


`ezgcd` returns a list whose first element is the greatest common divisor
of the polynomials *p_1* and *p_2*, and whose remaining elements are
the polynomials divided by the greatest common divisor.








```maxima
maxima
(%i1) p1:6*x^3+19*x^2+19*x+6 $
(%i2) p2:6*x^5+13*x^4+12*x^3+13*x^2+6*x $

(%i3) ezgcd(p1, p2);
                    2                     3
(%o3)           [6 x  + 13 x + 6, x + 1, x  + x]
```

See also: `ratsimp`, `factor`, `algebraic`, `ezgcd`, `gcdex`, `gcdivide`, `poly_gcd`.

### Function: gcdex (gcdex, f, g, gcdex, f, g, x)

Returns a list `[a, b, u]` where *u* is the greatest
common divisor (gcd) of *f* and *g*, and *u* is equal to
`a f + b g`.  The arguments *f* and *g*
should be univariate polynomials, or else polynomials in *x* a supplied
main variable since we need to be in a principal ideal domain for this to
work.  The gcd means the gcd regarding *f* and *g* as univariate
polynomials with coefficients being rational functions in the other variables.


`gcdex` implements the Euclidean algorithm, where we have a sequence of
`L[i]: [a[i], b[i], r[i]]` which are all perpendicular to `[f, g, -1]`
and the next one is built as if `q = quotient(r[i]/r[i+1])` then
`L[i+2]: L[i] - q L[i+1]`, and it terminates at `L[i+1]` when the
remainder `r[i+2]` is zero.


The arguments *f* and *g* can be integers.  For this case the function
`igcdex` is called by `gcdex`.


See also `ezgcd`, `gcd`, `gcdivide`, and
`poly_005fgcd`.


Examples:







```maxima
maxima

(%i1) gcdex (x^2 + 1, x^3 + 4);
                       2
                      x  + 4 x - 1  x + 4
(%o1)/R/           [- ------------, -----, 1]
                           17        17


(%i2) % . [x^2 + 1, x^3 + 4, -1];
(%o2)/R/                        0
```



Note that the gcd in the following is `1` since we work in `k(y)[x]`,
not the  `y+1` we would expect in `k[y, x]`.






```maxima
maxima

(%i1) gcdex (x*(y + 1), y^2 - 1, x);
                               1
(%o1)/R/                 [0, ------, 1]
                              2
                             y  - 1
```

See also: `igcdex`, `ezgcd`, `gcd`, `gcdivide`, `poly_gcd`.

### Function: gcfactor (n)

Factors the Gaussian integer *n* over the Gaussian integers, i.e., numbers
of the form `a + b %i` where *a* and *b* are
rational integers (i.e.,  ordinary integers).  Factors are normalized by making
*a* and *b* non-negative.

### Function: gen_laguerre (n, a, x)

The generalized Laguerre polynomial of degree $n$, 
$L_n^{(\alpha)}(x).$


These can be defined by



$$L_n^{(\alpha)}(x) = {n+\alpha \choose n}\; {_1F_1}(-n; \alpha+1; x)$$


$$L_n^{(\alpha)}(x) = {n+\alpha \choose n}\; {_1F_1}(-n; \alpha+1; x)$$



The polynomials can also be defined by the sum



$$L_n^{(\alpha)}(x) = \sum_{k=0}^n {(\alpha + k + 1)_{n-k} \over (n-k)! k!} (-x)^k$$


$$L_n^{(\alpha)}(x) = \sum_{k=0}^n {(\alpha + k + 1)_{n-k} \over (n-k)! k!} (-x)^k$$



or the Rodrigues formula



$$L_n^{(\alpha)}(x) = {1\over \kappa_n w(x)} {d^n\over dx^n}\left(w(x)x^n\right)$$


$$L_n^{(\alpha)}(x) = {1\over \kappa_n  w(x)} {d^n\over dx^n}\left(w(x)x^n\right)$$



where



$$\eqalign{ w(x) &= e^{-x}x^{\alpha} \cr \kappa_n &= n! }$$


$$\eqalign{
w(x) &= e^{-x}x^{\alpha} \cr
\kappa_n &= n!
}$$



Reference: [https://personal.math.ubc.ca/~cbm/aands/page_780.htmA&S eqn 22.5.54]().


Some examples:







```maxima
(%i1) gen_laguerre(1,k,x);
                                             x
(%o1)                         (k + 1) (1 - -----)
                                           k + 1
(%i2) gen_laguerre(2,k,x);
                                         2
                                        x            2 x
                 (k + 1) (k + 2) (--------------- - ----- + 1)
                                  (k + 1) (k + 2)   k + 1
(%o2)            ---------------------------------------------
                                       2
(%i3) binomial(2+k,2)*hgfred([-2],[1+k],x);
                                         2
                                        x            2 x
                 (k + 1) (k + 2) (--------------- - ----- + 1)
                                  (k + 1) (k + 2)   k + 1
(%o3)            ---------------------------------------------
                                       2
```


See also `orthopoly_returns_intervals` for how numerical results
are returned.

See also: `orthopoly_returns_intervals`.

### Function: gfactor (expr)

Factors the polynomial *expr* over the Gaussian integers
(that is, the integers with the imaginary unit `%i` adjoined).

This is like `factor (expr, a^2+1)` where *a* is `%i`.


Example:






```maxima
maxima

(%i1) gfactor (x^4 - 1);
(%o1)           (x - 1) (x + 1) (x - %i) (x + %i)
```

### Function: gfactorsum (expr)

is similar to `factorsum` but applies `gfactor` instead
of `factor`.

### Function: hermite (n, x)

The Hermite polynomial of degree $n$, 
$H_n(x).$


These polynomials may be defined by a hypergeometric function



$$H_n(x) = (2x)^n\; {_2F_0}\left(-{1\over 2} n, -{1\over 2}n+{1\over 2};;-{1\over x^2}\right)$$


$$H_n(x) = (2x)^n\; {_2F_0}\left(-{1\over 2} n, -{1\over 2}n+{1\over 2};;-{1\over x^2}\right)$$



or by the series



$$H_n(x) = n! \sum_{k=0}^{\lfloor n/2 \rfloor} {(-1)^k(2x)^{n-2k} \over k! (n-2k)!}$$


$$H_n(x) = n! \sum_{k=0}^{\lfloor n/2 \rfloor} {(-1)^k(2x)^{n-2k} \over k! (n-2k)!}$$



or the Rodrigues formula



$$H_n(x) = {1\over \kappa_n w(x)} {d^n\over dx^n}\left(w(x)\right)$$


$$H_n(x) = {1\over \kappa_n  w(x)} {d^n\over dx^n}\left(w(x)\right)$$



where



$$\eqalign{ w(x) &= e^{-{x^2/2}} \cr \kappa_n &= (-1)^n }$$


$$\eqalign{
w(x) &= e^{-{x^2/2}} \cr
\kappa_n &= (-1)^n
}$$



Reference: [https://personal.math.ubc.ca/~cbm/aands/page_780.htmA&S eqn 22.5.55]().


Some examples:









```maxima
(%i1) hermite(3,x);
                                              2
                                           2 x
(%o1)                          - 12 x (1 - ----)
                                            3
(%i2) expand(%);
                                     3
(%o2)                             8 x  - 12 x
(%i3) expand(hermite(4,x));
                                  4       2
(%o3)                         16 x  - 48 x  + 12
(%i4) expand((2*x)^4*hgfred([-2,-2+1/2],[],-1/x^2));
                                  4       2
(%o4)                         16 x  - 48 x  + 12
(%i5) expand(4!*sum((-1)^k*(2*x)^(4-2*k)/(k!*(4-2*k)!),k,0,floor(4/2)));
                                  4       2
(%o5)                         16 x  - 48 x  + 12
```


See also `orthopoly_returns_intervals` for how numerical results
are returned.

See also: `orthopoly_returns_intervals`.

### Function: hipow (expr, x)

Returns the highest explicit exponent of *x* in *expr*.
*x* may be a variable or a general expression.
If *x* does not appear in *expr*,
`hipow` returns `0`.


`hipow` does not consider expressions equivalent to `expr`.  In
particular, `hipow` does not expand `expr`, so 
`hipow (expr, x)` and
`hipow (expand (expr, x))` may yield different results.


Examples:










```maxima
maxima

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

### Function: intervalp (e)

Return `true` if the input is an interval and return false if it isn’t.

### Variable: intfaclim

Default value: true


If `true`, maxima will give up factorization of
integers if no factor is found after trial divisions and Pollard’s rho
method and factorization will not be complete.


When `intfaclim` is `false` (this is the case when the user
calls `factor` explicitly), complete factorization will be
attempted.  `intfaclim` is set to `false` when factors are
computed in `divisors`, `divsum` and `totient`.




Internal calls to `factor` respect the user-specified value of
`intfaclim`.  Setting `intfaclim` to `true` may reduce
the time spent factoring large integers.

### Function: jacobi_p (n, a, b, x)

The Jacobi polynomial, 
$P_n^{(a,b)}(x).$


The Jacobi polynomials are actually defined for all
$a$ and $b$; however, the Jacobi polynomial
weight $(1 - x)^a (1 + x)^b$ isn’t integrable
for 
$a \le -1$
or 
$b \le -1.$


Reference: [https://personal.math.ubc.ca/~cbm/aands/page_779.htmA&S eqn 22.5.42]().


The polynomial may be defined in terms of hypergeometric functions:



$$P_n^{(a,b)}(x) = {n+a\choose n} {_1F_2}\left(-n, n + a + b + 1; a+1; {1-x\over 2}\right)$$


$$P_n^{(a,b)}(x) = {n+a\choose n} {_1F_2}\left(-n, n + a + b + 1; a+1; {1-x\over 2}\right)$$



or the Rodrigues formula



$$P_n^{(a, b)}(x) = {1\over \kappa_n w(x)} {d^n\over dx^n}\left(w(x)\left(1-x^2\right)^n\right)$$


$$P_n^{(a, b)}(x) = {1\over \kappa_n  w(x)} {d^n\over dx^n}\left(w(x)\left(1-x^2\right)^n\right)$$



where



$$\eqalign{ w(x) &= (1-x)^a(1-x)^b \cr \kappa_n &= (-2)^n n! }$$


$$\eqalign{
w(x) &= (1-x)^a(1-x)^b \cr
\kappa_n &= (-2)^n n!
}$$



Some examples:






```maxima
(%i1) jacobi_p(0,a,b,x);
(%o1)                                  1
(%i2) jacobi_p(1,a,b,x);
                                    (b + a + 2) (1 - x)
(%o2)                  (a + 1) (1 - -------------------)
                                         2 (a + 1)
```


See also `orthopoly_returns_intervals` for how numerical results
are returned.

See also: `orthopoly_returns_intervals`.

### Variable: keepfloat

Default value: `false`


When `keepfloat` is `true`, prevents floating
point numbers from being rationalized when expressions which contain
them are converted to canonical rational expression (CRE) form.


Note that the function `solve` and those functions calling it 
(`eigenvalues`, for example) currently ignore this flag, converting 
floating point numbers anyway.


Examples:







```maxima
maxima

(%i1) rat(x/2.0);
rat: replaced 0.5 by 1/2 = 0.5
                                x
(%o1)/R/                        -
                                2


(%i2) rat(x/2.0), keepfloat;
(%o2)/R/                      0.5 x
```


`solve` ignores `keepfloat`:






```maxima
maxima

(%i1) solve(1.0-x,x), keepfloat;
rat: replaced 1.0 by 1/1 = 1.0
(%o1)                        [x = 1]
```

### Function: laguerre (n, x)

The Laguerre polynomial, 
$L_n(x)$
of degree $n$.


Reference: [https://personal.math.ubc.ca/~cbm/aands/page_778.htmA&S eqn 22.5.16]() and [https://personal.math.ubc.ca/~cbm/aands/page_780.htmA&S eqn 22.5.54]().


These are related to the generalized Laguerre polynomial by



$$L_n(x) = L_n^{(0)}(x)$$


$$L_n(x) = L_n^{(0)}(x)$$



The polynomials are given by the sum



$$L_n(x) = \sum_{k=0}^{n} {(-1)^k\over k!}{n \choose k} x^k$$


$$L_n(x) = \sum_{k=0}^{n} {(-1)^k\over k!}{n \choose k} x^k$$



Some examples:








```maxima
(%i1) laguerre(1,x);
(%o1)                                1 - x
(%i2) laguerre(2,x);
                                  2
                                 x
(%o2)                            -- - 2 x + 1
                                 2
(%i3) gen_laguerre(2,0,x);
                                  2
                                 x
(%o3)                            -- - 2 x + 1
                                 2
(%i4) sum((-1)^k/k!*binomial(2,k)*x^k,k,0,2);
                                  2
                                 x
(%o4)                            -- - 2 x + 1
                                 2
```


See also `orthopoly_returns_intervals` for how numerical results
are returned.

See also: `orthopoly_returns_intervals`.

### Function: legendre_p (n, x)

The Legendre polynomial of the first kind, 
$P_n(x),$
of degree $n$.


Reference: [https://personal.math.ubc.ca/~cbm/aands/page_779.htmA&S eqn 22.5.50]() and [https://personal.math.ubc.ca/~cbm/aands/page_779.htmA&S eqn 22.5.51]().


The Legendre polynomial is related to the Jacobi polynomials by



$$P_n(x) = P_n^{(0,0)}(x)$$


$$P_n(x) = P_n^{(0,0)}(x)$$



or the Rodrigues formula



$$P_n(x) = {1\over \kappa_n w(x)} {d^n\over dx^n}\left(w(x)\left(1-x^2\right)^n\right)$$


$$P_n(x) = {1\over \kappa_n  w(x)} {d^n\over dx^n}\left(w(x)\left(1-x^2\right)^n\right)$$



where



$$\eqalign{ w(x) &= 1 \cr \kappa_n &= (-2)^n n! }$$


$$\eqalign{
w(x) &= 1 \cr
\kappa_n &= (-2)^n n!
}$$



Some examples:









```maxima
(%i1) legendre_p(1,x);
(%o1)                                  x
(%i2) legendre_p(2,x);
                                                 2
                                        3 (1 - x)
(%o2)                   (- 3 (1 - x)) + ---------- + 1
                                            2
(%i3) expand(%);
                                      2
                                   3 x    1
(%o3)                              ---- - -
                                    2     2
(%i4) expand(legendre_p(3,x));
                                     3
                                  5 x    3 x
(%o4)                             ---- - ---
                                   2      2
(%i5) expand(jacobi_p(3,0,0,x));
                                     3
                                  5 x    3 x
(%o5)                             ---- - ---
                                   2      2
```


See also `orthopoly_returns_intervals` for how numerical results
are returned.

See also: `orthopoly_returns_intervals`.

### Function: legendre_q (n, x)

The Legendre function of the second kind, 
$Q_n(x)$
of degree $n$.


Reference: Abramowitz and Stegun, equations 8.5.3 and 8.1.8.


These are related to 
$Q_n^m(x)$
by



$$Q_n(x) = Q_n^0(x)$$


$$Q_n(x) = Q_n^0(x)$$



Some examples:







```maxima
(%i1) legendre_q(0,x);
                                       x + 1
                                 log(- -----)
                                       x - 1
(%o1)                            ------------
                                      2
(%i2) legendre_q(1,x);
                                    x + 1
                              log(- -----) x - 2
                                    x - 1
(%o2)/R/                      ------------------
                                      2
(%i3) assoc_legendre_q(1,0,x);
                                    x + 1
                              log(- -----) x - 2
                                    x - 1
(%o3)/R/                      ------------------
                                      2
```

### Function: lopow (expr, x)

Returns the lowest exponent of *x* which explicitly appears in
*expr*.  Thus






```maxima
maxima

(%i1) lopow ((x+y)^2 + (x+y)^a, x+y);
(%o1)                       min(2, a)
```

### Variable: lrats_max_iter

Default value: `100000`


The upper limit on the number of iterations that `fullratsubst` and
`lratsubst` may perform. It must be set to a positive integer. See
the example for `fullratsubst`.

See also: `fullratsubst`, `lratsubst`.

### Function: lratsubst (lratsubst, new, old, expr, lratsubst, old = new, expr, lratsubst, [ old_1 = new_1, ..., old_n = new_n ], expr)

`lratsubst` is analogous to `subst` except that it uses
`ratsubst` to perform substitutions.


When `lratsubst` is given two arguments,
the first argument may be an equation,
a list of equations,
or a list of exactly one element, which is a list of equations.


Substitutions are made in the order given
by the list of equations, that is, from left to right.


Multiple substitutions are serial, not parallel.
That is, later substitutions are performed on the results of earlier ones.


When `lratsubst` is given three arguments *new*, *old*, and *expr*,
it is equivalent to `lratsubst(old = new, expr)`.


Examples:





`lratsubst` can carry out multiple substitutions.
`lratsubst` is analogous to `subst`.







```maxima
maxima

(%i1) lratsubst ([a = b, c = d], a + c);
(%o1)                         d + b


(%i2) lratsubst ([a^2 = b, c^2 = d], (a + e)*c*(a + c));
(%o2)                (d + a c) e + a d + b c
```


If only one substitution is desired, then a single
equation may be given as first argument.






```maxima
maxima

(%i1) lratsubst (a^2 = b, a^3);
(%o1)                          a b
```


The first argument may be a list of exactly one element,
which is a list of equations.






```maxima
maxima

(%i1) lratsubst ([[a^2=b*a, b=c]], a^3);
                               2
(%o1)                         a  c
```


See also `fullratsubst`.

See also: `subst`, `fullratsubst`.

### Variable: modulus

Default value: `false`


When `modulus` is a positive number *p*, operations on canonical rational
expressions (CREs, as returned by `rat` and related functions) are carried out
modulo *p*, using the so-called "balanced" modulus system in which `n modulo p` is defined as an integer *k* in
`[-(p-1)/2, ..., 0, ..., (p-1)/2]` when *p* is odd, or
`[-(p/2 - 1), ..., 0, ...., p/2]` when *p* is even, such
that `a p + k` equals *n* for some integer *a*.





If *expr* is already in canonical rational expression (CRE) form when
`modulus` is reset, then you may need to re-rat *expr*, e.g.,
`expr: rat (ratdisrep (expr))`, in order to get correct results.


Typically `modulus` is set to a prime number.  If `modulus` is set to
a positive non-prime integer, this setting is accepted, but a warning message is
displayed.  Maxima signals an error, when zero or a negative integer is
assigned to `modulus`.


Examples:













```maxima
maxima

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

### Function: num (expr)

Returns the numerator of *expr* if it is a ratio.
If *expr* is not a ratio, *expr* is returned.


`num` evaluates its argument.


See also `denom`









```maxima
maxima

(%i1) g1:(x+2)*(x+1)/((x+3)^2);
                         (x + 1) (x + 2)
(%o1)                    ---------------
                                   2
                            (x + 3)


(%i2) num(g1);
(%o2)                    (x + 1) (x + 2)


(%i3) g2:sin(x)/10*cos(x)/y;
                          cos(x) sin(x)
(%o3)                     -------------
                              10 y


(%i4) num(g2);
(%o4)                     cos(x) sin(x)
```

See also: `denom`.

### Function: orthopoly_recur (f, args)

Returns a recursion relation for the orthogonal function family
*f* with arguments *args*. The recursion is with 
respect to the polynomial degree.






```maxima
(%i1) orthopoly_recur (legendre_p, [n, x]);
                    (2 n + 1) P (x) x - n P     (x)
                               n           n - 1
(%o1)   P     (x) = -------------------------------
         n + 1                   n + 1
```


The second argument to `orthopoly_recur` must be a list with the 
correct number of arguments for the function *f*; if it isn’t, 
Maxima signals an error.






```maxima
(%i1) orthopoly_recur (jacobi_p, [n, x]);

Function jacobi_p needs 4 arguments, instead it received 2
 -- an error.  Quitting.  To debug this try debugmode(true);
```


Additionally, when *f* isn’t the name of one of the 
families of orthogonal polynomials, an error is signalled.






```maxima
(%i1) orthopoly_recur (foo, [n, x]);

A recursion relation for foo isn't known to Maxima
 -- an error.  Quitting.  To debug this try debugmode(true);
```

### Variable: orthopoly_returns_intervals

Default value: `true`


When `orthopoly_returns_intervals` is `true`, floating point results are returned in
the form `interval (c, r)`, where *c* is the center of an interval
and *r* is its radius. The center can be a complex number; in that
case, the interval is a disk in the complex plane.

See also: `true`.

### Function: orthopoly_weight (f, args)

Returns a three element list; the first element is 
the formula of the weight for the orthogonal polynomial family
*f* with arguments given by the list *args*; the 
second and third elements give the lower and upper endpoints
of the interval of orthogonality. For example,







```maxima
(%i1) w : orthopoly_weight (hermite, [n, x]);
                            2
                         - x
(%o1)                 [%e    , - inf, inf]
(%i2) integrate(w[1]*hermite(3, x)*hermite(2, x), x, w[2], w[3]);
(%o2)                           0
```


The main variable of *f* must be a symbol; if it isn’t, Maxima
signals an error.

### Function: pochhammer (x, n)

The Pochhammer symbol, 
$(x)_n.$
(See [https://personal.math.ubc.ca/~cbm/aands/page_256.htmA&S eqn 6.1.22]() and [https://dlmf.nist.gov/5.2.iiiDLMF 5.2.iii]()).


For nonnegative
integers *n* with `n <= pochhammer_max_index`, the
expression 
$(x)_n$
evaluates to the
product 
$x(x+1)(x+2)\cdots(x+n-1)$
when
$n > 0$
and
to 1 when $n = 0$.
For negative $n$, 
$(x)_n$
is
defined as 
$(-1)^n/(1-x)_{-n}.$
Thus







```maxima
(%i1) pochhammer (x, 3);
(%o1)                   x (x + 1) (x + 2)
(%i2) pochhammer (x, -3);
                                 1
(%o2)               - -----------------------
                      (1 - x) (2 - x) (3 - x)
```


To convert a Pochhammer symbol into a quotient of gamma functions,
(see [https://personal.math.ubc.ca/~cbm/aands/page_256.htmA&S eqn 6.1.22]()) use `makegamma`; for example 






```maxima
(%i1) makegamma (pochhammer (x, n));
                          gamma(x + n)
(%o1)                     ------------
                            gamma(x)
```


When *n* exceeds `pochhammer_max_index` or when *n* 
is symbolic, `pochhammer` returns a noun form.






```maxima
(%i1) pochhammer (x, n);
(%o1)                         (x)
                                 n
```

See also: `pochhammer_max_index`, `pochhammer`.

### Variable: pochhammer_max_index

Default value: 100


`pochhammer (n, x)` expands to a product if and only if
`n <= pochhammer_max_index`.


Examples:







```maxima
(%i1) pochhammer (x, 3), pochhammer_max_index : 3;
(%o1)                   x (x + 1) (x + 2)
(%i2) pochhammer (x, 4), pochhammer_max_index : 3;
(%o2)                         (x)
                                 4
```


Reference: [https://personal.math.ubc.ca/~cbm/aands/page_256.htmA&S eqn 6.1.16]().

### Function: poly_add (poly1, poly2, varlist)

Adds two polynomials *poly1* and *poly2*.


```maxima
(%i1) poly_add(z+x^2*y,x-z,[x,y,z]);
                                    2
(%o1)                              x  y + x
```

### Function: poly_buchberger (polylist_fl, varlist)

`poly_buchberger` performs the Buchberger algorithm on a list of
polynomials and returns the resulting Groebner basis.

### Function: poly_buchberger_criterion (polylist, varlist)

Returns `true` if *polylist* is a Groebner basis with respect to the current term
order, by using the Buchberger
criterion: for every two polynomials $h1$ and $h2$ in *polylist* the
S-polynomial $S(h1,h2)$ reduces to 0 $modulo$ *polylist*.

### Variable: poly_coefficient_ring

Default value: `expression_ring`


This switch indicates the coefficient ring of the polynomials that
will be used in grobner calculations. If not set, *maxima’s* general
expression ring will be used. This variable may be set to
`ring_of_integers` if desired.

### Function: poly_colon_ideal (polylist1, polylist2, varlist)

Returns the reduced Groebner basis of the colon ideal 


$I(polylist1):I(polylist2)$



where $polylist1$ and $polylist2$ are two lists of polynomials.

### Function: poly_content (poly, ., varlist)

`poly_content` extracts the GCD of its coefficients


```maxima
(%i1) poly_content(35*y+21*x,[x,y]);
(%o1)                                  7
```

### Function: poly_depends_p (poly, var, varlist)

`poly_depends` tests whether a polynomial depends on a variable *var*.

### Function: poly_elimination_ideal (polylist, number, varlist)

`poly_elimination_ideal` returns the grobner basis of the $number$-th elimination ideal of an
ideal specified as a list of generating polynomials (not necessarily Groebner basis).

### Variable: poly_elimination_order

Default value: `false`


Name of the default elimination order used in elimination
calculations. If set, it overrides the settings in variables
`poly_primary_elimination_order` and `poly_secondary_elimination_order`.
The user must ensure that this is a true elimination order valid
for the number of eliminated variables.

### Function: poly_exact_divide (poly1, poly2, varlist)

Divide a polynomial *poly1* by another polynomial *poly2*. Assumes that exact
division with no remainder is possible. Returns the quotient.

### Function: poly_expand (poly, varlist)

This function parses polynomials to internal form and back. It
is equivalent to `expand(poly)` if *poly* parses correctly to
a polynomial. If the representation is not compatible with a
polynomial in variables *varlist*, the result is an error.
It can be used to test whether an expression correctly parses to the
internal representation. The following examples illustrate that
indexed and transcendental function variables are allowed.


```maxima
(%i1) poly_expand((x-y)*(y+x),[x,y]);
                                     2    2
(%o1)                               x  - y
(%i2) poly_expand((y+x)^2,[x,y]);
                                2            2
(%o2)                          y  + 2 x y + x
(%i3) poly_expand((y+x)^5,[x,y]);
                  5      4         2  3       3  2      4      5
(%o3)            y  + 5 x y  + 10 x  y  + 10 x  y  + 5 x  y + x
(%i4) poly_expand(-1-x*exp(y)+x^2/sqrt(y),[x]);
                                          2
                                  y      x
(%o4)                       - x %e  + ------- - 1
                                       sqrt(y)

(%i5) poly_expand(-1-sin(x)^2+sin(x),[sin(x)]);
                                2
(%o5)                      - sin (x) + sin(x) - 1
```

### Function: poly_expt (poly, number, varlist)

exponentitates *poly* by a positive integer *number*. If *number* is not a positive integer number an error will be raised.


```maxima
(%i1) poly_expt(x-y,3,[x,y])-(x-y)^3,expand;
(%o1)                                  0
```

### Function: poly_gcd (poly1, poly2, varlist)

Returns the greatest common divisor of *poly1* and *poly2*.


See also `ezgcd`, `gcd`, `gcdex`, and
`gcdivide`.


Example:



```maxima
(%i1) p1:6*x^3+19*x^2+19*x+6; 
                        3       2
(%o1)                6 x  + 19 x  + 19 x + 6
(%i2) p2:6*x^5+13*x^4+12*x^3+13*x^2+6*x;
                  5       4       3       2
(%o2)          6 x  + 13 x  + 12 x  + 13 x  + 6 x
(%i3) poly_gcd(p1, p2, [x]);
                            2
(%o3)                    6 x  + 13 x + 6
```

See also: `ezgcd`, `gcd`, `gcdex`, `gcdivide`.

### Function: poly_grobner (polylist, varlist)

Returns a Groebner basis of the ideal span by the polynomials *polylist*. Affected by the global flags.

### Variable: poly_grobner_algorithm

Default value: `buchberger`


Possible values: 


- * 
`buchberger`
- * 
`parallel_buchberger`
- * 
`gebauer_moeller`


The name of the algorithm used to find the Groebner Bases.

### Variable: poly_grobner_debug

Default value: `false`


If set to `true`, produce debugging and tracing output.

### Function: poly_grobner_equal (polylist1, polylist2, varlist)

`poly_grobner_equal` tests whether two Groebner Bases generate the same ideal.
Returns `true` if two lists of polynomials *polylist1* and *polylist2*, assumed to be Groebner Bases,
generate the same ideal, and `false` otherwise.
This is equivalent to checking that every polynomial of the first basis reduces to 0
modulo the second basis and vice versa. Note that in the example below the
first list is not a Groebner basis, and thus the result is `false`.



```maxima
(%i1) poly_grobner_equal([y+x,x-y],[x,y],[x,y]);
(%o1)                         false
```

### Function: poly_grobner_member (poly, polylist, varlist)

Returns `true` if a polynomial *poly* belongs to the ideal generated by the
polynomial list *polylist*, which is assumed to be a Groebner basis. Returns `false` otherwise.


`poly_grobner_member` tests whether a polynomial belongs to an ideal generated by a list of polynomials,
which is assumed to be a Groebner basis. Equivalent to `normal_form` being 0.

### Function: poly_grobner_subsetp (polylist1, polylist2, varlist)

`poly_grobner_subsetp` tests whether an ideal generated by *polylist1*
is contained in the ideal generated by *polylist2*. For this test to always succeed,
*polylist2* must be a Groebner basis.

### Function: poly_ideal_intersection (polylist1, polylist2, varlist)

`poly_ideal_intersection` returns the intersection of two ideals.

### Function: poly_ideal_polysaturation (polylist, polylistlist, varlist)

*polylistlist* is a list of n list of polynomials `[polylist1,...,polylistn]`.
Returns the reduced Groebner basis of the saturation of the ideal


I(polylist):I(polylist_1)^inf:...:I(polylist_n)^inf

### Function: poly_ideal_polysaturation1 (polylist1, polylist2, varlist)

*polylist2* is a list of n polynomials `[poly1,...,polyn]`.
Returns the reduced Groebner basis of the ideal


I(polylist):poly1^inf:...:polyn^inf



obtained by a
sequence of successive saturations in the polynomials
of the polynomial list *polylist2* of the ideal generated by the
polynomial list *polylist1*.

### Function: poly_ideal_saturation (polylist1, polylist2, varlist)

Returns the reduced Groebner basis of the saturation of the ideal


I(polylist1):I(polylist2)^inf



Geometrically, over an algebraically closed field, this is the set of polynomials in
the ideal generated by *polylist1* which do not identically vanish on the
variety of *polylist2*.

### Function: poly_ideal_saturation1 (polylist, poly, varlist)

Returns the reduced Groebner basis of the saturation of the ideal


I(polylist):poly^inf



Geometrically, over an algebraically closed field, this is the set
of polynomials in the ideal generated by *polylist* which do not identically
vanish on the variety of *poly*.

### Function: poly_lcm (poly1, poly2, varlist)

Returns the lowest common multiple of *poly1* and *poly2*.

### Function: poly_minimization (polylist, varlist)

Returns a sublist of the polynomial list *polylist* spanning the same
monomial ideal as *polylist* but minimal, i.e. no leading monomial
of a polynomial in the sublist divides the leading monomial
of another polynomial.

### Variable: poly_monomial_order

Default value: `lex`


This global switch controls which monomial order is used in polynomial and Groebner Bases calculations. If not set, `lex` will be used.

### Function: poly_multiply (poly1, poly2, varlist)

Returns the product of polynomials *poly1* and *poly2*.


```maxima
(%i2) poly_multiply(z+x^2*y,x-z,[x,y,z])-(z+x^2*y)*(x-z),expand;
(%o1)                                  0
```

### Function: poly_normal_form (poly, polylist, varlist)

`poly_normal_form` finds the normal form of a polynomial *poly* with respect
to a set of polynomials *polylist*.

### Function: poly_normalize (poly, varlist)

Returns the polynomial *poly* divided by the leading coefficient.
It assumes that the division is possible, which may not always be the
case in rings which are not fields.

### Function: poly_normalize_list (polylist, varlist)

`poly_normalize_list` applies `poly_normalize` to each polynomial in the list.
That means it divides every polynomial in a list *polylist* by its leading coefficient.

### Function: poly_polysaturation_extension (poly, polylist, varlist1, varlist2)

### Variable: poly_primary_elimination_order

Default value: `false`


Name of the default order for eliminated variables in
elimination-based functions. If not set, `lex` will be used.

### Function: poly_primitive_part (poly1, varlist)

Returns the polynomial *poly* divided by the GCD of its coefficients. 



```maxima
(%i1) poly_primitive_part(35*y+21*x,[x,y]);
(%o1)                              5 y + 3 x
```

### Function: poly_pseudo_divide (poly, polylist, varlist)

Pseudo-divide a polynomial *poly* by the list of $n$ polynomials *polylist*. Return
multiple values. The first value is a list of quotients $a$. The
second value is the remainder $r$. The third argument is a scalar
coefficient $c$, such that $c*poly$ can be divided by *polylist* within the ring
of coefficients, which is not necessarily a field. Finally, the
fourth value is an integer count of the number of reductions
performed. The resulting objects satisfy the equation:


$c*poly=sum(a[i]*polylist[i],i=1...n)+r$.

### Function: poly_reduced_grobner (polylist, varlist)

Returns a reduced Groebner basis of the ideal span by the polynomials *polylist*. Affected by the global flags.

### Function: poly_reduction (polylist, varlist)

`poly_reduction` reduces a list of polynomials *polylist*, so that
each polynomial is fully reduced with respect to the other polynomials.

### Variable: poly_return_term_list

Default value: `false`


If set to `true`, all functions in this package will return each
polynomial as a list of terms in the current monomial order rather
than a *maxima* general expression.

### Function: poly_s_polynomial (poly1, poly2, varlist)

Returns the *syzygy polynomial* (*S-polynomial*) of two polynomials *poly1* and *poly2*.

### Function: poly_saturation_extension (poly, polylist, varlist1, varlist2)

`poly_saturation_extension` implements the famous Rabinowitz trick.

### Variable: poly_secondary_elimination_order

Default value: `false`


Name of the default order for kept variables in elimination-based functions. If not set, `lex` will be used.

### Function: poly_subtract (poly1, poly2, varlist)

Subtracts a polynomial *poly2* from *poly1*.


```maxima
(%i1) poly_subtract(z+x^2*y,x-z,[x,y,z]);
                                      2
(%o1)                          2 z + x  y - x
```

### Variable: poly_top_reduction_only

Default value: `false`


If not `false`, use top reduction only whenever possible. Top
reduction means that division algorithm stops after the first
reduction.

### Function: polydecomp (p, x)

Decomposes the polynomial *p* in the variable *x*
into the functional composition of polynomials in *x*.
`polydecomp` returns a list `[p_1, ..., p_n]` such that



```maxima
lambda ([x], p_1) (lambda ([x], p_2) (... (lambda ([x], p_n) (x))
  ...))
```


is equal to *p*.
The degree of *p_i* is greater than 1 for *i* less than *n*.


Such a decomposition is not unique.


Examples:








```maxima
maxima

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


The following function composes `L = [e_1, ..., e_n]` as functions in
`x`; it is the inverse of polydecomp:







```maxima
maxima

(%i1) compose (L, x) :=
  block ([r : x], for e in L do r : subst (e, x, r), r) $
```


Re-express above example using `compose`:








```maxima
maxima

(%i1) compose (L, x) :=
  block ([r : x], for e in L do r : subst (e, x, r), r) $


(%i2) polydecomp (compose ([x^2 - a, x^3 - x - 1], x), x);
                        2       3
(%o2)                 [x  - a, x  - x - 1]
```


Note that though `compose (polydecomp (p, x), x)` always
returns *p* (unexpanded), `polydecomp (compose ([p_1, ..., p_n], x), x)` does *not* necessarily return
`[p_1, ..., p_n]`:









```maxima
maxima

(%i1) compose (L, x) :=
  block ([r : x], for e in L do r : subst (e, x, r), r) $


(%i2) polydecomp (compose ([x^2 + 2*x + 3, x^2], x), x);
                          2       2
(%o2)                   [x  + 2, x  + 1]


(%i3) polydecomp (compose ([x^2 + x + 1, x^2 + x + 1], x), x);
                      2       2
                     x  + 3  x  + 5
(%o3)               [------, ------, 2 x + 1]
                       4       2
```

### Function: polymod (polymod, p, polymod, p, m)

Converts the polynomial *p* to a modular representation with respect to the
current modulus which is the value of the variable `modulus`.


`polymod (p, m)` specifies a modulus *m* to be used 
instead of the current value of `modulus`.


See `modulus`.

See also: `modulus`.

### Function: polynomialp (polynomialp, p, L, coeffp, exponp, polynomialp, p, L, coeffp, polynomialp, p, L)

Return `true` if *p* is a polynomial in the variables in the list
*L*.  The predicate *coeffp* must evaluate to `true` for each
coefficient, and the predicate *exponp* must evaluate to `true` for all
exponents of the variables in *L*.  If you want to use a non-default value
for *exponp*, you must supply *coeffp* with a value even if you want
to use the default for *coeffp*.



The command `polynomialp (p, L, coeffp)` is equivalent to
`polynomialp (p, L, coeffp, 'nonnegintegerp)` and the
command `polynomialp (p, L)` is equivalent to
`polynomialp (p, L, 'constantp, 'nonnegintegerp)`.


The polynomial needn’t be expanded:







```maxima
maxima

(%i1) polynomialp ((x + 1)*(x + 2), [x]);
(%o1)                         true


(%i2) polynomialp ((x + 1)*(x + 2)^a, [x]);
(%o2)                         false
```


An example using non-default values for coeffp and exponp:








```maxima
maxima

(%i1) polynomialp ((x + 1)*(x + 2)^(3/2), [x], numberp, numberp);
(%o1)                         true


(%i2) polynomialp ((x^(1/2) + 1)*(x + 2)^(3/2), [x], numberp,
                                                       numberp);
(%o2)                         true
```


Polynomials with two variables:







```maxima
maxima

(%i1) polynomialp (x^2 + 5*x*y + y^2, [x]);
(%o1)                         false


(%i2) polynomialp (x^2 + 5*x*y + y^2, [x, y]);
(%o2)                         true
```


Polynomial in one variable and accepting any expression free of `x` as a coefficient.







```maxima
maxima

(%i1) polynomialp (a*x^2 + b*x + c, [x]);
(%o1)                         false


(%i2) polynomialp (a*x^2 + b*x + c, [x], lambda([ex], freeof(x, ex)));
(%o2)                         true
```

### Function: primelmt (f_b, p_a, c)

Computes a prime element for the extension of $K[a]$ by a root
*b* of a polynomial $f_b(b)$ whose coefficients may depend on
*a*. One assumes that *f_b* is square free. The function returns
an irreducible polynomial, a root of which generates $K[a, b]$, and
the expression of this primitive element in terms of *a* and
*b*.


Examples:



```maxima
(%i1) primelmt(b^2 - a*b - 1, a^2 - 2, c);
                              4       2
(%o1)                       [c  - 12 c  + 9, b + a]
(%i2) solve(b^2 - sqrt(2)*b - 1)[1];
                                  sqrt(6) - sqrt(2)
(%o2)                       b = - -----------------
                                          2
(%i3) primelmt(b^2 - 3, a^2 - 2, c);
                              4       2
(%o3)                       [c  - 10 c  + 1, b + a]
(%i4) factor(c^4 - 12*c^2 + 9, a^4 - 10*a^2 + 1);
                 3    2                       3    2
(%o4) ((4 c - 3 a  - a  + 27 a + 5) (4 c - 3 a  + a  + 27 a - 5)
                           3    2                       3    2
                 (4 c + 3 a  - a  - 27 a + 5) (4 c + 3 a  + a  - 27 a - 5))/256
(%i5) primelmt(b^3 - 3, a^2 - 2, c);
                   6      4      3       2
(%o5)            [c  - 6 c  - 6 c  + 12 c  - 36 c + 1, b + a]
(%i6) factor(b^3 - 3, %[1]);
            5       4        3        2
(%o6) ((48 c  + 27 c  - 320 c  - 468 c  + 124 c + 755 b - 1092)
           5        5         4       4          3        3          2        2
 ((- 48 b c ) - 54 c  - 27 b c  + 64 c  + 320 b c  + 360 c  + 468 b c  + 149 c
                           2
 - 124 b c - 1272 c + 755 b  + 1092 b + 1606))/570025
```


In (%o1), *f_b* depends on `a`. Using `solve`, the solution depends on sqrt(2) and sqrt(3).
In (%o3), $K[sqrt(2), sqrt(3)]$ is computed, and we see that the the primitive polynomial
in (%o1) factorizes completely here. In (%i5), we compute $K[sqrt(2), 3^{1/3}]$, and we see
that `b^3 - 3` gets one factor in this extension. If we assume this extension is real,
the two other factors are complex.

### Function: quotient (quotient, p_1, p_2, quotient, p_1, p_2, x_1, ..., x_n)

Returns the polynomial *p_1* divided by the polynomial *p_2*.  The
arguments *x_1*, ..., *x_n* are interpreted as in `ratvars`.


`quotient` returns the first element of the two-element list returned by
`divide`.

See also: `divide`.

### Variable: radsubstflag

Default value: `false`


`radsubstflag`, if `true`, permits `ratsubst` to make
substitutions such as `u` for `sqrt (x)` in `x`.

### Function: rat (rat, expr, rat, expr, x_1, ..., x_n)

Converts *expr* to canonical rational expression (CRE) form by expanding and
combining all terms over a common denominator and cancelling out the
greatest common divisor of the numerator and denominator, as well as
converting floating point numbers to rational numbers within a
tolerance of `ratepsilon`.
The variables are ordered according
to the *x_1*, ..., *x_n*, if specified, as in `ratvars`.


`rat` does not generally simplify functions other than addition `+`,
subtraction `-`, multiplication `*`, division `/`, and
exponentiation to an integer power,
whereas `ratsimp` does handle those cases.
Note that atoms (numbers and variables) in CRE form are not the
same as they are in the general form.
For example, `rat(x)- x` yields 
`rat(0)` which has a different internal representation than 0.



When `ratfac` is `true`, `rat` yields a partially factored
form for CRE.  During rational operations the expression is
maintained as fully factored as possible without an actual call to the
factor package.  This should always save space and may save some time
in some computations.  The numerator and denominator are still made
relatively prime
(e.g.,  `rat((x^2 - 1)^4/(x + 1)^2)` yields `(x - 1)^4 (x + 1)^2`
when `ratfac` is `true`),
but the factors within each part may not be relatively prime.


`ratprint` if `false` suppresses the printout of the message
informing the user of the conversion of floating point numbers to
rational numbers.


`keepfloat` if `true` prevents floating point numbers from being
converted to rational numbers.


See also `ratexpand` and  `ratsimp`.


Examples:







```maxima
maxima

(%i1) ((x - 2*y)^4/(x^2 - 4*y^2)^2 + 1)*(y + a)*(2*y + x) /
      (4*y^2 + x^2);
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

### Variable: ratalgdenom

Default value: `true`


When `ratalgdenom` is `true`, allows rationalization of denominators
with respect to radicals to take effect.  `ratalgdenom` has an effect only
when canonical rational expressions (CRE) are used in algebraic mode.

### Function: ratcoef (ratcoef, expr, x, n, ratcoef, expr, x)

Returns the coefficient of the expression `x^n`
in the expression *expr*.
If omitted, *n* is assumed to be 1.


The return value is free
(except possibly in a non-rational sense) of the variables in *x*.
If no coefficient of this type exists, 0 is returned.


`ratcoef`
expands and rationally simplifies its first argument and thus it may
produce answers different from those of `coeff` which is purely
syntactic.

Thus `ratcoef ((x + 1)/y + x, x)` returns `(y + 1)/y` whereas
`coeff` returns 1.


`ratcoef (expr, x, 0)`, viewing *expr* as a sum,
returns a sum of those terms which do not contain *x*.

Therefore if *x* occurs to any negative powers, `ratcoef` should not
be used.



Since *expr* is rationally
simplified before it is examined, coefficients may not appear quite
the way they were envisioned.


Example:







```maxima
maxima
(%i1) s: a*x + b*x + 5$

(%i2) ratcoef (s, a + b);
(%o2)                           x
```

### Function: ratdenom (expr)

Returns the denominator of *expr*,
after coercing *expr* to a canonical rational expression (CRE).
The return value is a CRE.



*expr* is coerced to a CRE by `rat`
if it is not already a CRE.
This conversion may change the form of *expr* by putting all terms
over a common denominator.


`denom` is similar, but returns an ordinary expression instead of a CRE.
Also, `denom` does not attempt to place all terms over a common
denominator, and thus some expressions which are considered ratios by
`ratdenom` are not considered ratios by `denom`.

### Variable: ratdenomdivide

Default value: `true`


When `ratdenomdivide` is `true`,
`ratexpand` expands a ratio in which the numerator is a sum 
into a sum of ratios,
all having a common denominator.
Otherwise, `ratexpand` collapses a sum of ratios into a single ratio,
the numerator of which is the sum of the numerators of each ratio.


Examples:












```maxima
maxima

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

### Function: ratdiff (expr, x)

Differentiates the rational expression *expr* with respect to *x*.
*expr* must be a ratio of polynomials or a polynomial in *x*.
The argument *x* may be a variable or a subexpression of *expr*.





The result is equivalent to `diff`, although perhaps in a different form.
`ratdiff` may be faster than `diff`, for rational expressions.


`ratdiff` returns a canonical rational expression (CRE) if `expr` is
a CRE.  Otherwise, `ratdiff` returns a general expression.


`ratdiff` considers only the dependence of *expr* on *x*,
and ignores any dependencies established by `depends`.







Example:











```maxima
maxima

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

### Function: ratdisrep (expr)

Returns its argument as a general expression.
If *expr* is a general expression, it is returned unchanged.


Typically `ratdisrep` is called to convert a canonical rational expression
(CRE) into a general expression.

This is sometimes convenient if one wishes to stop the "contagion", or
use rational functions in non-rational contexts.


See also `totaldisrep`.

See also: `totaldisrep`.

### Function: ratexpand (expr)

Expands *expr* by multiplying out products of sums and
exponentiated sums, combining fractions over a common denominator,
cancelling the greatest common divisor of the numerator and
denominator, then splitting the numerator (if a sum) into its
respective terms divided by the denominator.


The return value of `ratexpand` is a general expression,
even if *expr* is a canonical rational expression (CRE).



The switch `ratexpand` if `true` will cause CRE
expressions to be fully expanded when they are converted back to
general form or displayed, while if it is `false` then they will be put
into a recursive form.
See also `ratsimp`.


When `ratdenomdivide` is `true`,
`ratexpand` expands a ratio in which the numerator is a sum 
into a sum of ratios,
all having a common denominator.
Otherwise, `ratexpand` collapses a sum of ratios into a single ratio,
the numerator of which is the sum of the numerators of each ratio.


When `keepfloat` is `true`, prevents floating
point numbers from being rationalized when expressions which contain
them are converted to canonical rational expression (CRE) form.


Examples:









```maxima
maxima

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

See also: `ratsimp`.

### Variable: ratfac

Default value: `false`


When `ratfac` is `true`, canonical rational expressions (CRE) are
manipulated in a partially factored form.


During rational operations the expression is maintained as fully factored as
possible without calling `factor`.
This should always save space and may save time in some computations.
The numerator and denominator are made relatively prime, for example
`factor ((x^2 - 1)^4/(x + 1)^2)` yields `(x - 1)^4 (x + 1)^2`,
but the factors within each part may not be relatively prime.


In the `ctensor` (Component Tensor Manipulation) package,
Ricci, Einstein, Riemann, and Weyl tensors and the scalar curvature 
are factored automatically when `ratfac` is `true`.
*`ratfac` should only be
set for cases where the tensorial components are known to consist of
few terms.*


The `ratfac` and `ratweight` schemes are incompatible and may not
both be used at the same time.

### Function: ratnumer (expr)

Returns the numerator of *expr*,
after coercing *expr* to a canonical rational expression (CRE).
The return value is a CRE.



*expr* is coerced to a CRE by `rat`
if it is not already a CRE.
This conversion may change the form of *expr* by putting all terms
over a common denominator.


`num` is similar, but returns an ordinary expression instead of a CRE.
Also, `num` does not attempt to place all terms over a common denominator,
and thus some expressions which are considered ratios by `ratnumer`
are not considered ratios by `num`.

### Function: ratp (expr)

Returns `true` if *expr* is a canonical rational expression (CRE) or
extended CRE, otherwise `false`.


CRE are created by `rat` and related functions.
Extended CRE are created by `taylor` and related functions.

### Function: ratp_coeffs (expr, x)

Returns the powers and coefficients of *x* in `ratnumer(expr)` as a list of length-2 lists;
returned coefficients are in CRE form except for numbers.



`ratnumer(expr)`.






```maxima
(%i1) load("ratpow")$

(%i2) ratp_coeffs( 4*x^3 + x + sqrt(x), x);
(%o2)/R/         [[3, 4], [1, 1], [0, sqrt(x)]]
```

### Function: ratp_dense_coeffs (expr, x)

Returns the coefficients of powers of *x* in `ratnumer(expr)` from highest to lowest;
returned coefficients are in CRE form except for numbers.







```maxima
(%i1) load("ratpow")$

(%i2) ratp_dense_coeffs( 4*x^3 + x + sqrt(x), x);
(%o2)/R/               [4, 0, 1, sqrt(x)]
```

### Function: ratp_hipow (expr, x)

Returns the highest power of *x* in `ratnumer(expr)`








```maxima
(%i1) load("ratpow")$

(%i2) ratp_hipow( x^(5/2) + x^2 , x);
(%o2)                           2


(%i3) ratp_hipow( x^(5/2) + x^2 , sqrt(x));
(%o3)                           5
```

### Function: ratp_lopow (expr, x)

Returns the lowest power of *x* in `ratnumer(expr)`







```maxima
(%i1) load("ratpow")$

(%i2) ratp_lopow( x^5 + x^2 , x);
(%o2)                           2
```


The following example returns 0 since `1` equals `x^0`:






```maxima
(%i1) load("ratpow")$

(%i2) ratp_lopow( x^5 + x^2 + 1, x);
(%o2)                           0
```


The CRE form of the following equation contains `sqrt(x)` and
`x`. Since they are interpreted as independent variables,
`ratp_lopow` returns `0`:









```maxima
(%i1) load("ratpow")$

(%i2) g:sqrt(x)^5 + sqrt(x)^2;
                             5/2
(%o2)                       x    + x


(%i3) showratvars(g);
                              1/2
(%o3)                       [x   , x]


(%i4) ratp_lopow( g, x);
(%o4)                           0


(%i5) ratp_lopow( g, sqrt(x));
(%o5)                           0
```

### Variable: ratprint

Default value: `true`


When `ratprint` is `true`,
a message informing the user of the conversion of floating point numbers
to rational numbers is displayed.

### Function: ratsimp (ratsimp, expr, ratsimp, expr, x_1, ..., x_n)

Simplifies the expression *expr* and all of its subexpressions, including
the arguments to non-rational functions.  The result is returned as the quotient
of two polynomials in a recursive form, that is, the coefficients of the main
variable are polynomials in the other variables.  Variables may include
non-rational functions (e.g., `sin (x^2 + 1)`) and the arguments to any
such functions are also rationally simplified.


`ratsimp (expr, x_1, ..., x_n)`
enables rational simplification with the
specification of variable ordering as in `ratvars`.


When `ratsimpexpons` is `true`,
`ratsimp` is applied to the exponents of expressions during simplification.


See also `ratexpand`.
Note that `ratsimp` is affected by some of the
flags which affect `ratexpand`.


Examples:










```maxima
maxima

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

See also: `ratexpand`.

### Variable: ratsimpexpons

Default value: `false`


When `ratsimpexpons` is `true`,
`ratsimp` is applied to the exponents of expressions during simplification.

### Function: ratsubst (a, b, c)

Substitutes *a* for *b* in *c* and returns the resulting expression.

*b* may be a sum, product, power, etc.



`ratsubst` knows something of the meaning of expressions
whereas `subst` does a purely syntactic substitution.
Thus `subst (a, x + y, x + y + z)` returns `x + y + z`
whereas `ratsubst` returns `z + a`.


When `radsubstflag` is `true`,
`ratsubst` makes substitutions for radicals in expressions
which don’t explicitly contain them.


`ratsubst` ignores the value `true` of the option variables
`keepfloat`, `float`, and `numer`.


Examples:
















```maxima
maxima

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

### Function: ratvars (ratvars, x_1, ..., x_n, ratvars)

Declares main variables *x_1*, ..., *x_n* for rational expressions.
*x_n*, if present in a rational expression, is considered the main variable.
Otherwise, *x_[n-1]* is considered the main variable if present, and so on
through the preceding variables to *x_1*, which is considered the main
variable only if none of the succeeding variables are present.


If a variable in a rational expression is not present in the `ratvars`
list, it is given a lower priority than *x_1*.


The arguments to `ratvars` can be either variables or non-rational
functions such as `sin(x)`.


The variable `ratvars` is a list of the arguments of 
the function `ratvars` when it was called most recently.
Each call to the function `ratvars` resets the list.
`ratvars ()` clears the list.

### Variable: ratvarswitch

Default value: `true`


Maxima keeps an internal list in the Lisp variable `VARLIST` of the main
variables for rational expressions.  If `ratvarswitch` is `true`, 
every evaluation starts with a fresh list `VARLIST`.  This is the default
behavior.  Otherwise, the main variables from previous evaluations are not 
removed from the internal list `VARLIST`.


The main variables, which are declared with the function `ratvars` are
not affected by the option variable `ratvarswitch`.


Examples:


If `ratvarswitch` is `true`, every evaluation starts with a fresh
list `VARLIST`.










```maxima
maxima
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


If `ratvarswitch` is `false`, the main variables from the last 
evaluation are still present.










```maxima
maxima
(%i1) ratvarswitch:false$

(%i2) rat(2*x+y^2);
                             2
(%o2)/R/                    y  + 2 x


(%i3) :lisp varlist
($X $Y)


(%i3) rat(2*a+b^2);
                             2
(%o3)/R/                    b  + 2 a


(%i4) :lisp varlist
($A $B $X $Y)
```

### Function: ratweight (ratweight, x_1, w_1, ..., x_n, w_n, ratweight)

Assigns a weight *w_i* to the variable *x_i*.
This causes a term to be replaced by 0 if its weight exceeds the
value of the variable `ratwtlvl` (default yields no truncation).
The weight of a term is the sum of the products of the
weight of a variable in the term times its power.
For example, the weight of `3 x_1^2 x_2` is `2 w_1 + w_2`.
Truncation according to `ratwtlvl` is carried out only when multiplying
or exponentiating canonical rational expressions (CRE).


`ratweight ()` returns the cumulative list of weight assignments.


Note: The `ratfac` and `ratweight` schemes are incompatible and may
not both be used at the same time.


Examples:










```maxima
maxima

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

### Variable: ratweights

Default value: `[]`


`ratweights` is the list of weights assigned by `ratweight`.
The list is cumulative:
each call to `ratweight` places additional items in the list.



`kill (ratweights)` and `save (ratweights)` both work as expected.

### Variable: ratwtlvl

Default value: `false`


`ratwtlvl` is used in combination with the `ratweight`
function to control the truncation of canonical rational expressions (CRE).
For the default value of `false`, no truncation occurs.

### Function: remainder (remainder, p_1, p_2, remainder, p_1, p_2, x_1, ..., x_n)

Returns the remainder of the polynomial *p_1* divided by the polynomial
*p_2*.  The arguments *x_1*, ..., *x_n* are interpreted as in
`ratvars`.


`remainder` returns the second element
of the two-element list returned by `divide`.

### Function: resultant (p_1, p_2, x)

The function `resultant` computes the resultant of the two polynomials
*p_1* and *p_2*, eliminating the variable *x*.  The resultant is a
determinant of the coefficients of *x* in *p_1* and *p_2*, which
equals zero if and only if *p_1* and *p_2* have a non-constant factor
in common.


If *p_1* or *p_2* can be factored, it may be desirable to call
`factor` before calling `resultant`.


The option variable `resultant` controls which algorithm will be used to
compute the resultant.  See the option variable
`option_005fresultant`.


The function `bezout` takes the same arguments as `resultant` and
returns a matrix.  The determinant of the return value is the desired resultant.


Examples:











```maxima
maxima

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

See also: `factor`, `option_resultant`, `bezout`.

### Variable: savefactors

Default value: `false`



When `savefactors` is `true`, causes the factors of an
expression which is a product of factors to be saved by certain
functions in order to speed up later factorizations of expressions
containing some of the same factors.

### Function: showratvars (expr)

Returns a list of the canonical rational expression (CRE) variables in
expression `expr`.


See also `ratvars`.

See also: `ratvars`.

### Function: spherical_bessel_j (n, x)

The spherical Bessel function of the first kind, 
$j_n(x).$


Reference: [https://personal.math.ubc.ca/~cbm/aands/page_437.htmA&S eqn 10.1.8]() and [https://personal.math.ubc.ca/~cbm/aands/page_439.htmA&S eqn 10.1.15]().


It is related to the Bessel function by



$$j_n(x) = \sqrt{\pi\over 2x} J_{n+1/2}(x)$$


$$j_n(x) = \sqrt{\pi\over 2x} J_{n+1/2}(x)$$



Some examples:








```maxima
(%i1) spherical_bessel_j(1,x);
                                sin(x)
                                ------ - cos(x)
                                  x
(%o1)                           ---------------
                                       x
(%i2) spherical_bessel_j(2,x);
                                3             3 cos(x)
                        (- (1 - --) sin(x)) - --------
                                 2               x
                                x
(%o2)                   ------------------------------
                                      x
(%i3) expand(%);
                          sin(x)    3 sin(x)   3 cos(x)
(%o3)                  (- ------) + -------- - --------
                            x           3          2
                                       x          x
(%i4) expand(sqrt(%pi/(2*x))*bessel_j(2+1/2,x)),besselexpand:true;
                          sin(x)    3 sin(x)   3 cos(x)
(%o4)                  (- ------) + -------- - --------
                            x           3          2
                                       x          x
```

### Function: spherical_bessel_y (n, x)

The spherical Bessel function of the second kind, 
$y_n(x).$


Reference: [https://personal.math.ubc.ca/~cbm/aands/page_437.htmA&S eqn 10.1.9]() and [https://personal.math.ubc.ca/~cbm/aands/page_439.htmA&S eqn 10.1.15]().


It is related to the Bessel function by



$$y_n(x) = \sqrt{\pi\over 2x} Y_{n+1/2}(x)$$


$$y_n(x) = \sqrt{\pi\over 2x} Y_{n+1/2}(x)$$










```maxima
(%i1) spherical_bessel_y(1,x);
                                           cos(x)
                              (- sin(x)) - ------
                                             x
(%o1)                         -------------------
                                       x
(%i2) spherical_bessel_y(2,x);
                           3 sin(x)        3
                           -------- - (1 - --) cos(x)
                              x             2
                                           x
(%o2)                    - --------------------------
                                       x
(%i3) expand(%);
                          3 sin(x)    cos(x)   3 cos(x)
(%o3)                  (- --------) + ------ - --------
                              2         x          3
                             x                    x
(%i4) expand(sqrt(%pi/(2*x))*bessel_y(2+1/2,x)),besselexpand:true;
                          3 sin(x)    cos(x)   3 cos(x)
(%o4)                  (- --------) + ------ - --------
                              2         x          3
                             x                    x
```

### Function: spherical_hankel1 (n, x)

The spherical Hankel function of the
first kind, 
$h_n^{(1)}(x).$


Reference: [https://personal.math.ubc.ca/~cbm/aands/page_439.htmA&S eqn 10.1.36]().


This is defined by



$$h_n^{(1)}(x) = j_n(x) + iy_n(x)$$


$$h_n^{(1)}(x) = j_n(x) + iy_n(x)$$



See also `orthopoly_returns_intervals` for how numerical results
are returned.

See also: `orthopoly_returns_intervals`.

### Function: spherical_hankel2 (n, x)

The spherical Hankel function of the
second kind, 
$h_n^{(2)}(x).$


Reference: [https://personal.math.ubc.ca/~cbm/aands/page_439.htmA&S eqn 10.1.17]().


This is defined by



$$h_n^{(2)}(x) = j_n(x) + iy_n(x)$$


$$h_n^{(2)}(x) = j_n(x) + iy_n(x)$$



See also `orthopoly_returns_intervals` for how numerical results
are returned.

See also: `orthopoly_returns_intervals`.

### Function: spherical_harmonic (n, m, theta, phi)

The spherical harmonic function, 
$Y_n^m(\theta, \phi).$


Spherical harmonics satisfy the angular part of Laplace’s equation in spherical coordinates.


For integers $n$ and $m$ such
that 
$n \geq |m|$
and
for 
$\theta \in [0, \pi].$
Maxima’s
spherical harmonic function can be defined by



$$Y_n^m(\theta, \phi) = (-1)^m \sqrt{{2n+1\over 4\pi} {(n-m)!\over (n+m)!}} P_n^m(\cos\theta) e^{im\phi}$$


$$Y_n^m(\theta, \phi) = (-1)^m \sqrt{{2n+1\over 4\pi} {(n-m)!\over (n+m)!}} P_n^m(\cos\theta) e^{im\phi}$$


 

Further, when 
$n < |m|,$
the
spherical harmonic function vanishes.


The factor $(-1)^m$, frequently used in Quantum mechanics, is
called the [https://en.wikipedia.org/wiki/Spherical_harmonics#Condon%E2%80%93Shortley_phaseCondon-Shortely phase]().
Some references, including *NIST Digital Library of Mathematical Functions* omit
this factor; see [http://dlmf.nist.gov/14.30.E1]().


Reference: Merzbacher 9.64.


Some examples:









```maxima
(%i1) spherical_harmonic(1,0,theta,phi);
                              sqrt(3) cos(theta)
(%o1)                         ------------------
                                 2 sqrt(%pi)
(%i2) spherical_harmonic(1,1,theta,phi);
                                    %i phi
                          sqrt(3) %e       sin(theta)
(%o2)                     ---------------------------
                                 3/2
                                2    sqrt(%pi)
(%i3) spherical_harmonic(1,-1,theta,phi);
                                    - %i phi
                          sqrt(3) %e         sin(theta)
(%o3)                   - -----------------------------
                                  3/2
                                 2    sqrt(%pi)
(%i4) spherical_harmonic(2,0,theta,phi);
                                                              2
                                            3 (1 - cos(theta))
          sqrt(5) ((- 3 (1 - cos(theta))) + ------------------- + 1)
                                                     2
(%o4)     ----------------------------------------------------------
                                 2 sqrt(%pi)
(%i5) factor(%);
                                        2
                          sqrt(5) (3 cos (theta) - 1)
(%o5)                     ---------------------------
                                  4 sqrt(%pi)
```


See also `orthopoly_returns_intervals` for how numerical results
are returned.

See also: `orthopoly_returns_intervals`.

### Function: splitfield (p, x)

Computes the splitting field of the polynomial $p(x)$.
In the generic case it is of degree $n!$ in terms of the degree $n$
of *p*, but may be of lower order if the Galois group of *p*
is a strict subgroup of the group of permutations of $n$
elements. The function returns a primitive polynomial for this extension
and the expressions of the roots of *p* as polynomials of a root
of this primitive polynomial. The polynomial *f* may be
irreducible or factorizable.


Examples:



```maxima
(%i1) splitfield(x^3 + x + 1, x);
                                              4         2
              6         4         2       alg1  + 5 alg1  - 9 alg1 + 4
(%o1)/R/ [alg1  + 6 alg1  + 9 alg1  + 31, ----------------------------, 
                                                       18
                                 4         2          4         2
                             alg1  + 5 alg1  + 4  alg1  + 5 alg1  + 9 alg1 + 4
                           - -------------------, ----------------------------]
                                      9                        18
(%i2) splitfield(x^4 + 10*x^2 - 96*x - 71, x)[1];
             8           6           5            4             3
(%o2)/R/ alg2  + 148 alg2  - 576 alg2  + 9814 alg2  - 42624 alg2
                                                    2
                                       + 502260 alg2  + 1109952 alg2 + 18860337
```


In the first case we have the primitive polynomial of degree 6 and the 3 roots
of the third degree equations in terms of a variable `alg1` produced by
the system. In the second case the primitive polynomial is of degree 8
instead of 24, because the Galois group of the equation is reduced to D8
since there are relations between the roots.

### Function: sqfr (expr)

is similar to `factor` except that the polynomial factors are
"square-free."  That is, they have factors only of degree one.
This algorithm, which is also used by the first stage of `factor`, utilizes
the fact that a polynomial has in common with its n’th derivative all
its factors of degree greater than n.  Thus by taking greatest common divisors
with the polynomial of
the derivatives with respect to each variable in the polynomial, all
factors of degree greater than 1 can be found.


Example:






```maxima
maxima

(%i1) sqfr (4*x^4 + 4*x^3 - 3*x^2 - 4*x - 1);
                                2   2
(%o1)                  (2 x + 1)  (x  - 1)
```

See also: `factor`.

### Function: tellrat (tellrat, p_1, ..., p_n, tellrat)

Adds to the ring of algebraic integers known to Maxima
the elements which are the solutions of the polynomials *p_1*, ...,
*p_n*.  Each argument *p_i* is a polynomial with integer coefficients.


`tellrat (x)` effectively means substitute 0 for *x* in rational
functions.


`tellrat ()` returns a list of the current substitutions.


`algebraic` must be set to `true` in order for the simplification of
algebraic integers to take effect.


Maxima initially knows about the imaginary unit `%i`
and all roots of integers.


There is a command `untellrat` which takes kernels and
removes `tellrat` properties.


When `tellrat`’ing a multivariate
polynomial, e.g., `tellrat (x^2 - y^2)`, there would be an ambiguity as to
whether to substitute `y^2` for `x^2`
or vice versa.  
Maxima picks a particular ordering, but if the user wants to specify which, e.g.
`tellrat (y^2 = x^2)` provides a syntax which says replace
`y^2` by `x^2`.









Examples:











```maxima
maxima

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
                              3/2           3/2
              (7 sqrt(3) - 5 2    + 2) a - 2    - 1
(%o5)         -------------------------------------
                                7


(%i6) tellrat (y^2 = x^2);
                        2    2   2
(%o6)                 [y  - x , a  + a + 1]
```

### Function: totaldisrep (expr)

Converts every subexpression of *expr* from canonical rational expressions
(CRE) to general form and returns the result.
If *expr* is itself in CRE form then `totaldisrep` is identical to
`ratdisrep`.


`totaldisrep` may be useful for
ratdisrepping expressions such as equations, lists, matrices, etc., which
have some subexpressions in CRE form.

### Function: ultraspherical (n, a, x)

The ultraspherical polynomial, 
$C_n^{(a)}(x)$
(also known as the Gegenbauer polynomial).


Reference: [https://personal.math.ubc.ca/~cbm/aands/page_779.htmA&S eqn 22.5.46]().


These polynomials can be given in terms of Jacobi polynomials:



$$C_n^{(\alpha)}(x) = {\Gamma\left(\alpha + {1\over 2}\right) \over \Gamma(2\alpha)} {\Gamma(n+2\alpha) \over \Gamma\left(n+\alpha + {1\over 2}\right)} P_n^{(\alpha-1/2, \alpha-1/2)}(x)$$


$$C_n^{(\alpha)}(x) = {\Gamma\left(\alpha + {1\over 2}\right) \over \Gamma(2\alpha)}
   {\Gamma(n+2\alpha) \over \Gamma\left(n+\alpha + {1\over 2}\right)}
   P_n^{(\alpha-1/2, \alpha-1/2)}(x)$$



or the series



$$C_n^{(\alpha)}(x) = \sum_{k=0}^{\lfloor n/2 \rfloor} {(-1)^k (\alpha)_{n-k} \over k! (n-2k)!}(2x)^{n-2k}$$


$$C_n^{(\alpha)}(x) = \sum_{k=0}^{\lfloor n/2 \rfloor} {(-1)^k (\alpha)_{n-k} \over k! (n-2k)!}(2x)^{n-2k}$$



or the Rodrigues formula



$$C_n^{(\alpha)}(x) = {1\over \kappa_n w(x)} {d^n\over dx^n}\left(w(x)\left(1-x^2\right)^n\right)$$


$$C_n^{(\alpha)}(x) = {1\over \kappa_n  w(x)} {d^n\over dx^n}\left(w(x)\left(1-x^2\right)^n\right)$$



where



$$\eqalign{ w(x) &= \left(1-x^2\right)^{\alpha-{1\over 2}} \cr \kappa_n &= {(-2)^n\left(\alpha + {1\over 2}\right)_n n!\over (2\alpha)_n} \cr }$$


$$\eqalign{
w(x) &= \left(1-x^2\right)^{\alpha-{1\over 2}} \cr
\kappa_n &= {(-2)^n\left(\alpha + {1\over 2}\right)_n n!\over (2\alpha)_n} \cr
}$$



Some examples:







```maxima
(%i1) ultraspherical(1,a,x);
                                   (2 a + 1) (1 - x)
(%o1)                     2 a (1 - -----------------)
                                              1
                                       2 (a + -)
                                              2
(%i2) factor(%);
(%o2)                                2 a x
(%i3) factor(ultraspherical(2,a,x));
                                     2      2
(%o3)                        a (2 a x  + 2 x  - 1)
```


See also `orthopoly_returns_intervals` for how numerical results
are returned.

See also: `orthopoly_returns_intervals`.

### Function: unit_step (x)

The left-continuous unit step function; thus
`unit_step (x)` vanishes for `x <= 0` and equals
1 for `x > 0`.


If you want a unit step function that takes on the value 1/2 at zero,
use `hstep`.

See also: `hstep`.

### Function: untellrat (x_1, ..., x_n)

Removes `tellrat` properties from *x_1*, ..., *x_n*.

