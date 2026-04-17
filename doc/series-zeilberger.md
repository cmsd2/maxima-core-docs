## zeilberger

<!-- category: Series -->
<!-- keywords: AntiDifference -->
<!-- signatures: AntiDifference(F_k, k) -->
### Function: AntiDifference (F_k, k)

Returns the hypergeometric anti-difference of $F_k$, if it exists.

Otherwise `AntiDifference` returns `no_hyp_antidifference`.

<!-- category: Series -->
<!-- keywords: ev_point -->
<!-- signatures: ev_point -->
### Variable: ev_point

Default value: `big_primes[10]`


`ev_point` is the value at which the variable *n* is evaluated
when executing the modular test in `parGosper`.

<!-- category: Series -->
<!-- keywords: Gosper -->
<!-- signatures: Gosper(F_k, k) -->
### Function: Gosper (F_k, k)

Returns the rational certificate $R(k)$ for $F_k$, that is,
a rational function such
that 
$F_k = R\left(k+1\right) \, F_{k+1} - R\left(k\right) \, F_k,$
if it exists.
Otherwise, `Gosper` returns `no_hyp_sol`.

<!-- category: Series -->
<!-- keywords: Gosper_in_Zeilberger -->
<!-- signatures: Gosper_in_Zeilberger -->
### Variable: Gosper_in_Zeilberger

Default value: `true`


When `Gosper_in_Zeilberger` is `true`,
the `Zeilberger` function calls `Gosper` before calling `parGosper`.
Otherwise, `Zeilberger` goes immediately to `parGosper`.

<!-- category: Series -->
<!-- keywords: GosperSum -->
<!-- signatures: GosperSum(F_k, k, a, b) -->
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

<!-- category: Series -->
<!-- keywords: linear_solver -->
<!-- signatures: linear_solver -->
### Variable: linear_solver

Default value: `linsolve`


`linear_solver` names the solver which is used to solve the system
of equations in Zeilberger’s algorithm.

<!-- category: Series -->
<!-- keywords: MAX_ORD -->
<!-- signatures: MAX_ORD -->
### Variable: MAX_ORD

Default value: 5


`MAX_ORD` is the maximum recurrence order attempted by `Zeilberger`.

<!-- category: Series -->
<!-- keywords: mod_big_prime -->
<!-- signatures: mod_big_prime -->
### Variable: mod_big_prime

Default value: `big_primes[1]`


`mod_big_prime` is the modulus used by the modular test in `parGosper`.

<!-- category: Series -->
<!-- keywords: mod_test -->
<!-- signatures: mod_test -->
### Variable: mod_test

Default value: `false`


When `mod_test` is `true`,
`parGosper` executes a
modular test for discarding systems with no solutions.

<!-- category: Series -->
<!-- keywords: mod_threshold -->
<!-- signatures: mod_threshold -->
### Variable: mod_threshold

Default value: 4


`mod_threshold` is the
greatest order for which the modular test in `parGosper` is attempted.

<!-- category: Series -->
<!-- keywords: modular_linear_solver -->
<!-- signatures: modular_linear_solver -->
### Variable: modular_linear_solver

Default value: `linsolve`


`modular_linear_solver` names the linear solver used by the modular test in `parGosper`.

<!-- category: Series -->
<!-- keywords: parGosper -->
<!-- signatures: parGosper(F_(n,k), k, n, d) -->
### Function: parGosper (F_(n,k), k, n, d)

Attempts to find a *d*-th order recurrence for $F_(n,k)$.


The algorithm yields a sequence $[s_1, s_2, ..., s_m]$ of solutions.
Each solution has the form


$[R(n, k), [a_0, a_1, ..., a_d]].$


`parGosper` returns `[]` if it fails to find a recurrence.

<!-- category: Series -->
<!-- keywords: simplified_output -->
<!-- signatures: simplified_output -->
### Variable: simplified_output

Default value: `false`


When `simplified_output` is `true`,
functions in the `zeilberger` package attempt
further simplification of the solution.

<!-- category: Series -->
<!-- keywords: trivial_solutions -->
<!-- signatures: trivial_solutions -->
### Variable: trivial_solutions

Default value: `true`


When `trivial_solutions` is `true`,
`Zeilberger` returns solutions
which have certificate equal to zero, or all coefficients equal to zero.

<!-- category: Series -->
<!-- keywords: warnings -->
<!-- signatures: warnings -->
### Variable: warnings

Default value: `true`


When `warnings` is `true`,
functions in the `zeilberger` package print
warning messages during execution.

<!-- category: Series -->
<!-- keywords: Zeilberger -->
<!-- signatures: Zeilberger(F_(n,k), k, n) -->
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

