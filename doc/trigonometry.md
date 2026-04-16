## Trigonometry

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

### Function: acos (x)

– Arc Cosine.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: acosh (x)

– Hyperbolic Arc Cosine.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: acot (x)

– Arc Cotangent.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: acoth (x)

– Hyperbolic Arc Cotangent.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: acsc (x)

– Arc Cosecant.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: acsch (x)

– Hyperbolic Arc Cosecant.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: asec (x)

– Arc Secant.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: asech (x)

– Hyperbolic Arc Secant.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: asin (x)

– Arc Sine.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: asinh (x)

– Hyperbolic Arc Sine.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: atan (x)

– Arc Tangent.


See also `atan2`.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `atan2`, `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

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

### Function: atan_contract (r)

The function atan_contract(r) contracts atan functions. We
assume: 
$|r| < {\pi\over 2}.$


`load("trigtools")` loads this function.



Examples:



1. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) atan_contract(atan(x)+atan(y));
(%o2)                   atan(y) + atan(x)

(%i3) assume(abs(atan(x)+atan(y))<%pi/2)$

(%i4) atan(x)+atan(y)=atan_contract(atan(x)+atan(y));
                                          y + x
(%o4)           atan(y) + atan(x) = atan(-------)
                                         1 - x y
```
2. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) atan(1/3)+atan(1/5)+atan(1/7)+atan(1/8)$ %=atan_contract(%);
                1         1         1         1    %pi
(%o3)      atan(-) + atan(-) + atan(-) + atan(-) = ---
                3         5         7         8     4
```
3. Machin’s formulae






```maxima
maxima
(%i1) load("trigtools")$

(%i2) 4*atan(1/5)-atan(1/239)=atan_contract(4*atan(1/5)-atan(1/239));
                          1          1     %pi
(%o2)              4 atan(-) - atan(---) = ---
                          5         239     4
```
4. see [https://en.wikipedia.org/wiki/Machin-like_formula]()







```maxima
maxima
(%i1) load("trigtools")$
(%i2) 12*atan(1/49)+32*atan(1/57)-5*atan(1/239)+12*atan(1/110443)$

(%i3) %=atan_contract(%);
              1             1             1
(%o3) 12 atan(--) + 32 atan(--) - 5 atan(---)
              49            57           239
                                                      1       %pi
                                          + 12 atan(------) = ---
                                                    110443     4
```

### Function: atanh (x)

– Hyperbolic Arc Tangent.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

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

### Function: c2hyp (x)

The function c2hyp (convert to hyperbolic) convert expression with exp function
to expression with hyperbolic functions sinh, cosh.


`load("trigtools")` loads this function.


Examples:









```maxima
maxima
(%i1) load("trigtools")$

(%i2) c2hyp(exp(x));
(%o2)                   sinh(x) + cosh(x)


(%i3) c2hyp(exp(x)+exp(x^2)+1);
                 2          2
(%o3)      sinh(x ) + cosh(x ) + sinh(x) + cosh(x) + 1


(%i4) c2hyp(exp(x)/(2*exp(y)-3*exp(z)));
                        sinh(x) + cosh(x)
(%o4)     ---------------------------------------------
          2 (sinh(y) + cosh(y)) - 3 (sinh(z) + cosh(z))
```

### Function: c2sin (x)

The function c2sin converts the expression 
$a\cos x + b\sin x$
to
$r\sin(x+\phi).$


The function c2cos converts the expression 
$a\cos x + b\sin x$
to
$r\cos(x-\phi).$


`load("trigtools")` loads these functions.


Examples:













```maxima
maxima
(%i1) load("trigtools")$

(%i2) c2sin(3*sin(x)+4*cos(x));
                                      4
(%o2)                  5 sin(x + atan(-))
                                      3


(%i3) trigexpand(%),expand;
(%o3)                  3 sin(x) + 4 cos(x)


(%i4) c2cos(3*sin(x)-4*cos(x));
                                       3
(%o4)                 - 5 cos(x + atan(-))
                                       4


(%i5) trigexpand(%),expand;
(%o5)                  3 sin(x) - 4 cos(x)


(%i6) c2sin(sin(x)+cos(x));
                                      %pi
(%o6)                 sqrt(2) sin(x + ---)
                                       4


(%i7) trigexpand(%),expand;
(%o7)                    sin(x) + cos(x)


(%i8) c2cos(sin(x)+cos(x));
                                      %pi
(%o8)                 sqrt(2) cos(x - ---)
                                       4


(%i9) trigexpand(%),expand;
(%o9)                    sin(x) + cos(x)
```


Example. Solve trigonometric equation







```maxima
maxima

(%i1) eq:3*sin(x)+4*cos(x)=2;
(%o1)                3 sin(x) + 4 cos(x) = 2


(%i2) plot2d([3*sin(x)+4*cos(x),2],[x,-%pi,%pi]);
(%o2)                         false
```


figures/trigtools-15inplot1














```maxima
maxima
(%i1) load("trigtools")$
(%i2) eq:3*sin(x)+4*cos(x)=2$

(%i3) eq1:c2sin(lhs(eq))=2;
                                    4
(%o3)                5 sin(x + atan(-)) = 2
                                    3

(%i4) solvetrigwarn:false$

(%i5) solve(eq1)[1]$ x1:rhs(%);
                             2         4
(%o6)                   asin(-) - atan(-)
                             5         3


(%i7) float(%), numer;
(%o7)                 - 0.5157783719341241


(%i8) eq2:c2cos(lhs(eq))=2;
                                    3
(%o8)                5 cos(x - atan(-)) = 2
                                    4


(%i9) solve(eq2,x)[1]$ x2:rhs(%);
                             3         2
(%o10)                  atan(-) + acos(-)
                             4         5


(%i11) float(%), numer;
(%o11)                  1.802780589520693


(%i12) sol:[x1,x2];
                   2         4        3         2
(%o12)       [asin(-) - atan(-), atan(-) + acos(-)]
                   5         3        4         5
```



Answ.: 
$x = x_1 + 2\pi k,$
$x_1 = \sin^{-1}{2\over 5} - \tan^{-1}{4\over 3},$
or
$x_1 = \tan^{-1}{3\over 4} + \cos^{-1}{2\over 5},$
for $k$ any integer.

### Function: c2trig (x)

The function c2trig (convert to trigonometric) reduce expression with hyperbolic functions
sinh, cosh, tanh, coth to trigonometric expression with sin, cos, tan, cot.


`load("trigtools")` loads these functions.


Examples:



1. ```maxima
maxima
(%i1) load(trigtools)$

(%i2) sinh(x)=c2trig(sinh(x));
(%o2)               sinh(x) = - %i sin(%i x)


(%i3) cosh(x)=c2trig(cosh(x));
(%o3)                  cosh(x) = cos(%i x)


(%i4) tanh(x)=c2trig(tanh(x));
(%o4)               tanh(x) = - %i tan(%i x)


(%i5) coth(x)=c2trig(coth(x));
(%o5)                coth(x) = %i cot(%i x)
```
2. see [https://maxima.sourceforge.io/ext/list_archives/2013/msg03230.html]()








```maxima
maxima
(%i1) load("trigtools")$

(%i2) cos(p+q*%i);
(%o2)                     cos(%i q + p)


(%i3) trigexpand(%);
(%o3)          cos(p) cosh(q) - %i sin(p) sinh(q)


(%i4) c2trig(%);
(%o4)                     cos(%i q + p)
```
3. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) sin(a+b*%i);
(%o2)                     sin(%i b + a)


(%i3) trigexpand(%);
(%o3)          %i cos(a) sinh(b) + sin(a) cosh(b)


(%i4) c2trig(%);
(%o4)                     sin(%i b + a)
```
4. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) cos(a*%i+b*%i);
(%o2)                   cos(%i b + %i a)


(%i3) trigexpand(%);
(%o3)           sinh(a) sinh(b) + cosh(a) cosh(b)


(%i4) c2trig(%);
(%o4)                   cos(%i b + %i a)
```
5. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) tan(a+%i*b);
(%o2)                     tan(%i b + a)


(%i3) trigexpand(%);
                       %i tanh(b) + tan(a)
(%o3)                 ---------------------
                      1 - %i tan(a) tanh(b)


(%i4) c2trig(%);
(%o4)                     tan(%i b + a)
```
6. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) cot(x+%i*y);
(%o2)                     cot(%i y + x)


(%i3) trigexpand(%);
                     - %i cot(x) coth(y) - 1
(%o3)                -----------------------
                       cot(x) - %i coth(y)


(%i4) c2trig(%);
(%o4)                     cot(%i y + x)
```

### Function: cos (x)

– Cosine.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: cosh (x)

– Hyperbolic Cosine.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: cot (x)

– Cotangent.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: coth (x)

– Hyperbolic Cotangent.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: csc (x)

– Cosecant.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: csch (x)

– Hyperbolic Cosecant.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

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

### Variable: ntrig

The `ntrig` package contains a set of simplification rules that are
used to simplify trigonometric function whose arguments are of the form
`f(n %pi/10)` where *f* is any of the functions
`sin`, `cos`, `tan`, `csc`, `sec` and `cot`.

### Function: sec (x)

– Secant.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: sech (x)

– Hyperbolic Secant.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: sin (x)

– Sine.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: sinh (x)

– Hyperbolic Sine.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: tan (x)

– Tangent.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: tanh (x)

– Hyperbolic Tangent.


For variables that control simplification `_0025piargs`,
`_0025iargs`, `halfangles`, `triginverses`, and
`trigsign`.

See also: `%piargs`, `%iargs`, `halfangles`, `triginverses`, `trigsign`.

### Function: trigeval (x)

The function trigeval compute values of expressions with 
$\sin {m\pi\over n},$
$\cos {m\pi\over n},$
$\tan {m\pi\over n},$
and 
$\cot {m\pi\over n}$
in radicals.

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

### Variable: trigexpandplus

Default value: `true`


`trigexpandplus` controls the "sum" rule for
`trigexpand`.  Thus, when the `trigexpand` command is used or the
`trigexpand` switch set to `true`, expansion of sums
(e.g. `sin(x+y))` will take place only if `trigexpandplus` is
`true`.

See also: `trigexpand`.

### Variable: trigexpandtimes

Default value: `true`


`trigexpandtimes` controls the "product" rule for `trigexpand`.
Thus, when the `trigexpand` command is used or the `trigexpand`
switch set to `true`, expansion of products (e.g. `sin(2*x)`)
will take place only if `trigexpandtimes` is `true`.

See also: `trigexpand`.

### Function: trigfactor (x)

The function trigfactor factors expressions of
form 
$\pm \sin x \pm \cos y.$


`load("trigtools")` loads this function.


Examples:



1. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) trigfactor(sin(x)+cos(x));
                                      %pi
(%o2)                 sqrt(2) cos(x - ---)
                                       4


(%i3) trigrat(%);
(%o3)                    sin(x) + cos(x)
```
2. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) trigfactor(sin(x)+cos(y));
                     y   x   %pi      y   x   %pi
(%o2)          2 cos(- - - + ---) cos(- + - - ---)
                     2   2    4       2   2    4


(%i3) trigrat(%);
(%o3)                    cos(y) + sin(x)
```
3. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) trigfactor(sin(x)-cos(3*y));
                   3 y   x   %pi      3 y   x   %pi
(%o2)        2 sin(--- - - + ---) sin(--- + - - ---)
                    2    2    4        2    2    4


(%i3) trigrat(%);
(%o3)                   sin(x) - cos(3 y)
```
4. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) trigfactor(-sin(5*x)-cos(3*y));
                  3 y   5 x   %pi      3 y   5 x   %pi
(%o2)     - 2 cos(--- - --- + ---) cos(--- + --- - ---)
                   2     2     4        2     2     4


(%i3) trigrat(%);
(%o3)                 - cos(3 y) - sin(5 x)
```
5. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) sin(alpha)+sin(beta)=trigfactor(sin(alpha)+sin(beta));
                                     beta   alpha
(%o2) sin(beta) + sin(alpha) = 2 cos(---- - -----)
                                      2       2
                                                    beta   alpha
                                                sin(---- + -----)
                                                     2       2


(%i3) trigrat(%);
(%o3)    sin(beta) + sin(alpha) = sin(beta) + sin(alpha)
```
6. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) sin(alpha)-sin(beta)=trigfactor(sin(alpha)-sin(beta));
                                       beta   alpha
(%o2) sin(alpha) - sin(beta) = - 2 sin(---- - -----)
                                        2       2
                                                    beta   alpha
                                                cos(---- + -----)
                                                     2       2
```
7. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) cos(alpha)+cos(beta)=trigfactor(cos(alpha)+cos(beta));
                                     beta   alpha
(%o2) cos(beta) + cos(alpha) = 2 cos(---- - -----)
                                      2       2
                                                    beta   alpha
                                                cos(---- + -----)
                                                     2       2
```
8. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) cos(alpha)-cos(beta)=trigfactor(cos(alpha)-cos(beta));
                                     beta   alpha
(%o2) cos(alpha) - cos(beta) = 2 sin(---- - -----)
                                      2       2
                                                    beta   alpha
                                                sin(---- + -----)
                                                     2       2
```
9. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) trigfactor(3*sin(x)+7*cos(x));
(%o2)                  3 sin(x) + 7 cos(x)


(%i3) c2sin(%);
                                          7
(%o3)               sqrt(58) sin(x + atan(-))
                                          3


(%i4) trigexpand(%),expand;
(%o4)                  3 sin(x) + 7 cos(x)
```
10. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) trigfactor(sin(2*x));
(%o2)                       sin(2 x)


(%i3) trigexpand(%);
(%o3)                    2 cos(x) sin(x)
```

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

### Function: trigreduce (trigreduce, expr, x, trigreduce, expr)

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

### Variable: trigsign

Default value: `true`


When `trigsign` is `true`, it permits simplification of negative
arguments to trigonometric functions.  E.g., 
$\sin(-x)$
will
become 
$-\sin x$
only if `trigsign` is `true`.

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

### Function: trigsolve (x)

The function trigsolve find solutions of trigonometric equation from
interval 
$[a,b).$


`load("trigtools")` loads this function.



Examples:


1. ```maxima
maxima

(%i1) eq:eq:3*sin(x)+4*cos(x)=2;
(%o1)                3 sin(x) + 4 cos(x) = 2


(%i2) plot2d([3*sin(x)+4*cos(x),2],[x,-%pi,%pi]);
(%o2)                         false
```


figures/trigtools-25inplot2








```maxima
maxima
(%i1) load("trigtools")$
(%i2) eq:eq:3*sin(x)+4*cos(x)=2$

(%i3) sol:trigsolve(eq,-%pi,%pi);
            2 sqrt(21)   12              2 sqrt(21)   12
(%o3) {atan(---------- - --), %pi - atan(---------- + --)}
                5        5                   5        5


(%i4) float(%), numer;
(%o4)      {- 0.5157783719341241, 1.8027805895206928}
```


Answ. : 
$x = \tan^{-1}\left({2\sqrt{21}\over 5} - {12\over 5}\right) + 2\pi k$
;
$x = \pi - \tan^{-1}\left({2\sqrt{21}\over 5} + {12\over 5}\right) + 2\pi k,$
$k$ – any integer.
2. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) eq:cos(3*x)-sin(x)=sqrt(3)*(cos(x)-sin(3*x));
(%o2)    cos(3 x) - sin(x) = sqrt(3) (cos(x) - sin(3 x))

(%i3) plot2d([lhs(eq)-rhs(eq)], [x,0,2*%pi])$
```


figures/trigtools-35inplot3

We have 6 solutions from [0, 2*pi].







```maxima
maxima
(%i1) load("trigtools")$
(%i2) eq:cos(3*x)-sin(x)=sqrt(3)*(cos(x)-sin(3*x))$
(%i3) plot2d([lhs(eq)-rhs(eq)], [x,0.2,0.5])$
```


figures/trigtools-45inplot4








```maxima
maxima
(%i1) load("trigtools")$
(%i2) load("trigtools")$
(%i3) eq:cos(3*x)-sin(x)=sqrt(3)*(cos(x)-sin(3*x))$
(%i4) plot2d([lhs(eq)-rhs(eq)], [x,3.3,3.6])$
```


figures/trigtools-55inplot4








```maxima
maxima
(%i1) load("trigtools")$
(%i2) eq:cos(3*x)-sin(x)=sqrt(3)*(cos(x)-sin(3*x))$

(%i3) trigfactor(lhs(eq))=map(trigfactor,rhs(eq));
                  %pi            %pi
(%o3) - 2 sin(x + ---) sin(2 x - ---) = 
                   4              4
                                              %pi            %pi
                            2 sqrt(3) sin(x - ---) sin(2 x - ---)
                                               4              4


(%i4) factor(lhs(%)-rhs(%));
               4 x + %pi                4 x - %pi
(%o4) - 2 (sin(---------) + sqrt(3) sin(---------))
                   4                        4
                                                       8 x - %pi
                                                   sin(---------)
                                                           4
```


Equation is equivalent to














```maxima
maxima
(%i1) load("trigtools")$
(%i2) eq:cos(3*x)-sin(x)=sqrt(3)*(cos(x)-sin(3*x))$

(%i3) trigfactor(lhs(eq))=map(trigfactor,rhs(eq));
                  %pi            %pi
(%o3) - 2 sin(x + ---) sin(2 x - ---) = 
                   4              4
                                              %pi            %pi
                            2 sqrt(3) sin(x - ---) sin(2 x - ---)
                                               4              4


(%i4) L:factor(rhs(%)-lhs(%));
             4 x + %pi                4 x - %pi       8 x - %pi
(%o4) 2 (sin(---------) + sqrt(3) sin(---------)) sin(---------)
                 4                        4               4


(%i5) eq1:part(L,2)=0;
               4 x + %pi                4 x - %pi
(%o5)      sin(---------) + sqrt(3) sin(---------) = 0
                   4                        4


(%i6) eq2:part(L,3)=0;
                           8 x - %pi
(%o6)                  sin(---------) = 0
                               4


(%i7) S1:trigsolve(eq1,0,2*%pi);
                           %pi  13 %pi
(%o7)                     {---, ------}
                           12     12


(%i8) S2:trigsolve(eq2,0,2*%pi);
                    %pi  5 %pi  9 %pi  13 %pi
(%o8)              {---, -----, -----, ------}
                     8     8      8      8


(%i9) S:listify(union(S1,S2));
             %pi  %pi  5 %pi  13 %pi  9 %pi  13 %pi
(%o9)       [---, ---, -----, ------, -----, ------]
             12    8     8      12      8      8


(%i10) float(%), numer;
(%o10) [0.2617993877991494, 0.39269908169872414, 
1.9634954084936207, 3.4033920413889422, 3.5342917352885173, 
5.105088062083414]
```


Answer: 
$x = a + 2\pi k,$
where $a$ any from $S$, $k$ any integer.
3. ```maxima
maxima
(%i1) load("trigtools")$

(%i2) eq:8*cos(x)*cos(4*x)*cos(5*x)-1=0;
(%o2)          8 cos(x) cos(4 x) cos(5 x) - 1 = 0


(%i3) trigrat(%);
(%o3)     2 cos(10 x) + 2 cos(8 x) + 2 cos(2 x) + 1 = 0
```


Left side is periodic with period 
$T=\pi.$


We have 10 solutions from [0, pi].







```maxima
maxima
(%i1) load("trigtools")$
(%i2) eq:8*cos(x)*cos(4*x)*cos(5*x)-1=0$

(%i3) plot2d([lhs(eq),rhs(eq)],[x,0,%pi]);
(%o3)                         false
```


figures/trigtools-65inplot6









```maxima
maxima
(%i1) load("trigtools")$
(%i2) eq:8*cos(x)*cos(4*x)*cos(5*x)-1=0$

(%i3) x4:find_root(eq, x, 1.3, 1.32);
(%o3)                  1.3089969389957472


(%i4) x5:find_root(eq, x, 1.32, 1.35);
(%o4)                  1.3463968515384828


(%i5) plot2d([lhs(eq),0], [x,1.3,1.35], [gnuplot_preamble, "set grid;"]);
(%o5)                         false
```


figures/trigtools-75inplot7

Equation we multiply by 
$2\sin x\cos 2x:$













```maxima
maxima
(%i1) load("trigtools")$
(%i2) eq:8*cos(x)*cos(4*x)*cos(5*x)-1=0$

(%i3) eq*2*sin(x)*cos(2*x);
(%o3) 2 sin(x) cos(2 x) (8 cos(x) cos(4 x) cos(5 x) - 1) = 0


(%i4) eq1:trigreduce(%),expand;
(%o4)                sin(13 x) + sin(x) = 0


(%i5) trigfactor(lhs(eq1))=0;
(%o5)                2 cos(6 x) sin(7 x) = 0


(%i6) S1:trigsolve(cos(6*x),0,%pi);
              %pi  %pi  5 %pi  7 %pi  3 %pi  11 %pi
(%o6)        {---, ---, -----, -----, -----, ------}
              12    4    12     12      4      12


(%i7) S2:trigsolve(sin(7*x),0,%pi);
               %pi  2 %pi  3 %pi  4 %pi  5 %pi  6 %pi
(%o7)      {0, ---, -----, -----, -----, -----, -----}
                7     7      7      7      7      7
```


We remove solutions of 
$\sin x = 0$
and
$\cos 2x = 0.$










```maxima
maxima
(%i1) load("trigtools")$
(%i2) S1:trigsolve(cos(6*x),0,%pi)$
(%i3) S2:trigsolve(sin(7*x),0,%pi)$

(%i4) S3:trigsolve(sin(x),0,%pi);
(%o4)                          {0}


(%i5) S4:trigsolve(cos(2*x),0,%pi);
                           %pi  3 %pi
(%o5)                     {---, -----}
                            4     4
```


We find 10 solutions from 
$[0, \pi]:$














```maxima
maxima
(%i1) load("trigtools")$
(%i2) S1:trigsolve(cos(6*x),0,%pi)$
(%i3) S2:trigsolve(sin(7*x),0,%pi)$
(%i4) S3:trigsolve(sin(x),0,%pi)$
(%i5) S4:trigsolve(cos(2*x),0,%pi)$

(%i6) union(S1,S2)$ setdifference(%,S3)$ setdifference(%,S4);
       %pi  %pi  2 %pi  5 %pi  3 %pi  4 %pi  7 %pi  5 %pi
(%o8) {---, ---, -----, -----, -----, -----, -----, -----, 
       12    7     7     12      7      7     12      7
                                                   6 %pi  11 %pi
                                                   -----, ------}
                                                     7      12


(%i9) S:listify(%);
       %pi  %pi  2 %pi  5 %pi  3 %pi  4 %pi  7 %pi  5 %pi
(%o9) [---, ---, -----, -----, -----, -----, -----, -----, 
       12    7     7     12      7      7     12      7
                                                   6 %pi  11 %pi
                                                   -----, ------]
                                                     7      12


(%i10) length(S);
(%o10)                         10


(%i11) float(S), numer;
(%o11) [0.2617993877991494, 0.4487989505128276, 
0.8975979010256552, 1.3089969389957472, 1.3463968515384828, 
1.7951958020513104, 1.8325957145940461, 2.243994752564138, 
2.6927937030769655, 2.8797932657906435]
```

Answer: 
$x = a + 2\pi k,$
where $a$ any from $S$, $k$ any integer.

### Function: trigvalue (x)

The function trigvalue compute values of 
$\sin {m\pi\over n},$
$\cos {m\pi\over n},$
$\tan {m\pi\over n},$
and 
$\cot {m\pi\over n}$
in radicals.


`trigvalue` is essentially an internal function.
Use function `trigeval` in preference.


`load("trigtools")` loads this function.

See also: `trigeval`.

