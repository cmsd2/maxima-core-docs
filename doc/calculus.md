## Calculus

### Variable: %c

`%c` is the integration constant in the solutions of first
order ODEs returned from `ode2`.

See also: `ode2`.

### Variable: %k1

`%k1` is the first integration constant in the solutions of second
order ODEs returned from `ode2`.

See also: `ode2`.

### Variable: %k2

`%k2` is the second integration constant in the solutions of second
order ODEs returned from `ode2`.

See also: `ode2`.

### Function: antid (expr, x, u(x))

Returns a two-element list, such that an antiderivative of *expr* with
respect to *x* can be constructed from the list.  The expression *expr*
may contain an unknown function *u* and its derivatives.


Let *L*, a list of two elements, be the return value of `antid`.
Then `L[1] + 'integrate (L[2], x)`
is an antiderivative of *expr* with respect to *x*.


When `antid` succeeds entirely,
the second element of the return value is zero.
Otherwise, the second element is nonzero,
and the first element is nonzero or zero.
If `antid` cannot make any progress,
the first element is zero and the second nonzero.


`load ("antid")` loads this function.  The `antid` package also
defines the functions `nonzeroandfreeof` and `linear`.


`antid` is related to `antidiff` as follows.
Let *L*, a list of two elements, be the return value of `antid`.
Then the return value of `antidiff` is equal to
`L[1] + 'integrate (L[2], x)` where *x* is the
variable of integration.


Examples:












```maxima
maxima
(%i1) load ("antid")$

(%i2) expr: exp (z(x)) * diff (z(x), x) * y(x);
                       z(x)       d
(%o2)                %e     y(x) (-- (z(x)))
                                  dx


(%i3) a1: antid (expr, x, z(x));
                  z(x)           z(x)  d
(%o3)          [%e     y(x), - %e     (-- (y(x)))]
                                       dx


(%i4) a2: antidiff (expr, x, z(x));
                            /
                z(x)        |   z(x)  d
(%o4)         %e     y(x) - | %e     (-- (y(x))) dx
                            |         dx
                            /


(%i5) a2 - (first (a1) + 'integrate (second (a1), x));
(%o5)                           0


(%i6) antid (expr, x, y(x));
                        z(x)       d
(%o6)             [0, %e     y(x) (-- (z(x)))]
                                   dx


(%i7) antidiff (expr, x, y(x));
                  /
                  |   z(x)       d
(%o7)             | %e     y(x) (-- (z(x))) dx
                  |              dx
                  /
```

See also: `antidiff`.

### Function: antidiff (expr, x, u, x)

Returns an antiderivative of *expr* with respect to *x*.
The expression *expr* may contain an unknown function *u* and its
derivatives.


When `antidiff` succeeds entirely, the resulting expression is free of
integral signs (that is, free of the `integrate` noun).
Otherwise, `antidiff` returns an expression
which is partly or entirely within an integral sign.
If `antidiff` cannot make any progress,
the return value is entirely within an integral sign.


`load ("antid")` loads this function.
The `antid` package also defines the functions `nonzeroandfreeof` and
`linear`.


`antidiff` is related to `antid` as follows.
Let *L*, a list of two elements, be the return value of `antid`.
Then the return value of `antidiff` is equal to
`L[1] + 'integrate (L[2], x)` where *x* is the
variable of integration.


Examples:















```maxima
maxima
(%i1) load ("antid")$

(%i2) expr: exp (z(x)) * diff (z(x), x) * y(x);
                       z(x)       d
(%o2)                %e     y(x) (-- (z(x)))
                                  dx


(%i3) a1: antid (expr, x, z(x));
                  z(x)           z(x)  d
(%o3)          [%e     y(x), - %e     (-- (y(x)))]
                                       dx


(%i4) a2: antidiff (expr, x, z(x));
                            /
                z(x)        |   z(x)  d
(%o4)         %e     y(x) - | %e     (-- (y(x))) dx
                            |         dx
                            /


(%i5) a2 - (first (a1) + 'integrate (second (a1), x));
(%o5)                           0


(%i6) antid (expr, x, y(x));
                        z(x)       d
(%o6)             [0, %e     y(x) (-- (z(x)))]
                                   dx


(%i7) antidiff (expr, x, y(x));
                  /
                  |   z(x)       d
(%o7)             | %e     y(x) (-- (z(x))) dx
                  |              dx
                  /
```

### Function: at (at, expr, eqn_1, ..., eqn_n, at, expr, eqn)

Evaluates the expression *expr* with the variables assuming the values as
specified for them in the list of equations `[eqn_1, ..., eqn_n]` or the single equation *eqn*.


If a subexpression depends on any of the variables for which a value is
specified but there is no `atvalue` specified and it can’t be otherwise
evaluated, then a noun form of the `at` is returned which displays in a
two-dimensional form.


`at` carries out multiple substitutions in parallel.


See also `atvalue`.  For other functions which carry out substitutions,
see also `subst` and `ev`.


Examples:










```maxima
maxima

(%i1) atvalue (f(x,y), [x = 0, y = 1], a^2);
                                2
(%o1)                          a


(%i2) atvalue ('diff (f(x,y), x), x = 0, 1 + y);
(%o2)                        @2 + 1


(%i3) printprops (all, atvalue);
                                |
                  d             |
                 --- (f(@1, @2))|       = @2 + 1
                 d@1            |
                                |@1 = 0

                                     2
                          f(0, 1) = a

(%o3)                         done


(%i4) diff (4*f(x, y)^2 - u(x, y)^2, x);
                  d                          d
(%o4)  8 f(x, y) (-- (f(x, y))) - 2 u(x, y) (-- (u(x, y)))
                  dx                         dx


(%i5) at (%, [x = 0, y = 1]);
                                            |
                 2              d           |
(%o5)        16 a  - 2 u(0, 1) (-- (u(x, 1))|     )
                                dx          |
                                            |x = 0
```


Note that in the last line `y` is treated differently to `x`
as `y` isn’t used as a differentiation variable.


The difference between `subst`, `at` and `ev` can be
seen in the following example:










```maxima
maxima
(%i1) e1:I(t)=C*diff(U(t),t)$
(%i2) e2:U(t)=L*diff(I(t),t)$

(%i3) at(e1,e2);
                               |
                      d        |
(%o3)       I(t) = C (-- (U(t))|                    )
                      dt       |          d
                               |U(t) = L (-- (I(t)))
                                          dt


(%i4) subst(e2,e1);
                            d      d
(%o4)             I(t) = C (-- (L (-- (I(t)))))
                            dt     dt


(%i5) ev(e1,e2,diff);
                                  2
                                 d
(%o5)                I(t) = C L (--- (I(t)))
                                   2
                                 dt
```

See also: `atvalue`, `subst`, `ev`, `at`.

### Function: at_difference (expr, x, a, b)

Returns the difference of *expr* evaluated with *x* equal to *b*
minus *expr* evaluated with *x* equal to *a*.


Noun expressions `'at_difference(expr, x, a, b)`
are displayed with a vertical bar.
This is a conventional way to represent the value of a definite integral in some contexts.


When *expr* is an antiderivative of some function, say *f*,
`at_difference` is the value of the integral of *f* with respect to *x*
over the interval from *a* to *b*,
assuming that *expr* is a continuous function of *x* on that interval.


Examples:


`at_difference` returns the difference of *expr* evaluated with *x* equal to *b*
minus *expr* evaluated with *x* equal to *a*.






```maxima
maxima

(%i1) at_difference (sin(u), u, 2, w);
(%o1)                    sin(w) - sin(2)
```


Noun expressions `'at_difference(...)` are displayed with a vertical bar.






```maxima
maxima

(%i1) 'at_difference (sin(u), u, 2, w);
                                |u = w
(%o1)                     sin(u)|
                                |u = 2
```


When *expr* is an antiderivative of some function, say *f*,
`at_difference` is the value of the integral of *f* with respect to *x*
over the interval from *a* to *b*,
assuming that *expr* is a continuous function of *x* on that interval.







```maxima
maxima

(%i1) 'integrate (cos(u), u, 3, 5) = 'at_difference (integrate (cos(u), u), u, 3, 5);
                    5
                   /
                   |                    |u = 5
(%o1)              |  cos(u) du = sin(u)|
                   |                    |u = 3
                   /
                    3


(%i2) ev (%, at_difference);
                  5
                 /
                 |
(%o2)            |  cos(u) du = sin(5) - sin(3)
                 |
                 /
                  3
```

### Variable: atomgrad

`atomgrad` is the atomic gradient property of an expression.
This property is assigned by `gradef`.

### Function: atvalue (atvalue, expr, x_1, =, a_1, ..., x_m, =, a_m, c, atvalue, expr, x_1, =, a_1, c)

Assigns the value *c* to *expr* at the point `x = a`.
Typically boundary values are established by this mechanism.


*expr* is a function evaluation, `f(x_1, ..., x_m)`,
or a derivative, `diff (f(x_1, ..., x_m), x_1, n_1, ..., x_n, n_m)`


in which the function arguments explicitly appear.
*n_i* is the order of differentiation with respect to *x_i*.


The point at which the atvalue is established is given by the list of equations
`[x_1 = a_1, ..., x_m = a_m]`.
If there is a single variable *x_1*,
the sole equation may be given without enclosing it in a list.


`printprops ([f_1, f_2, ...], atvalue)` displays the atvalues
of the functions `f_1, f_2, ...` as specified by calls to
`atvalue`.  `printprops (f, atvalue)` displays the atvalues of
one function *f*.  `printprops (all, atvalue)` displays the atvalues
of all functions for which atvalues are defined.


The symbols `@1`, `@2`, ... represent the
variables *x_1*, *x_2*, ... when atvalues are displayed.


`atvalue` evaluates its arguments.
`atvalue` returns *c*, the atvalue.


See also `at`.


Examples:










```maxima
maxima

(%i1) atvalue (f(x,y), [x = 0, y = 1], a^2);
                                2
(%o1)                          a


(%i2) atvalue ('diff (f(x,y), x), x = 0, 1 + y);
(%o2)                        @2 + 1


(%i3) printprops (all, atvalue);
                                |
                  d             |
                 --- (f(@1, @2))|       = @2 + 1
                 d@1            |
                                |@1 = 0

                                     2
                          f(0, 1) = a

(%o3)                         done


(%i4) diff (4*f(x,y)^2 - u(x,y)^2, x);
                  d                          d
(%o4)  8 f(x, y) (-- (f(x, y))) - 2 u(x, y) (-- (u(x, y)))
                  dx                         dx


(%i5) at (%, [x = 0, y = 1]);
                                            |
                 2              d           |
(%o5)        16 a  - 2 u(0, 1) (-- (u(x, 1))|     )
                                dx          |
                                            |x = 0
```

See also: `at`.

### Function: bc2 (solution, xval1, yval1, xval2, yval2)

Solves a boundary value problem for a second order differential equation.
Here: *solution* is a general solution to the equation, as found by
`ode2`; *xval1* specifies the value of the independent variable
in a first point, in the form `x = x1`, and *yval1*
gives the value of the dependent variable in that point, in the form
`y = y1`. The expressions *xval2* and *yval2*
give the values for these variables at a second point, using the same
form.


See `ode2` for an example of its usage.

See also: `ode2`.

### Function: bessel_simplify (expr)

Simplifies expressions containing Bessel functions `bessel_j`,
`bessel_y`, `bessel_i`, `bessel_k`,
`hankel_1`, `hankel_2`, `struve_h`
and `struve_005fl`.
Recurrence relations  [https://personal.math.ubc.ca/~cbm/aands/page_361.htmA&S eqn 9.1.27]() and [https://dlmf.nist.gov/10.6#iDLMF 10.6#i]()

are used to replace functions of highest order n
by functions of order n-1 and n-2.


This process is repeated until all the orders
differ by less than 2.















```maxima
(%i1) load("contrib_ode")$

(%i2) bessel_simplify(4*bessel_j(n,x^2)*(x^2-n^2/x^2)
  +x*((bessel_j(n-2,x^2)-bessel_j(n,x^2))*x
  -(bessel_j(n,x^2)-bessel_j(n+2,x^2))*x)
  -2*bessel_j(n+1,x^2)+2*bessel_j(n-1,x^2));
(%o2)                           0


(%i3) bessel_simplify( -2*bessel_j(1,z)*z^3 - 10*bessel_j(2,z)*z^2
 + 15*%pi*bessel_j(1,z)*struve_h(3,z)*z - 15*%pi*struve_h(1,z)
   *bessel_j(3,z)*z - 15*%pi*bessel_j(0,z)*struve_h(2,z)*z
 + 15*%pi*struve_h(0,z)*bessel_j(2,z)*z - 30*%pi*bessel_j(1,z)
   *struve_h(2,z) + 30*%pi*struve_h(1,z)*bessel_j(2,z));
(%o3)                           0
```

See also: `bessel_j`, `bessel_y`, `bessel_i`, `bessel_k`, `hankel_1`, `hankel_2`, `struve_h`, `struve_l`.

### Function: bode_gain (H, range, ..., plot_opts, ...)

Function to draw Bode gain plots.


Examples (1 through 7 from 


```maxima
http://www.swarthmore.edu/NatSci/echeeve1/Ref/Bode/BodeHow.html,
```

8 from Ron Crummett):


```maxima
(%i1) load("bode")$

(%i2) H1 (s) := 100 * (1 + s) / ((s + 10) * (s + 100))$

(%i3) bode_gain (H1 (s), [w, 1/1000, 1000])$

(%i4) H2 (s) := 1 / (1 + s/omega0)$

(%i5) bode_gain (H2 (s), [w, 1/1000, 1000]), omega0 = 10$

(%i6) H3 (s) := 1 / (1 + s/omega0)^2$

(%i7) bode_gain (H3 (s), [w, 1/1000, 1000]), omega0 = 10$

(%i8) H4 (s) := 1 + s/omega0$

(%i9) bode_gain (H4 (s), [w, 1/1000, 1000]), omega0 = 10$

(%i10) H5 (s) := 1/s$

(%i11) bode_gain (H5 (s), [w, 1/1000, 1000])$

(%i12) H6 (s) := 1/((s/omega0)^2 + 2 * zeta * (s/omega0) + 1)$

(%i13) bode_gain (H6 (s), [w, 1/1000, 1000]), 
                  omega0 = 10, zeta = 1/10$

(%i14) H7 (s) := (s/omega0)^2 + 2 * zeta * (s/omega0) + 1$

(%i15) bode_gain (H7 (s), [w, 1/1000, 1000]),
                  omega0 = 10, zeta = 1/10$

(%i16) H8 (s) := 0.5 / (0.0001 * s^3 + 0.002 * s^2 + 0.01 * s)$

(%i17) bode_gain (H8 (s), [w, 1/1000, 1000])$
```


To use this function write first `load("bode")`. See also `bode_005fphase`.

See also: `bode_phase`.

### Function: bode_phase (H, range, ..., plot_opts, ...)

Function to draw Bode phase plots.


Examples (1 through 7 from 


```maxima
http://www.swarthmore.edu/NatSci/echeeve1/Ref/Bode/BodeHow.html,
```

8 from Ron Crummett):


```maxima
(%i1) load("bode")$

(%i2) H1 (s) := 100 * (1 + s) / ((s + 10) * (s + 100))$

(%i3) bode_phase (H1 (s), [w, 1/1000, 1000])$

(%i4) H2 (s) := 1 / (1 + s/omega0)$

(%i5) bode_phase (H2 (s), [w, 1/1000, 1000]), omega0 = 10$

(%i6) H3 (s) := 1 / (1 + s/omega0)^2$

(%i7) bode_phase (H3 (s), [w, 1/1000, 1000]), omega0 = 10$

(%i8) H4 (s) := 1 + s/omega0$

(%i9) bode_phase (H4 (s), [w, 1/1000, 1000]), omega0 = 10$

(%i10) H5 (s) := 1/s$

(%i11) bode_phase (H5 (s), [w, 1/1000, 1000])$

(%i12) H6 (s) := 1/((s/omega0)^2 + 2 * zeta * (s/omega0) + 1)$

(%i13) bode_phase (H6 (s), [w, 1/1000, 1000]), 
                   omega0 = 10, zeta = 1/10$

(%i14) H7 (s) := (s/omega0)^2 + 2 * zeta * (s/omega0) + 1$

(%i15) bode_phase (H7 (s), [w, 1/1000, 1000]), 
                   omega0 = 10, zeta = 1/10$

(%i16) H8 (s) := 0.5 / (0.0001 * s^3 + 0.002 * s^2 + 0.01 * s)$

(%i17) bode_phase (H8 (s), [w, 1/1000, 1000])$

(%i18) block ([bode_phase_unwrap : false],
              bode_phase (H8 (s), [w, 1/1000, 1000]));

(%i19) block ([bode_phase_unwrap : true], 
              bode_phase (H8 (s), [w, 1/1000, 1000]));
```


To use this function write first `load("bode")`. See also `bode_005fgain`.

See also: `bode_gain`.

### Function: carlson_rc (x, y)

Carlson’s RC integral is defined by



$$R_C(x, y) = \frac{1}{2} \int_0^{\infty} \frac{1}{\sqrt{t+x}(t+y)}\, dt$$


$$R_C(x, y) = \frac{1}{2} \int_0^{\infty} \frac{1}{\sqrt{t+x}(t+y)}\, dt
$$



See
[https://arxiv.org/pdf/math/9409227Numerical Computation of Real or Complex Elliptic Integrals]()
for more information.


This integral is related to many elementary functions in the following
way:



$$\eqalign{ \log x &= (x-1) R_C\left(\left({\frac{1+x}{2}}\right)^2, x\right), \quad x > 0 \cr \sin^{-1} x &= x R_C(1-x^2, 1), \quad |x| \le 1 \cr \cos^{-1} x &= \sqrt{1-x^2} R_C(x^2,1), \quad 0 \le x \le 1 \cr \tan^{-1} x &= x R_C(1,1+x^2) \cr \sinh^{-1} x &= x R_C(1+x^2,1) \cr \cosh^{-1} x &= \sqrt{x^2-1} R_C(x^2,1), \quad x \ge 1 \cr \tanh^{-1}(x) &= x R_C(1,1-x^2), \quad |x| \le 1 }$$


$$\eqalign{
\log x &= (x-1) R_C\left(\left({\frac{1+x}{2}}\right)^2, x\right), \quad x > 0 \cr
\sin^{-1} x &= x R_C(1-x^2, 1), \quad |x| \le 1 \cr
\cos^{-1} x &= \sqrt{1-x^2} R_C(x^2,1), \quad 0 \le x \le 1  \cr
\tan^{-1} x &= x  R_C(1,1+x^2)  \cr
\sinh^{-1} x &= x  R_C(1+x^2,1)  \cr
\cosh^{-1} x &= \sqrt{x^2-1}  R_C(x^2,1), \quad x \ge 1  \cr
\tanh^{-1}(x) &= x  R_C(1,1-x^2), \quad |x| \le 1
}
$$



Also, we have the relationship



$$R_C(x,y) = R_F(x,y,y)$$


$$R_C(x,y) = R_F(x,y,y)
$$



Some special values:

$$\eqalign{R_C(0, 1) &= \frac{\pi}{2} \cr R_C(0, 1/4) &= \pi \cr R_C(2,1) &= \log(\sqrt{2} + 1) \cr R_C(i,i+1) &= \frac{\pi}{4} + \frac{i}{2} \log(\sqrt{2}-1) \cr R_C(0,i) &= (1-i)\frac{\pi}{2\sqrt{2}} \cr }$$


$$\eqalign{R_C(0, 1) &= \frac{\pi}{2} \cr
R_C(0, 1/4) &= \pi \cr
R_C(2,1) &= \log(\sqrt{2} + 1) \cr
R_C(i,i+1) &= \frac{\pi}{4} + \frac{i}{2} \log(\sqrt{2}-1) \cr
R_C(0,i) &= (1-i)\frac{\pi}{2\sqrt{2}} \cr
}
$$

### Function: carlson_rd (x, y, z)

Carlson’s RD integral is defined by



$$R_D(x,y,z) = \frac{3}{2} \int_0^{\infty} \frac{1}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}\,(t+z)}\, dt$$


$$R_D(x,y,z) = \frac{3}{2} \int_0^{\infty} \frac{1}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}\,(t+z)}\, dt
$$



See
[https://arxiv.org/pdf/math/9409227Numerical Computation of Real or Complex Elliptic Integrals]()
for more information.


We also have the special values



$$\eqalign{ R_D(x,x,x) &= x^{-\frac{3}{2}} \cr R_D(0,y,y) &= \frac{3}{4} \pi y^{-\frac{3}{2}} \cr R_D(0,2,1) &= 3 \sqrt{\pi} \frac{\Gamma(\frac{3}{4})}{\Gamma(\frac{1}{4})} }$$


$$\eqalign{
R_D(x,x,x) &= x^{-\frac{3}{2}} \cr
R_D(0,y,y) &= \frac{3}{4} \pi y^{-\frac{3}{2}} \cr
R_D(0,2,1) &= 3 \sqrt{\pi} \frac{\Gamma(\frac{3}{4})}{\Gamma(\frac{1}{4})}
}
$$




It is also related to the complete elliptic integral of the second
kind, $E$,
(`elliptic_ec`) as follows 



$$E(m) = R_F(0, 1 - m, 1) - \frac{m}{3} R_D(0, 1 - m, 1)$$


$$E(m) = R_F(0, 1 - m, 1) - \frac{m}{3} R_D(0, 1 - m, 1)
$$

See also: `elliptic_ec`.

### Function: carlson_rf (x, y, z)

Carlson’s RF integral is defined by



$$R_F(x,y,z) = \frac{1}{2} \int_0^{\infty} \frac{1}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}}\, dt$$


$$R_F(x,y,z) = \frac{1}{2} \int_0^{\infty} \frac{1}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}}\, dt
$$



See
[https://arxiv.org/pdf/math/9409227Numerical Computation of Real or Complex Elliptic Integrals]()
for more information.


We also have the special values



$$\eqalign{ R_F(0,1,2) &= \frac{\Gamma({\frac{1}{4}})^2}{4\sqrt{2\pi}} \cr R_F(i,-i,0) &= \frac{\Gamma({\frac{1}{4}})^2}{4\sqrt{\pi}} }$$


$$\eqalign{
R_F(0,1,2)  &= \frac{\Gamma({\frac{1}{4}})^2}{4\sqrt{2\pi}} \cr
R_F(i,-i,0) &= \frac{\Gamma({\frac{1}{4}})^2}{4\sqrt{\pi}}
}
$$



It is also related to the complete elliptic integral of the second
kind, $E$,
(`elliptic_ec`) as follows 



$$E(m) = R_F(0, 1 - m, 1) - \frac{m}{3} R_D(0, 1 - m, 1)$$


$$E(m) = R_F(0, 1 - m, 1) - \frac{m}{3} R_D(0, 1 - m, 1)
$$

See also: `elliptic_ec`.

### Function: carlson_rj (x, y, z, p)

Carlson’s RJ integral is defined by



$$R_J(x,y,z) = \frac{1}{2} \int_0^{\infty} \frac{1}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}\,(t+p)}\, dt$$


$$R_J(x,y,z) = \frac{1}{2} \int_0^{\infty} \frac{1}{\sqrt{t+x}\sqrt{t+y}\sqrt{t+z}\,(t+p)}\, dt
$$



See
[https://arxiv.org/pdf/math/9409227Numerical Computation of Real or Complex Elliptic Integrals]()
for more information.


It is related to the elliptic integral of the third kind (`elliptic_pi`)
by



$$\int_0^\phi {1\over \left(1+n\sin^2\theta\right) \sqrt{1-m\sin^2\theta}} \, d\theta = R_F(c-1,c-m,c) - {n\over 3}R_j(c-1,c-m,c,c+n)$$


$$\int_0^\phi {1\over \left(1+n\sin^2\theta\right) \sqrt{1-m\sin^2\theta}}
\, d\theta = R_F(c-1,c-m,c) - {n\over 3}R_j(c-1,c-m,c,c+n)$$



where
$c = \csc\phi.$
Note that this differs in our definition of `elliptic_pi` by the
sign of the parameter $n$.

See also: `elliptic_pi`.

### Function: changevar (expr, f(x,y), y, x)

Makes the change of variable given by `f(x,y) = 0` in all integrals
occurring in *expr* with integration with respect to *x*.
The new variable is *y*.


The change of variable can also be written `f(x) = g(y)`.









```maxima
maxima
(%i1) assume(a > 0)$

(%i2) 'integrate (%e**sqrt(a*y), y, 0, 4);
                      4
                     /
                     |    sqrt(a) sqrt(y)
(%o2)                |  %e                dy
                     |
                     /
                      0


(%i3) changevar (%, y-z^2/a, z, y);
                      0
                     /
                     |              abs(z)
                   2 |            %e       z dz
                     |
                     /
                      - 2 sqrt(a)
(%o3)            - ----------------------------
                                a
```


An expression containing a noun form, such as the instances of `'integrate`
above, may be evaluated by `ev` with the `nouns` flag.
For example, the expression returned by `changevar` above may be evaluated
by `ev (%o3, nouns)`.


`changevar` may also be used to make changes in the indices of a sum or
product.  However, it must be realized that when a change is made in a
sum or product, this change must be a shift, i.e., `i = j+ ...`, not a
higher degree function.  E.g.,







```maxima
maxima

(%i1) sum (a[i]*x^(i-2), i, 0, inf);
                         inf
                         ____
                         \         i - 2
(%o1)                     >    a  x
                         /      i
                         ----
                         i = 0


(%i2) changevar (%, i-2-n, n, i);
                        inf
                        ____
                        \               n
(%o2)                    >      a      x
                        /        n + 2
                        ----
                        n = - 2
```

### Function: contrib_ode (eqn, y, x)

Returns a list of solutions of the ODE *eqn* with 
independent variable *x* and dependent variable *y*.

### Function: dblint (f, r, s, a, b)

A double-integral routine which was written in
top-level Maxima and then translated and compiled to machine code.
Use `load ("dblint")` to access this package.  It uses the Simpson’s rule
method in both the x and y directions to calculate



$$\int_a^b \int_{r\left(x\right)}^{s\left(x\right)} f\left(x,y\right) \, dy \, dx$$


$$\int_a^b \int_{r\left(x\right)}^{s\left(x\right)} f\left(x,y\right) \, dy \, dx
$$



The function *f* must be a translated or compiled function of two variables,
and *r* and *s* must each be a translated or compiled function of one
variable, while *a* and *b* must be floating point numbers.  The routine
has two global variables which determine the number of divisions of the x and y
intervals: `dblint_x` and `dblint_y`, both of which are initially 10,
and can be changed independently to other integer values (there are
`2*dblint_x+1` points computed in the x direction, and `2*dblint_y+1`
in the y direction).  The routine subdivides the X axis and then for each value
of X it first computes `r(x)` and `s(x)`; then the Y axis
between `r(x)` and `s(x)` is subdivided and the integral
along the Y axis is performed using Simpson’s rule; then the integral along the
X axis is done using Simpson’s rule with the function values being the
Y-integrals.  This procedure may be numerically unstable for a great variety of
reasons, but is reasonably fast: avoid using it on highly oscillatory functions
and functions with singularities (poles or branch points in the region).  The Y
integrals depend on how far apart `r(x)` and `s(x)` are,
so if the distance `s(x) - r(x)` varies rapidly with X, there
may be substantial errors arising from truncation with different step-sizes in
the various Y integrals.  One can increase `dblint_x` and `dblint_y`
in an effort to improve the coverage of the region, at the expense of
computation time.  The function values are not saved, so if the function is very
time-consuming, you will have to wait for re-computation if you change anything
(sorry).  It is required that the functions *f*, *r*, and *s* be
either translated or compiled prior to calling `dblint`.  This will result
in orders of magnitude speed improvement over interpreted code in many cases!


`demo ("dblint")` executes a demonstration of `dblint` applied to an
example problem.

### Function: defint (expr, x, a, b)

Attempts to compute a definite integral.  `defint` is called by
`integrate` when limits of integration are specified, i.e., when
`integrate` is called as
`integrate (expr, x, a, b)`.
Thus from the user’s point of view, it is sufficient to call `integrate`.



`defint` returns a symbolic expression, either the computed integral or the
noun form of the integral.  See `quad_qag` and related functions for
numerical approximation of definite integrals.

See also: `quad_qag`.

### Function: del (x)

`del (x)` represents the differential of the variable $x$.


`diff` returns an expression containing `del`
if an independent variable is not specified.
In this case, the return value is the so-called "total differential".


See also `diff`, `del` and `derivdegree`.


Examples:








```maxima
maxima

(%i1) diff (log (x));
                             del(x)
(%o1)                        ------
                               x


(%i2) diff (exp (x*y));
                   x y              x y
(%o2)            %e    x del(y) + %e    y del(x)


(%i3) diff (x*y*z);
(%o3)         x y del(z) + x z del(y) + y z del(x)
```

See also: `diff`, `del`, `derivdegree`.

### Function: delta (t)

The Dirac Delta function.


Currently only `laplace` knows about the `delta` function.


Example:







```maxima
maxima
(%i1) assume(a > 0)$

(%i2) laplace (delta (t - a) * sin(b*t), t, s);
                  2 %i a b        - a s - %i a b
               (%e         - 1) %e               %i
(%o2)        - ------------------------------------
                                2
```

See also: `laplace`.

### Variable: dependencies

The variable `dependencies` is the list of atoms which have functional
dependencies, assigned by `depends`, the function `dependencies`, or `gradef`.
The `dependencies` list is cumulative:
each call to `depends`, `dependencies`, or `gradef` appends additional items.
The default value of `dependencies` is `[]`.


The function `dependencies(f_1, ..., f_n)` appends *f_1*, ..., *f_n*,
to the `dependencies` list,
where *f_1*, ..., *f_n* are expressions of the form `f(x_1, ..., x_m)`,
and *x_1*, ..., *x_m* are any number of arguments.


`dependencies(f(x_1, ..., x_m))` is equivalent to `depends(f, [x_1, ..., x_m])`.


See also `depends` and `gradef`.













```maxima
maxima

(%i1) dependencies;
(%o1)                          []


(%i2) depends (foo, [bar, baz]);
(%o2)                    [foo(bar, baz)]


(%i3) depends ([g, h], [a, b, c]);
(%o3)               [g(a, b, c), h(a, b, c)]


(%i4) dependencies;
(%o4)        [foo(bar, baz), g(a, b, c), h(a, b, c)]


(%i5) dependencies (quux (x, y), mumble (u));
(%o5)                [quux(x, y), mumble(u)]


(%i6) dependencies;
(%o6) [foo(bar, baz), g(a, b, c), h(a, b, c), quux(x, y), 
                                                       mumble(u)]


(%i7) remove (quux, dependency);
(%o7)                         done


(%i8) dependencies;
(%o8)  [foo(bar, baz), g(a, b, c), h(a, b, c), mumble(u)]
```

See also: `depends`, `gradef`.

### Function: depends (f_1, x_1, ..., f_n, x_n)

Declares functional dependencies among variables for the purpose of computing
derivatives.  In the absence of declared dependence, `diff (f, x)` yields
zero.  If `depends (f, x)` is declared, `diff (f, x)` yields a
symbolic derivative (that is, a `diff` noun).


Each argument *f_1*, *x_1*, etc., can be the name of a variable or
array, or a list of names.
Every element of *f_i* (perhaps just a single element)
is declared to depend
on every element of *x_i* (perhaps just a single element).
If some *f_i* is the name of an array or contains the name of an array,
all elements of the array depend on *x_i*.


`diff` recognizes indirect dependencies established by `depends`
and applies the chain rule in these cases.


`remove (f, dependency)` removes all dependencies declared for
*f*.


`depends` returns a list of the dependencies established.
The dependencies are appended to the global variable `dependencies`.
`depends` evaluates its arguments.


`diff` is the only Maxima command which recognizes dependencies established
by `depends`.  Other functions (`integrate`, `laplace`, etc.)
only recognize dependencies explicitly represented by their arguments.
For example, `integrate` does not recognize the dependence of `f` on
`x` unless explicitly represented as `integrate (f(x), x)`.


`depends(f, [x_1, ..., x_n])` is equivalent to `dependencies(f(x_1, ..., x_n))`.


See also `diff`, `del`, `derivdegree` and
`derivabbrev`.










```maxima
maxima

(%i1) depends ([f, g], x);
(%o1)                     [f(x), g(x)]


(%i2) depends ([r, s], [u, v, w]);
(%o2)               [r(u, v, w), s(u, v, w)]


(%i3) depends (u, t);
(%o3)                        [u(t)]


(%i4) dependencies;
(%o4)      [f(x), g(x), r(u, v, w), s(u, v, w), u(t)]


(%i5) diff (r.s, u);
                         dr            ds
(%o5)                   (--) . s + r . --
                         du            du
```






```maxima
maxima

(%i1) diff (r.s, t);
(%o1)                           0
```







```maxima
maxima

(%i1) remove (r, dependency);
(%o1)                         done


(%i2) diff (r.s, t);
(%o2)                           0
```

See also: `dependencies`, `integrate`, `diff`, `del`, `derivdegree`, `derivabbrev`.

### Variable: derivabbrev

Default value: `false`


When `derivabbrev` is `true`,
symbolic derivatives (that is, `diff` nouns) are displayed as subscripts.
Otherwise, derivatives are displayed in the Leibniz notation `dy/dx`.

### Function: derivdegree (expr, y, x)

Returns the highest degree of the derivative
of the dependent variable *y* with respect to the independent variable
*x* occurring in *expr*.


Example:







```maxima
maxima

(%i1) 'diff (y, x, 2) + 'diff (y, z, 3) + 'diff (y, x) * x^2;
                         3     2
                        d y   d y    2 dy
(%o1)                   --- + --- + x  --
                          3     2      dx
                        dz    dx


(%i2) derivdegree (%, y, x);
(%o2)                           2
```

### Function: derivlist (var_1, ..., var_k)

Causes only differentiations with respect to
the indicated variables, within the `ev` command.

See also: `ev`.

### Variable: derivsubst

Default value: `false`


When `derivsubst` is `true`, a non-syntactic substitution such as
`subst (x, 'diff (y, t), 'diff (y, t, 2))` yields `'diff (x, t)`.

### Function: desolve (desolve, eqn, y, desolve, eqn_1, ..., eqn_n, y_1, ..., y_n)

The function `desolve` solves systems of linear ordinary
differential equations using Laplace transform. Here the *eqn*’s are
differential equations in the dependent variables *y_1*, ...,
*y_n*. The functional dependence of *y_1*, ..., *y_n* on an
independent variable, for instance *x*, must be explicitly indicated
in the variables and its derivatives. For example, the *correct*
way to define the differential equations would be:



```maxima
eqn_1: 'diff(f(x),x,2) = sin(x) + 'diff(g(x),x);
eqn_2: 'diff(f(x),x) + x^2 - f(x) = 2*'diff(g(x),x,2);
```


The call to the function `desolve` would then be:


```maxima
desolve([eqn_1, eqn_2], [f(x),g(x)]);
```


If initial conditions at `x=0` are known, they can be supplied before
calling `desolve` by using `atvalue`.











```maxima
maxima

(%i1) 'diff(f(x),x)='diff(g(x),x)+sin(x);
                 d           d
(%o1)            -- (f(x)) = -- (g(x)) + sin(x)
                 dx          dx


(%i2) 'diff(g(x),x,2)='diff(f(x),x)-cos(x);
                  2
                 d            d
(%o2)            --- (g(x)) = -- (f(x)) - cos(x)
                   2          dx
                 dx


(%i3) atvalue('diff(g(x),x),x=0,a);
(%o3)                           a


(%i4) atvalue(f(x),x=0,1);
(%o4)                           1


(%i5) desolve([%o1,%o2],[f(x),g(x)]);
                x
(%o5) [f(x) = %e  a - a + 1, g(x) = 
                                              x
                                   cos(x) + %e  a - a + g(0) - 1]


(%i6) [%o1,%o2],%o5,diff;
           x       x      x                x
(%o6)   [%e  a = %e  a, %e  a - cos(x) = %e  a - cos(x)]
```


If `desolve` cannot obtain a solution, it returns `false`.


See also `ode2`, `drawdf` and `rk`.

See also: `atvalue`, `ode2`, `drawdf`, `rk`.

### Function: dgauss_a (a, b, c, x)

The derivative with respect to *x* 
of `gauss_a``(a, b, c, x)`.

See also: `gauss_a`.

### Function: dgauss_b (a, b, c, x)

The derivative with respect to *x* 
of `gauss_b``(a, b, c, x)`.

See also: `gauss_b`.

### Function: diff (diff, expr, x_1, n_1, ..., x_m, n_m, diff, expr, x, n, diff, expr, x, diff, expr)

Returns the derivative or differential of *expr* with respect to some or
all variables in *expr*.


`diff (expr, x, n)` returns the *n*’th derivative of
*expr* with respect to *x*.


`diff (expr, x_1, n_1, ..., x_m, n_m)`
returns the mixed partial derivative of *expr* with respect to *x_1*, 
..., *x_m*.  It is equivalent to `diff (... (diff (expr, x_m, n_m) ...), x_1, n_1)`.


`diff (expr, x)`
returns the first derivative of *expr* with respect to
the variable *x*.


`diff (expr)` returns the total differential of *expr*, that is,
the sum of the derivatives of *expr* with respect to each its variables
times the differential `del` of each variable.

No further simplification of `del` is offered.


The noun form of `diff` is required in some contexts,
such as stating a differential equation.
In these cases, `diff` may be quoted (as `'diff`) to yield the noun
form instead of carrying out the differentiation.


When `derivabbrev` is `true`, derivatives are displayed as subscripts.
Otherwise, derivatives are displayed in the Leibniz notation, `dy/dx`.


See also `depends`, `del`, `derivdegree`, `derivabbrev`, and `gradef`.


Examples:









```maxima
maxima

(%i1) diff (exp (f(x)), x, 2);
                     2
              f(x)  d               f(x)  d         2
(%o1)       %e     (--- (f(x))) + %e     (-- (f(x)))
                      2                   dx
                    dx

(%i2) derivabbrev: true$

(%i3) 'integrate (f(x, y), y, g(x), h(x));
                         h(x)
                        /
                        |
(%o3)                   |     f(x, y) dy
                        |
                        /
                         g(x)


(%i4) diff (%, x);
       h(x)
      /
      |
(%o4) |     (f(x, y))  dy + f(x, h(x)) (h(x))
      |              x                       x
      /
       g(x)
                                             - f(x, g(x)) (g(x))
                                                                x
```


For the tensor package, the following modifications have been
incorporated:


(1) The derivatives of any indexed objects in *expr* will have the
variables *x_i* appended as additional arguments.  Then all the
derivative indices will be sorted.


(2) The *x_i* may be integers from 1 up to the value of the variable
`dimension` [default value: 4].  This will cause the differentiation to be
carried out with respect to the *x_i*’th member of the list
`coordinates` which should be set to a list of the names of the
coordinates, e.g., `[x, y, z, t]`. If `coordinates` is bound to an
atomic variable, then that variable subscripted by *x_i* will be used for
the variable of differentiation.  This permits an array of coordinate names or
subscripted names like `X[1]`, `X[2]`, ... to be used.  If
`coordinates` has not been assigned a value, then the variables will be
treated as in (1) above.

See also: `depends`, `del`, `derivdegree`, `derivabbrev`, `gradef`.

### Function: dkummer_m (a, b, x)

The derivative with respect to *x*
of `kummer_m``(a, b, x)`.

See also: `kummer_m`.

### Function: dkummer_u (a, b, x)

The derivative with respect to *x*
of `kummer_u``(a, b, x)`.

See also: `kummer_u`.

### Function: dlsode_init (fex, vars, method)

This must be called before running the solver.  This function returns
a state object for use in the solver.  The user must not modify the
state.


The ODE to be solved is given in *fex*, which is a list of the
equations.  *vars* is a list of independent variable and the
dependent variables.  The list of dependent variables must be in the
same order as the equations if *fex*.  Finally, *method*
indicates the method to be used by the solver:


> **10** — Nonstiff (Adams) method, no Jacobian used.
> **21** — Stiff (BDF) method, user-supplied full Jacobian.
> **22** — Stiff method, internally generated full Jacobian.



The returned state object is a list of lists.  The sublist is a list
of two elements:

> **f** — The compiled function for the ODE.
> **vars** — The list independent and dependent variables (*vars*).
> **mf** — The method to be used (*method*).
> **neq** — The number of equations.
> **lrw** — Length of the work vector for real values.
> **liw** — Length of the work vector for integer values.
> **rwork** — Lisp array holding the real-valued work vector.
> **iwork** — Lisp array holding the integer-valued work vector.
> **fjac** — Compiled analytical Jacobian of the equations



See also `dlsode_005fstep`.  `Getting-Started-with-ODEPACK` for
an example of usage.

See also: `dlsode_step`, `Getting-Started-with-ODEPACK`.

### Function: dlsode_step (inity, t, tout, rtol, atol, istate, state)

Performs one step of the solver, returning the values of the
independent and dependent variables, a success or error code.


The parameters for `dlsode_step` are:


> **inity** — For the first call (when istate = 1), the initial values
> **t** — Current value of the independent value
> **tout** — Next point where output is desired which must not be equal to *t*.
> **rtol** — relative tolerance parameter
> **atol** — Absolute tolerance parameter, scalar of vector.  If
> scalar, it applies to all dependent variables.
> Otherwise it must be the tolerance for each dependent
> variable. 
> Use *rtol* = 0 for pure absolute error and use *atol* = 0
> for pure relative error.
> **istate** — 1 for the first call to dlsode, 2 for subsequent calls.
> **state** — state returned by dlsode_init.



The output is a list of the following items:

> **t** — independent variable value
> **y** — list of values of the dependent variables at time t.
> **istate** — Integration status: > **1** — no work because tout = tt
> > **2** — successful result
> > **-1** — Excess work done on this call
> > **-2** — Excess accuracy requested
> > **-3** — Illegal input detected
> > **-4** — Repeated error test failures
> > **-5** — Repeated convergence failures (perhaps bad Jacobian or wrong choice of
> > mf or tolerances)
> > **-6** — Error weight because zero during problem (solution component is
> > vanished and atol(i) = 0.
> **info** — association list of various bits of information: > **n_steps** — total steps taken thus far
> > **n_f_eval** — total number of function evals
> > **n_j_eval** — total number of Jacobian evals
> > **method_order** — method order
> > **len_rwork** — Actual length used for real work array
> > **len_iwork** — Actual length used for integer work array



See also `dlsode_005finit`.  `Getting-Started-with-ODEPACK` for
an example of usage.

See also: `dlsode_init`, `Getting-Started-with-ODEPACK`.

### Function: elliptic_e (phi, m)

The incomplete elliptic integral of the second kind, defined as



$$\int_0^\phi {\sqrt{1 - m\sin^2\theta}}\, d\theta$$


$$\int_0^\phi {\sqrt{1 - m\sin^2\theta}}\, d\theta
$$



See also `elliptic_005ff` and `elliptic_005fec`.

See also: `elliptic_f`, `elliptic_ec`.

### Function: elliptic_ec (m)

The complete elliptic integral of the second kind, defined as



$$\int_0^{\frac{\pi}{2}} \sqrt{1 - m\sin^2\theta}\, d\theta$$


$$\int_0^{\frac{\pi}{2}} \sqrt{1 - m\sin^2\theta}\, d\theta
$$



For certain values of $m$, the value of the integral is known in
terms of `gamma` functions.  Use `makegamma` to evaluate them.

See also: `gamma`, `makegamma`.

### Function: elliptic_eu (u, m)

The incomplete elliptic integral of the second kind, defined as



$$E(u, m) = \int_0^u {\rm dn}(v, m)\, dv = \int_0^\tau \sqrt{\frac{1-m t^2}{1-t^2}}\, dt$$


$$E(u, m) = \int_0^u {\rm dn}(v, m)\, dv  = \int_0^\tau \sqrt{\frac{1-m t^2}{1-t^2}}\, dt
$$



where 
$\tau = {\rm sn}(u,m) .$



This is related to `elliptic_e` by



$$E(u,m) = E(\sin^{-1} {\rm sn}(u, m), m)$$


$$E(u,m) = E(\sin^{-1} {\rm sn}(u, m), m)
$$



See also `elliptic_005fe`.

See also: `elliptic_e`.

### Function: elliptic_f (phi, m)

The incomplete elliptic integral of the first kind, defined as



$$\int_0^{\phi} {\frac{d\theta}{\sqrt{1-m\sin^2\theta}}}$$


$$\int_0^{\phi} {\frac{d\theta}{\sqrt{1-m\sin^2\theta}}}
$$



See also `elliptic_005fe` and `elliptic_005fkc`.

See also: `elliptic_e`, `elliptic_kc`.

### Function: elliptic_kc (m)

The complete elliptic integral of the first kind, defined as



$$\int_0^{\frac{\pi}{2}} {{d\theta}\over{\sqrt{1 - m\sin^2\theta}}}$$


$$\int_0^{\frac{\pi}{2}} {{d\theta}\over{\sqrt{1 - m\sin^2\theta}}}
$$



For certain values of $m$, the value of the integral is known in
terms of `gamma` functions.  Use `makegamma` to evaluate them.

See also: `gamma`, `makegamma`.

### Function: elliptic_pi (n, phi, m)

The incomplete elliptic integral of the third kind, defined as



$$\int_0^\phi {{d\theta}\over{(1-n\sin^2 \theta)\sqrt{1 - m\sin^2\theta}}}$$


$$\int_0^\phi {{d\theta}\over{(1-n\sin^2 \theta)\sqrt{1 - m\sin^2\theta}}}
$$

### Variable: erfflag

Default value: `true`


When `erfflag` is `false`, prevents `risch` from introducing the
`erf` function in the answer if there were none in the integrand to
begin with.

### Function: expintegral_chi (z)

The Exponential Integral Chi(z) ([https://personal.math.ubc.ca/~cbm/aands/page_231.htmA&S eqn 5.2.4]()
and [https://dlmf.nist.gov/6.2#E16DLMF 6.2#E16]()) defined as



$${\rm Chi}(z) = \gamma + \log z + \int_0^z {{\cosh t - 1} \over t} dt$$


$${\rm Chi}(z) = \gamma + \log z + \int_0^z {{\cosh t - 1} \over t} dt$$



with 
$|\arg z| < \pi.$


This can be written in terms of other functions.  `expintrep` for examples.

See also: `expintrep`.

### Function: expintegral_ci (z)

The Exponential Integral Ci(z) ([https://personal.math.ubc.ca/~cbm/aands/page_231.htmA&S eqn 5.2.2]()
and [https://dlmf.nist.gov/6.2#E13DLMF 6.2#E13]()) defined as



$${\rm Ci}(z) = \gamma + \log z + \int_0^z {{\cos t - 1} \over t} dt$$


$${\rm Ci}(z) = \gamma + \log z + \int_0^z {{\cos t - 1} \over t} dt$$



with 
$|\arg z| < \pi.$


This can be written in terms of other functions.  `expintrep` for examples.

See also: `expintrep`.

### Function: expintegral_e (n, z)

The Exponential Integral En(z) ([https://personal.math.ubc.ca/~cbm/aands/page_228.htmA&S eqn 5.1.4]()) defined as



$$E_n(z) = \int_1^\infty {e^{-zt} \over t^n} dt$$


$$E_n(z) = \int_1^\infty {e^{-zt} \over t^n} dt$$


with 
${\rm Re}(z) > 1$
and $n$ a
non-negative integer.


For half-integral orders, this can be written in terms of `erfc`
or `erf`.  `expintexpand` for examples.

See also: `erfc`, `erf`, `expintexpand`.

### Function: expintegral_e1 (z)

The Exponential Integral E1(z) defined as



$$E_1(z) = \int_z^\infty {e^{-t} \over t} dt$$


$$E_1(z) = \int_z^\infty {e^{-t} \over t} dt$$



with 
$\left| \arg z \right| < \pi.$
([https://personal.math.ubc.ca/~cbm/aands/page_228.htmA&S eqn 5.1.1]()) and ([https://dlmf.nist.gov/6.2E2DLMF 6.2E2]())


This can be written in terms of other functions.  `expintrep` for examples.

See also: `expintrep`.

### Function: expintegral_e_simplify (expr)

Simplify expressions containing exponential integral `expintegral_e`
using the recurrence [https://personal.math.ubc.ca/~cbm/aands/page_229.htmA&S eqn 5.1.14]().


   

expintegral_e(n+1,z) 
        = (1/n) * (exp(-z)-z*expintegral_e(n,z))      n = 1,2,3 ....

See also: `expintegral_e`.

### Function: expintegral_ei (x)

The Exponential Integral Ei(x) defined as



$$Ei(x) = - -\kern-10.5pt\int_{-x}^\infty {e^{-t} \over t} dt = -\kern-10.5pt\int_{-\infty}^x {e^{t} \over t} dt$$


$$Ei(x)
  = - -\kern-10.5pt\int_{-x}^\infty {e^{-t} \over t} dt
  = -\kern-10.5pt\int_{-\infty}^x {e^{t} \over t} dt  $$



with $x$ real and $x > 0$. ([https://personal.math.ubc.ca/~cbm/aands/page_228.htmA&S eqn 5.1.2]()) and ([https://dlmf.nist.gov/6.2E5DLMF 6.2E5]())


This can be written in terms of other functions.  `expintrep` for examples.

See also: `expintrep`.

### Function: expintegral_li (x)

The Exponential Integral li(x) defined as



$$li(x) = -\kern-10.5pt\int_0^x {dt \over \ln t}$$


$$li(x) = -\kern-10.5pt\int_0^x {dt \over \ln t}$$



with $x$ real and $x > 1$. ([https://personal.math.ubc.ca/~cbm/aands/page_228.htmA&S eqn 5.1.3]()) and ([https://dlmf.nist.gov/6.2E8DLMF 6.2E8]())


This can be written in terms of other functions.  `expintrep` for examples.

See also: `expintrep`.

### Function: expintegral_shi (z)

The Exponential Integral Shi(z) ([https://personal.math.ubc.ca/~cbm/aands/page_231.htmA&S eqn 5.2.3]()
and [https://dlmf.nist.gov/6.2#E15DLMF 6.2#E15]()) defined as



$${\rm Shi}(z) = \int_0^z {\sinh t \over t} dt$$


$${\rm Shi}(z) = \int_0^z {\sinh t \over t} dt$$



This can be written in terms of other functions.  `expintrep` for examples.

See also: `expintrep`.

### Function: expintegral_si (z)

The Exponential Integral Si(z) ([https://personal.math.ubc.ca/~cbm/aands/page_231.htmA&S eqn 5.2.1]()
and [https://dlmf.nist.gov/6.2#E9DLMF 6.2#E9]()) defined as



$${\rm Si}(z) = \int_0^z {\sin t \over t} dt$$


$${\rm Si}(z) = \int_0^z {\sin t \over t} dt$$



This can be written in terms of other functions.  `expintrep` for examples.

See also: `expintrep`.

### Variable: expintexpand

Default value: false


Expand `expintegral_005fe` for half
integral values in terms of `erfc` or `erf` and
for positive integers in terms of `expintegral_ei`.










```maxima
maxima

(%i1) expintegral_e(1/2,z);
                                     1
(%o1)                  expintegral_e(-, z)
                                     2


(%i2) expintegral_e(1,z);
(%o2)                  expintegral_e(1, z)


(%i3) expintexpand:true;
(%o3)                         true


(%i4) expintegral_e(1/2,z);
                     sqrt(%pi) erfc(sqrt(z))
(%o4)                -----------------------
                             sqrt(z)


(%i5) expintegral_e(1,z);
                       1
                 log(- -) - log(- z)
                       z
(%o5) - log(z) - ------------------- - expintegral_ei(- z)
                          2
```

See also: `expintegral_e`, `erfc`, `erf`, `expintegral_ei`.

### Variable: expintrep

Default value: `false`


Change the representation of one of the exponential integrals,
`expintegral_005fe`,
`expintegral_005fe1`, or
`expintegral_005fei` to an equivalent form if possible.






















The possible values for `expintrep` are:


**false** — The representation is not changed.
**gamma_incomplete** — The representation uses `gamma_incomplete`.
**expintegral_e1** — The representation uses `expintegral_e1`.
**expintegral_ei** — The representation uses `expintegral_ei`.
**expintegral_li** — The representation uses `expintegral_li`.
**expintegral_trig** — The representation uses `expintegral_si` or `expintegral_ci`.
**expintegral_hyp** — The representation uses `expintegral_shi` or `expintegral_chi`.


Here are some examples for `expintrep` set to
`expintrep_002dgamma_002dincomplete`:













```maxima
maxima

(%i1) expintrep:'gamma_incomplete;
(%o1)                   gamma_incomplete


(%i2) expintegral_e1(z);
(%o2)                gamma_incomplete(0, z)


(%i3) expintegral_ei(z);
(%o3)     log(z) - log(- z) - gamma_incomplete(0, - z)


(%i4) expintegral_li(z);
(%o4) log(log(z)) - log(- log(z)) - gamma_incomplete(0, - log(z))


(%i5) expintegral_e(n,z);
                                            n - 1
(%o5)           gamma_incomplete(1 - n, z) z


(%i6) expintegral_si(z);
(%o6) (%i (- log(%i z) + log(- %i z) - gamma_incomplete(0, %i z)
                                + gamma_incomplete(0, - %i z)))/2


(%i7) expintegral_ci(z);
(%o7) log(z) - (log(%i z) + log(- %i z)
     + gamma_incomplete(0, %i z) + gamma_incomplete(0, - %i z))/2


(%i8) expintegral_shi(z);
(%o8) (log(z) - log(- z) + gamma_incomplete(0, z)
                                    - gamma_incomplete(0, - z))/2


(%i9) expintegral_chi(z);
(%o9) - (- log(z) + log(- z) + gamma_incomplete(0, z)
                                    + gamma_incomplete(0, - z))/2
```


For `expintrep` set to `expintrep_002dexpintegral_002de1`:













```maxima
maxima

(%i1) expintrep:'expintegral_e1;
(%o1)                    expintegral_e1


(%i2) expintegral_ei(z);
(%o2)        log(z) - log(- z) - expintegral_e1(- z)


(%i3) expintegral_li(z);
(%o3) log(log(z)) - log(- log(z)) - expintegral_e1(- log(z))


(%i4) expintegral_e(n,z);
(%o4)                  expintegral_e(n, z)


(%i5) expintegral_si(z);
(%o5) (%i (- log(%i z) - expintegral_e1(%i z) + log(- %i z)
                                     + expintegral_e1(- %i z)))/2


(%i6) expintegral_ci(z);
(%o6) log(z) - (log(- %i z) (expintegral_e1(%i z)
                           + expintegral_e1(- %i z)) log(%i z))/2


(%i7) expintegral_shi(z);
      log(z) + expintegral_e1(z) - log(- z) - expintegral_e1(- z)
(%o7) -----------------------------------------------------------
                                   2


(%i8) expintegral_chi(z);
(%o8) 
    - log(z) + expintegral_e1(z) + log(- z) + expintegral_e1(- z)
  - -------------------------------------------------------------
                                  2
```


For `expintrep` set to `expintrep_002dexpintegral_002dei`:














```maxima
maxima

(%i1) expintrep:'expintegral_ei;
(%o1)                    expintegral_ei


(%i2) expintegral_e1(z);
                                  1
                 log(- z) - log(- -)
                                  z
(%o2) - log(z) + ------------------- - expintegral_ei(- z)
                          2


(%i3) expintegral_ei(z);
(%o3)                   expintegral_ei(z)


(%i4) expintegral_li(z);
(%o4)                expintegral_ei(log(z))


(%i5) expintegral_e(n,z);
(%o5)                  expintegral_e(n, z)


(%i6) expintegral_si(z);
(%o6) (%i (log(%i z) + 2 (expintegral_ei(- %i z)
                                              %i          %i
  - expintegral_ei(%i z)) - log(- %i z) + log(--) - log(- --)))/4
                                              z           z


(%i7) expintegral_ci(z);
(%o7) (- log(%i z) + 2 (expintegral_ei(%i z)
                                               %i          %i
 + expintegral_ei(- %i z)) - log(- %i z) + log(--) + log(- --))/4
                                               z           z
 + log(z)


(%i8) expintegral_shi(z);
(%o8) (- 2 log(z) + 2 (expintegral_ei(z) - expintegral_ei(- z))
                                                            1
                                         + log(- z) - log(- -))/4
                                                            z


(%i9) expintegral_chi(z);
(%o9) (2 log(z) + 2 (expintegral_ei(z) + expintegral_ei(- z))
                                                            1
                                         - log(- z) + log(- -))/4
                                                            z
```


For `expintrep` set to `expintrep_002dexpintegral_002dli`:














```maxima
maxima

(%i1) expintrep:'expintegral_li;
(%o1)                    expintegral_li


(%i2) expintegral_e1(z);
                                                          1
                                         log(- z) - log(- -)
                         - z                              z
(%o2) - expintegral_li(%e   ) - log(z) + -------------------
                                                  2


(%i3) expintegral_ei(z);
                                        z
(%o3)                  expintegral_li(%e )


(%i4) expintegral_li(z);
(%o4)                   expintegral_li(z)


(%i5) expintegral_e(n,z);
(%o5)                  expintegral_e(n, z)


(%i6) expintegral_si(z);
                              %i z                     - %e z
(%o6) - (%i (expintegral_li(%e    ) - expintegral_li(%e      )
                                                %pi signum(z)
                                              - -------------))/2
                                                      2


(%i7) expintegral_ci(z);
                       %i z                     - %i z
      expintegral_li(%e    ) + expintegral_li(%e      )
(%o7) -------------------------------------------------
                              2
                                                  - signum(z) + 1


(%i8) expintegral_shi(z);
                            z                     - z
           expintegral_li(%e ) - expintegral_li(%e   )
(%o8)      -------------------------------------------
                                2


(%i9) expintegral_chi(z);
                            z                     - z
           expintegral_li(%e ) + expintegral_li(%e   )
(%o9)      -------------------------------------------
                                2
```


For `expintrep` set to `expintrep_002dexpintegral_002dtrig`:














```maxima
maxima

(%i1) expintrep:'expintegral_trig;
(%o1)                   expintegral_trig


(%i2) expintegral_e1(z);
(%o2) log(%i z) - %i expintegral_si(%i z) - expintegral_ci(%i z)
                                                         - log(z)


(%i3) expintegral_ei(z);
(%o3) - log(%i z) - %i expintegral_si(%i z)
                                  + expintegral_ci(%i z) + log(z)


(%i4) expintegral_li(z);
(%o4) - log(%i log(z)) - %i expintegral_si(%i log(z))
                        + expintegral_ci(%i log(z)) + log(log(z))


(%i5) expintegral_e(n,z);
(%o5)                  expintegral_e(n, z)


(%i6) expintegral_si(z);
(%o6)                   expintegral_si(z)


(%i7) expintegral_ci(z);
(%o7)                   expintegral_ci(z)


(%i8) expintegral_shi(z);
(%o8)               - %i expintegral_si(%i z)


(%i9) expintegral_chi(z);
(%o9)      - log(%i z) + expintegral_ci(%i z) + log(z)
```


For `expintrep` set to `expintrep_002dexpintegral_002dhyp`:














```maxima
maxima

(%i1) expintrep:'expintegral_hyp;
(%o1)                    expintegral_hyp


(%i2) expintegral_e1(z);
(%o2)        expintegral_shi(z) - expintegral_chi(z)


(%i3) expintegral_ei(z);
(%o3)        expintegral_shi(z) + expintegral_chi(z)


(%i4) expintegral_li(z);
(%o4)   expintegral_shi(log(z)) + expintegral_chi(log(z))


(%i5) expintegral_e(n,z);
(%o5)                  expintegral_e(n, z)


(%i6) expintegral_si(z);
(%o6)              - %i expintegral_shi(%i z)


(%i7) expintegral_ci(z);
(%o7)     - log(%i z) + expintegral_chi(%i z) + log(z)


(%i8) expintegral_shi(z);
(%o8)                  expintegral_shi(z)


(%i9) expintegral_chi(z);
(%o9)                  expintegral_chi(z)
```

See also: `false`, `expintegral_e`, `expintegral_e1`, `expintegral_ei`, `expintrep`, `gamma_incomplete`, `expintegral_li`, `expintegral_si`, `expintegral_ci`, `expintegral_shi`, `expintegral_chi`, `expintrep-gamma-incomplete`, `expintrep-expintegral-e1`, `expintrep-expintegral-ei`, `expintrep-expintegral-li`, `expintrep-expintegral-trig`, `expintrep-expintegral-hyp`.

### Function: express (expr)

Expands differential operator nouns into expressions in terms of partial
derivatives.  `express` recognizes the operators `grad`, `div`,
`curl`, `laplacian`.  `express` also expands the cross product
`~`.


Symbolic derivatives (that is, `diff` nouns)
in the return value of express may be evaluated by including `diff`
in the `ev` function call or command line.
In this context, `diff` acts as an `evfun`.


`load ("vect")` loads this function.



Examples:




















```maxima
maxima
(%i1) load ("vect")$

(%i2) grad (x^2 + y^2 + z^2);
                              2    2    2
(%o2)                  grad (z  + y  + x )


(%i3) express (%);
       d    2    2    2   d    2    2    2   d    2    2    2
(%o3) [-- (z  + y  + x ), -- (z  + y  + x ), -- (z  + y  + x )]
       dx                 dy                 dz


(%i4) ev (%, diff);
(%o4)                    [2 x, 2 y, 2 z]


(%i5) div ([x^2, y^2, z^2]);
                              2   2   2
(%o5)                   div [x , y , z ]


(%i6) express (%);
                   d    2    d    2    d    2
(%o6)              -- (z ) + -- (y ) + -- (x )
                   dz        dy        dx


(%i7) ev (%, diff);
(%o7)                    2 z + 2 y + 2 x


(%i8) curl ([x^2, y^2, z^2]);
                               2   2   2
(%o8)                   curl [x , y , z ]


(%i9) express (%);
       d    2    d    2   d    2    d    2   d    2    d    2
(%o9) [-- (z ) - -- (y ), -- (x ) - -- (z ), -- (y ) - -- (x )]
       dy        dz       dz        dx       dx        dy


(%i10) ev (%, diff);
(%o10)                      [0, 0, 0]


(%i11) laplacian (x^2 * y^2 * z^2);
                                  2  2  2
(%o11)                laplacian (x  y  z )


(%i12) express (%);
         2                2                2
        d     2  2  2    d     2  2  2    d     2  2  2
(%o12)  --- (x  y  z ) + --- (x  y  z ) + --- (x  y  z )
          2                2                2
        dz               dy               dx


(%i13) ev (%, diff);
                      2  2      2  2      2  2
(%o13)             2 y  z  + 2 x  z  + 2 x  y


(%i14) [a, b, c] ~ [x, y, z];
(%o14)                [a, b, c] ~ [x, y, z]


(%i15) express (%);
(%o15)          [b z - c y, c x - a z, a y - b x]
```

See also: `~`, `diff`, `evfun`.

### Function: gauss_a (a, b, c, x)

`gauss_a(a,b,c,x)` and `gauss_b(a,b,c,x)` are 2F1 
hypergeometric functions.  They represent any two independent
solutions of the hypergeometric differential equation 
`x*(1-x) diff(y,x,2) + [c-(a+b+1)x] diff(y,x) - a*b*y = 0`
See [https://personal.math.ubc.ca/~cbm/aands/page_562.htmA&S eqn 15.5.1]() and [https://dlmf.nist.gov/15.10DLMF 15.10]().  


The only use of these functions is in solutions of ODEs returned by 
`odelin` and `contrib_ode`.  The definition and use of these 
functions may change in future releases of Maxima.


See also `gauss_b`, `dgauss_a` and `gauss_005fb`.

See also: `odelin`, `contrib_ode`, `gauss_b`, `dgauss_a`.

### Function: gauss_b (a, b, c, x)

See `gauss_005fa`.

See also: `gauss_a`.

### Function: gradef (gradef, f, x_1, ..., x_n, g_1, ..., g_m, gradef, a, x, expr)

Defines the partial derivatives (i.e., the components of the gradient) of the
function *f* or variable *a*.


`gradef (f(x_1, ..., x_n), g_1, ..., g_m)`
defines `df/dx_i` as *g_i*, where *g_i* is an
expression; *g_i* may be a function call, but not the name of a function.
The number of partial derivatives *m* may be less than the number of
arguments *n*, in which case derivatives are defined with respect to
*x_1* through *x_m* only.


`gradef (a, x, expr)` defines the derivative of variable
*a* with respect to *x* as *expr*.  This also establishes the
dependence of *a* on *x* (via `depends (a, x)`).


The first argument `f(x_1, ..., x_n)` or *a* is
quoted, but the remaining arguments *g_1*, ..., *g_m* are evaluated.
`gradef` returns the function or variable for which the partial derivatives
are defined.


`gradef` can redefine the derivatives of Maxima’s built-in functions.
For example, `gradef (sin(x), sqrt (1 - sin(x)^2))` redefines the
derivative of `sin`.


`gradef` cannot define partial derivatives for a subscripted function.


`printprops ([f_1, ..., f_n], gradef)` displays the partial
derivatives of the functions *f_1*, ..., *f_n*, as defined by
`gradef`.


`printprops ([a_n, ..., a_n], atomgrad)` displays the partial
derivatives of the variables *a_n*, ..., *a_n*, as defined by
`gradef`.


`gradefs` is the list of the functions
for which partial derivatives have been defined by `gradef`.
`gradefs` does not include any variables
for which partial derivatives have been defined by `gradef`.



Gradients are needed when, for example, a function is not known
explicitly but its first derivatives are and it is desired to obtain
higher order derivatives.

### Variable: gradefs

Default value: `[]`


`gradefs` is the list of the functions
for which partial derivatives have been defined by `gradef`.
`gradefs` does not include any variables
for which partial derivatives have been defined by `gradef`.

### Function: ic1 (solution, xval, yval)

Solves initial value problems for first order differential equations.
Here *solution* is a general solution to the equation, as found by
`ode2`, *xval* gives an initial value for the independent
variable in the form `x = x0`, and *yval* gives the
initial value for the dependent variable in the form `y = y0`.


See `ode2` for an example of its usage.

See also: `ode2`.

### Function: ic2 (solution, xval, yval, dval)

Solves initial value problems for second-order differential equations.
Here *solution* is a general solution to the equation, as found by
`ode2`, *xval* gives the initial value for the independent
variable in the form `x = x0`, *yval* gives the
initial value of the dependent variable in the form `y = y0`, and *dval* gives the initial value for the first
derivative of the dependent variable with respect to independent
variable, in the form `'diff(y,x) = dy0`.


See `ode2` for an example of its usage.

See also: `ode2`.

### Function: ilt (expr, s, t)

Computes the inverse Laplace transform of *expr* with
respect to *s* and parameter *t*. *expr* must be a ratio of
polynomials whose denominator has only linear and quadratic factors;
there is an extension of `ilt`, called `pwilt` (Piece-Wise
Inverse Laplace Transform) that handles several other cases where
`ilt` fails.


By using the functions `laplace` and `ilt` together with the
`solve` or `linsolve` functions the user can solve a single
differential or convolution integral equation or a set of them.













```maxima
maxima

(%i1) 'integrate (sinh(a*x)*f(t-x), x, 0, t) + b*f(t) = t**2;
              t
             /
             |                                    2
(%o1)        |  f(t - x) sinh(a x) dx + b f(t) = t
             |
             /
              0


(%i2) laplace (%, t, s);
       a laplace(f(t), t, s)                           2
(%o2)  --------------------- + b laplace(f(t), t, s) = --
               2    2                                   3
              s  - a                                   s


(%i3) linsolve ([%], ['laplace(f(t), t, s)]);
                                        2      2
                                     2 s  - 2 a
(%o3)     [laplace(f(t), t, s) = --------------------]
                                    5         2     3
                                 b s  + (a - a  b) s


(%i4) ilt (rhs (first (%)), s, t);
Is a b (a b - 1) positive, negative or zero?
pos;

               sqrt(a b (a b - 1)) t
        2 cosh(---------------------)       2
                         b               a t
(%o4) - ----------------------------- + -------
              3  2      2               a b - 1
             a  b  - 2 a  b + a
                                                       2
                                             + ------------------
                                                3  2      2
                                               a  b  - 2 a  b + a

(%i5) pos;
```

See also: `pwilt`.

### Variable: intanalysis

Default value: `true`


When `true`, definite integration tries to find poles in the integrand in 
the interval of integration.  If there are, then the integral is evaluated
appropriately as a principal value integral.  If intanalysis is `false`, 
this check is not performed and integration is done assuming there are no poles.


See also `ldefint`.


Examples:


Maxima can solve the following integrals, when `intanalysis` is set to
`false`:











```maxima
maxima

(%i1) intanalysis:false;
(%o1)                         false


(%i2) integrate(1/(sqrt(x+1)+1),x,0,1);
                                              3/2
(%o2)      - 2 log(sqrt(2) + 1) + 2 log(2) + 2    - 2


(%i3) integrate(1/(sqrt(x)+1),x,0,1),intanalysis:false;
(%o3)                     2 - 2 log(2)


(%i4) integrate(cos(a)/sqrt((tan(a))^2+1),a,-%pi/2,%pi/2),intanalysis:false;
(%o4)               %i log(2) - %i log(2 %i)

(%i5) intanalysis:false$

(%i6) integrate(cos(a)/sqrt((tan(a))^2 +1),a,-%pi/2,%pi/2);
(%o6)               %i log(2) - %i log(2 %i)
```

See also: `ldefint`, `intanalysis`.

### Function: integrate (integrate, expr, x, integrate, expr, x, a, b)

Attempts to symbolically compute the integral of *expr* with respect to
*x*.  `integrate (expr, x)` is an indefinite integral,
while `integrate (expr, x, a, b)` is a definite
integral, with limits of integration *a* and *b*.  The limits should
not contain *x*, although `integrate` does not enforce this
restriction.  *a* need not be less than *b*.
If *b* is equal to *a*, `integrate` returns zero.


See `quad_qag` and related functions for numerical approximation of
definite integrals.  See `residue` for computation of residues
(complex integration).  See `antid` for an alternative means of computing
indefinite integrals.


The integral (an expression free of `integrate`) is returned if
`integrate` succeeds.  Otherwise the return value is
the noun form of the integral (the quoted operator `'integrate`)
or an expression containing one or more noun forms.
The noun form of `integrate` is displayed with an integral sign.


In some circumstances it is useful to construct a noun form by hand, by quoting
`integrate` with a single quote, e.g.,
`'integrate (expr, x)`.  For example, the integral may depend
on some parameters which are not yet computed.
The noun may be applied to its arguments by `ev (i, nouns)`
where *i* is the noun form of interest.



`integrate` handles definite integrals separately from indefinite, and
employs a range of heuristics to handle each case.  Special cases of definite
integrals include limits of integration equal to zero or infinity (`inf` or
`minf`), trigonometric functions with limits of integration equal to zero
and `%pi` or `2 %pi`, rational functions, integrals related to the
definitions of the `beta` and `psi` functions, and some logarithmic
and trigonometric integrals.  Processing rational functions may include
computation of residues.  If an applicable special case is not found, an attempt
will be made to compute the indefinite integral and evaluate it at the limits of
integration.  This may include taking a limit as a limit of integration goes to
infinity or negative infinity; see also `ldefint`.


Special cases of indefinite integrals include trigonometric functions,
exponential and logarithmic functions,
and rational functions.
`integrate` may also make use of a short table of elementary integrals.


`integrate` may carry out a change of variable
if the integrand has the form `f(g(x)) * diff(g(x), x)`.
`integrate` attempts to find a subexpression `g(x)` such that
the derivative of `g(x)` divides the integrand.
This search may make use of derivatives defined by the `gradef` function.
See also `changevar` and `antid`.


If none of the preceding heuristics find the indefinite integral, the Risch
algorithm is executed.  The flag `risch` may be set as an `evflag`,
in a call to `ev` or on the command line, e.g.,
`ev (integrate (expr, x), risch)` or
`integrate (expr, x), risch`.  If `risch` is present,
`integrate` calls the `risch` function without attempting heuristics
first.  See also `risch`.



`integrate` works only with functional relations represented explicitly
with the `f(x)` notation.  `integrate` does not respect implicit
dependencies established by the `depends` function.


`integrate` may need to know some property of a parameter in the integrand.
`integrate` will first consult the `assume` database,
and, if the variable of interest is not there,
`integrate` will ask the user.
Depending on the question,
suitable responses are `yes;` or `no;`,
or `pos;`, `zero;`, or `neg;`.


`integrate` is not, by default, declared to be linear.  See `declare`
and `linear`.


`integrate` attempts integration by parts only in a few special cases.


Examples:



- *
Elementary indefinite and definite integrals.




```maxima
maxima
(%i1) integrate (sin(x)^3, x);
                           3
                        cos (x)
(%o1)                   ------- - cos(x)
                           3

(%i2) integrate (x/ sqrt (b^2 - x^2), x);
                                 2    2
(%o2)                    - sqrt(b  - x )

(%i3) integrate (cos(x)^2 * exp(x), x, 0, %pi);
                               %pi
                           3 %e      3
(%o3)                      ------- - -
                              5      5

(%i4) integrate (x^2 * exp(-x^2), x, minf, inf);
                            sqrt(%pi)
(%o4)                       ---------
                                2
```
- *
Use of `assume` and interactive query.





```maxima
maxima
(%i1) assume (a > 1)$
(%i2) integrate (x**a/(x+1)**(5/2), x, 0, inf);
Is a an integer?
no;

Is 2 a - 1 positive, negative or zero?
neg;
                            3
(%o2)                  beta(- - a, a + 1)
                            2

Is 2 a - 1 positive, negative or zero?
no;
                            3
(%o2)                  beta(- - a, a + 1)
                            2
(%i3) neg;
```
- *
Change of variable.  There are two changes of variable in this example:
one using a derivative established by `gradef`, and one using the
derivation `diff(r(x))` of an unspecified function `r(x)`.




```maxima
maxima
(%i1) gradef (q(x), sin(x**2));
(%o1)                         q(x)

(%i2) diff (log (q (r (x))), x);
                      d               2
                     (-- (r(x))) sin(r (x))
                      dx
(%o2)                ----------------------
                            q(r(x))

(%i3) integrate (%, x);
(%o3)                     log(q(r(x)))
```
- *
Return value contains the `'integrate` noun form.  In this example, Maxima
can extract one factor of the denominator of a rational function, but cannot
factor the remainder or otherwise find its integral.  `grind` shows the
noun form `'integrate` in the result.  See also
`integrate_use_rootsof` for more on integrals of rational functions.




```maxima
maxima
(%i1) expand ((x-4) * (x^3+2*x+1));
                    4      3      2
(%o1)              x  - 4 x  + 2 x  - 7 x - 4

(%i2) integrate (1/%, x);
                              /  2
                              | x  + 4 x + 18
                              | ------------- dx
                              |  3
                 log(x - 4)   / x  + 2 x + 1
(%o2)            ---------- - ------------------
                     73               73

(%i3) grind (%);
log(x-4)/73-('integrate((x^2+4*x+18)/(x^3+2*x+1),x))/73$
(%o3)                         done
```
- *
Defining a function in terms of an integral.  The body of a function is not
evaluated when the function is defined.  Thus the body of `f_1` in this
example contains the noun form of `integrate`.  The quote-quote operator
`''` causes the integral to be evaluated, and the result becomes the
body of `f_2`.




```maxima
maxima
(%i1) f_1 (a) := integrate (x^3, x, 1, a);
                                     3
(%o1)           f_1(a) := integrate(x , x, 1, a)

(%i2) ev (f_1 (7), nouns);
(%o2)                          600

(%i3) /* Note parentheses around integrate(...) here */      f_2 (a) := ''(integrate (x^3, x, 1, a));
                                   4
                                  a    1
(%o3)                   f_2(a) := -- - -
                                  4    4

(%i4) f_2 (7);
(%o4)                          600
```

See also: `quad_qag`, `residue`, `antid`, `inf`, `minf`, `beta`, `psi`, `ldefint`, `changevar`, `risch`, `evflag`, `depends`, `assume`, `gradef`, `grind`, `integrate_use_rootsof`.

### Variable: integrate_use_rootsof

Default value: `false`


When `integrate_use_rootsof` is `true` and the denominator of
a rational function cannot be factored, `integrate` returns the integral
in a form which is a sum over the roots (not yet known) of the denominator.


For example, with `integrate_use_rootsof` set to `false`,
`integrate` returns an unsolved integral of a rational function in noun
form:







```maxima
maxima
(%i1) integrate_use_rootsof: false$

(%i2) integrate (1/(1+x+x^5), x);
      /  2
      | x  - 4 x + 5
      | ------------ dx                            2 x + 1
      |  3    2                2            5 atan(-------)
      / x  - x  + 1       log(x  + x + 1)          sqrt(3)
(%o2) ----------------- - --------------- + ---------------
              7                 14             7 sqrt(3)
```


Now we set the flag to be true and the unsolved part of the integral will be
expressed as a summation over the roots of the denominator of the rational
function:







```maxima
maxima
(%i1) integrate_use_rootsof: true$

(%i2) integrate (1/(1+x+x^5), x);
       ____
       \                                         2
(%o2) ( >                                   ((%r1  - 4 %r1 + 5)
       /
       ----
                         3      2
       %r1 in rootsof(%r1  - %r1  + 1, %r1)
                                          2
                     2               log(x  + x + 1)
 log(x - %r1))/(3 %r1  - 2 %r1))/7 - ---------------
                                           14
          2 x + 1
   5 atan(-------)
          sqrt(3)
 + ---------------
      7 sqrt(3)
```


Alternatively the user may compute the roots of the denominator separately,
and then express the integrand in terms of these roots, e.g.,
`1/((x - a)*(x - b)*(x - c))` or `1/((x^2 - (a+b)*x + a*b)*(x - c))`
if the denominator is a cubic polynomial.
Sometimes this will help Maxima obtain a more useful result.

See also: `integrate`.

### Variable: integration_constant

Default value: `%c`


When a constant of integration is introduced by indefinite integration of an
equation, the name of the constant is constructed by concatenating
`integration_constant` and `integration_constant_counter`.


`integration_constant` may be assigned any symbol.


Examples:








```maxima
maxima

(%i1) integrate (x^2 = 1, x);
                           3
                          x
(%o1)                     -- = x + %c1
                          3


(%i2) integration_constant : 'k;
(%o2)                           k


(%i3) integrate (x^2 = 1, x);
                            3
                           x
(%o3)                      -- = x + k2
                           3
```

### Variable: integration_constant_counter

Default value: 0


When a constant of integration is introduced by indefinite integration of an
equation, the name of the constant is constructed by concatenating
`integration_constant` and `integration_constant_counter`.


`integration_constant_counter` is incremented before constructing the next
integration constant.


Examples:










```maxima
maxima

(%i1) integrate (x^2 = 1, x);
                           3
                          x
(%o1)                     -- = x + %c1
                          3


(%i2) integrate (x^2 = 1, x);
                           3
                          x
(%o2)                     -- = x + %c2
                          3


(%i3) integrate (x^2 = 1, x);
                           3
                          x
(%o3)                     -- = x + %c3
                          3


(%i4) reset (integration_constant_counter);
(%o4)            [integration_constant_counter]


(%i5) integrate (x^2 = 1, x);
                           3
                          x
(%o5)                     -- = x + %c1
                          3
```

### Function: kummer_m (a, b, x)

Kummer’s M function, see [https://personal.math.ubc.ca/~cbm/aands/page_504.htmA&S eqn 13.1.2]() and [https://dlmf.nist.gov/13.2DLMF 13.2]().


The only use of this function is in solutions of ODEs returned by 
`odelin` and `contrib_ode`.  The definition and use of this 
function may change in future releases of Maxima.


See also `kummer_u`, `dkummer_m`, and `dkummer_005fu`.

See also: `odelin`, `contrib_ode`, `kummer_u`, `dkummer_m`, `dkummer_u`.

### Function: kummer_u (a, b, x)

Kummer’s U function, see [https://personal.math.ubc.ca/~cbm/aands/page_504.htmA&S eqn 13.1.3]() and [https://dlmf.nist.gov/13.2.6DLMF 13.2.6]().


See `kummer_005fm`.

See also: `kummer_m`.

### Function: laplace (expr, t, s)

Attempts to compute the Laplace transform of *expr* with respect to the 
variable *t* and transform parameter *s*.  The Laplace
transform of the function `f(t)` is the one-sided transform defined by

$$F(s) = \int_0^{\infty} f(t) e^{-st} dt$$


$$F(s) = \int_0^{\infty} f(t) e^{-st} dt$$




where $F(s)$ is the transform of $f(t)$, represented by *expr*.


`laplace` recognizes in *expr* the functions `delta`, `exp`,
`log`, `sin`, `cos`, `sinh`, `cosh`, and `erf`,
as well as `derivative`, `integrate`, `sum`, and `ilt`. If
`laplace` fails to find a transform the function `specint` is called.
`specint` can find the laplace transform for expressions with special
functions like the bessel functions `bessel_j`, `bessel_i`, ...
and can handle the `unit_step` function.  See also `specint`.


If `specint` cannot find a solution too, a noun `laplace` is returned.



*expr* may also be a linear, constant coefficient differential equation in
which case `atvalue` of the dependent variable is used.

The required atvalue may be supplied either before or after the transform is
computed.  Since the initial conditions must be specified at zero, if one has
boundary conditions imposed elsewhere he can impose these on the general
solution and eliminate the constants by solving the general solution
for them and substituting their values back.


`laplace` recognizes convolution integrals of the form

$$\int_0^t f(x) g(t-x) dx$$


$$\int_0^t f(x) g(t-x) dx$$




Other kinds of convolutions are not recognized.


Functional relations must be explicitly represented in *expr*;
implicit relations, established by `depends`, are not recognized.
That is, if $f$ depends on $x$ and $y$,
$f (x, y)$ must appear in *expr*.


See also `ilt`, the inverse Laplace transform.


Examples:
















```maxima
maxima

(%i1) laplace (exp (2*t + a) * sin(t) * t, t, s);
                            a
                          %e  (2 s - 4)
(%o1)             -----------------------------
                   4      3       2
                  s  - 8 s  + 26 s  - 40 s + 25


(%i2) laplace ('diff (f (x), x), x, s);
(%o2)             s laplace(f(x), x, s) - f(0)


(%i3) diff (diff (delta (t), t), t);
                          2
                         d
(%o3)                    --- (delta(t))
                           2
                         dt


(%i4) laplace (%, t, s);
                            |
               d            |         2
(%o4)        - -- (delta(t))|      + s  - delta(0) s
               dt           |
                            |t = 0

(%i5) assume(a>1)$
(%i6) declare(a, integer)$

(%i7) laplace(gamma_incomplete(a,t),t,s),gamma_expand:true;
                                       - a - 1
                  gamma(a)   gamma(a) s
(%o7)             -------- - -----------------
                     s            1     a
                                 (- + 1)
                                  s


(%i8) factor(laplace(gamma_incomplete(1/2,t),t,s));
                                       s + 1
               sqrt(%pi) (sqrt(s) sqrt(-----) - 1)
                                         s
(%o8)          -----------------------------------
                         3/2      s + 1
                        s    sqrt(-----)
                                    s

(%i9) assume(exp(%pi*s)>1, n > 0)$

(%i10) laplace(sum((-1)^n*unit_step(t-n*%pi)*sin(t),n,0,inf),t,s),
  simpsum;
                              %pi s
                            %e
(%o10)           ------------------------------
                    %pi s       2     %pi s
                 (%e      - 1) s  + %e      - 1
```

See also: `delta`, `exp`, `log`, `sin`, `cos`, `sinh`, `cosh`, `erf`, `integrate`, `sum`, `ilt`, `specint`, `bessel_j`, `bessel_i`, `unit_step`, `atvalue`, `depends`.

### Function: ldefint (expr, x, a, b)

Attempts to compute the definite integral of *expr* by using `limit`
to evaluate the indefinite integral of *expr* with respect to *x*
at the upper limit *b* and at the lower limit *a*.
If it fails to compute the definite integral,
`ldefint` returns an expression containing limits as noun forms.


`ldefint` is not called from `integrate`, so executing
`ldefint (expr, x, a, b)` may yield a different
result than `integrate (expr, x, a, b)`.
`ldefint` always uses the same method to evaluate the definite integral,
while `integrate` may employ various heuristics and may recognize some
special cases.

See also: `limit`, `integrate`.

### Variable: method

The variable `method` is set by `ode2` to the successful solution
method.

See also: `ode2`.

### Function: ode2 (eqn, dvar, ivar)

The function `ode2` solves an ordinary differential equation (ODE)
of first or second order. It takes three arguments: an ODE given by
*eqn*, the dependent variable *dvar*, and the independent
variable *ivar*. When successful, it returns either an explicit or
implicit solution for the dependent variable. `%c` is used to
represent the integration constant in the case of first-order equations,
and `%k1` and `%k2` the constants for second-order
equations. The dependence of the dependent variable on the independent
variable does not have to be written explicitly, as in the case of
`desolve`, but the independent variable must always be given as the
third argument.


If `ode2` cannot obtain a solution for whatever reason, it returns
`false`, after perhaps printing out an error message. The methods
implemented for first order equations in the order in which they are
tested are: linear, separable, exact - perhaps requiring an integrating
factor, homogeneous, Bernoulli’s equation, and a generalized homogeneous
method. The types of second-order equations which can be solved are:
constant coefficients, exact, linear homogeneous with non-constant
coefficients which can be transformed to constant coefficients, the
Euler or equi-dimensional equation, equations solvable by the method of
variation of parameters, and equations which are free of either the
independent or of the dependent variable so that they can be reduced to
two first order linear equations to be solved sequentially.


In the course of solving ODE’s, several variables are set purely for
informational purposes: `method` denotes the method of solution
used (e.g., `linear`), `intfactor` denotes any integrating
factor used, `odeindex` denotes the index for Bernoulli’s method or
for the generalized homogeneous method, and `yp` denotes the
particular solution for the variation of parameters technique.


In order to solve initial value problems (IVP) functions `ic1` and
`ic2` are available for first and second order equations, and to
solve second-order boundary value problems (BVP) the function `bc2`
can be used.


See also `desolve`, `drawdf` and `rk`.


Example:












```maxima
maxima

(%i1) x^2*'diff(y,x) + 3*y*x = sin(x)/x;
                      2 dy           sin(x)
(%o1)                x  -- + 3 x y = ------
                        dx             x


(%i2) soln1: ode2(%,y,x);
                             %c - cos(x)
(%o2)                    y = -----------
                                  3
                                 x


(%i3) ic1 (soln1,x=%pi,y=0);
                              cos(x) + 1
(%o3)                   y = - ----------
                                   3
                                  x


(%i4) 'diff(y,x,2) + y*'diff(y,x)^3 = 0;
                         2
                        d y      dy 3
(%o4)                   --- + y (--)  = 0
                          2      dx
                        dx


(%i5) soln2: ode2(%,y,x);
                      3
                     y  + 6 %k1 y
(%o5)                ------------ = x + %k2
                          6


(%i6) ratsimp (ic2(soln2,x=0,y=0,'diff(y,x)=2));
                           3
                          y  + 3 y
(%o6)                     -------- = x
                             6


(%i7) bc2 (soln2,x=0,y=1,x=1,y=3);
                         3
                        y  - 10 y       3
(%o7)                   --------- = x - -
                            6           2
```

See also: `%c`, `%k1`, `%k2`, `desolve`, `method`, `yp`, `ic1`, `ic2`, `bc2`, `drawdf`, `rk`.

### Function: ode_check (eqn, soln)

Returns the value of ODE *eqn* after substituting a
possible solution *soln*.  The value is equivalent to 
zero if *soln* is a solution of *eqn*.










```maxima
(%i1) load("contrib_ode")$

(%i2) eqn:'diff(y,x,2)+(a*x+b)*y;
                         2
                        d y
(%o2)                   --- + (b + a x) y
                          2
                        dx

(%i3) ans:[y = bessel_y(1/3,2*(a*x+b)^(3/2)/(3*a))*%k2*sqrt(a*x+b)
         +bessel_j(1/3,2*(a*x+b)^(3/2)/(3*a))*%k1*sqrt(a*x+b)];
                                  3/2
                    1  2 (b + a x)
(%o3) [y = bessel_y(-, --------------) %k2 sqrt(a x + b)
                    3       3 a
                                          3/2
                            1  2 (b + a x)
                 + bessel_j(-, --------------) %k1 sqrt(a x + b)]
                            3       3 a

(%i4) ode_check(eqn,ans[1]);
(%o4)                           0
```

### Function: odelin (eqn, y, x)

`odelin` solves linear homogeneous ODEs of first and 
second order with 
independent variable *x* and dependent variable *y*.  
It returns a fundamental solution set of the ODE.


For second order ODEs, `odelin` uses a method, due to Bronstein
and Lafaille, that searches for solutions in terms of given 
special functions. 







```maxima
(%i1) load("contrib_ode")$

(%i2) odelin(x*(x+1)*'diff(y,x,2)+(x+5)*'diff(y,x,1)+(-4)*y,y,x);
       gauss_a(- 6, - 2, - 3, - x)  gauss_b(- 6, - 2, - 3, - x)
(%o2) {---------------------------, ---------------------------}
                    4                            4
                   x                            x
```

### Function: plotdf (plotdf, dydx, options, ..., plotdf, dvdu, u, v, options, ..., plotdf, dxdt, c, dydt, options, ..., plotdf, dudt, c, dvdt, u, c, v, options, ...)

The function `plotdf` creates a two-dimensional plot of the direction
field (also called slope field) for a first-order Ordinary Differential
Equation (ODE) or a system of two autonomous first-order ODE’s.


Plotdf requires Xmaxima, even if its run from a Maxima session in
a console, since the plot will be created by the Tk scripts in Xmaxima.
If Xmaxima is not installed plotdf will not work.


*dydx*, *dxdt* and *dydt* are expressions that depend on
*x* and *y*. *dvdu*, *dudt* and *dvdt* are
expressions that depend on *u* and *v*. In addition to those two
variables, the expressions can also depend on a set of parameters, with
numerical values given with the `parameters` option (the option
syntax is given below), or with a range of allowed values specified by a
*sliders* option.


Several other options can be given within the command, or selected in
the menu. Integral curves can be obtained by clicking on the plot, or
with the option `trajectory_at`. The direction of the integration
can be controlled with the `direction` option, which can have
values of *forward*, *backward* or *both*. The number of
integration steps is given by `nsteps`; at each integration
step the time increment will be adjusted automatically to produce
displacements much smaller than the size of the plot window. The
numerical method used is 4th order Runge-Kutta with variable time steps.


**Plot window menu:**


The menu bar of the plot window has the following five buttons:


Close: can be used to close the plot window.


Config: opens the configuration menu with several
fields that show the ODE(s) in use and various other settings. If a pair
of coordinates are entered in the field *Trajectory at* and the
enter key is pressed, a new integral curve will be shown, in
addition to the ones already shown.


Save: used to save a copy of the plot, in Postscript format, in the file
specified in a field of the window that appears when that button is clicked.


Replot: replots the direction field with the new settings defined in the
configuration menu and replots only the last integral curve that was
previously plotted. If you just resized the plot window, the size and
width of the arrows and curves will be adapted to the new size if you
click on Replot.


Time plot: creates two new window showing the plots of the two variables
in terms of time, for the last integral curve that was plotted.


**Plot options:**


Options can also be given within the `plotdf` itself, each one being
a list of two or more elements. The first element in each option is the name
of the option, and the remainder is the value or values assigned to the
option.


The options which are recognized by `plotdf` are the following:



- *
*nsteps* defines the number of steps that will be used for the
independent variable, to compute an integral curve. The default value is
100.
- *
*direction* defines the direction of the independent
variable that will be followed to compute an integral curve. Possible
values are `forward`, to make the independent variable increase
`nsteps` times, with increments `tstep`, `backward`, to
make the independent variable decrease, or `both` that will lead to
an integral curve that extends `nsteps` forward, and `nsteps`
backward. The keywords `right` and `left` can be used as
synonyms for `forward` and `backward`.
The default value is `both`.
- *
*tinitial* defines the initial value of variable *t* used
to compute integral curves. Since the differential equations are
autonomous, that setting will only appear in the plot of the curves as
functions of *t*. 
The default value is 0.
- *
*versus_t* is used to create a second plot window, with a
plot of an integral curve, as two functions *x*, *y*, of the
independent variable *t*. If `versus_t` is given any value
different from 0, the second plot window will be displayed. The second
plot window includes another menu, similar to the menu of the main plot
window.
The default value is 0.
- *
*trajectory_at* defines the coordinates *xinitial* and
*yinitial* for the starting point of an integral curve.
The option is empty by default.
- *
*parameters* defines a list of parameters, and their
numerical values, used in the definition of the differential
equations. The name and values of the parameters must be given in a
string with a comma-separated sequence of pairs `name=value`.
- *
*sliders* defines a list of parameters that will be changed
interactively using slider buttons, and the range of variation of those
parameters. The names and ranges of the parameters must be given in a
string with a comma-separated sequence of elements `name=min:max`
- *
*tstep* sets the value of the time intervals used in the integration
algorithm. It must be a floating point number; you might have to adjust
its value to get good results for the integral curves. If not given, a
default value will be chosen according to the region to be plotted.
- *
*xfun* defines a string with semi-colon-separated sequence
of functions of *x* to be displayed, on top of the direction field.
Those functions will be parsed by Tcl and not by Maxima.
- *
*x* should be followed by two numbers, which will set up the minimum
and maximum values shown on the horizontal axis. If the variable on the
horizontal axis is not *x*, then this option should have the name of
the variable on the horizontal axis.
The default horizontal range is from -10 to 10.
- *
*y* should be followed by two numbers, which will set up the minimum
and maximum values shown on the vertical axis. If the variable on the
vertical axis is not *y*, then this option should have the name of
the variable on the vertical axis.
The default vertical range is from -10 to 10.
- *
*xaxislabel* will be used to identify the horizontal axis. Its default value is the name of the first state variable.
- *
*yaxislabel* will be used to identify the vertical axis. Its default value is the name of the second state variable.
- *
*number_of_arrows* should be set to a square number and defines the approximate
density of the arrows being drawn. The default value is 225.


**Examples:**



- *
To show the direction field of the differential equation $y' = e^{-x} + y$ and the solution that goes through $(2, -0.1)$:


```maxima
maxima
(%i1) plotdf(exp(-x)+y,[trajectory_at,2,-0.1])$
```

figures/plotdf18cm
- *
To obtain the direction field for the equation
$dy/dx = x - y^2$

and the solution with initial condition $y(-1) = 3$, we can use the command:



```maxima
maxima
(%i1) plotdf(x-y^2,[xfun,"sqrt(x);-sqrt(x)"],
         [trajectory_at,-1,3], [direction,forward],
         [y,-5,5], [x,-4,16])$
```

The graph also shows the function
$y = \sqrt{x}.$

figures/plotdf28cm
- *
The following example shows the direction field of a harmonic oscillator,
defined by the two equations $dz/dt = v$ and
$dv/dt = -kz/m,$

and the integral curve through $(z,v) = (6,0)$, with a slider that
will allow you to change the value of $m$ interactively ($k$ is
fixed at 2):



```maxima
maxima
(%i1) plotdf([v,-k*z/m], [z,v], [parameters,"m=2,k=2"],
           [sliders,"m=1:5"], [trajectory_at,6,0])$
```

figures/plotdf38cm
- *
To plot the direction field of the Duffing equation,
$m x''+c x' + kx + bx^3 = 0,$
we introduce the variable $y=x'$ and use:



```maxima
maxima
(%i1) plotdf([y,-(k*x + c*y + b*x^3)/m],
             [parameters,"k=-1,m=1.0,c=0,b=1"],
             [sliders,"k=-2:2,m=-1:1"],[tstep,0.1])$
```

figures/plotdf48cm
- *
The direction field for a damped pendulum, including the
solution for the given initial conditions, with a slider that
can be used to change the value of the mass $m$, and with a plot of
the two state variables as a function of time:





```maxima
maxima
(%i1) plotdf([w,-g*sin(a)/l - b*w/m/l], [a,w],
        [parameters,"g=9.8,l=0.5,m=0.3,b=0.05"],
        [trajectory_at,1.05,-9],[tstep,0.01],
        [a,-10,2], [w,-14,14], [direction,forward],
        [nsteps,300], [sliders,"m=0.1:1"], [versus_t,1])$
```

figures/plotdf58cmfigures/plotdf68cm

### Function: ploteq (exp, ...options...)

Plots equipotential curves for *exp*, which should be an expression
depending on two variables. The curves are obtained by integrating the
differential equation that define the orthogonal trajectories to the solutions
of the autonomous system obtained from the gradient of the expression given.
The plot can also show the integral curves for that gradient system (option
fieldlines).


This program also requires Xmaxima, even if its run from a Maxima session in
a console, since the plot will be created by the Tk scripts in Xmaxima.
By default, the plot region will be empty until the user clicks in a point
(or gives its coordinate with in the set-up menu or via the trajectory_at option).


Most options accepted by plotdf can also be used for ploteq and the plot
interface is the same that was described in plotdf.


Example:







```maxima
maxima
(%i1) V: 900/((x+1)^2+y^2)^(1/2)-900/((x-1)^2+y^2)^(1/2)$
(%i2) ploteq(V,[x,-2,2],[y,-2,2],[fieldlines,"blue"])$
```


Clicking on a point will plot the equipotential curve that passes by that point
(in red) and the orthogonal trajectory (in blue).

### Function: potential (givengradient)

The calculation makes use of the global variable `potentialzeroloc[0]`
which must be `nonlist` or of the form



```maxima
[indeterminatej=expressionj, indeterminatek=expressionk, ...]
```


the former being equivalent to the nonlist expression for all right-hand
sides in the latter.  The indicated right-hand sides are used as the
lower limit of integration.  The success of the integrations may
depend upon their values and order.  `potentialzeroloc` is initially set
to 0.

### Variable: prefer_d

Default value: `false`


When `prefer_d` is `true`, `specint` will prefer to
express solutions using `parabolic_cylinder_d` rather than
hypergeometric functions.


In the example below, the solution contains `parabolic_cylinder_d`
when `prefer_d` is `true`. 








```maxima
maxima

(%i1) assume(s>0);
(%o1)                        [s > 0]


(%i2) factor(ex:specint(%e^-(t^2/8)*exp(-s*t),t));
                        2
                     2 s
(%o2)    - sqrt(2) %e     sqrt(%pi) (erf(sqrt(2) s) - 1)


(%i3) specint(ex,t),prefer_d=true;
                             2
                          2 s
(%o3) specint(- sqrt(2) %e     sqrt(%pi) erf(sqrt(2) s), t)
                                                  2
                                               2 s
                           + specint(sqrt(2) %e     sqrt(%pi), t)
```

See also: `specint`, `parabolic_cylinder_d`.

### Function: pwilt (expr, s, t)

Computes the inverse Laplace transform of *expr* with
respect to *s* and parameter *t*. Unlike `ilt`,
`pwilt` is able to return piece-wise and periodic functions
and can also handle some cases with polynomials of degree greater than 3
in the denominator.


Two examples where `ilt` fails:






```maxima
(%i1) pwilt (exp(-s)*s/(s^3-2*s-s+2), s, t);
                        t - 1               - 2 (t - 1)
                      %e      (t - 1)   2 %e
(%o1)   hstep(t - 1) (--------------- - ---------------)
                             3                 9


(%i2) pwilt ((s^2+2)/(s^2-1), s, t);
                                  t       - t
                              3 %e    3 %e
(%o2)              delta(t) + ----- - -------
                                2        2
```

See also: `ilt`.

### Function: quad_control (parameter, value)

Control error handling for quadpack.  The parameter should be one of
the following symbols:



**current_error** — The current error number
**control** — Controls if messages are printed or not.  If it is set to zero or
less, messages are suppressed.
**max_message** — The maximum number of times any message is to be printed.


If *value* is not given, then the current value of the
*parameter* is returned.  If *value* is given, the value of
*parameter* is set to the given value.

### Function: quad_qag (quad_qag, f(x), x, a, b, key, epsrel, epsabs, limit, quad_qag, f, x, a, b, key, epsrel, epsabs, limit)

Integration of a general function over a finite interval.  `quad_qag`
implements a simple globally adaptive integrator using the strategy of Aind
(Piessens, 1973).  The caller may choose among 6 pairs of Gauss-Kronrod
quadrature formulae for the rule evaluation component.  The high-degree rules
are suitable for strongly oscillating integrands.


`quad_qag` computes the integral



$$\int_a^b f(x)\, dx$$


$$\int_a^b f(x)\, dx$$



The function to be integrated is $f(x)$, with dependent
variable $x$, and the function is to be integrated between the
limits $a$ and $b$.  *key* is the integrator to be used
and should be an integer between 1 and 6, inclusive.  The value of
*key* selects the order of the Gauss-Kronrod integration rule.
High-order rules are suitable for strongly oscillating integrands.


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


The numerical integration is done adaptively by subdividing the
integration region into sub-intervals until the desired accuracy is
achieved.


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsrel** — Desired relative error of approximation.  Default is 1d-8.
**epsabs** — Desired absolute error of approximation.  Default is 0.
**limit** — Size of internal work array.  *limit* is the
maximum number of subintervals to use.  Default is 200.


`quad_qag` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — if no problems were encountered;
**1** — if too many sub-intervals were done;
**2** — if excessive roundoff error is detected;
**3** — if extremely bad integrand behavior occurs;
**6** — if the input is invalid.




Examples:







```maxima
maxima

(%i1) quad_qag (x^(1/2)*log(1/x), x, 0, 1, 3, 'epsrel=5d-8);
(%o1)  [0.44444444445742953, 8.737223570614865e-9, 899, 0]


(%i2) integrate (x^(1/2)*log(1/x), x, 0, 1);
                                4
(%o2)                           -
                                9
```

### Function: quad_qagi (quad_qagi, f(x), x, a, b, epsrel, epsabs, limit, quad_qagi, f, x, a, b, epsrel, epsabs, limit)

Integration of a general function over an infinite or semi-infinite interval.
The interval is mapped onto a finite interval and
then the same strategy as in `quad_qags` is applied.


`quad_qagi` evaluates one of the following integrals



$$\int_a^\infty f(x) \, dx$$


$$\int_a^\infty f(x) \, dx$$




$$\int_\infty^a f(x) \, dx$$


$$\int_\infty^a f(x) \, dx$$




$$\int_{-\infty}^\infty f(x) \, dx$$


$$\int_{-\infty}^\infty f(x) \, dx$$



using the Quadpack QAGI routine.  The function to be integrated is
$f(x)$, with dependent variable $x$, and the function is to
be integrated over an infinite range.


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


One of the limits of integration must be infinity.  If not, then
`quad_qagi` will just return the noun form.


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsrel** — Desired relative error of approximation.  Default is 1d-8.
**epsabs** — Desired absolute error of approximation.  Default is 0.
**limit** — Size of internal work array.  *limit* is the
maximum number of subintervals to use.  Default is 200.


`quad_qagi` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — no problems were encountered;
**1** — too many sub-intervals were done;
**2** — excessive roundoff error is detected;
**3** — extremely bad integrand behavior occurs;
**4** — failed to converge
**5** — integral is probably divergent or slowly convergent
**6** — if the input is invalid.




Examples:







```maxima
maxima

(%i1) quad_qagi (x^2*exp(-4*x), x, 0, inf, 'epsrel=1d-8);
(%o1)       [0.03125, 2.9591610299500215e-11, 105, 0]


(%i2) integrate (x^2*exp(-4*x), x, 0, inf);
                               1
(%o2)                          --
                               32
```

### Function: quad_qagp (quad_qagp, f(x), x, a, b, points, epsrel, epsabs, limit, quad_qagp, f, x, a, b, points, epsrel, epsabs, limit)

Integration of a general function over a finite interval.
`quad_qagp` implements globally adaptive interval subdivision with
extrapolation (de Doncker, 1978) by the Epsilon algorithm (Wynn, 1956).


`quad_qagp` computes the integral



$$\int_a^b f(x) \, dx$$


$$\int_a^b f(x) \, dx$$



The function to be integrated is $f(x)$, with
dependent variable $x$, and the function is to be integrated
between the limits $a$ and $b$.


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


To help the integrator, the user must supply a list of points where
the integrand is singular or discontinuous.  The list is provided by
*points*.  It may be an empty list.  The elements of the list must
be between *a* and *b*, exclusive.  An error is thrown if
there are elements out of range.  The list points may be in any order. 


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsrel** — Desired relative error of approximation.  Default is 1d-8.
**epsabs** — Desired absolute error of approximation.  Default is 0.
**limit** — Size of internal work array.  *limit* is the
maximum number of subintervals to use.  Default is 200.


`quad_qagp` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — no problems were encountered;
**1** — too many sub-intervals were done;
**2** — excessive roundoff error is detected;
**3** — extremely bad integrand behavior occurs;
**4** — failed to converge
**5** — integral is probably divergent or slowly convergent
**6** — if the input is invalid.




Examples:







```maxima
maxima

(%i1) quad_qagp(x^3*log(abs((x^2-1)*(x^2-2))),x,0,3,[1,sqrt(2)]);
(%o1) [52.740748383471434, 2.6247632689546663e-7, 1029, 0]


(%i2) quad_qags(x^3*log(abs((x^2-1)*(x^2-2))), x, 0, 3);
(%o2)  [52.74074847951494, 4.088443219529836e-7, 1869, 0]
```


The integrand has singularities at `1` and `sqrt(2)` so we supply
these points to `quad_qagp`.  We also note that `quad_qagp` is
more accurate and more efficient that `quad_005fqags`.

See also: `quad_qags`.

### Function: quad_qags (quad_qags, f(x), x, a, b, epsrel, epsabs, limit, quad_qags, f, x, a, b, epsrel, epsabs, limit)

Integration of a general function over a finite interval.
`quad_qags` implements globally adaptive interval subdivision with
extrapolation (de Doncker, 1978) by the Epsilon algorithm (Wynn, 1956).


`quad_qags` computes the integral



$$\int_a^b f(x)\, dx$$


$$\int_a^b f(x)\, dx$$



The function to be integrated is $f(x)$, with
dependent variable $x$, and the function is to be integrated
between the limits $a$ and $b$.


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsrel** — Desired relative error of approximation.  Default is 1d-8.
**epsabs** — Desired absolute error of approximation.  Default is 0.
**limit** — Size of internal work array.  *limit* is the
maximum number of subintervals to use.  Default is 200.


`quad_qags` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — no problems were encountered;
**1** — too many sub-intervals were done;
**2** — excessive roundoff error is detected;
**3** — extremely bad integrand behavior occurs;
**4** — failed to converge
**5** — integral is probably divergent or slowly convergent
**6** — if the input is invalid.




Examples:






```maxima
maxima

(%i1) quad_qags (x^(1/2)*log(1/x), x, 0, 1, 'epsrel=1d-10);
(%o1) [0.44444444444444475, 1.1102230246251565e-15, 315, 0]
```


Note that `quad_qags` is more accurate and efficient than `quad_qag` for this integrand.

### Function: quad_qawc (quad_qawc, f(x), x, c, a, b, epsrel, epsabs, limit, quad_qawc, f, x, c, a, b, epsrel, epsabs, limit)

Computes the Cauchy principal value of $f(x)/(x - c)$ over a finite
interval.  The strategy is globally adaptive, and modified
Clenshaw-Curtis integration is used on the subranges
which contain the point $x = c$.


`quad_qawc` computes the Cauchy principal value of



$$\int_{a}^{b}{{{f\left(x\right)}\over{x-c}}\>dx}$$


$$\int_{a}^{b}{{{f\left(x\right)}\over{x-c}}\>dx}$$



using the Quadpack QAWC routine.  The function to be integrated is
$f(x)/(x-c)$, with dependent variable $x$, and the
function is to be integrated over the interval $a$ to $b$.


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsrel** — Desired relative error of approximation.  Default is 1d-8.
**epsabs** — Desired absolute error of approximation.  Default is 0.
**limit** — Size of internal work array.  *limit* is the
maximum number of subintervals to use.  Default is 200.


`quad_qawc` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — no problems were encountered;
**1** — too many sub-intervals were done;
**2** — excessive roundoff error is detected;
**3** — extremely bad integrand behavior occurs;
**6** — if the input is invalid.


Examples:








```maxima
maxima

(%i1) quad_qawc (2^(-5)*((x-1)^2+4^(-5))^(-1), x, 2, 0, 5, 'epsrel=1d-7);
(%o1) [- 3.130120337415925, 1.3068301402495579e-8, 495, 0]


(%i2) integrate (2^(-alpha)*(((x-1)^2 + 4^(-alpha))*(x-2))^(-1), x, 0, 5);
Principal Value
          2 alpha - 1      2 alpha + 4
         2            log(2            + 1)
(%o2) (- ----------------------------------
                     2 alpha
                    2        + 1
    3 alpha       alpha + 2     2 alpha - 1      2 alpha
   2        atan(2         )   2            log(2        + 1)
 - ------------------------- + ------------------------------
          2 alpha                        2 alpha
         2        + 1                   2        + 1
    3 alpha + 1       alpha     3 alpha       alpha
   2            atan(2     )   2        atan(2     )
 - ------------------------- + ---------------------
          2 alpha                   2 alpha
         2        + 1              2        + 1
    2 alpha           2 alpha
   2        log(3)   2        log(2)   alpha
 + --------------- - ---------------)/2
     2 alpha           2 alpha
    2        + 1      2        + 1


(%i3) ev (%, alpha=5, numer);
(%o3)                 - 3.1301203374159177
```

### Function: quad_qawf (quad_qawf, f(x), x, a, omega, trig, epsabs, limit, maxp1, limlst, quad_qawf, f, x, a, omega, trig, epsabs, limit, maxp1, limlst)

Calculates a Fourier cosine or Fourier sine transform on a semi-infinite
interval using the Quadpack QAWF function.  The same approach as in
`quad_qawo` is applied on successive finite intervals, and convergence
acceleration by means of the Epsilon algorithm (Wynn, 1956) is applied to the
series of the integral contributions.


`quad_qawf` computes the integral



$$\int_a^\infty f(x) \, w(x) \, dx$$


$$\int_a^\infty f(x) \, w(x) \, dx$$



The weight function $w$ is selected by *trig*:



**cos** — $w(x) = \cos\omega x$
**sin** — $w(x) = \sin\omega x$


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsabs** — Desired absolute error of approximation.  Default is 1d-10.
**limit** — Size of internal work array.  (*limit* - *limlst*)/2 is the
maximum number of subintervals to use.  Default is 200.
**maxp1** — Maximum number of Chebyshev moments.  Must be greater than 0.  Default
is 100.
**limlst** — Upper bound on the number of cycles.  Must be greater than or equal to
3.  Default is 10.


`quad_qawf` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — no problems were encountered;
**1** — too many sub-intervals were done;
**2** — excessive roundoff error is detected;
**3** — extremely bad integrand behavior occurs;
**6** — if the input is invalid.


Examples:








```maxima
maxima

(%i1) quad_qawf (exp(-x^2), x, 0, 1, 'cos, 'epsabs=1d-9);
(%o1)  [0.6901942235215714, 2.848463002545743e-11, 215, 0]


(%i2) integrate (exp(-x^2)*cos(x), x, 0, inf);
                          - 1/4
                        %e      sqrt(%pi)
(%o2)                   -----------------
                                2


(%i3) ev (%, numer);
(%o3)                  0.6901942235215714
```

### Function: quad_qawo (quad_qawo, f(x), x, a, b, omega, trig, epsrel, epsabs, limit, maxp1, limlst, quad_qawo, f, x, a, b, omega, trig, epsrel, epsabs, limit, maxp1, limlst)

Integration of 
$\cos(\omega x) f(x)$
or 
$\sin(\omega x)$
over a finite interval,
where 
$\omega$
is a constant.
The rule evaluation component is based on the modified
Clenshaw-Curtis technique.  `quad_qawo` applies adaptive subdivision with
extrapolation, similar to `quad_qags`.


`quad_qawo` computes the integral using the Quadpack QAWO
routine:



$$\int_a^b f(x) \, w(x) \, dx$$


$$\int_a^b f(x) \, w(x) \, dx$$



The weight function $w$ is selected by *trig*:



**cos** — $w(x) = \cos\omega x$
**sin** — $w(x) = \sin\omega x$


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsrel** — Desired relative error of approximation.  Default is 1d-8.
**epsabs** — Desired absolute error of approximation.  Default is 0.
**limit** — Size of internal work array.  *limit*/2 is the
maximum number of subintervals to use.  Default is 200.
**maxp1** — Maximum number of Chebyshev moments.  Must be greater than 0.  Default
is 100.
**limlst** — Upper bound on the number of cycles.  Must be greater than or equal to
3.  Default is 10.


`quad_qawo` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — no problems were encountered;
**1** — too many sub-intervals were done;
**2** — excessive roundoff error is detected;
**3** — extremely bad integrand behavior occurs;
**6** — if the input is invalid.


Examples:








```maxima
maxima

(%i1) quad_qawo (x^(-1/2)*exp(-2^(-2)*x), x, 1d-8, 20*2^2, 1, cos);
(%o1) [1.3760433898776214, 4.7271075942489915e-11, 765, 0]


(%i2) rectform (integrate (x^(-1/2)*exp(-2^(-alpha)*x) * cos(x), x, 0, inf));
         alpha + 1
         --------- - 1
             2                    2 alpha
        2              sqrt(sqrt(2        + 1) %pi + %pi)
(%o2)   -------------------------------------------------
                             2 alpha
                       sqrt(2        + 1)


(%i3) ev (%, alpha=2, numer);
(%o3)                   1.376043390090716

(%i4) ev (%, alpha=2, numer);
```

### Function: quad_qaws (quad_qaws, f(x), x, a, b, alpha, beta, wfun, epsrel, epsabs, limit, quad_qaws, f, x, a, b, alpha, beta, wfun, epsrel, epsabs, limit)

Integration of $w(x) f(x)$ over a finite interval, where $w(x)$ is a
certain algebraic or logarithmic function.  A globally adaptive subdivision
strategy is applied, with modified Clenshaw-Curtis integration on the
subintervals which contain the endpoints of the interval of integration.


`quad_qaws` computes the integral using the Quadpack QAWS routine:



$$\int_a^b f(x) \, w(x) \, dx$$


$$\int_a^b f(x) \, w(x) \, dx$$



The weight function $w$ is selected by *wfun*:



**1** — $w(x) = (x - a)^\alpha (b - x)^\beta$
**2** — $w(x) = (x - a)^\alpha (b - x)^\beta \log(x - a)$
**3** — $w(x) = (x - a)^\alpha (b - x)^\beta \log(b - x)$
**4** — $w(x) = (x - a)^\alpha (b - x)^\beta \log(x - a) \log(b - x)$


The integrand may be specified as the name of a Maxima or Lisp function or
operator, a Maxima lambda expression, or a general Maxima expression.


The keyword arguments are optional and may be specified in any order.
They all take the form `key=val`.  The keyword arguments are:



**epsrel** — Desired relative error of approximation.  Default is 1d-8.
**epsabs** — Desired absolute error of approximation.  Default is 0.
**limit** — Size of internal work array.  *limit*is the
maximum number of subintervals to use.  Default is 200.


`quad_qaws` returns a list of four elements:



- *
an approximation to the integral,
- *
the estimated absolute error of the approximation,
- *
the number integrand evaluations,
- *
an error code.


The error code (fourth element of the return value) can have the values:



**0** — no problems were encountered;
**1** — too many sub-intervals were done;
**2** — excessive roundoff error is detected;
**3** — extremely bad integrand behavior occurs;
**6** — if the input is invalid.


Examples:








```maxima
maxima

(%i1) quad_qaws (1/(x+1+2^(-4)), x, -1, 1, -0.5, -0.5, 1, 'epsabs=1d-9);
(%o1)  [8.750097361672843, 1.2761903591126173e-8, 130, 0]


(%i2) integrate ((1-x*x)^(-1/2)/(x+1+2^(-alpha)), x, -1, 1);
                            alpha
                           2      %pi
(%o2)                 --------------------
                            alpha + 1
                      sqrt(2          + 1)


(%i3) ev (%, alpha=4, numer);
(%o3)                   8.75009736167283
```

### Function: residue (expr, z, z_0)

Computes the residue in the complex plane of the expression *expr* when the
variable *z* assumes the value *z_0*.  The residue is the coefficient of
`(z - z_0)^(-1)` in the Laurent series for *expr*.







```maxima
maxima

(%i1) residue (s/(s**2+a**2), s, a*%i);
                                1
(%o1)                           -
                                2


(%i2) residue (sin(a*x)/x**4, x, 0);
                                 3
                                a
(%o2)                         - --
                                6
```

### Function: risch (expr, x)

Integrates *expr* with respect to *x* using the
transcendental case of the Risch algorithm.  (The algebraic case of
the Risch algorithm has not been implemented.)  This currently
handles the cases of nested exponentials and logarithms which the main
part of `integrate` can’t do.  `integrate` will automatically apply
`risch` if given these cases.


`erfflag`, if `false`, prevents `risch` from introducing the
`erf` function in the answer if there were none in the integrand to begin
with.







```maxima
maxima

(%i1) risch (x^2*erf(x), x);
                             2
             3            - x              2
        %pi x  erf(x) + %e     (sqrt(%pi) x  + sqrt(%pi))
(%o1)   -------------------------------------------------
                              3 %pi


(%i2) diff(%, x), ratsimp;
                             2
(%o2)                       x  erf(x)
```

See also: `integrate`.

### Function: rk (rk, ODE, var, initial, domain, rk, ODE1, ..., ODEm, v1, ..., vm, init1, ..., initm, domain)

The first form solves numerically one first-order ordinary differential
equation, and the second form solves a system of m of those equations,
using the 4th order Runge-Kutta method. *var* represents the dependent
variable. *ODE* must be an expression that depends only on the independent
and dependent variables and defines the derivative of the dependent
variable with respect to the independent variable.


The independent variable is specified with `domain`, which must be a
list of four elements as, for instance:


```maxima
[t, 0, 10, 0.1]
```

the first element of the list identifies the independent variable, the
second and third elements are the initial and final values for that
variable, and the last element sets the increments that should be used
within that interval.


If *m* equations are going to be solved, there should be *m*
dependent variables *v1*, *v2*, ..., *vm*. The initial values
for those variables will be *init1*, *init2*, ..., *initm*.
There will still be just one independent variable defined by `domain`,
as in the previous case. *ODE1*, ..., *ODEm* are the expressions
that define the derivatives of each dependent variable in
terms of the independent variable. The only variables that may appear in
those expressions are the independent variable and any of the dependent
variables. It is important to give the derivatives *ODE1*, ...,
*ODEm* in the list in exactly the same order used for the dependent
variables; for instance, the third element in the list will be interpreted
as the derivative of the third dependent variable.


The program will try to integrate the equations from the initial value
of the independent variable until its last value, using constant
increments. If at some step one of the dependent variables takes an
absolute value too large, the integration will be interrupted at that
point. The result will be a list with as many elements as the number of
iterations made. Each element in the results list is itself another list
with *m*+1 elements: the value of the independent variable, followed
by the values of the dependent variables corresponding to that point.


See also `drawdf`, `rk_adaptive`, `desolve` and
`ode2`.


Examples:


To solve numerically the differential equation



$${{dx}\over{dt}} = t - x^2$$


$${{dx}\over{dt}} = t - x^2$$



With initial value $x(t=0) = 1$, in the interval of $t$ from 0 to 8 and with
increments of 0.1 for $t$, use:







```maxima
maxima
(%i1) results: rk(t-x^2,x,1,[t,0,8,0.1])$
(%i2) plot2d ([discrete, results])$
```


The results will be saved in the list `results` and the plot will show the solution obtained, with *t* on the horizontal axis and *x* on the vertical axis.


figures/plotrk8cm

To solve numerically the system:



$$\eqalign{ {dx\over dy} &= 4-x^2-4y^2 \cr {dy\over dt} &= y^2 - x^2 + 1 }$$


$$\eqalign{
{dx\over dy} &= 4-x^2-4y^2 \cr
{dy\over dt} &= y^2 - x^2 + 1
}$$








for $t$ between 0 and 4, and with values of -1.25 and 0.75 for $x$ and $y$ at $t=0$:









```maxima
maxima

(%i1) sol: rk([4-x^2-4*y^2, y^2-x^2+1], [x, y], [-1.25, 0.75],
              [t,0,4,0.02])$


(%i2) plot2d([discrete, makelist([p[1], p[3]], p, sol)], [xlabel, "t"],
             [ylabel, "y"])$
```


The plot will show the solution for variable *y* as a function of *t*.


figures/plotrk28cm

See also: `drawdf`, `rk_adaptive`, `desolve`, `ode2`.

### Function: romberg (romberg, expr, x, a, b, romberg, F, a, b)

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

### Variable: rombergit

Default value: 11


`romberg` halves the stepsize at most `rombergit` times before it gives up;
the maximum number of function evaluations is therefore `2^rombergit`.
`romberg` always makes at least `rombergmin` iterations;
this is a heuristic intended to prevent spurious termination when the integrand is oscillatory.


See also `rombergabs` and `rombergtol`.

See also: `rombergabs`, `rombergtol`.

### Variable: rombergmin

Default value: 0


`romberg` always makes at least `rombergmin` iterations;
this is a heuristic intended to prevent spurious termination when the integrand is oscillatory.


See also `rombergit`, `rombergabs`, and `rombergtol`.

See also: `rombergit`, `rombergabs`, `rombergtol`.

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

### Function: specint (exp, -, s*, t, *, expr, t)

Compute the Laplace transform of *expr* with respect to the variable *t*.
The integrand *expr* may contain special functions.   The
parameter *s* maybe be named something else; it is determined
automatically, as the examples below show where *p* is used in
some places.


The following special functions are handled by `specint`: incomplete gamma 
function, error functions (but not the error function `erfi`, it is easy to 
transform `erfi` e.g. to the error function `erf`), exponential 
integrals, bessel functions (including products of bessel functions), hankel 
functions, hermite and the laguerre polynomials.


Furthermore, `specint` can handle the hypergeometric function 
`%f[p,q]([],[],z)`, the Whittaker function of the first kind 
`%m[u,k](z)` and of the second kind `%w[u,k](z)`.


The result may be in terms of special functions and can include unsimplified 
hypergeometric functions.  If variable `prefer_d` is `true`
then the `parabolic_cylinder_d` function may be used in the result
in preference to hypergeometric functions.


When `laplace` fails to find a Laplace transform, `specint` is called. 
Because `laplace` knows more general rules for Laplace transforms, it is 
preferable to use `laplace` and not `specint`.


`demo("hypgeo")` displays several examples of Laplace transforms computed by 
`specint`.


Examples:








```maxima
maxima
(%i1) assume (p > 0, a > 0)$

(%i2) specint (t^(1/2) * exp(-a*t/4) * exp(-p*t), t);
                           sqrt(%pi)
(%o2)                     ------------
                                 a 3/2
                          2 (p + -)
                                 4


(%i3) specint (t^(1/2) * bessel_j(1, 2 * a^(1/2) * t^(1/2))
              * exp(-p*t), t);
                           - a/p
                         %e      sqrt(a)
(%o3)                    ---------------
                                2
                               p
```


Examples for exponential integrals:











```maxima
maxima
(%i1) assume(s>0,a>0,s-a>0)$

(%i2) ratsimp(specint(%e^(a*t)*(log(a)+expintegral_e1(a*t))*%e^(-s*t),t));
                             log(s)
(%o2)                        ------
                             s - a

(%i3) logarc:true$
(%i4) gamma_expand:true$

(%i5) radcan(specint((cos(t)*expintegral_si(t) -sin(t)*expintegral_ci(t))*%e^(-s*t),t));
                             log(s)
(%o5)                        ------
                              2
                             s  + 1


(%i6) ratsimp(specint((2*t*log(a)+2/a*sin(a*t) -2*t*expintegral_ci(a*t))*%e^(-s*t),t));
                               2    2
                          log(s  + a )
(%o6)                     ------------
                                2
                               s
```


Results when using the expansion of `gamma_incomplete` and when changing 
the representation to `expintegral_e1`:











```maxima
maxima
(%i1) assume(s>0)$

(%i2) specint(1/sqrt(%pi*t)*unit_step(t-k)*%e^(-s*t),t);
                                     1
                    gamma_incomplete(-, k s)
                                     2
(%o2)               ------------------------
                       sqrt(%pi) sqrt(s)

(%i3) gamma_expand:true$

(%i4) specint(1/sqrt(%pi*t)*unit_step(t-k)*%e^(-s*t),t);
                      erfc(sqrt(k) sqrt(s))
(%o4)                 ---------------------
                             sqrt(s)

(%i5) expintrep:expintegral_e1$

(%i6) ratsimp(specint(1/(t+a)^2*%e^(-s*t),t));
                       a s
                 a s %e    expintegral_e1(a s) - 1
(%o6)          - ---------------------------------
                                 a
```

See also: `prefer_d`, `parabolic_cylinder_d`, `laplace`, `gamma_incomplete`, `expintegral_e1`.

### Function: tldefint (expr, x, a, b)

Equivalent to `ldefint` with `tlimswitch` set to `true`.

### Variable: yp

`yp` is the particular solution of an ODE found by `ode2`
when using the variation of parameters technique.

See also: `yp`, `ode2`.

