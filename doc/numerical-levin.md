## levin

<!-- category: Numerical -->
<!-- keywords: bflevin_u_sum -->
<!-- signatures: bflevin_u_sum(a, n, n_0) -->
### Function: bflevin_u_sum (a, n, n_0)

Estimate `sum(a(n), n, n_0, inf)` using the
Levin u-transform in bigfloat arithmetic.



`bflevin_u_sum` attempts to return the sum of the infinite series
with a precision given by the global variable `fpprec` using bigfloat arithmetic.


See `levin_options` for options to control this function.
`bflevin_u_sum` uses an adaptive algorithm to increase both the number of
terms and the bigfloat precision used for internal calculations
until the estimated error is acceptable.


`load("levin")` loads this function.


See `Examples for levin` for examples.

See also: `fpprec`, `levin_options`, `Examples-for-levin`.

<!-- category: Numerical -->
<!-- keywords: levin_options -->
<!-- signatures: levin_options -->
### Function: levin_options

Function `bflevin_u_sum` attempts to return the sum of an infinite series
with a precision given by the global variable `fpprec` using bigfloat arithmetic.
`bflevin_u_sum` uses an adaptive algorithm to increase both the number of
terms used and the bigfloat precision used for internal calculations
until the estimated error is acceptable.


The undeclared array `levin_options` contains options for controlling `bflevin_u_sum`.
Note that the subscript values for `levin_options` are strings.



**levin_options["debug"]** — When `true`, `bflevin_u_sum` generates additional output. Default: `false`
**levin_options["min_terms"]** — Minimum number of terms used by `bflevin_u_sum`. Default: 5
**levin_options["max_terms"]** — Maximum number of terms used by `bflevin_u_sum`. Default: 640 (equal to 5*2^7)
**levin_options["min_precision"]** — Initial bigfloat precision for `bflevin_u_sum`. Default: 16
**levin_options["max_precision"]** — Maximum bigfloat precision for `bflevin_u_sum`. Default: 1000

See also: `bflevin_u_sum`, `fpprec`.

<!-- category: Numerical -->
<!-- keywords: levin_u_sum -->
<!-- signatures: levin_u_sum(a, n, n_0, nterms, mode), levin_u_sum(a, n, n_0, nterms) -->
### Function: levin_u_sum (a, n, n_0, nterms, mode)

Estimate `sum(a(n), n, n_0, inf)` using at most *nterms*
terms using the Levin u-transform `levin_002d1973`.


The following values are recognized for the optional argument *mode*.
If *mode* is not supplied, it is assumed to be `levin_algebraic`.



**levin_algebraic** — The calculation is performed in exact arithmetic. `levin_u_sum` returns the result.
**levin_numeric** — The calculation is performed in bigfloat arithmetic.
The return value is a list `[result, variance]`
where *result* is the result of the bigfloat calculation,
and *variance* is in units of `10^(-2*fpprec)`.


`load("levin")` loads this function.


See `Examples for levin` for examples.

See also: `levin-1973`, `Examples-for-levin`.

