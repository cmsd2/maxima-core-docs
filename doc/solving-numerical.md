## Numerical

### Function: find_root (find_root, expr, x, a, b, abserr, relerr, find_root, f, a, b, abserr, relerr, bf_find_root, expr, x, a, b, abserr, relerr, bf_find_root, f, a, b, abserr, relerr)

Finds a root of the expression *expr* or the function *f* over the
closed interval $[a, b]$.  The expression *expr* may be an
equation, in which case `find_root` seeks a root of
`lhs(expr) - rhs(expr)`.


Given that Maxima can evaluate *expr* or *f* over
$[a, b]$ and that *expr* or *f* is continuous,
`find_root` is guaranteed to find the root,
or one of the roots if there is more than one.


`find_root` initially applies binary search.
If the function in question appears to be smooth enough,
`find_root` applies linear interpolation instead.


`bf_find_root` is a bigfloat version of `find_root`.  The
function is computed using bigfloat arithmetic and a bigfloat result
is returned.  Otherwise, `bf_find_root` is identical to
`find_root`, and the following description is equally applicable
to `bf_find_root`.


The accuracy of `find_root` is governed by `abserr` and
`relerr`, which are optional keyword arguments to
`find_root`.  These keyword arguments take the form
`key=val`.  The keyword arguments are



**abserr** — Desired absolute error of function value at root.  Default is
`find_root_abs`.
**relerr** — Desired relative error of root.  Default is `find_root_rel`.


`find_root` stops when the function in question evaluates to
something less than or equal to `abserr`, or if successive
approximants *x_0*, *x_1* differ by no more than `relerr * max(abs(x_0), abs(x_1))`.  The default values of
`find_root_abs` and `find_root_rel` are both zero.


`find_root` expects the function in question to have a different sign at
the endpoints of the search interval.
When the function evaluates to a number at both endpoints
and these numbers have the same sign,
the behavior of `find_root` is governed by `find_root_error`.
When `find_root_error` is `true`,
`find_root` prints an error message.
Otherwise `find_root` returns the value of `find_root_error`.
The default value of `find_root_error` is `true`.


If *f* evaluates to something other than a number at any step in the search
algorithm, `find_root` returns a partially-evaluated `find_root`
expression.


The order of *a* and *b* is ignored; the region in which a root is
sought is $[min(a, b), max(a, b)]$.


Examples:

























```maxima
maxima

(%i1) f(x) := sin(x) - x/2;
                                        x
(%o1)                  f(x) := sin(x) - -
                                        2


(%i2) find_root (sin(x) - x/2, x, 0.1, %pi);
(%o2)                   1.895494267033981


(%i3) find_root (sin(x) = x/2, x, 0.1, %pi);
(%o3)                   1.895494267033981


(%i4) find_root (f(x), x, 0.1, %pi);
(%o4)                   1.895494267033981


(%i5) find_root (f, 0.1, %pi);
(%o5)                   1.895494267033981


(%i6) find_root (exp(x) = y, x, 0, 100);
                            x
(%o6)           find_root(%e  = y, x, 0.0, 100.0)


(%i7) find_root (exp(x) = y, x, 0, 100), y = 10;
(%o7)                   2.302585092994046


(%i8) log (10.0);
(%o8)                   2.302585092994046


(%i9) fpprec:32;
(%o9)                          32


(%i10) 32;
(%o10)                         32


(%i11) bf_find_root (exp(x) = y, x, 0, 100), y = 10;
(%o11)         2.3025850929940456840179914546844b0


(%i12) log(10b0);
(%o12)         2.3025850929940456840179914546844b0
```

See also: `find_root`.

### Function: horner (horner, expr, x, horner, expr)

Returns a rearranged representation of *expr* as in Horner’s rule, using
*x* as the main variable if it is specified.  `x` may be omitted in
which case the main variable of the canonical rational expression form of
*expr* is used.


`horner` sometimes improves stability if `expr` is
to be numerically evaluated.  It is also useful if Maxima is used to
generate programs to be run in Fortran.  See also `stringout`.









```maxima
maxima

(%i1) expr: 1e-155*x^2 - 5.5*x + 5.2e155;
                            2
(%o1)             1.0e-155 x  - 5.5 x + 5.2e155


(%i2) expr2: horner (%, x), keepfloat: true;
(%o2)         1.0 ((1.0e-155 x - 5.5) x + 5.2e155)


(%i3) ev (expr, x=1e155);
Maxima encountered a Lisp error:

 Arithmetic error FLOATING-POINT-OVERFLOW signalled.
Operation was *, operands (1.0e155 NIL).

Automatically continuing.
To enable the Lisp debugger set *debugger-hook* to nil.


(%i4) ev (expr2, x=1e155);
(%o4)                 7.000000000000006e154
```

See also: `stringout`.

### Function: newton (expr, x, x_0, eps)

Returns an approximate solution of `expr = 0` by Newton’s method,
considering *expr* to be a function of one variable, *x*.
The search begins with `x = x_0`
and proceeds until `abs(expr) < eps`
(with *expr* evaluated at the current value of *x*).


`newton` allows undefined variables to appear in *expr*,
so long as the termination test `abs(expr) < eps` evaluates
to `true` or `false`.
Thus it is not necessary that *expr* evaluate to a number.


`load("newton1")` loads this function.


See also `realroots`, `allroots`, `find_root` and
`mnewton`.


Examples:











```maxima
maxima

(%i1) load ("newton1");
(%o1) /maxima/share/numeric/newton1.mac


(%i2) newton (cos (u), u, 1, 1/100);
(%o2)                  1.5706752771612507


(%i3) ev (cos (u), u = %);
(%o3)                 1.2104963335033528e-4


(%i4) assume (a > 0);
(%o4)                        [a > 0]


(%i5) newton (x^2 - a^2, x, a/2, a^2/100);
(%o5)                 1.0003048780487804 a


(%i6) ev (x^2 - a^2, x = %);
                                           2
(%o6)                6.098490481853958e-4 a
```

See also: `realroots`, `allroots`, `find_root`, `mnewton`.

