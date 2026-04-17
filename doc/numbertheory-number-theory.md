## Number Theory

<!-- category: NumberTheory -->
<!-- keywords: bern -->
<!-- signatures: bern(n) -->
### Function: bern (n)

Returns the *n*’th Bernoulli number for integer *n*.


Bernoulli numbers equal to zero are suppressed if `zerobern` is
`false`.


See also `burn`.









```maxima
maxima
(%i1) zerobern: true$

(%i2) map (bern, [0, 1, 2, 3, 4, 5, 6, 7, 8]);
                    1  1       1      1        1
(%o2)         [1, - -, -, 0, - --, 0, --, 0, - --]
                    2  6       30     42       30

(%i3) zerobern: false$

(%i4) map (bern, [0, 1, 2, 3, 4, 5, 6, 7, 8]);
                 1  1    1   1     1   5     691   7
(%o4)      [1, - -, -, - --, --, - --, --, - ----, -]
                 2  6    30  42    30  66    2730  6
```

See also: `burn`.

<!-- category: NumberTheory -->
<!-- keywords: bernpoly -->
<!-- signatures: bernpoly(x, n) -->
### Function: bernpoly (x, n)

Returns the *n*’th Bernoulli polynomial in the
variable *x*.

<!-- category: NumberTheory -->
<!-- keywords: bfhzeta -->
<!-- signatures: bfhzeta(s, h, n) -->
### Function: bfhzeta (s, h, n)

Returns the Hurwitz zeta function for the arguments *s* and *h*.
The return value is a big float (bfloat);
*n* is the number of digits in the return value.


The Hurwitz zeta function is defined as



$$\zeta \left(s,h\right) = \sum_{k=0}^\infty {1 \over \left(k+h\right)^{s}}$$


```maxima
inf
                        ====
                        \        1
         zeta (s,h)  =   >    --------
                        /            s
                        ====  (k + h)
                        k = 0
```


`load ("bffac")` loads this function.

<!-- category: NumberTheory -->
<!-- keywords: bfzeta -->
<!-- signatures: bfzeta(s, n) -->
### Function: bfzeta (s, n)

Returns the Riemann zeta function for the argument *s*.
The return value is a big float (bfloat);
*n* is the number of digits in the return value.

<!-- category: NumberTheory -->
<!-- keywords: burn -->
<!-- signatures: burn(n) -->
### Function: burn (n)

Returns a rational number, which is an approximation of the *n*’th Bernoulli
number for integer *n*.  `burn` exploits the observation that
(rational) Bernoulli numbers can be approximated by (transcendental) zetas with
tolerable efficiency:



```maxima
n - 1  1 - 2 n
              (- 1)      2        zeta(2 n) (2 n)!
     B(2 n) = ------------------------------------
                                2 n
                             %pi
```


`burn` may be more efficient than `bern` for large, isolated *n*
as `bern` computes all the Bernoulli numbers up to index *n* before 
returning.  `burn` invokes the approximation for even integers `n > 255`.  For odd integers and `n <= 255` the function `bern` is called.


`load ("bffac")` loads this function.  See also `bern`.

See also: `bern`.

<!-- category: NumberTheory -->
<!-- keywords: cf -->
<!-- signatures: cf(expr) -->
### Function: cf (expr)

Computes a continued fraction approximation.
*expr* is an expression comprising continued fractions,
square roots of integers, and literal real numbers
(integers, rational numbers, ordinary floats, and bigfloats).
`cf` computes exact expansions for rational numbers,
but expansions are truncated at `ratepsilon` for ordinary floats
and `10^(-fpprec)` for bigfloats.


Operands in the expression may be combined with arithmetic operators.
Maxima does not know about operations on continued fractions
outside of `cf`.


`cf` evaluates its arguments after binding `listarith` to
`false`.  `cf` returns a continued fraction, represented as a list.


A continued fraction `a + 1/(b + 1/(c + ...))` is represented by the list
`[a, b, c, ...]`.  The list elements `a`, `b`, `c`, ...
must evaluate to integers.  *expr* may also contain `sqrt (n)` where
`n` is an integer.  In this case `cf` will give as many terms of the
continued fraction as the value of the variable `cflength` times the
period.


A continued fraction can be evaluated to a number by evaluating the arithmetic
representation returned by `cfdisrep`.  See also `cfexpand` for
another way to evaluate a continued fraction.


See also `cfdisrep`, `cfexpand`, and `cflength`.


Examples:



- *
*expr* is an expression comprising continued fractions and square roots of
integers.


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
maxima
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
A continued fraction can be evaluated by evaluating the arithmetic
representation returned by `cfdisrep`.




```maxima
maxima
(%i1) cflength: 3$
(%i2) cfdisrep (cf (sqrt (3)))$
(%i3) ev (%, numer);
(%o3)                  1.7317073170731707
```
- *
Maxima does not know about operations on continued fractions outside of
`cf`.



```maxima
maxima
(%i1) cf ([1,1,1,1,1,2] * 3);
(%o1)                     [4, 1, 5, 2]

(%i2) cf ([1,1,1,1,1,2]) * 3;
(%o2)                  [3, 3, 3, 3, 3, 6]
```

See also: `cflength`, `cfdisrep`, `cfexpand`.

<!-- category: NumberTheory -->
<!-- keywords: cfdisrep -->
<!-- signatures: cfdisrep(list) -->
### Function: cfdisrep (list)

Constructs and returns an ordinary arithmetic expression
of the form `a + 1/(b + 1/(c + ...))`
from the list representation of a continued fraction `[a, b, c, ...]`.







```maxima
maxima

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

<!-- category: NumberTheory -->
<!-- keywords: cfexpand -->
<!-- signatures: cfexpand(x) -->
### Function: cfexpand (x)

Returns a matrix of the numerators and denominators of the last (column 1) and
next-to-last (column 2) convergents of the continued fraction *x*.








```maxima
maxima

(%i1) cf (rat (ev (%pi, numer)));
rat: replaced 3.141592653589793 by 80143857/25510582 = 3.1415926535897927
(%o1)      [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14]


(%i2) cfexpand (%);
                      [ 80143857  5419351 ]
(%o2)                 [                   ]
                      [ 25510582  1725033 ]


(%i3) %[1,1]/%[2,1], numer;
(%o3)                  3.1415926535897927
```

<!-- category: NumberTheory -->
<!-- keywords: cflength -->
<!-- signatures: cflength -->
### Variable: cflength

Default value: 1


`cflength` controls the number of terms of the continued fraction the
function `cf` will give, as the value `cflength` times the period.
Thus the default is to give one period.











```maxima
maxima
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

<!-- category: NumberTheory -->
<!-- keywords: divsum -->
<!-- signatures: divsum(n, k), divsum(n) -->
### Function: divsum (n, k)

`divsum (n, k)` returns the sum of the divisors of *n*
raised to the *k*’th power.


`divsum (n)` returns the sum of the divisors of *n*.









```maxima
maxima

(%i1) divsum (12);
(%o1)                          28


(%i2) 1 + 2 + 3 + 4 + 6 + 12;
(%o2)                          28


(%i3) divsum (12, 2);
(%o3)                          210


(%i4) 1^2 + 2^2 + 3^2 + 4^2 + 6^2 + 12^2;
(%o4)                          210
```

<!-- category: NumberTheory -->
<!-- keywords: euler -->
<!-- signatures: euler(n) -->
### Function: euler (n)

Returns the *n*’th Euler number for nonnegative integer *n*.
Euler numbers equal to zero are suppressed if `zerobern` is
`false`.


For the Euler-Mascheroni constant, see `%gamma`.









```maxima
maxima
(%i1) zerobern: true$

(%i2) map (euler, [0, 1, 2, 3, 4, 5, 6]);
(%o2)              [1, 0, - 1, 0, 5, 0, - 61]

(%i3) zerobern: false$

(%i4) map (euler, [0, 1, 2, 3, 4, 5, 6]);
(%o4)       [1, - 1, 5, - 61, 1385, - 50521, 2702765]
```

<!-- category: NumberTheory -->
<!-- keywords: factors_only -->
<!-- signatures: factors_only -->
### Variable: factors_only

Default value: `false`


Controls the value returned by `ifactors`. The default `false` 
causes `ifactors` to provide information about multiplicities of the 
computed prime factors. If `factors_only` is set to `true`, 
`ifactors` returns nothing more than a list of prime factors.


Example: See `ifactors`.

See also: `ifactors`.

<!-- category: NumberTheory -->
<!-- keywords: fib -->
<!-- signatures: fib(n) -->
### Function: fib (n)

Returns the *n*’th Fibonacci number.
`fib(0)` is equal to 0 and `fib(1)` equal to 1, and 
`fib (-n)` equal to `(-1)^(n + 1) * fib(n)`.






```maxima
maxima

(%i1) map (fib, [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]);
(%o1)     [- 3, 2, - 1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
```

<!-- category: NumberTheory -->
<!-- keywords: fibtophi -->
<!-- signatures: fibtophi(expr) -->
### Function: fibtophi (expr)

Expresses Fibonacci numbers in *expr* in terms of the constant `%phi`,
which is `(1 + sqrt(5))/2`, approximately 1.61803399.


Examples:









```maxima
maxima

(%i1) fibtophi (fib (n));
                           n             n
                       %phi  - (1 - %phi)
(%o1)                  -------------------
                           2 %phi - 1


(%i2) fib (n-1) + fib (n) - fib (n+1);
(%o2)          - fib(n + 1) + fib(n) + fib(n - 1)


(%i3) fibtophi (%);
            n + 1             n + 1       n             n
        %phi      - (1 - %phi)        %phi  - (1 - %phi)
(%o3) - --------------------------- + -------------------
                2 %phi - 1                2 %phi - 1
                                          n - 1             n - 1
                                      %phi      - (1 - %phi)
                                    + ---------------------------
                                              2 %phi - 1


(%i4) ratsimp (%);
(%o4)                           0
```

<!-- category: NumberTheory -->
<!-- keywords: ifactors -->
<!-- signatures: ifactors(n) -->
### Function: ifactors (n)

For a positive integer *n* returns the factorization of *n*.  If
`n=p1^e1..pk^nk` is the decomposition of *n* into prime
factors, ifactors returns `[[p1, e1], ... , [pk, ek]]`.


Factorization methods used are trial divisions by primes up to 9973,
Pollard’s rho and p-1 method and elliptic curves.


If the variable `ifactor_verbose` is set to `true`
ifactor produces detailed output about what it is doing including
immediate feedback as soon as a factor has been found.


The value returned by `ifactors` is controlled by the option variable `factors_005fonly`.
The default `false` causes `ifactors` to provide information about 
the multiplicities of the computed prime factors. If `factors_only` 
is set to `true`, `ifactors` simply returns the list of 
prime factors.








```maxima
maxima

(%i1) ifactors(51575319651600);
(%o1)   [[2, 4], [3, 2], [5, 2], [1583, 1], [9050207, 1]]


(%i2) apply("*", map(lambda([u], u[1]^u[2]), %));
(%o2)                    51575319651600


(%i3) ifactors(51575319651600), factors_only : true;
(%o3)               [2, 3, 5, 1583, 9050207]
```

See also: `factors_only`.

<!-- category: NumberTheory -->
<!-- keywords: igcdex -->
<!-- signatures: igcdex(n, k) -->
### Function: igcdex (n, k)

Returns a list `[a, b, u]` where *u* is the greatest
common divisor of *n* and *k*, and *u* is equal to
`a n + b k`.  The arguments *n* and *k*
must be integers.


`igcdex` implements the Euclidean algorithm.  See also `gcdex`.


The command `load("gcdex")` loads the function.


Examples:









```maxima
maxima
(%i1) load("gcdex")$

(%i2) igcdex(30,18);
(%o2)                      [- 1, 2, 6]


(%i3) igcdex(1526757668, 7835626735736);
(%o3)            [845922341123, - 164826435, 4]


(%i4) igcdex(fib(20), fib(21));
(%o4)                   [4181, - 2584, 1]
```

See also: `gcdex`.

<!-- category: NumberTheory -->
<!-- keywords: inrt -->
<!-- signatures: inrt(x, n) -->
### Function: inrt (x, n)

Returns the integer *n*’th root of the absolute value of *x*.







```maxima
maxima
(%i1) l: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]$

(%i2) map (lambda ([a], inrt (10^a, 3)), l);
(%o2) [2, 4, 10, 21, 46, 100, 215, 464, 1000, 2154, 4641, 10000]
```

<!-- category: NumberTheory -->
<!-- keywords: inv_mod -->
<!-- signatures: inv_mod(n, m) -->
### Function: inv_mod (n, m)

Computes the inverse of *n* modulo *m*.
`inv_mod (n,m)` returns `false`, 
if *n* is a zero divisor modulo *m*.








```maxima
maxima

(%i1) inv_mod(3, 41);
(%o1)                          14


(%i2) ratsimp(3^-1), modulus = 41;
(%o2)                          14


(%i3) inv_mod(3, 42);
(%o3)                         false
```

<!-- category: NumberTheory -->
<!-- keywords: isqrt -->
<!-- signatures: isqrt(x) -->
### Function: isqrt (x)

Returns the "integer square root" of the absolute value of *x*, which is an
integer.

<!-- category: NumberTheory -->
<!-- keywords: jacobi -->
<!-- signatures: jacobi(p, q) -->
### Function: jacobi (p, q)

Returns the Jacobi symbol of *p* and *q*.







```maxima
maxima
(%i1) l: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]$

(%i2) map (lambda ([a], jacobi (a, 9)), l);
(%o2)         [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
```

<!-- category: NumberTheory -->
<!-- keywords: lcm -->
<!-- signatures: lcm(expr_1, ..., expr_n) -->
### Function: lcm (expr_1, ..., expr_n)

Returns the least common multiple of its arguments.
The arguments may be general expressions as well as integers.


`load ("functs")` loads this function.

<!-- category: NumberTheory -->
<!-- keywords: lucas -->
<!-- signatures: lucas(n) -->
### Function: lucas (n)

Returns the *n*’th Lucas number.
`lucas(0)` is equal to 2 and `lucas(1)` equal to 1, and
in general, `lucas(n) = lucas(n-1) + lucas(n-2)`.  Also 
`lucas(-n)` is equal to `(-1)^(-n) * lucas(n)`.






```maxima
maxima

(%i1) map (lucas, [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]);
(%o1)    [7, - 4, 3, - 1, 2, 1, 3, 4, 7, 11, 18, 29, 47]
```

<!-- category: NumberTheory -->
<!-- keywords: mod -->
<!-- signatures: mod(x, y) -->
### Function: mod (x, y)

If *x* and *y* are real numbers and *y* is nonzero, return
`x - y * floor(x / y)`.  Further for all real
*x*, we have `mod (x, 0) = x`.  For a discussion of the
definition `mod (x, 0) = x`, see Section 3.4, of
"Concrete Mathematics," by Graham, Knuth, and Patashnik.  The function
`mod (x, 1)` is a sawtooth function with period 1 with
`mod (1, 1) = 0` and `mod (0, 1) = 0`.


To find the principal argument (a number in the interval `(-%pi, %pi]`) of
a complex number, use the function
`x |-> %pi - mod (%pi - x, 2*%pi)`, where *x* is an
argument.


When *x* and *y* are constant expressions (`10 * %pi`, for 
example), `mod` uses the same big float evaluation scheme that `floor`
and `ceiling` uses.  Again, it’s possible, although unlikely, that
`mod` could return an erroneous value in such cases.


For nonnumerical arguments *x* or *y*, `mod` knows several
simplification rules:








```maxima
maxima

(%i1) mod (x, 0);
(%o1)                           x


(%i2) mod (a*x, a*y);
(%o2)                      a mod(x, y)


(%i3) mod (0, x);
(%o3)                           0
```

<!-- category: NumberTheory -->
<!-- keywords: next_prime -->
<!-- signatures: next_prime(n) -->
### Function: next_prime (n)

Returns the smallest prime bigger than *n*.






```maxima
maxima

(%i1) next_prime(27);
(%o1)                          29
```

<!-- category: NumberTheory -->
<!-- keywords: partfrac -->
<!-- signatures: partfrac(expr, var) -->
### Function: partfrac (expr, var)

Expands the expression *expr* in partial fractions
with respect to the main variable *var*.  `partfrac` does a complete
partial fraction decomposition.  The algorithm employed is based on
the fact that the denominators of the partial fraction expansion (the
factors of the original denominator) are relatively prime.  The
numerators can be written as linear combinations of denominators, and
the expansion falls out.


`partfrac` ignores the value `true` of the option variable
`keepfloat`.








```maxima
maxima

(%i1) 1/(1+x)^2 - 2/(1+x) + 2/(2+x);
                      2       2        1
(%o1)               ----- - ----- + --------
                    x + 2   x + 1          2
                                    (x + 1)


(%i2) ratsimp (%);
                                 x
(%o2)                 - -------------------
                         3      2
                        x  + 4 x  + 5 x + 2


(%i3) partfrac (%, x);
                      2       2        1
(%o3)               ----- - ----- + --------
                    x + 2   x + 1          2
                                    (x + 1)
```

<!-- category: NumberTheory -->
<!-- keywords: power_mod -->
<!-- signatures: power_mod(a, n, m) -->
### Function: power_mod (a, n, m)

Uses a modular algorithm to compute `a^n mod m` 
where *a* and *n* are integers and *m* is a positive integer.
If *n* is negative, `inv_mod` is used to find the modular inverse.









```maxima
maxima

(%i1) power_mod(3, 15, 5);
(%o1)                           2


(%i2) mod(3^15,5);
(%o2)                           2


(%i3) power_mod(2, -1, 5);
(%o3)                           3


(%i4) inv_mod(2,5);
(%o4)                           3
```

<!-- category: NumberTheory -->
<!-- keywords: prev_prime -->
<!-- signatures: prev_prime(n) -->
### Function: prev_prime (n)

Returns the greatest prime smaller than *n*.






```maxima
maxima

(%i1) prev_prime(27);
(%o1)                          23
```

<!-- category: NumberTheory -->
<!-- keywords: primep -->
<!-- signatures: primep(n) -->
### Function: primep (n)

Primality test.  If `primep (n)` returns `false`, *n* is a
composite number and if it returns `true`, *n* is a prime number
with very high probability.


For *n* less than 3317044064679887385961981 a deterministic version of
Miller-Rabin’s test is used.  If `primep (n)` returns
`true`, then *n* is a prime number.


For *n* bigger than 3317044064679887385961981 `primep` uses
`primep_number_of_tests` Miller-Rabin’s pseudo-primality tests and one 
Lucas pseudo-primality test.  The probability that a non-prime *n* will 
pass one Miller-Rabin test is less than 1/4.  Using the default value 25 for
`primep_number_of_tests`, the probability of *n* being
composite is much smaller that 10^-15.

<!-- category: NumberTheory -->
<!-- keywords: primep_number_of_tests -->
<!-- signatures: primep_number_of_tests -->
### Variable: primep_number_of_tests

Default value: 25


Number of Miller-Rabin’s tests used in `primep`.

<!-- category: NumberTheory -->
<!-- keywords: primes -->
<!-- signatures: primes(start, end) -->
### Function: primes (start, end)

Returns the list of all primes from *start* to *end*.






```maxima
maxima

(%i1) primes(3, 7);
(%o1)                       [3, 5, 7]
```

<!-- category: NumberTheory -->
<!-- keywords: qunit -->
<!-- signatures: qunit(n) -->
### Function: qunit (n)

Returns the principal unit of the real quadratic number field
`sqrt (n)` where *n* is an integer,
i.e., the element whose norm is unity.
This amounts to solving Pell’s equation `a^2 - n b^2 = 1`.







```maxima
maxima

(%i1) qunit (17);
(%o1)                     sqrt(17) + 4


(%i2) expand (% * (sqrt(17) - 4));
(%o2)                           1
```

<!-- category: NumberTheory -->
<!-- keywords: solve_congruences -->
<!-- signatures: solve_congruences([r_1, ..., r_n], [m_1, ..., m_n]) -->
### Function: solve_congruences ([r_1, ..., r_n], [m_1, ..., m_n])

Solves the system of congruences `x = r_1 mod m_1`, ..., `x = r_n mod m_n`.
The remainders *r_n* may be arbitrary integers while the moduli *m_n* have to be 
positive and pairwise coprime integers.












```maxima
maxima

(%i1) mods : [1000, 1001, 1003, 1007];
(%o1)               [1000, 1001, 1003, 1007]


(%i2) lreduce('gcd, mods);
(%o2)                           1


(%i3) x : random(apply("*", mods));
(%o3)                     685124877004


(%i4) rems : map(lambda([z], mod(x, z)), mods);
(%o4)                   [4, 568, 54, 624]


(%i5) solve_congruences(rems, mods);
(%o5)                     685124877004


(%i6) solve_congruences([1, 2], [3, n]);
(%o6)           solve_congruences([1, 2], [3, n])


(%i7) %, n = 4;
(%o7)                          10
```

<!-- category: NumberTheory -->
<!-- keywords: totient -->
<!-- signatures: totient(n) -->
### Function: totient (n)

Returns the number of integers less than or equal to *n* which
are relatively prime to *n*.

<!-- category: NumberTheory -->
<!-- keywords: zerobern -->
<!-- signatures: zerobern -->
### Variable: zerobern

Default value: `true`


When `zerobern` is `false`, `bern` excludes the Bernoulli numbers
and `euler` excludes the Euler numbers which are equal to zero.
See `bern` and `euler`.

<!-- category: NumberTheory -->
<!-- keywords: zeta -->
<!-- signatures: zeta(n) -->
### Function: zeta (n)

Returns the Riemann zeta function.  If *n* is a negative integer, 0, or a
positive even integer, the Riemann zeta function simplifies to an exact value.
For a positive even integer the option variable `zeta%pi` has to be
`true` in addition (See `zeta%pi`).  For a floating point or bigfloat
number the Riemann zeta function is evaluated numerically.  Maxima returns a
noun form `zeta (n)` for all other arguments, including rational
noninteger, and complex arguments, or for even integers, if `zeta%pi` has
the value `false`.


`zeta(1)` is undefined, but Maxima knows the limit 
`limit(zeta(x), x, 1)` from above and below.


The Riemann zeta function distributes over lists, matrices, and equations.


See also `bfzeta` and `zeta_0025pi`.


Examples:








```maxima
maxima

(%i1) zeta([-2, -1, 0, 0.5, 2, 3,1+%i]);
                                              2
            1     1                        %pi
(%o1) [0, - --, - -, - 1.4603545088095862, ----, zeta(3), 
            12    2                         6
                                                    zeta(%i + 1)]


(%i2) limit(zeta(x),x,1,plus);
(%o2)                          inf


(%i3) limit(zeta(x),x,1,minus);
(%o3)                         minf
```

See also: `bfzeta`, `zeta%pi`.

<!-- category: NumberTheory -->
<!-- keywords: zeta%pi -->
<!-- signatures: zeta%pi -->
### Variable: zeta%pi

Default value: `true`


When `zeta%pi` is `true`, `zeta` returns an expression 
proportional to `%pi^n` for even integer `n`.  Otherwise, `zeta` 
returns a noun form `zeta (n)` for even integer `n`.


Examples:









```maxima
maxima
(%i1) zeta%pi: true$

(%i2) zeta (4);
                                 4
                              %pi
(%o2)                         ----
                               90

(%i3) zeta%pi: false$

(%i4) zeta (4);
(%o4)                        zeta(4)
```

See also: `true`.

<!-- category: NumberTheory -->
<!-- keywords: zn_add_table -->
<!-- signatures: zn_add_table(n) -->
### Function: zn_add_table (n)

Shows an addition table of all elements in (Z/*n*Z).


See also `zn_mult_table`,  `zn_005fpower_005ftable`.

See also: `zn_mult_table`, `zn_power_table`.

<!-- category: NumberTheory -->
<!-- keywords: zn_carmichael_lambda -->
<!-- signatures: zn_carmichael_lambda(n) -->
### Function: zn_carmichael_lambda (n)

Returns `1` if *n* is `1` and otherwise 
the greatest characteristic factor of the totient of *n*.


For remarks and examples see `zn_005fcharacteristic_005ffactors`.

See also: `zn_characteristic_factors`.

<!-- category: NumberTheory -->
<!-- keywords: zn_characteristic_factors -->
<!-- signatures: zn_characteristic_factors(n) -->
### Function: zn_characteristic_factors (n)

Returns a list containing the characteristic factors of the totient of *n*.


Using the characteristic factors a multiplication group modulo *n* 
can be expressed as a group direct product of cyclic subgroups.


In case the group itself is cyclic the list only contains the totient 
and using `zn_primroot` a generator can be computed. 
If the totient splits into more than one characteristic factors 
`zn_factor_generators` finds generators of the corresponding subgroups.

 

Each of the `r` factors in the list divides the right following factors. 
For the last factor `f_r` therefore holds `a^f_r = 1 (mod n)` 
for all `a` coprime to *n*.  
This factor is also known as Carmichael function or Carmichael lambda.


If `n > 2`, then `totient(n)/2^r` is the number of quadratic residues, 
and each of these has `2^r` square roots.


See also `totient`,  `zn_primroot`,  `zn_005ffactor_005fgenerators`.


Examples:


The multiplication group modulo `14` is cyclic and its `6` elements 
can be generated by a primitive root.








```maxima
maxima

(%i1) [zn_characteristic_factors(14), phi: totient(14)];
(%o1)                       [[6], 6]


(%i2) [zn_factor_generators(14), g: zn_primroot(14)];
(%o2)                       [[3], 3]


(%i3) M14: makelist(power_mod(g,i,14), i,0,phi-1);
(%o3)                 [1, 3, 9, 13, 11, 5]
```


The multiplication group modulo `15` is not cyclic and its `8` elements 
can be generated by two factor generators.










```maxima
maxima

(%i1) [[f1,f2]: zn_characteristic_factors(15), totient(15)];
(%o1)                      [[2, 4], 8]


(%i2) [[g1,g2]: zn_factor_generators(15), zn_primroot(15)];
(%o2)                   [[11, 7], false]


(%i3) UG1: makelist(power_mod(g1,i,15), i,0,f1-1);
(%o3)                        [1, 11]


(%i4) UG2: makelist(power_mod(g2,i,15), i,0,f2-1);
(%o4)                     [1, 7, 4, 13]


(%i5) M15: create_list(mod(i*j,15), i,UG1, j,UG2);
(%o5)              [1, 7, 4, 13, 11, 2, 14, 8]
```


For the last characteristic factor `4` it holds that `a^4 = 1 (mod 15)` 
for all `a` in `M15`. 


`M15` has two characteristic factors and therefore `8/2^2` quadratic residues, 
and each of these has `2^2` square roots.







```maxima
maxima

(%i1) zn_power_table(15);
                        [ 1   1  1   1 ]
                        [              ]
                        [ 2   4  8   1 ]
                        [              ]
                        [ 4   1  4   1 ]
                        [              ]
                        [ 7   4  13  1 ]
(%o1)                   [              ]
                        [ 8   4  2   1 ]
                        [              ]
                        [ 11  1  11  1 ]
                        [              ]
                        [ 13  4  7   1 ]
                        [              ]
                        [ 14  1  14  1 ]


(%i2) map(lambda([i], zn_nth_root(i,2,15)), [1,4]);
(%o2)            [[1, 4, 11, 14], [2, 7, 8, 13]]
```

See also: `totient`, `zn_primroot`, `zn_factor_generators`.

<!-- category: NumberTheory -->
<!-- keywords: zn_determinant -->
<!-- signatures: zn_determinant(matrix, p) -->
### Function: zn_determinant (matrix, p)

Uses the technique of LU-decomposition to compute the determinant of *matrix* 
over (Z/*p*Z). *p* must be a prime. 


However if the determinant is equal to zero the LU-decomposition might fail. 
In that case `zn_determinant` computes the determinant non-modular 
and reduces thereafter.


See also `zn_005finvert_005fby_005flu`.


Examples:









```maxima
maxima

(%i1) m : matrix([1,3],[2,4]);
                            [ 1  3 ]
(%o1)                       [      ]
                            [ 2  4 ]


(%i2) zn_determinant(m, 5);
(%o2)                           3


(%i3) m : matrix([2,4,1],[3,1,4],[4,3,2]);
                           [ 2  4  1 ]
                           [         ]
(%o3)                      [ 3  1  4 ]
                           [         ]
                           [ 4  3  2 ]


(%i4) zn_determinant(m, 5);
(%o4)                           0
```

See also: `zn_invert_by_lu`.

<!-- category: NumberTheory -->
<!-- keywords: zn_factor_generators -->
<!-- signatures: zn_factor_generators(n) -->
### Function: zn_factor_generators (n)

Returns a list containing factor generators corresponding to the 
characteristic factors of the totient of *n*.


For remarks and examples see `zn_005fcharacteristic_005ffactors`.

See also: `zn_characteristic_factors`.

<!-- category: NumberTheory -->
<!-- keywords: zn_invert_by_lu -->
<!-- signatures: zn_invert_by_lu(matrix, p) -->
### Function: zn_invert_by_lu (matrix, p)

Uses the technique of LU-decomposition to compute the modular inverse of 
*matrix* over (Z/*p*Z). *p* must be a prime and *matrix* 
invertible. `zn_invert_by_lu` returns `false` if *matrix* 
is not invertible.


See also `zn_005fdeterminant`.


Example:









```maxima
maxima

(%i1) m : matrix([1,3],[2,4]);
                            [ 1  3 ]
(%o1)                       [      ]
                            [ 2  4 ]


(%i2) zn_determinant(m, 5);
(%o2)                           3


(%i3) mi : zn_invert_by_lu(m, 5);
                            [ 3  4 ]
(%o3)                       [      ]
                            [ 1  2 ]


(%i4) matrixmap(lambda([a], mod(a, 5)), m . mi);
                            [ 1  0 ]
(%o4)                       [      ]
                            [ 0  1 ]
```

See also: `zn_determinant`.

<!-- category: NumberTheory -->
<!-- keywords: zn_log -->
<!-- signatures: zn_log(a, g, n), zn_log(a, g, n, [[p1, e1], ..., [pk, ek]]) -->
### Function: zn_log (a, g, n)

Computes the discrete logarithm. Let (Z/*n*Z)* be a cyclic group, *g* a 
primitive root modulo *n* or a generator of a subgroup of (Z/*n*Z)* 
and let *a* be a member of this group.  
`zn_log (a, g, n)` then solves the congruence `g^x = a mod n`.
Please note that if *a* is not a power of *g* modulo *n*, 
`zn_log` will not terminate.


The applied algorithm needs a prime factorization of `zn_order(g)` resp. `totient(n)` 
in case *g* is a primitive root modulo *n*. 
A precomputed list of factors of `zn_order(g)` might be used as the optional fourth argument.
This list must be of the same form as the list returned by `ifactors(zn_order(g))` 
using the default option `factors_only : false`.
However, compared to the running time of the logarithm algorithm 
providing the list of factors has only a quite small effect.


The algorithm uses a Pohlig-Hellman-reduction and Pollard’s Rho-method for 
discrete logarithms. The running time of `zn_log` primarily depends on the 
bitlength of the greatest prime factor of `zn_order(g)`.


See also `zn_primroot`,  `zn_order`,  `ifactors`,  `totient`.


Examples:


`zn_log (a, g, n)` solves the congruence `g^x = a mod n`.














```maxima
maxima
(%i1) n : 22$

(%i2) g : zn_primroot(n);
(%o2)                           7


(%i3) ord_7 : zn_order(7, n);
(%o3)                          10


(%i4) powers_7 : makelist(power_mod(g, x, n), x, 0, ord_7 - 1);
(%o4)          [1, 7, 5, 13, 3, 21, 15, 17, 9, 19]


(%i5) zn_log(9, g, n);
(%o5)                           8


(%i6) map(lambda([x], zn_log(x, g, n)), powers_7);
(%o6)            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


(%i7) ord_5 : zn_order(5, n);
(%o7)                           5


(%i8) powers_5 : makelist(power_mod(5,x,n), x, 0, ord_5 - 1);
(%o8)                   [1, 5, 3, 15, 9]


(%i9) zn_log(9, 5, n);
(%o9)                           4
```


The optional fourth argument must be of the same form as the list returned by 
`ifactors(zn_order(g))`.
The running time primarily depends on the bitlength of the totient’s greatest prime factor.
















```maxima
maxima

(%i1) (p : 2^127-1, primep(p));
(%o1)                         true

(%i2) ifs : ifactors(p - 1)$

(%i3) g : zn_primroot(p, ifs);
(%o3)                          43

(%i4) a : power_mod(g, 4711, p)$

(%i5) zn_log(a, g, p, ifs);
(%o5)                         4711


(%i6) f_max : last(ifs);
(%o6)                   [77158673929, 1]

(%i7) ord_5 : zn_order(5,p,ifs)$

(%i8) (p - 1)/ord_5;
(%o8)                          73

(%i9) ifs_5 : ifactors(ord_5)$
(%i10) a : power_mod(5, 4711, p)$

(%i11) zn_log(a, 5, p, ifs_5);
(%o11)                        4711
```

See also: `zn_primroot`, `zn_order`, `ifactors`, `totient`.

<!-- category: NumberTheory -->
<!-- keywords: zn_mult_table -->
<!-- signatures: zn_mult_table(n), zn_mult_table(n, gcd) -->
### Function: zn_mult_table (n)

Without the optional argument *gcd* `zn_mult_table(n)` shows a 
multiplication table of all elements in (Z/*n*Z)* which are all elements 
coprime to *n*.


The optional second argument *gcd* allows to select a specific 
subset of (Z/*n*Z). If *gcd* is an integer, a multiplication table of 
all residues `x` with `gcd(x,n) =`*gcd* are returned.
Additionally row and column headings are added for better readability. 
If necessary, these can be easily removed by `submatrix(1, table, 1)`. 

 

If *gcd* is set to `all`, the table is printed for all non-zero 
elements in (Z/*n*Z).


The second example shows an alternative way to create a multiplication table 
for subgroups.


See also `zn_add_table`,  `zn_005fpower_005ftable`.


Examples:


The default table shows all elements in (Z/*n*Z)* and allows to demonstrate 
and study basic properties of modular multiplication groups.
E.g. the principal diagonal contains all quadratic residues, 
each row and column contains every element, the tables are symmetric, etc..


If *gcd* is set to `all`, the table is printed for all non-zero 
elements in (Z/*n*Z).







```maxima
maxima

(%i1) zn_mult_table(8);
                         [ 1  3  5  7 ]
                         [            ]
                         [ 3  1  7  5 ]
(%o1)                    [            ]
                         [ 5  7  1  3 ]
                         [            ]
                         [ 7  5  3  1 ]


(%i2) zn_mult_table(8, all);
                     [ 1  2  3  4  5  6  7 ]
                     [                     ]
                     [ 2  4  6  0  2  4  6 ]
                     [                     ]
                     [ 3  6  1  4  7  2  5 ]
                     [                     ]
(%o2)                [ 4  0  4  0  4  0  4 ]
                     [                     ]
                     [ 5  2  7  4  1  6  3 ]
                     [                     ]
                     [ 6  4  2  0  6  4  2 ]
                     [                     ]
                     [ 7  6  5  4  3  2  1 ]
```


If *gcd* is an integer, row and column headings are added for better readability. 


If the subset chosen by *gcd* is a group there is another way to create 
a multiplication table. An isomorphic mapping from a group with `1` as 
identity builds a table which is easy to read. The mapping is accomplished via CRT.


In the second version of `T36_4` the identity, here `28`, is placed in 
the top left corner, just like in table `T9`. 








```maxima
maxima

(%i1) T36_4: zn_mult_table(36,4);
                 [ *   4   8   16  20  28  32 ]
                 [                            ]
                 [ 4   16  32  28  8   4   20 ]
                 [                            ]
                 [ 8   32  28  20  16  8   4  ]
                 [                            ]
(%o1)            [ 16  28  20  4   32  16  8  ]
                 [                            ]
                 [ 20  8   16  32  4   20  28 ]
                 [                            ]
                 [ 28  4   8   16  20  28  32 ]
                 [                            ]
                 [ 32  20  4   8   28  32  16 ]


(%i2) T9: zn_mult_table(36/4);
                      [ 1  2  4  5  7  8 ]
                      [                  ]
                      [ 2  4  8  1  5  7 ]
                      [                  ]
                      [ 4  8  7  2  1  5 ]
(%o2)                 [                  ]
                      [ 5  1  2  7  8  4 ]
                      [                  ]
                      [ 7  5  1  8  4  2 ]
                      [                  ]
                      [ 8  7  5  4  2  1 ]


(%i3) T36_4: matrixmap(lambda([x], solve_congruences([0,x],[4,9])), T9);
                   [ 28  20  4   32  16  8  ]
                   [                        ]
                   [ 20  4   8   28  32  16 ]
                   [                        ]
                   [ 4   8   16  20  28  32 ]
(%o3)              [                        ]
                   [ 32  28  20  16  8   4  ]
                   [                        ]
                   [ 16  32  28  8   4   20 ]
                   [                        ]
                   [ 8   16  32  4   20  28 ]
```

See also: `zn_add_table`, `zn_power_table`.

<!-- category: NumberTheory -->
<!-- keywords: zn_nth_root -->
<!-- signatures: zn_nth_root(x, n, m), zn_nth_root(x, n, m, [[p1, e1], ..., [pk, ek]]) -->
### Function: zn_nth_root (x, n, m)

Returns a list with all *n*-th roots of *x* from the multiplication 
subgroup of (Z/*m*Z) which contains *x*, or `false`, if *x* 
is no *n*-th power modulo *m* or not contained in any multiplication 
subgroup of (Z/*m*Z).


*x* is an element of a multiplication subgroup modulo *m*, if the 
greatest common divisor `g = gcd(x,m)` is coprime to `m/g`.


`zn_nth_root` is based on an algorithm by Adleman, Manders and Miller 
and on theorems about modulo multiplication groups by Daniel Shanks.

 

The algorithm needs a prime factorization of the modulus *m*. 
So in case the factorization of *m* is known, the list of factors 
can be passed as the fourth argument. This optional argument
must be of the same form as the list returned by `ifactors(m)` 
using the default option `factors_only: false`.



Examples:


A power table of the multiplication group modulo `14` 
followed by a list of lists containing all *n*-th roots of `1` 
with *n* from `1` to `6`.







```maxima
maxima

(%i1) zn_power_table(14);
                    [ 1   1   1   1   1   1 ]
                    [                       ]
                    [ 3   9   13  11  5   1 ]
                    [                       ]
                    [ 5   11  13  9   3   1 ]
(%o1)               [                       ]
                    [ 9   11  1   9   11  1 ]
                    [                       ]
                    [ 11  9   1   11  9   1 ]
                    [                       ]
                    [ 13  1   13  1   13  1 ]


(%i2) makelist(zn_nth_root(1,n,14), n,1,6);
(%o2) [[1], [1, 13], [1, 9, 11], [1, 13], [1], 
                                            [1, 3, 5, 9, 11, 13]]
```


In the following example *x* is not coprime to *m*, 
but is a member of a multiplication subgroup of (Z/*m*Z) 
and any *n*-th root is a member of the same subgroup.


The residue class `3` is no member of any multiplication subgroup of (Z/63Z) 
and is therefore not returned as a third root of `27`.


Here `zn_power_table` shows all residues `x` in (Z/63Z) 
with `gcd(x,63) = 9`. This subgroup is isomorphic to (Z/7Z)*  
and its identity `36` is computed via CRT.









```maxima
maxima
(%i1) m: 7*9$

(%i2) zn_power_table(m,9);
                   [ 9   18  36  9   18  36 ]
                   [                        ]
                   [ 18  9   36  18  9   36 ]
                   [                        ]
                   [ 27  36  27  36  27  36 ]
(%o2)              [                        ]
                   [ 36  36  36  36  36  36 ]
                   [                        ]
                   [ 45  9   27  18  54  36 ]
                   [                        ]
                   [ 54  18  27  9   45  36 ]


(%i3) zn_nth_root(27,3,m);
(%o3)                     [27, 45, 54]


(%i4) id7:1$  id63_9: solve_congruences([id7,0],[7,9]);
(%o5)                          36
```


In the following RSA-like example, where the modulus `N` is squarefree, 
i.e. it splits into 
exclusively first power factors, every `x` from `0` to `N-1` 
is contained in a multiplication subgroup.


The process of decryption needs the `e`-th root. 
`e` is coprime to `totient(N)` and therefore the `e`-th root is unique. 
In this case `zn_nth_root` effectively performs CRT-RSA. 
(Please note that `flatten` removes braces but no solutions.)










```maxima
maxima
(%i1) [p,q,e]: [5,7,17]$  N: p*q$
(%i3) xs: makelist(x,x,0,N-1)$
(%i4) ys: map(lambda([x],power_mod(x,e,N)),xs)$
(%i5) zs: flatten(map(lambda([y], zn_nth_root(y,e,N)), ys))$

(%i6) is(zs = xs);
(%o6)                         true
```


In the following example the factorization of the modulus is known 
and passed as the fourth argument.










```maxima
maxima
(%i1) p: 2^107-1$  q: 2^127-1$  N: p*q$
(%i4) ibase: obase: 16$
(%i5) msg: 11223344556677889900aabbccddeeff$

(%i6) enc: power_mod(msg, 10001, N);
(%o6) 1A8DB7892AE588BDC2BE25DD5107A425001FE9C82161ABC673241C8B383


(%i7) zn_nth_root(enc, 10001, N, [[p,1],[q,1]]);
(%o7)          [11223344556677889900AABBCCDDEEFF]
```

<!-- category: NumberTheory -->
<!-- keywords: zn_order -->
<!-- signatures: zn_order(x, n), zn_order(x, n, [[p1, e1], ..., [pk, ek]]) -->
### Function: zn_order (x, n)

Returns the order of *x* if it is a unit of the finite group (Z/*n*Z)*
or returns `false`.  *x* is a unit modulo *n* if it is coprime to *n*.


The applied algorithm needs a prime factorization of `totient(n)`. This factorization 
might be time consuming in some cases and it can be useful to factor first 
and then to pass the list of factors to `zn_log` as the third argument. 
The list must be of the same form as the list returned by `ifactors(totient(n))` 
using the default option `factors_only : false`.


See also `zn_primroot`,  `ifactors`,  `totient`.


Examples:


`zn_order` computes the order of the unit *x* in (Z/*n*Z)*.













```maxima
maxima
(%i1) n: 22$

(%i2) g: zn_primroot(n);
(%o2)                           7


(%i3) units_22: sublist(makelist(i,i,1,21), lambda([x], gcd(x,n)=1));
(%o3)          [1, 3, 5, 7, 9, 13, 15, 17, 19, 21]


(%i4) (ord_7: zn_order(7, n)) = totient(n);
(%o4)                        10 = 10


(%i5) powers_7: makelist(power_mod(g,i,n), i,0,ord_7 - 1);
(%o5)          [1, 7, 5, 13, 3, 21, 15, 17, 9, 19]


(%i6) map(lambda([x], zn_order(x, n)), powers_7);
(%o6)          [1, 10, 5, 10, 5, 2, 5, 10, 5, 10]


(%i7) map(lambda([x], ord_7/gcd(x,ord_7)), makelist(i,i,0,ord_7-1));
(%o7)          [1, 10, 5, 10, 5, 2, 5, 10, 5, 10]


(%i8) totient(totient(n));
(%o8)                           4
```


The optional third argument must be of the same form as the list returned by 
`ifactors(totient(n))`.










```maxima
maxima

(%i1) (p : 2^142 + 217, primep(p));
(%o1)                         true

(%i2) ifs: ifactors( totient(p) )$

(%i3) g: zn_primroot(p, ifs);
(%o3)                           3


(%i4) is( (ord_3 : zn_order(g, p, ifs)) = totient(p) );
(%o4)                         true


(%i5) map(lambda([x], ord_3/zn_order(x,p,ifs)), makelist(i,i,2,15));
(%o5)    [22, 1, 44, 10, 5, 2, 22, 2, 8, 2, 1, 1, 20, 1]
```

See also: `zn_primroot`, `ifactors`, `totient`.

<!-- category: NumberTheory -->
<!-- keywords: zn_power_table -->
<!-- signatures: zn_power_table(n), zn_power_table(n, gcd), zn_power_table(n, gcd, max_exp) -->
### Function: zn_power_table (n)

Without any optional argument `zn_power_table(n)` 
shows a power table of all elements in (Z/*n*Z)* 
which are all residue classes coprime to *n*. 
The exponent loops from `1` to the greatest characteristic factor of 
`totient(n)` (also known as Carmichael function or Carmichael lambda)
and the table ends with a column of ones on the right side. 


The optional second argument *gcd* allows to select powers of a specific 
subset of (Z/*n*Z). If *gcd* is an integer, powers of all residue 
classes `x` with `gcd(x,n) =`*gcd* are returned,
i.e. the default value for *gcd* is `1`.   
If *gcd* is set to `all`, the table contains powers of all elements 
in (Z/*n*Z).


If the optional third argument *max_exp* is given, the exponent loops from 
`1` to *max_exp*. 


See also `zn_add_table`,  `zn_005fmult_005ftable`.


Examples:


The default which is *gcd*`= 1` allows to demonstrate and study basic 
theorems of e.g. Fermat and Euler.


The argument *gcd* allows to select subsets of (Z/*n*Z) and to study 
multiplication subgroups and isomorphisms. 
E.g. the groups `G10` and `G10_2` are under multiplication both 
isomorphic to `G5`. `1` is the identity in `G5`. 
So are `1` resp. `6` the identities in `G10` resp. `G10_2`. 
There are corresponding mappings for primitive roots, n-th roots, etc..












```maxima
maxima

(%i1) zn_power_table(10);
                         [ 1  1  1  1 ]
                         [            ]
                         [ 3  9  7  1 ]
(%o1)                    [            ]
                         [ 7  9  3  1 ]
                         [            ]
                         [ 9  1  9  1 ]


(%i2) zn_power_table(10,2);
                         [ 2  4  8  6 ]
                         [            ]
                         [ 4  6  4  6 ]
(%o2)                    [            ]
                         [ 6  6  6  6 ]
                         [            ]
                         [ 8  4  2  6 ]


(%i3) zn_power_table(10,5);
(%o3)                    [ 5  5  5  5 ]


(%i4) zn_power_table(10,10);
(%o4)                    [ 0  0  0  0 ]


(%i5) G5: [1,2,3,4];
(%o5)                     [1, 2, 3, 4]


(%i6) G10_2: map(lambda([x], solve_congruences([0,x],[2,5])), G5);
(%o6)                     [6, 2, 8, 4]


(%i7) G10: map(lambda([x], power_mod(3, zn_log(x,2,5), 10)), G5);
(%o7)                     [1, 3, 7, 9]
```


If *gcd* is set to `all`, the table contains powers of all elements 
in (Z/*n*Z).


The third argument *max_exp* allows to set the highest exponent. 
The following table shows a very small example of RSA.







```maxima
maxima
(%i1) linel:100$ N:2*5$ phi:totient(N)$ e:7$ d:inv_mod(e,phi)$

(%i6) zn_power_table(N, all, e*d);
                 [ 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 ]
                 [                                                               ]
                 [ 1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1 ]
                 [                                                               ]
                 [ 2  4  8  6  2  4  8  6  2  4  8  6  2  4  8  6  2  4  8  6  2 ]
                 [                                                               ]
                 [ 3  9  7  1  3  9  7  1  3  9  7  1  3  9  7  1  3  9  7  1  3 ]
                 [                                                               ]
                 [ 4  6  4  6  4  6  4  6  4  6  4  6  4  6  4  6  4  6  4  6  4 ]
(%o6)            [                                                               ]
                 [ 5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5 ]
                 [                                                               ]
                 [ 6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6 ]
                 [                                                               ]
                 [ 7  9  3  1  7  9  3  1  7  9  3  1  7  9  3  1  7  9  3  1  7 ]
                 [                                                               ]
                 [ 8  4  2  6  8  4  2  6  8  4  2  6  8  4  2  6  8  4  2  6  8 ]
                 [                                                               ]
                 [ 9  1  9  1  9  1  9  1  9  1  9  1  9  1  9  1  9  1  9  1  9 ]
```

See also: `zn_add_table`, `zn_mult_table`.

<!-- category: NumberTheory -->
<!-- keywords: zn_primroot -->
<!-- signatures: zn_primroot(n), zn_primroot(n, [[p1, e1], ..., [pk, ek]]) -->
### Function: zn_primroot (n)

If the multiplicative group (Z/*n*Z)* is cyclic, `zn_primroot` computes the 
smallest primitive root modulo *n*.  (Z/*n*Z)* is cyclic if *n* is equal to 
`2`, `4`, `p^k` or `2*p^k`, where `p` is prime and 
greater than `2` and `k` is a natural number.  `zn_primroot` 
performs an according pretest if the option variable `zn_primroot_pretest`
(default: `false`) is set to `true`.  In any case the computation is limited 
by the upper bound `zn_005fprimroot_005flimit`.


If (Z/*n*Z)* is not cyclic or if there is no primitive root up to 
`zn_primroot_limit`, `zn_primroot` returns `false`.


The applied algorithm needs a prime factorization of `totient(n)`. This factorization 
might be time consuming in some cases and it can be useful to factor first 
and then to pass the list of factors to `zn_log` as an additional argument. 
The list must be of the same form as the list returned by `ifactors(totient(n))` 
using the default option `factors_only : false`.


See also `zn_primroot_p`,  `zn_order`,  `ifactors`,  `totient`.


Examples:


`zn_primroot` computes the smallest primitive root modulo *n* or returns 
`false`.










```maxima
maxima
(%i1) n : 14$

(%i2) g : zn_primroot(n);
(%o2)                           3


(%i3) zn_order(g, n) = totient(n);
(%o3)                         6 = 6

(%i4) n : 15$

(%i5) zn_primroot(n);
(%o5)                         false
```


The optional second argument must be of the same form as the list returned by 
`ifactors(totient(n))`.
















```maxima
maxima

(%i1) (p : 2^142 + 217, primep(p));
(%o1)                         true

(%i2) ifs : ifactors( totient(p) )$

(%i3) g : zn_primroot(p, ifs);
(%o3)                           3


(%i4) [time(%o2), time(%o3)];
(%o4)                    [[3.2], [0.0]]


(%i5) is(zn_order(g, p, ifs) = p - 1);
(%o5)                         true

(%i6) n : 2^142 + 216$
(%i7) ifs : ifactors(totient(n))$

(%i8) zn_primroot(n, ifs), zn_primroot_limit : 200, zn_primroot_verbose : true;
`zn_primroot' stopped at zn_primroot_limit = 200
(%o8)                         false
```

See also: `zn_primroot_pretest`, `zn_primroot_limit`, `zn_primroot_p`, `zn_order`, `ifactors`, `totient`.

<!-- category: NumberTheory -->
<!-- keywords: zn_primroot_limit -->
<!-- signatures: zn_primroot_limit -->
### Variable: zn_primroot_limit

Default value: `1000` 


If `zn_primroot` cannot find a primitive root, it stops at this upper bound.
If the option variable `zn_primroot_verbose` (default: `false`) is 
set to `true`, a message will be printed when `zn_primroot_limit` is reached.

See also: `zn_primroot`, `zn_primroot_verbose`.

<!-- category: NumberTheory -->
<!-- keywords: zn_primroot_p -->
<!-- signatures: zn_primroot_p(x, n), zn_primroot_p(x, n, [[p1, e1], ..., [pk, ek]]) -->
### Function: zn_primroot_p (x, n)

Checks whether *x* is a primitive root in the multiplicative group (Z/*n*Z)*.


The applied algorithm needs a prime factorization of `totient(n)`. This factorization 
might be time consuming and in case `zn_primroot_p` will be consecutively 
applied to a list of candidates it can be useful to factor first and then to 
pass the list of factors to `zn_log` as a third argument. 
The list must be of the same form as the list returned by `ifactors(totient(n))` 
using the default option `factors_only : false`.


See also `zn_primroot`,  `zn_order`,  `ifactors`,  `totient`.


Examples:


`zn_primroot_p` as a predicate function.










```maxima
maxima
(%i1) n : 14$

(%i2) units_14 : sublist(makelist(i,i,1,13), lambda([i], gcd(i, n) = 1));
(%o2)                 [1, 3, 5, 9, 11, 13]


(%i3) zn_primroot_p(13, n);
(%o3)                         false


(%i4) sublist(units_14, lambda([x], zn_primroot_p(x, n)));
(%o4)                        [3, 5]


(%i5) map(lambda([x], zn_order(x, n)), units_14);
(%o5)                  [1, 6, 6, 3, 3, 2]
```


The optional third argument must be of the same form as the list returned by 
`ifactors(totient(n))`.









```maxima
maxima

(%i1) (p: 2^142 + 217, primep(p));
(%o1)                         true

(%i2) ifs: ifactors( totient(p) )$

(%i3) sublist(makelist(i,i,1,50), lambda([x], zn_primroot_p(x,p,ifs)));
(%o3)  [3, 12, 13, 15, 21, 24, 26, 27, 29, 33, 38, 42, 48]


(%i4) [time(%o2), time(%o3)];
(%o4)                   [[3.01], [0.03]]
```

See also: `zn_primroot`, `zn_order`, `ifactors`, `totient`.

<!-- category: NumberTheory -->
<!-- keywords: zn_primroot_pretest -->
<!-- signatures: zn_primroot_pretest -->
### Variable: zn_primroot_pretest

Default value: `false` 


The multiplicative group (Z/*n*Z)* is cyclic if *n* is equal to 
`2`, `4`, `p^k` or `2*p^k`, where `p` is prime and 
greater than `2` and `k` is a natural number.  


`zn_primroot_pretest` controls whether `zn_primroot` will check 
if one of these cases occur before it computes the smallest primitive root. 
Only if `zn_primroot_pretest` is set to `true` this pretest will be 
performed.

See also: `zn_primroot`.

<!-- category: NumberTheory -->
<!-- keywords: zn_primroot_verbose -->
<!-- signatures: zn_primroot_verbose -->
### Variable: zn_primroot_verbose

Default value: `false` 


Controls whether `zn_primroot` prints a message when reaching 
`zn_005fprimroot_005flimit`.

See also: `zn_primroot`, `zn_primroot_limit`.

