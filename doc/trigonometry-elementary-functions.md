## Elementary Functions

<!-- category: Trigonometry -->
<!-- keywords: %iargs -->
<!-- signatures: %iargs -->
### Variable: %iargs

Default value: `true`


When `%iargs` is `true`,
trigonometric functions are simplified to hyperbolic functions
when the argument is apparently a multiple of the imaginary
unit 
$i.$








Even when the argument is demonstrably real, the simplification is applied;
Maxima considers only whether the argument is a literal multiple
of 
$i.$








Examples:









```maxima
maxima
(%i1) %iargs : false$

(%i2) [sin (%i * x), cos (%i * x), tan (%i * x)];
(%o2)           [sin(%i x), cos(%i x), tan(%i x)]

(%i3) %iargs : true$

(%i4) [sin (%i * x), cos (%i * x), tan (%i * x)];
(%o4)           [%i sinh(x), cosh(x), %i tanh(x)]
```


Even when the argument is demonstrably real, the simplification is applied.








```maxima
maxima
(%i1) declare (x, imaginary)$

(%i2) [featurep (x, imaginary), featurep (x, real)];
(%o2)                     [true, false]


(%i3) sin (%i * x);
(%o3)                      %i sinh(x)
```

<!-- category: Trigonometry -->
<!-- keywords: %piargs -->
<!-- signatures: %piargs -->
### Variable: %piargs

Default value: `true`


When `%piargs` is `true`,
trigonometric functions are simplified to algebraic constants
when the argument is an integer multiple
of
$\pi,$
$\pi/2,$
$\pi/4,$
or
$\pi/6.$








Maxima knows some identities which can be applied when
$\pi,$
etc.,






are multiplied by an integer variable (that is, a symbol declared to be
integer).


Examples:













```maxima
maxima
(%i1) %piargs : false$

(%i2) [sin (%pi), sin (%pi/2), sin (%pi/3)];
                                %pi       %pi
(%o2)            [sin(%pi), sin(---), sin(---)]
                                 2         3


(%i3) [sin (%pi/4), sin (%pi/5), sin (%pi/6)];
                      %pi       %pi       %pi
(%o3)            [sin(---), sin(---), sin(---)]
                       4         5         6

(%i4) %piargs : true$

(%i5) [sin (%pi), sin (%pi/2), sin (%pi/3)];
                                sqrt(3)
(%o5)                    [0, 1, -------]
                                   2


(%i6) [sin (%pi/4), sin (%pi/5), sin (%pi/6)];
                         1         %pi   1
(%o6)                [-------, sin(---), -]
                      sqrt(2)       5    2


(%i7) [cos (%pi/3), cos (10*%pi/3), tan (10*%pi/3),
       cos (sqrt(2)*%pi/3)];
                1    1               sqrt(2) %pi
(%o7)          [-, - -, sqrt(3), cos(-----------)]
                2    2                    3
```


Some identities are applied when 
$\pi$
and 
$\pi/2$
are
multiplied by an integer variable.
















```maxima
maxima
(%i1) declare (n, integer, m, even)$

(%i2) [sin (%pi * n), cos (%pi * m), sin (%pi/2 * m),
       cos (%pi/2 * m)];
                                      m/2
(%o2)                  [0, 1, 0, (- 1)   ]
```

<!-- category: Trigonometry -->
<!-- keywords: acos -->
<!-- signatures: acos(x) -->
### Function: acos (x)

– Arc Cosine.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: acosh -->
<!-- signatures: acosh(x) -->
### Function: acosh (x)

– Hyperbolic Arc Cosine.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: acot -->
<!-- signatures: acot(x) -->
### Function: acot (x)

– Arc Cotangent.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: acoth -->
<!-- signatures: acoth(x) -->
### Function: acoth (x)

– Hyperbolic Arc Cotangent.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: acsc -->
<!-- signatures: acsc(x) -->
### Function: acsc (x)

– Arc Cosecant.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: acsch -->
<!-- signatures: acsch(x) -->
### Function: acsch (x)

– Hyperbolic Arc Cosecant.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: asec -->
<!-- signatures: asec(x) -->
### Function: asec (x)

– Arc Secant.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: asech -->
<!-- signatures: asech(x) -->
### Function: asech (x)

– Hyperbolic Arc Secant.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: asin -->
<!-- signatures: asin(x) -->
### Function: asin (x)

– Arc Sine.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: asinh -->
<!-- signatures: asinh(x) -->
### Function: asinh (x)

– Hyperbolic Arc Sine.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: atan -->
<!-- signatures: atan(x) -->
### Function: atan (x)

– Arc Tangent.


See also `atan2`.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `atan2`, `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: atan2 -->
<!-- signatures: atan2(y, x) -->
### Function: atan2 (y, x)

– yields the value of
$\tan^{-1}(y/x)$
in the interval
$-\pi$
to
$\pi$
taking into
consideration the quadrant of the point 
$(x,y).$


Along the branch cut with $y = 0$ and $x < 0$, `atan2`
is continuous with the second quadrant.
See also `atan`.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `atan`, `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: atanh -->
<!-- signatures: atanh(x) -->
### Function: atanh (x)

– Hyperbolic Arc Tangent.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: atrig1 -->
<!-- signatures: atrig1 -->
### Variable: atrig1

The `atrig1` package contains several additional simplification rules
for inverse trigonometric functions.  Together with rules
already known to Maxima, the following angles are fully implemented:
$0$,
$\pi/6,$
$\pi/4,$
$\pi/3,$
and
$\pi/2.$
Corresponding angles in the other three quadrants are also available.
Do `load("atrig1");` to use them.

<!-- category: Trigonometry -->
<!-- keywords: cos -->
<!-- signatures: cos(x) -->
### Function: cos (x)

– Cosine.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: cosh -->
<!-- signatures: cosh(x) -->
### Function: cosh (x)

– Hyperbolic Cosine.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: cot -->
<!-- signatures: cot(x) -->
### Function: cot (x)

– Cotangent.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: coth -->
<!-- signatures: coth(x) -->
### Function: coth (x)

– Hyperbolic Cotangent.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: csc -->
<!-- signatures: csc(x) -->
### Function: csc (x)

– Cosecant.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: csch -->
<!-- signatures: csch(x) -->
### Function: csch (x)

– Hyperbolic Cosecant.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: halfangles -->
<!-- signatures: halfangles -->
### Variable: halfangles

Default value: `false`


When `halfangles` is `true`, trigonometric functions of arguments 
`expr/2` are simplified to functions of *expr*.


For a real argument $x$ in the interval
$0 \le x < 2\pi,$
$\sin{x\over 2}$
simplifies to a simple formula:

$${\sqrt{1-\cos x}\over\sqrt{2}}$$


$${\sqrt{1-\cos x}\over\sqrt{2}}$$




A complicated factor is needed to make this formula correct for all complex 
arguments $z = x+iy$:

$$(-1)^{\lfloor{x/(2\pi)}\rfloor} \left[1-\rm{unit\_step}(-y) \left(1+(-1)^{\lfloor{x/(2\pi)}\rfloor - \lceil{x/(2\pi)}\rceil}\right)\right]$$


$$(-1)^{\lfloor{x/(2\pi)}\rfloor}
\left[1-\rm{unit\_step}(-y)
\left(1+(-1)^{\lfloor{x/(2\pi)}\rfloor - \lceil{x/(2\pi)}\rceil}\right)\right]
$$




Maxima knows this factor and similar factors for the functions `sin`, 
`cos`, `sinh`, and `cosh`.  For special values of the argument 
$z$ these factors simplify accordingly.


Examples:











```maxima
maxima
(%i1) halfangles : false$

(%i2) sin (x / 2);
                                 x
(%o2)                        sin(-)
                                 2

(%i3) halfangles : true$

(%i4) sin (x / 2);
                            x
                    floor(-----)
                          2 %pi
               (- 1)             sqrt(1 - cos(x))
(%o4)          ----------------------------------
                            sqrt(2)

(%i5) assume(x>0, x<2*%pi)$

(%i6) sin(x / 2);
                        sqrt(1 - cos(x))
(%o6)                   ----------------
                            sqrt(2)
```

<!-- category: Trigonometry -->
<!-- keywords: ntrig -->
<!-- signatures: ntrig -->
### Variable: ntrig

The `ntrig` package contains a set of simplification rules that are
used to simplify trigonometric function whose arguments are of the form
`f(n %pi/10)` where *f* is any of the functions
`sin`, `cos`, `tan`, `csc`, `sec` and `cot`.

<!-- category: Trigonometry -->
<!-- keywords: sec -->
<!-- signatures: sec(x) -->
### Function: sec (x)

– Secant.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: sech -->
<!-- signatures: sech(x) -->
### Function: sech (x)

– Hyperbolic Secant.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: sin -->
<!-- signatures: sin(x) -->
### Function: sin (x)

– Sine.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: sinh -->
<!-- signatures: sinh(x) -->
### Function: sinh (x)

– Hyperbolic Sine.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: tan -->
<!-- signatures: tan(x) -->
### Function: tan (x)

– Tangent.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: tanh -->
<!-- signatures: tanh(x) -->
### Function: tanh (x)

– Hyperbolic Tangent.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

<!-- category: Trigonometry -->
<!-- keywords: trigexpand -->
<!-- signatures: trigexpand(expr) -->
### Function: trigexpand (expr)

Expands trigonometric and hyperbolic functions of
sums of angles and of multiple angles occurring in *expr*.  For best
results, *expr* should be expanded.  To enhance user control of
simplification, this function expands only one level at a time,
expanding sums of angles or multiple angles.  To obtain full expansion
into sines and cosines immediately, set the switch `trigexpand: true`.


`trigexpand` is governed by the following global flags:



**`trigexpand`** — If `true` causes expansion of all
expressions containing sin’s and cos’s occurring subsequently.
**`halfangles`** — If `true` causes half-angles to be simplified
away.
**`trigexpandplus`** — Controls the "sum" rule for `trigexpand`,
expansion of sums (e.g. `sin(x + y)`) will take place only if
`trigexpandplus` is `true`.
**`trigexpandtimes`** — Controls the "product" rule for `trigexpand`,
expansion of products (e.g. `sin(2 x)`) will take place only if
`trigexpandtimes` is `true`.


Examples:







```maxima
maxima

(%i1) x+sin(3*x)/sin(x),trigexpand=true,expand;
                         2           2
(%o1)               - sin (x) + 3 cos (x) + x


(%i2) trigexpand(sin(10*x+y));
(%o2)          cos(10 x) sin(y) + sin(10 x) cos(y)
```

See also: `trigexpand`, `halfangles`, `trigexpandplus`, `trigexpandtimes`.

<!-- category: Trigonometry -->
<!-- keywords: trigexpandplus -->
<!-- signatures: trigexpandplus -->
### Variable: trigexpandplus

Default value: `true`


`trigexpandplus` controls the "sum" rule for
`trigexpand`.  Thus, when the `trigexpand` command is used or the
`trigexpand` switch set to `true`, expansion of sums
(e.g. `sin(x+y))` will take place only if `trigexpandplus` is
`true`.

See also: `trigexpand`.

<!-- category: Trigonometry -->
<!-- keywords: trigexpandtimes -->
<!-- signatures: trigexpandtimes -->
### Variable: trigexpandtimes

Default value: `true`


`trigexpandtimes` controls the "product" rule for `trigexpand`.
Thus, when the `trigexpand` command is used or the `trigexpand`
switch set to `true`, expansion of products (e.g. `sin(2*x)`)
will take place only if `trigexpandtimes` is `true`.

See also: `trigexpand`.

<!-- category: Trigonometry -->
<!-- keywords: triginverses -->
<!-- signatures: triginverses -->
### Variable: triginverses

Default value: `true`


`triginverses` controls the simplification of the
composition of trigonometric and hyperbolic functions with their inverse
functions.


If `all`, both e.g. `atan(tan(x))`
and `tan(atan(x))` simplify to *x*.


If `true`, the `arcfun(fun(x))`
simplification is turned off.


If `false`, both the
`arcfun(fun(x))` and
`fun(arcfun(x))`
simplifications are turned off.

<!-- category: Trigonometry -->
<!-- keywords: trigrat -->
<!-- signatures: trigrat(expr) -->
### Function: trigrat (expr)

Gives a canonical simplified quasilinear form of a trigonometrical expression;
*expr* is a rational fraction of several `sin`, `cos` or
`tan`, the arguments of them are linear forms in some variables (or
kernels) and `%pi/n` (*n* integer) with integer coefficients.
The result is a simplified fraction with numerator and denominator linear in
`sin` and `cos`.  Thus `trigrat` linearize always when it is
possible.






```maxima
maxima

(%i1) trigrat(sin(3*a)/sin(a+%pi/3));
(%o1)            sqrt(3) sin(2 a) + cos(2 a) - 1
```


The following example is taken from
Davenport, Siret, and Tournier, *Calcul Formel*, Masson (or in English,
Addison-Wesley), section 1.5.5, Morley theorem.










```maxima
maxima
(%i1) c : %pi/3 - a - b$

(%i2) bc : sin(a)*sin(3*c)/sin(a+b);
                                          %pi
                  sin(a) sin(3 (- b - a + ---))
                                           3
(%o2)             -----------------------------
                           sin(b + a)


(%i3) ba : bc, c=a, a=c;
                                         %pi
                    sin(3 a) sin(b + a - ---)
                                          3
(%o3)               -------------------------
                                  %pi
                          sin(a - ---)
                                   3


(%i4) ac2 : ba^2 + bc^2 - 2*bc*ba*cos(b);
         2         2         %pi
      sin (3 a) sin (b + a - ---)
                              3
(%o4) ---------------------------
                2     %pi
             sin (a - ---)
                       3
                                       %pi
 - (2 sin(a) sin(3 a) sin(3 (- b - a + ---)) cos(b)
                                        3
             %pi            %pi
 sin(b + a - ---))/(sin(a - ---) sin(b + a))
              3              3
      2       2              %pi
   sin (a) sin (3 (- b - a + ---))
                              3
 + -------------------------------
                2
             sin (b + a)


(%i5) trigrat (ac2);
(%o5) - (sqrt(3) sin(4 b + 4 a) - cos(4 b + 4 a)
 - 2 sqrt(3) sin(4 b + 2 a) + 2 cos(4 b + 2 a)
 - 2 sqrt(3) sin(2 b + 4 a) + 2 cos(2 b + 4 a)
 + 4 sqrt(3) sin(2 b + 2 a) - 8 cos(2 b + 2 a) - 4 cos(2 b - 2 a)
 + sqrt(3) sin(4 b) - cos(4 b) - 2 sqrt(3) sin(2 b) + 10 cos(2 b)
 + sqrt(3) sin(4 a) - cos(4 a) - 2 sqrt(3) sin(2 a) + 10 cos(2 a)
 - 9)/4
```

<!-- category: Trigonometry -->
<!-- keywords: trigreduce -->
<!-- signatures: trigreduce(expr, x), trigreduce(expr) -->
### Function: trigreduce (expr, x)

Combines products and powers of trigonometric
and hyperbolic sin’s and cos’s of *x* into those of multiples of *x*.
It also tries to eliminate these functions when they occur in
denominators.  If *x* is omitted then all variables in *expr* are used.


See also `poissimp`.






```maxima
maxima

(%i1) trigreduce(-sin(x)^2+3*cos(x)^2+x);
               cos(2 x)      cos(2 x)   1        1
(%o1)          -------- + 3 (-------- + -) + x - -
                  2             2       2        2
```

See also: `poissimp`.

<!-- category: Trigonometry -->
<!-- keywords: trigsign -->
<!-- signatures: trigsign -->
### Variable: trigsign

Default value: `true`


When `trigsign` is `true`, it permits simplification of negative
arguments to trigonometric functions.  E.g., 
$\sin(-x)$
will
become 
$-\sin x$
only if `trigsign` is `true`.

<!-- category: Trigonometry -->
<!-- keywords: trigsimp -->
<!-- signatures: trigsimp(expr) -->
### Function: trigsimp (expr)

Employs the identities
$\sin\left(x\right)^2 + \cos\left(x\right)^2 = 1$
and 
$\cosh\left(x\right)^2 - \sinh\left(x\right)^2 = 1$
to








simplify expressions containing `tan`, `sec`,
etc., to `sin`, `cos`, `sinh`, `cosh`.








`trigreduce`, `ratsimp`, and `radcan` may be
able to further simplify the result.


`demo ("trgsmp.dem")` displays some examples of `trigsimp`.

See also: `trigreduce`, `ratsimp`, `radcan`.

