## romberg

<!-- category: Calculus -->
<!-- keywords: romberg -->
<!-- signatures: romberg(expr, x, a, b), romberg(F, a, b) -->
### Function: romberg (expr, x, a, b)

Computes a numerical integration by Romberg’s method.


`romberg(expr, x, a, b)`
returns an estimate of the integral `integrate(expr, x, a, b)`.
*expr* must be an expression which evaluates to a floating point value
when *x* is bound to a floating point value.


`romberg(F, a, b)`
returns an estimate of the integral `integrate(F(x), x, a, b)`
where `x` represents the unnamed, sole argument of *F*;
the actual argument is not named `x`.
*F* must be a Maxima or Lisp function which returns a floating point value
when the argument is a floating point value.
*F* may name a translated or compiled Maxima function.


The accuracy of `romberg` is governed by the global variables
`rombergabs` and `rombergtol`.
`romberg` terminates successfully when
the absolute difference between successive approximations is less than `rombergabs`,
or the relative difference in successive approximations is less than `rombergtol`.
Thus when `rombergabs` is 0.0 (the default)
only the relative error test has any effect on `romberg`.


`romberg` halves the stepsize at most `rombergit` times before it gives up;
the maximum number of function evaluations is therefore `2^rombergit`.
If the error criterion established by `rombergabs` and `rombergtol`
is not satisfied, `romberg` prints an error message.
`romberg` always makes at least `rombergmin` iterations;
this is a heuristic intended to prevent spurious termination when the integrand is oscillatory.


`romberg` repeatedly evaluates the integrand after binding the variable
of integration to a specific value (and not before).
This evaluation policy makes it possible to nest calls to `romberg`,
to compute multidimensional integrals.
However, the error calculations do not take the errors of nested integrations
into account, so errors may be underestimated.
Also, methods devised especially for multidimensional problems may yield
the same accuracy with fewer function evaluations.


See also `Introduction to QUADPACK`, a collection of numerical integration functions.


Examples:


A 1-dimensional integration.











```maxima
(%i1) f(x) := 1/((x - 1)^2 + 1/100) + 1/((x - 2)^2 + 1/1000)
              + 1/((x - 3)^2 + 1/200);
                    1                 1                1
(%o1) f(x) := -------------- + --------------- + --------------
                     2    1           2    1            2    1
              (x - 1)  + ---   (x - 2)  + ----   (x - 3)  + ---
                         100              1000              200


(%i2) rombergtol : 1e-6;
(%o2)                 9.999999999999999e-7


(%i3) rombergit : 15;
(%o3)                          15


(%i4) estimate : romberg (f(x), x, -5, 5);
(%o4)                   173.6730736617464


(%i5) exact : integrate (f(x), x, -5, 5);
        3/2          3/2      3/2          3/2
(%o5) 10    atan(7 10   ) + 10    atan(3 10   )
      3/2         9/2       3/2         5/2
 + 5 2    atan(5 2   ) + 5 2    atan(5 2   ) + 10 atan(60)
 + 10 atan(40)


(%i6) abs (estimate - exact) / exact, numer;
(%o6)                 7.552722451569877e-11
```


A 2-dimensional integration, implemented by nested calls to `romberg`.











```maxima
(%i1) g(x, y) := x*y / (x + y);
                                    x y
(%o1)                   g(x, y) := -----
                                   x + y


(%i2) rombergtol : 1e-6;
(%o2)                 9.999999999999999e-7


(%i3) estimate : romberg (romberg (g(x, y), y, 0, x/2), x, 1, 3);
(%o3)                  0.8193023962835647


(%i4) assume (x > 0);
(%o4)                        [x > 0]


(%i5) integrate (integrate (g(x, y), y, 0, x/2), x, 1, 3);
                                           3
                                     2 log(-) - 1
                    9                      2        9
(%o5)      (- 9 log(-)) + 9 log(3) + ------------ + -
                    2                     6         2


(%i6) exact : radcan (%);
                    26 log(3) - 26 log(2) - 13
(%o6)             - --------------------------
                                3


(%i7) abs (estimate - exact) / exact, numer;
(%o7)                 1.371197987185102e-10
```

See also: `Introduction-to-QUADPACK`.

<!-- category: Calculus -->
<!-- keywords: rombergabs -->
<!-- signatures: rombergabs -->
### Variable: rombergabs

Default value: 0.0


The accuracy of `romberg` is governed by the global variables
`rombergabs` and `rombergtol`.
`romberg` terminates successfully when
the absolute difference between successive approximations is less than `rombergabs`,
or the relative difference in successive approximations is less than `rombergtol`.
Thus when `rombergabs` is 0.0 (the default)
only the relative error test has any effect on `romberg`.


See also `rombergit` and `rombergmin`.

See also: `rombergit`, `rombergmin`.

<!-- category: Calculus -->
<!-- keywords: rombergit -->
<!-- signatures: rombergit -->
### Variable: rombergit

Default value: 11


`romberg` halves the stepsize at most `rombergit` times before it gives up;
the maximum number of function evaluations is therefore `2^rombergit`.
`romberg` always makes at least `rombergmin` iterations;
this is a heuristic intended to prevent spurious termination when the integrand is oscillatory.


See also `rombergabs` and `rombergtol`.

See also: `rombergabs`, `rombergtol`.

<!-- category: Calculus -->
<!-- keywords: rombergmin -->
<!-- signatures: rombergmin -->
### Variable: rombergmin

Default value: 0


`romberg` always makes at least `rombergmin` iterations;
this is a heuristic intended to prevent spurious termination when the integrand is oscillatory.


See also `rombergit`, `rombergabs`, and `rombergtol`.

See also: `rombergit`, `rombergabs`, `rombergtol`.

<!-- category: Calculus -->
<!-- keywords: rombergtol -->
<!-- signatures: rombergtol -->
### Variable: rombergtol

Default value: 1e-4


The accuracy of `romberg` is governed by the global variables
`rombergabs` and `rombergtol`.
`romberg` terminates successfully when
the absolute difference between successive approximations is less than `rombergabs`,
or the relative difference in successive approximations is less than `rombergtol`.
Thus when `rombergabs` is 0.0 (the default)
only the relative error test has any effect on `romberg`.


See also `rombergit` and `rombergmin`.

See also: `rombergit`, `rombergmin`.

