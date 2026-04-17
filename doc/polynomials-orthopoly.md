## orthopoly

<!-- category: Polynomials -->
<!-- keywords: assoc_legendre_p -->
<!-- signatures: assoc_legendre_p(n, m, x) -->
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

<!-- category: Polynomials -->
<!-- keywords: assoc_legendre_q -->
<!-- signatures: assoc_legendre_q(n, m, x) -->
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

<!-- category: Polynomials -->
<!-- keywords: chebyshev_t -->
<!-- signatures: chebyshev_t(n, x) -->
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

<!-- category: Polynomials -->
<!-- keywords: chebyshev_u -->
<!-- signatures: chebyshev_u(n, x) -->
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

<!-- category: Polynomials -->
<!-- keywords: gen_laguerre -->
<!-- signatures: gen_laguerre(n, a, x) -->
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

<!-- category: Polynomials -->
<!-- keywords: hermite -->
<!-- signatures: hermite(n, x) -->
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

<!-- category: Polynomials -->
<!-- keywords: intervalp -->
<!-- signatures: intervalp(e) -->
### Function: intervalp (e)

Return `true` if the input is an interval and return false if it isn’t.

<!-- category: Polynomials -->
<!-- keywords: jacobi_p -->
<!-- signatures: jacobi_p(n, a, b, x) -->
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

<!-- category: Polynomials -->
<!-- keywords: laguerre -->
<!-- signatures: laguerre(n, x) -->
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

<!-- category: Polynomials -->
<!-- keywords: legendre_p -->
<!-- signatures: legendre_p(n, x) -->
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

<!-- category: Polynomials -->
<!-- keywords: legendre_q -->
<!-- signatures: legendre_q(n, x) -->
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

<!-- category: Polynomials -->
<!-- keywords: orthopoly_recur -->
<!-- signatures: orthopoly_recur(f, args) -->
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

<!-- category: Polynomials -->
<!-- keywords: orthopoly_returns_intervals -->
<!-- signatures: orthopoly_returns_intervals -->
### Variable: orthopoly_returns_intervals

Default value: `true`


When `orthopoly_returns_intervals` is `true`, floating point results are returned in
the form `interval (c, r)`, where *c* is the center of an interval
and *r* is its radius. The center can be a complex number; in that
case, the interval is a disk in the complex plane.

See also: `true`.

<!-- category: Polynomials -->
<!-- keywords: orthopoly_weight -->
<!-- signatures: orthopoly_weight(f, args) -->
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

<!-- category: Polynomials -->
<!-- keywords: pochhammer -->
<!-- signatures: pochhammer(x, n) -->
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


Reference: [https://personal.math.ubc.ca/~cbm/aands/page_256.htmA&S eqn 6.1.16]().

<!-- category: Polynomials -->
<!-- keywords: spherical_bessel_j -->
<!-- signatures: spherical_bessel_j(n, x) -->
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

<!-- category: Polynomials -->
<!-- keywords: spherical_bessel_y -->
<!-- signatures: spherical_bessel_y(n, x) -->
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

<!-- category: Polynomials -->
<!-- keywords: spherical_hankel1 -->
<!-- signatures: spherical_hankel1(n, x) -->
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

<!-- category: Polynomials -->
<!-- keywords: spherical_hankel2 -->
<!-- signatures: spherical_hankel2(n, x) -->
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

<!-- category: Polynomials -->
<!-- keywords: spherical_harmonic -->
<!-- signatures: spherical_harmonic(n, m, theta, phi) -->
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

<!-- category: Polynomials -->
<!-- keywords: ultraspherical -->
<!-- signatures: ultraspherical(n, a, x) -->
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

<!-- category: Polynomials -->
<!-- keywords: unit_step -->
<!-- signatures: unit_step(x) -->
### Function: unit_step (x)

The left-continuous unit step function; thus
`unit_step (x)` vanishes for `x <= 0` and equals
1 for `x > 0`.


If you want a unit step function that takes on the value 1/2 at zero,
use `hstep`.

See also: `hstep`.

