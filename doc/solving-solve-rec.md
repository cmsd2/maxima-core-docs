## solve_rec

### Function: harmonic_number (x)

When *x* is positive integer $n$, `harmonic_number` is
the $n$’th harmonic number.  More generally,
`harmonic_number(x) = psi[0](x+1) + %gamma`.  (See `polygamma`).










```maxima
(%i1) load("simplify_sum")$

(%i2) harmonic_number(5);
                               137
(%o2)                          ---
                               60


(%i3) sum(1/k, k, 1, 5);
                               137
(%o3)                          ---
                               60


(%i4) float(harmonic_number(sqrt(2)));
(%o4)              %gamma + 0.6601971549171388


(%i5) float(psi[0](1+sqrt(2)))+%gamma;
(%o5)              %gamma + 0.6601971549171388
```

See also: `polygamma`.

### Function: harmonic_to_psi (x)

Converts expressions with `harmonic_number` to the equivalent
expression involving `psi[0]` (see `polygamma`).







```maxima
(%i1) load("simplify_sum")$

(%i2) harmonic_to_psi(harmonic_number(sqrt(2)));
(%o2)              psi (sqrt(2) + 1) + %gamma
                      0
```

See also: `polygamma`.

### Variable: product_use_gamma

Default value: `true`


When simplifying products, `solve_rec` introduces gamma function
into the expression if `product_use_gamma` is `true`.


See also: `simplify_products`, `solve_005frec`.

See also: `simplify_products`, `solve_rec`.

### Function: reduce_order (rec, sol, var)

Reduces the order of linear recurrence *rec* when a particular solution
*sol* is known. The reduced recurrence can be used to get other solutions.


Example:



```maxima
(%i3) rec: x[n+2] = x[n+1] + x[n]/n;
                                      x
                                       n
(%o3)               x      = x      + --
                     n + 2    n + 1   n


(%i4) solve_rec(rec, x[n]);
WARNING: found some hypergeometrical solutions! 
(%o4)                    x  = %k  n
                          n     1


(%i5) reduce_order(rec, n, x[n]);
(%t5)                    x  = n %z
                          n       n

                           n - 1
                           ====
                           \
(%t6)                %z  =  >     %u
                       n   /        %j
                           ====
                           %j = 0

(%o6)             (- n - 2) %u     - %u
                              n + 1     n


(%i6) solve_rec((n+2)*%u[n+1] + %u[n], %u[n]);
                                     n
                            %k  (- 1)
                              1
(%o6)                 %u  = ----------
                        n    (n + 1)!

So the general solution is

             n - 1
             ====        j
             \      (- 1)
       %k  n  >    -------- + %k  n
         2   /     (j + 1)!     1
             ====
             j = 0
```

### Variable: simplify_products

Default value: `true`


If `simplify_products` is `true`, `solve_rec` will try to
simplify products in result.


See also: `solve_005frec`.

See also: `solve_rec`.

### Function: simplify_sum (expr)

Tries to simplify all sums appearing in *expr* to a closed form.


To use this function first load the `simplify_sum` package with
`load("simplify_sum")`.


Example:








```maxima
(%i1) load("simplify_sum")$

(%i2) sum(binomial(n+k,k)/2^k, k, 1, n) + sum(binomial(2*n, 2*k), k, 1,n);
        n                          n
       ====                       ====
       \     binomial(n + k, k)   \
(%o2)   >    ------------------ +  >    binomial(2 n, 2 k)
       /              k           /
       ====          2            ====
       k = 1                      k = 1


(%i3) simplify_sum(%);
                         2 n - 1    n
(%o3)                   2        + 2  - 2
```

### Function: solve_rec (eqn, var, init)

Solves for hypergeometrical solutions to linear recurrence *eqn* with
polynomials coefficient in variable *var*. Optional arguments *init*
are initial conditions.


`solve_rec` can solve linear recurrences with constant coefficients,
finds hypergeometrical solutions to homogeneous linear recurrences with
polynomial coefficients, rational solutions to linear recurrences with
polynomial coefficients and can solve Ricatti type recurrences.


Note that the running time of the algorithm used to find hypergeometrical
solutions is exponential in the degree of the leading and trailing
coefficient.


To use this function first load the `solve_rec` package with
`load("solve_rec");`.


Example of linear recurrence with constant coefficients:



```maxima
(%i2) solve_rec(a[n]=a[n-1]+a[n-2]+n/2^n, a[n]);
                        n          n
           (sqrt(5) - 1)  %k  (- 1)
                            1           n
(%o2) a  = ------------------------- - ----
       n               n                  n
                      2                5 2
                                                n
                                   (sqrt(5) + 1)  %k
                                                    2    2
                                 + ------------------ - ----
                                            n              n
                                           2            5 2
```


Example of linear recurrence with polynomial coefficients:



```maxima
(%i7) 2*x*(x+1)*y[x] - (x^2+3*x-2)*y[x+1] + (x-1)*y[x+2];
                         2
(%o7) (x - 1) y      - (x  + 3 x - 2) y      + 2 x (x + 1) y
               x + 2                   x + 1                x


(%i8) solve_rec(%, y[x], y[1]=1, y[3]=3);
                              x
                           3 2    x!
(%o9)                 y  = ---- - --
                       x    4     2
```


Example of Ricatti type recurrence:



```maxima
(%i2) x*y[x+1]*y[x] - y[x+1]/(x+2) + y[x]/(x-1) = 0;
                            y         y
                             x + 1     x
(%o2)         x y  y      - ------ + ----- = 0
                 x  x + 1   x + 2    x - 1

(%i3) solve_rec(%, y[x], y[3]=5)$

(%i4) ratsimp(minfactorial(factcomb(%)));
                                   3
                               30 x  - 30 x
(%o4) y  = - -------------------------------------------------
       x        6      5       4       3       2
             5 x  - 3 x  - 25 x  + 15 x  + 20 x  - 12 x - 1584
```



See also: `solve_rec_rat`, `simplify_products` and `product_005fuse_005fgamma`.

See also: `solve_rec_rat`, `simplify_products`, `product_use_gamma`.

### Function: solve_rec_rat (eqn, var, init)

Solves for rational solutions to linear recurrences. See solve_rec for
description of arguments.


To use this function first load the `solve_rec` package with
`load("solve_rec");`.


Example:



```maxima
(%i1) (x+4)*a[x+3] + (x+3)*a[x+2] - x*a[x+1] + (x^2-1)*a[x];
(%o1)  (x + 4) a      + (x + 3) a      - x a
                x + 3            x + 2      x + 1
                                                   2
                                               + (x  - 1) a
                                                            x


(%i2) solve_rec_rat(% = (x+2)/(x+1), a[x]);
                       1
(%o2)      a  = ---------------
            x   (x - 1) (x + 1)
```



See also: `solve_005frec`.

See also: `solve_rec`.

### Function: summand_to_rec (summand_to_rec, summand, k, n, summand_to_rec, summand, k, lo, hi, n)

Returns the recurrence satisfied by the sum



```maxima
hi
    ====
    \
     >     summand
    /
    ====
  k = lo
```


where summand is hypergeometrical in *k* and *n*. If *lo* and *hi*
are omitted, they are assumed to be `lo = -inf` and `hi = inf`.


To use this function first load the `simplify_sum` package with
`load("simplify_sum")`.


Example:



```maxima
(%i1) load("simplify_sum")$

(%i2) summand: binom(n,k);
(%o2)                           binomial(n, k)


(%i3) summand_to_rec(summand,k,n);
(%o3)                      2 sm  - sm      = 0
                               n     n + 1


(%i7) summand: binom(n, k)/(k+1);
                                binomial(n, k)
(%o7)                           --------------
                                    k + 1


(%i8) summand_to_rec(summand, [k, 0, n], n);
(%o8)               2 (n + 1) sm  - (n + 2) sm      = - 1
                                n             n + 1
```

