## orthopoly

<!-- category: Polynomials -->
<!-- keywords: assoc_legendre_p -->
<!-- signatures: assoc_legendre_p(n, m, x) -->
### Function: assoc_legendre_p (n, m, x)

The associated Legendre function of the first kind of degree *n* and
order *m*.


Reference: Abramowitz and Stegun, equations 22.5.37, page 779, 8.6.6
(second equation), page 334, and 8.2.5, page 333.

<!-- category: Polynomials -->
<!-- keywords: assoc_legendre_q -->
<!-- signatures: assoc_legendre_q(n, m, x) -->
### Function: assoc_legendre_q (n, m, x)

The associated Legendre function of the second kind of degree *n*
and order *m*.


Reference: Abramowitz and Stegun, equation 8.5.3 and 8.1.8.

<!-- category: Polynomials -->
<!-- keywords: chebyshev_t -->
<!-- signatures: chebyshev_t(n, x) -->
### Function: chebyshev_t (n, x)

The Chebyshev function of the first kind.


Reference: Abramowitz and Stegun, equation 22.5.47, page 779.

<!-- category: Polynomials -->
<!-- keywords: chebyshev_u -->
<!-- signatures: chebyshev_u(n, x) -->
### Function: chebyshev_u (n, x)

The Chebyshev function of the second kind.


Reference: Abramowitz and Stegun, equation 22.5.48, page 779.

<!-- category: Polynomials -->
<!-- keywords: gen_laguerre -->
<!-- signatures: gen_laguerre(n, a, x) -->
### Function: gen_laguerre (n, a, x)

The generalized Laguerre polynomial of degree *n*.


Reference: Abramowitz and Stegun, equation 22.5.54, page 780.

<!-- category: Polynomials -->
<!-- keywords: hermite -->
<!-- signatures: hermite(n, x) -->
### Function: hermite (n, x)

The Hermite polynomial.


Reference: Abramowitz and Stegun, equation 22.5.55, page 780.

<!-- category: Polynomials -->
<!-- keywords: intervalp -->
<!-- signatures: intervalp(e) -->
### Function: intervalp (e)

Return `true` if the input is an interval and return false if it isn’t.

<!-- category: Polynomials -->
<!-- keywords: jacobi_p -->
<!-- signatures: jacobi_p(n, a, b, x) -->
### Function: jacobi_p (n, a, b, x)

The Jacobi polynomial.


The Jacobi polynomials are actually defined for all *a* and *b*;
however, the Jacobi polynomial weight
`(1 - x)^a (1 + x)^b` isn’t integrable for
`a <= -1` or `b <= -1`.


Reference: Abramowitz and Stegun, equation 22.5.42, page 779.

<!-- category: Polynomials -->
<!-- keywords: laguerre -->
<!-- signatures: laguerre(n, x) -->
### Function: laguerre (n, x)

The Laguerre polynomial.


Reference: Abramowitz and Stegun, equations 22.5.16 and 22.5.54, page 780.

<!-- category: Polynomials -->
<!-- keywords: legendre_p -->
<!-- signatures: legendre_p(n, x) -->
### Function: legendre_p (n, x)

The Legendre polynomial of the first kind.


Reference: Abramowitz and Stegun, equations 22.5.50 and 22.5.51, page 779.

<!-- category: Polynomials -->
<!-- keywords: legendre_q -->
<!-- signatures: legendre_q(n, x) -->
### Function: legendre_q (n, x)

The Legendre polynomial of the first kind.


Reference: Abramowitz and Stegun, equations 8.5.3 and 8.1.8.

<!-- category: Polynomials -->
<!-- keywords: orthopoly_recur -->
<!-- signatures: orthopoly_recur(f, args) -->
### Function: orthopoly_recur (f, args)

Returns a recursion relation for the orthogonal function family *f* with
arguments *args*.  The recursion is with respect to the polynomial degree.



```maxima
(%i1) orthopoly_recur (legendre_p, [n, x]);

                (2 n - 1) P     (x) x + (1 - n) P     (x)
                           n - 1                 n - 2
(%o1)   P (x) = -----------------------------------------
         n                          n
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

<!-- category: Polynomials -->
<!-- keywords: orthopoly_returns_intervals -->
<!-- signatures: orthopoly_returns_intervals -->
### Variable: orthopoly_returns_intervals

Default value: `true`


When `orthopoly_returns_intervals` is `true`, floating point results
are returned in the form `interval (c, r)`, where *c* is
the center of an interval and *r* is its radius.  The center can be a
complex number; in that case, the interval is a disk in the complex plane.

<!-- category: Polynomials -->
<!-- keywords: orthopoly_weight -->
<!-- signatures: orthopoly_weight(f, args) -->
### Function: orthopoly_weight (f, args)

Returns a three element list; the first element is 
the formula of the weight for the orthogonal polynomial family
*f* with arguments given by the list *args*; the 
second and third elements give the lower and upper endpoints
of the interval of orthogonality.  For example,



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

<!-- category: Polynomials -->
<!-- keywords: pochhammer -->
<!-- signatures: pochhammer(n, x) -->
### Function: pochhammer (n, x)

The Pochhammer symbol. For nonnegative integers *n* with
`n <= pochhammer_max_index`, the expression
`pochhammer (x, n)` evaluates to the product
`x (x + 1) (x + 2) ... (x + n - 1)` when
`n > 0` and to 1 when `n = 0`.  For negative *n*,
`pochhammer (x, n)` is defined as
`(-1)^n / pochhammer (1 - x, -n)`.  Thus



```maxima
(%i1) pochhammer (x, 3);
(%o1)                   x (x + 1) (x + 2)
(%i2) pochhammer (x, -3);
                                 1
(%o2)               - -----------------------
                      (1 - x) (2 - x) (3 - x)
```


To convert a Pochhammer symbol into a quotient of gamma functions,
(see Abramowitz and Stegun, equation 6.1.22) use `makegamma`, for
example 



```maxima
(%i1) makegamma (pochhammer (x, n));
                          gamma(x + n)
(%o1)                     ------------
                            gamma(x)
```


When *n* exceeds `pochhammer_max_index` or when *n* is symbolic,
`pochhammer` returns a noun form.



```maxima
(%i1) pochhammer (x, n);
(%o1)                         (x)
                                 n
```

See also: `makegamma`, `pochhammer_max_index`.

<!-- category: Polynomials -->
<!-- keywords: pochhammer_max_index -->
<!-- signatures: pochhammer_max_index -->
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


Reference: Abramowitz and Stegun, equation 6.1.16, page 256.

<!-- category: Polynomials -->
<!-- keywords: spherical_bessel_j -->
<!-- signatures: spherical_bessel_j(n, x) -->
### Function: spherical_bessel_j (n, x)

The spherical Bessel function of the first kind.


Reference: Abramowitz and Stegun, equations 10.1.8, page 437 and 10.1.15,
page 439.

<!-- category: Polynomials -->
<!-- keywords: spherical_bessel_y -->
<!-- signatures: spherical_bessel_y(n, x) -->
### Function: spherical_bessel_y (n, x)

The spherical Bessel function of the second kind.


Reference: Abramowitz and Stegun, equations 10.1.9, page 437 and 10.1.15,
page 439.

<!-- category: Polynomials -->
<!-- keywords: spherical_hankel1 -->
<!-- signatures: spherical_hankel1(n, x) -->
### Function: spherical_hankel1 (n, x)

The spherical Hankel function of the first kind.


Reference: Abramowitz and Stegun, equation 10.1.36, page 439.

<!-- category: Polynomials -->
<!-- keywords: spherical_hankel2 -->
<!-- signatures: spherical_hankel2(n, x) -->
### Function: spherical_hankel2 (n, x)

The spherical Hankel function of the second kind.


Reference: Abramowitz and Stegun, equation 10.1.17, page 439.

<!-- category: Polynomials -->
<!-- keywords: spherical_harmonic -->
<!-- signatures: spherical_harmonic(n, m, x, y) -->
### Function: spherical_harmonic (n, m, x, y)

The spherical harmonic function.


Reference: Merzbacher 9.64.

<!-- category: Polynomials -->
<!-- keywords: ultraspherical -->
<!-- signatures: ultraspherical(n, a, x) -->
### Function: ultraspherical (n, a, x)

The ultraspherical polynomial (also known as the Gegenbauer polynomial).


Reference: Abramowitz and Stegun, equation 22.5.46, page 779.

<!-- category: Polynomials -->
<!-- keywords: unit_step -->
<!-- signatures: unit_step(x) -->
### Function: unit_step (x)

The left-continuous unit step function; thus `unit_step (x)` vanishes
for `x <= 0` and equals 1 for `x > 0`.


If you want a unit step function that takes on the value 1/2 at zero, use
`(1 + signum (x))/2`.

