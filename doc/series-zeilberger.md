## zeilberger

### Function: AntiDifference (F_k, k)

Returns the hypergeometric anti-difference of $F_k$, if it exists.

Otherwise `AntiDifference` returns `no_hyp_antidifference`.

### Variable: ev_point

Default value: `big_primes[10]`


`ev_point` is the value at which the variable *n* is evaluated
when executing the modular test in `parGosper`.

### Function: Gosper (F_k, k)

Returns the rational certificate $R(k)$ for $F_k$, that is,
a rational function such
that 
$F_k = R\left(k+1\right) \, F_{k+1} - R\left(k\right) \, F_k,$
if it exists.
Otherwise, `Gosper` returns `no_hyp_sol`.

### Variable: Gosper_in_Zeilberger

Default value: `true`


When `Gosper_in_Zeilberger` is `true`,
the `Zeilberger` function calls `Gosper` before calling `parGosper`.
Otherwise, `Zeilberger` goes immediately to `parGosper`.

### Function: GosperSum (F_k, k, a, b)

Returns the summation of $F_k$ from $k = a$ to $k = b$
if $F_k$ has a hypergeometric anti-difference.
Otherwise, `GosperSum` returns `nongosper_summable`.


Examples:













```maxima
(%i1) load ("zeilberger")$

(%i2) GosperSum ((-1)^k*k / (4*k^2 - 1), k, 1, n);
                           n + 1      3
                      (- 1)      (n + -)
                                      2    1
(%o2)               - ------------------ - -
                                  2        4
                      2 (4 (n + 1)  - 1)


(%i3) GosperSum (1 / (4*k^2 - 1), k, 1, n);
                                3
                          - n - -
                                2       1
(%o3)                  -------------- + -
                                2       2
                       4 (n + 1)  - 1


(%i4) GosperSum (x^k, k, 1, n);
                          n + 1
                         x          x
(%o4)                    ------ - -----
                         x - 1    x - 1


(%i5) GosperSum ((-1)^k*a! / (k!*(a - k)!), k, 1, n);
                     n + 1
                (- 1)      a! (n + 1)         a!
(%o5)       - ------------------------- - ----------
              a (- n + a - 1)! (n + 1)!   (a - 1)! a


(%i6) GosperSum (k*k!, k, 1, n);
(%o6)                     (n + 1)! - 1


(%i7) GosperSum ((k + 1)*k! / (k + 1)!, k, 1, n);
                  (n + 1) (n + 2) (n + 1)!
(%o7)             ------------------------ - 1
                          (n + 2)!


(%i8) GosperSum (1 / ((a - k)!*k!), k, 1, n);
(%o8)                  NON_GOSPER_SUMMABLE
```

### Variable: linear_solver

Default value: `linsolve`


`linear_solver` names the solver which is used to solve the system
of equations in Zeilberger’s algorithm.

### Variable: MAX_ORD

Default value: 5


`MAX_ORD` is the maximum recurrence order attempted by `Zeilberger`.

### Variable: mod_big_prime

Default value: `big_primes[1]`


`mod_big_prime` is the modulus used by the modular test in `parGosper`.

### Variable: mod_test

Default value: `false`


When `mod_test` is `true`,
`parGosper` executes a
modular test for discarding systems with no solutions.

### Variable: mod_threshold

Default value: 4


`mod_threshold` is the
greatest order for which the modular test in `parGosper` is attempted.

### Variable: modular_linear_solver

Default value: `linsolve`


`modular_linear_solver` names the linear solver used by the modular test in `parGosper`.

### Function: parGosper (F_(n,k), k, n, d)

Attempts to find a *d*-th order recurrence for $F_(n,k)$.


The algorithm yields a sequence $[s_1, s_2, ..., s_m]$ of solutions.
Each solution has the form


$[R(n, k), [a_0, a_1, ..., a_d]].$


`parGosper` returns `[]` if it fails to find a recurrence.

### Variable: simplified_output

Default value: `false`


When `simplified_output` is `true`,
functions in the `zeilberger` package attempt
further simplification of the solution.

### Variable: trivial_solutions

Default value: `true`


When `trivial_solutions` is `true`,
`Zeilberger` returns solutions
which have certificate equal to zero, or all coefficients equal to zero.

### Variable: warnings

Default value: `true`


When `warnings` is `true`,
functions in the `zeilberger` package print
warning messages during execution.

### Function: Zeilberger (F_(n,k), k, n)

Attempts to compute the indefinite hypergeometric summation of $F_(n,k)$.


`Zeilberger` first invokes `Gosper`, and if that fails to find a solution, then invokes
`parGosper` with order 1, 2, 3, ..., up to `MAX_ORD`.
If Zeilberger finds a solution before reaching `MAX_ORD`,
it stops and returns the solution.


The algorithms yields a sequence $[s_1, s_2, ..., s_m]$ of solutions.
Each solution has the form


$[R(n,k), [a_0, a_1, ..., a_d]].$


`Zeilberger` returns `[]` if it fails to find a solution.


`Zeilberger` invokes `Gosper` only if `Gosper_in_Zeilberger` is `true`.

