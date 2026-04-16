## NumberTheory

### Function: abs (z)

The `abs` function represents the mathematical absolute value function and
works for both numerical and symbolic values. If the argument, *z*, is a
real or complex number, `abs` returns the absolute value of *z*. If
possible, symbolic expressions using the absolute value function are
also simplified.


Maxima can differentiate, integrate and calculate limits for expressions
containing `abs`. The `abs_integrate` package further extends
Maxima’s ability to calculate integrals involving the abs function. See
(%i12) in the examples below.


When applied to a list or matrix, `abs` automatically distributes over
the terms. Similarly, it distributes over both sides of an
equation. To alter this behaviour, see the variable `distribute_005fover`.


See also `cabs`.


Examples:


Calculation of `abs` for real and complex numbers, including numerical
constants and various infinities. The first example shows how `abs`
distributes over the elements of a list.









```maxima
maxima

(%i1) abs([-4, 0, 1, 1+%i]);
(%o1)                  [4, 0, 1, sqrt(2)]


(%i2) abs((1+%i)*(1-%i));
(%o2)                           2


(%i3) abs(%e+%i);
                                 2
(%o3)                     sqrt(%e  + 1)


(%i4) abs([inf, infinity, minf]);
(%o4)                    [inf, inf, inf]
```


Simplification of expressions containing `abs`:









```maxima
maxima

(%i1) abs(x^2);
                                2
(%o1)                          x


(%i2) abs(x^3);
                             2
(%o2)                       x  abs(x)


(%i3) abs(abs(x));
(%o3)                        abs(x)


(%i4) abs(conjugate(x));
(%o4)                        abs(x)
```


Integrating and differentiating with the `abs` function. Note that more
integrals involving the `abs` function can be performed, if the
`abs_integrate` package is loaded. The last example shows the Laplace
transform of `abs`: see `laplace`.












```maxima
maxima

(%i1) diff(x*abs(x),x),expand;
(%o1)                       2 abs(x)


(%i2) integrate(abs(x),x);
                            x abs(x)
(%o2)                       --------
                               2


(%i3) integrate(x*abs(x),x);
                          /
                          |
(%o3)                     | x abs(x) dx
                          |
                          /

(%i4) load("abs_integrate")$

(%i5) integrate(x*abs(x),x);
                           3
                          x  signum(x)
(%o5)                     ------------
                               3


(%i6) integrate(abs(x),x,-2,%pi);
                               2
                            %pi
(%o6)                       ---- + 2
                             2


(%i7) laplace(abs(x),x,s);
                               1
(%o7)                          --
                                2
                               s
```

See also: `distribute_over`, `cabs`, `laplace`.

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

### Function: bernpoly (x, n)

Returns the *n*’th Bernoulli polynomial in the
variable *x*.

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

### Function: bfloat (expr)

`bfloat` replaces integers, rationals, floating point numbers, and some symbolic constants
in *expr* with bigfloat (variable-precision floating point) numbers.


The constants `%e`, `%gamma`, `%phi`, and `%pi`
are replaced by a numerical approximation.
However, `%e` in `%e^x` is not replaced by a numeric value
unless `bfloat(x)` is a number.


`bfloat` also causes numerical evaluation of some built-in functions,
namely trigonometric functions, exponential functions, `abs`, and `log`.



The number of significant digits in the resulting bigfloats is specified by the
global variable `fpprec`.
Bigfloats already present in *expr* are replaced with values which have
precision specified by the current value of `fpprec`.


When `float2bf` is `false`, a warning message is printed when
a floating point number is replaced by a bigfloat number with less precision.


Examples:


`bfloat` replaces integers, rationals, floating point numbers, and some symbolic constants
in *expr* with bigfloat numbers.








```maxima
(%i1) bfloat([123, 17/29, 1.75]);
(%o1)        [1.23b2, 5.862068965517241b-1, 1.75b0]
(%i2) bfloat([%e, %gamma, %phi, %pi]);
(%o2) [2.718281828459045b0, 5.772156649015329b-1, 
                        1.618033988749895b0, 3.141592653589793b0]
(%i3) bfloat((f(123) + g(h(17/29)))/(x + %gamma));
         1.0b0 (g(h(5.862068965517241b-1)) + f(1.23b2))
(%o3)    ----------------------------------------------
                    x + 5.772156649015329b-1
```


`bfloat` also causes numerical evaluation of some built-in functions.









```maxima
(%i1) bfloat(sin(17/29));
(%o1)                 5.532051841609784b-1
(%i2) bfloat(exp(%pi));
(%o2)                  2.314069263277927b1
(%i3) bfloat(abs(-%gamma));
(%o3)                 5.772156649015329b-1
(%i4) bfloat(log(%phi));
(%o4)                 4.812118250596035b-1
```

See also: `fpprec`, `float2bf`.

### Function: bfloatp (expr)

Returns `true` if *expr* is a bigfloat number, otherwise `false`.

### Variable: bftorat

Default value: `false`


`bftorat` controls the conversion of bfloats to rational numbers.  When
`bftorat` is `false`, `ratepsilon` will be used to control the
conversion (this results in relatively small rational numbers).  When
`bftorat` is `true`, the rational number generated will accurately
represent the bfloat.


Note: `bftorat` has no effect on the transformation to rational numbers
with the function `rationalize`.


Example:








```maxima
(%i1) ratepsilon:1e-4;
(%o1)                         1.0e-4
(%i2) rat(bfloat(11111/111111)), bftorat:false;
`rat' replaced 9.99990999991B-2 by 1/10 = 1.0B-1
                               1
(%o2)/R/                       --
                               10
(%i3) rat(bfloat(11111/111111)), bftorat:true;
`rat' replaced 9.99990999991B-2 by 11111/111111 = 9.99990999991B-2
                             11111
(%o3)/R/                     ------
                             111111
```

See also: `ratepsilon`, `rationalize`.

### Variable: bftrunc

Default value: `true`


`bftrunc` causes trailing zeroes in non-zero bigfloat numbers not to be
displayed.  Thus, if `bftrunc` is `false`, `bfloat (1)`
displays as `1.000000000000000B0`.  Otherwise, this is displayed as
`1.0B0`.

### Function: bfzeta (s, n)

Returns the Riemann zeta function for the argument *s*.
The return value is a big float (bfloat);
*n* is the number of digits in the return value.

### Function: bigfloat_bits ()

Returns the number of bits of precision in a bigfloat number.  This
value depends, of course, on the value of `fpprec`. 









```maxima
(%i1) fpprec:16;
(%o1)                                 16
(%i2) bigfloat_bits();
(%o2)                                 56
(%i3) fpprec:32;
(%o3)                                 32
(%i4) bigfloat_bits();
(%o4)                                 109
```

See also: `fpprec`.

### Function: bigfloat_eps ()

Returns the smallest bigfloat value, `eps`, such that
`1+eps` is not equal to 1.  The value depends on `fpprec`,
of course.









```maxima
(%i1) fpprec:16;
(%o1)                                 16
(%i2) bigfloat_eps();
(%o2)                        1.387778780781446b-17
(%i3) fpprec:32;
(%o3)                                 32
(%i4) bigfloat_eps();
(%o4)                1.5407439555097886824447823540679b-33
```

See also: `fpprec`.

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

### Function: cabs (expr)

Calculates the absolute value of an expression representing a complex
number.  Unlike the function `abs`, the `cabs` function always
decomposes its argument into a real and an imaginary part.  If `x` and
`y` represent real variables or expressions, the `cabs` function
calculates the absolute value of `x + %i*y` as











```maxima
maxima

(%i1) cabs (1);
(%o1)                           1


(%i2) cabs (1 + %i);
(%o2)                        sqrt(2)


(%i3) cabs (exp (%i));
(%o3)                           1


(%i4) cabs (exp (%pi * %i));
(%o4)                           1


(%i5) cabs (exp (3/2 * %pi * %i));
(%o5)                           1


(%i6) cabs (17 * exp (2 * %i));
(%o6)                          17
```


If `cabs` returns a noun form this most commonly is caused by
some properties of the variables involved not being known:










```maxima
maxima

(%i1) cabs (a+%i*b);
                                2    2
(%o1)                     sqrt(b  + a )


(%i2) declare(a,real,b,real);
(%o2)                         done


(%i3) cabs (a+%i*b);
                                2    2
(%o3)                     sqrt(b  + a )


(%i4) assume(a>0,b>0);
(%o4)                    [a > 0, b > 0]


(%i5) cabs (a+%i*b);
                                2    2
(%o5)                     sqrt(b  + a )
```


The `cabs` function can use known properties like symmetry properties of
complex functions to help it calculate the absolute value of an expression.  If
such identities exist, they can be advertised to `cabs` using function
properties.  The symmetries that `cabs` understands are: mirror symmetry,
conjugate function and complex characteristic.


`cabs` is a verb function and is not suitable for symbolic
calculations.  For such calculations (including integration,
differentiation and taking limits of expressions containing absolute
values), use `abs`.


The result of `cabs` can include the absolute value function,
`abs`, and the arc tangent, `atan2`.


When applied to a list or matrix, `cabs` automatically distributes over
the terms.  Similarly, it distributes over both sides of an equation.


For further ways to compute with complex numbers, see the functions
`rectform`, `realpart`, `imagpart`,
`carg`, `conjugate` and `polarform`.


Examples:


Examples with `sqrt` and `sin`.







```maxima
maxima

(%i1) cabs(sqrt(1+%i*x));
                             2     1/4
(%o1)                      (x  + 1)


(%i2) cabs(sin(x+%i*y));
                    2        2         2        2
(%o2)       sqrt(cos (x) sinh (y) + sin (x) cosh (y))
```


The error function, `erf`, has mirror symmetry, which is used here in
the calculation of the absolute value with a complex argument:






```maxima
maxima

(%i1) cabs(erf(x+%i*y));
                                          2
           (erf(%i y + x) - erf(%i y - x))
(%o1) sqrt(--------------------------------
                          4
                                                               2
                              (- erf(%i y + x) - erf(%i y - x))
                            - ----------------------------------)
                                              4
```


Maxima knows complex identities for the Bessel functions, which allow
it to compute the absolute value for complex arguments.  Here is an
example for `bessel_005fj`.






```maxima
maxima

(%i1) cabs(bessel_j(1,%i));
(%o1)                    bessel_i(1, 1)
```

See also: `abs`, `atan2`, `rectform`, `realpart`, `imagpart`, `carg`, `conjugate`, `polarform`, `sqrt`, `sin`, `erf`, `bessel_j`.

### Function: carg (z)

Returns the complex argument of *z*.  The complex argument is an angle
`theta` in `(-%pi, %pi]` such that `r exp (theta %i) = z`
where `r` is the magnitude of *z*.


`carg` is a computational function, not a simplifying function.



See also `abs` (complex magnitude), `polarform`,
`rectform`, `realpart`, and `imagpart`.


Examples:











```maxima
maxima

(%i1) carg (1);
(%o1)                           0


(%i2) carg (1 + %i);
                               %pi
(%o2)                          ---
                                4


(%i3) carg (exp (%i));
                               sin(1)
(%o3)                     atan(------)
                               cos(1)


(%i4) carg (exp (%pi * %i));
(%o4)                          %pi


(%i5) carg (exp (3/2 * %pi * %i));
                                %pi
(%o5)                         - ---
                                 2


(%i6) carg (17 * exp (2 * %i));
                            sin(2)
(%o6)                  atan(------) + %pi
                            cos(2)
```


If `carg` returns a noun form this most commonly is caused by
some properties of the variables involved not being known:










```maxima
maxima

(%i1) carg (a+%i*b);
(%o1)                      atan2(b, a)


(%i2) declare(a,real,b,real);
(%o2)                         done


(%i3) carg (a+%i*b);
(%o3)                      atan2(b, a)


(%i4) assume(a>0,b>0);
(%o4)                    [a > 0, b > 0]


(%i5) carg (a+%i*b);
                                  b
(%o5)                        atan(-)
                                  a
```

See also: `abs`, `polarform`, `rectform`, `realpart`, `imagpart`.

### Function: ceiling (x)

When *x* is a real number, return the least integer that 
is greater than or equal to *x*.


If *x* is a constant expression (`10 * %pi`, for example), 
`ceiling` evaluates *x* using big floating point numbers, and 
applies `ceiling` to the resulting big float.  Because `ceiling` uses
floating point evaluation, it’s possible, although unlikely, that `ceiling`
could return an erroneous value for constant inputs.  To guard against errors,
the floating point evaluation is done using three values for `fpprec`.


For non-constant inputs, `ceiling` tries to return a simplified value.
Here are examples of the simplifications that `ceiling` knows about:












```maxima
maxima

(%i1) ceiling (ceiling (x));
(%o1)                      ceiling(x)


(%i2) ceiling (floor (x));
(%o2)                       floor(x)

(%i3) declare (n, integer)$

(%i4) [ceiling (n), ceiling (abs (n)), ceiling (max (n, 6))];
(%o4)                [n, abs(n), max(6, n)]

(%i5) assume (x > 0, x < 1)$

(%i6) ceiling (x);
(%o6)                           1


(%i7) tex (ceiling (a));
$$\left \lceil a \right \rceil$$
(%o7)                         false
```


The `ceiling` function distributes over lists, matrices and equations.
See `distribute_005fover`.


Finally, for all inputs that are manifestly complex, `ceiling` returns 
a noun form.


If the range of a function is a subset of the integers, it can be declared to
be `integervalued`.  Both the `ceiling` and `floor` functions
can use this information; for example:








```maxima
maxima
(%i1) declare (f, integervalued)$

(%i2) floor (f(x));
(%o2)                         f(x)


(%i3) ceiling (f(x) - 1);
(%o3)                       f(x) - 1
```


Example use:


















```maxima
maxima

(%i1) unitfrac(r) := block([uf : [], q],
    if not(ratnump(r)) then
       error("unitfrac: argument must be a rational number"),
    while r # 0 do (
        uf : cons(q : 1/ceiling(1/r), uf),
        r : r - q),
    reverse(uf));
(%o1) unitfrac(r) := block([uf : [], q], 
if not ratnump(r) then error("unitfrac: argument must be a rational number"
                                     1
), while r # 0 do (uf : cons(q : ----------, uf), r : r - q), 
                                         1
                                 ceiling(-)
                                         r
reverse(uf))


(%i2) unitfrac (9/10);
                            1  1  1
(%o2)                      [-, -, --]
                            2  3  15


(%i3) apply ("+", %);
                               9
(%o3)                          --
                               10


(%i4) unitfrac (-9/10);
                                  1
(%o4)                       [- 1, --]
                                  10


(%i5) apply ("+", %);
                                9
(%o5)                         - --
                                10


(%i6) unitfrac (36/37);
                        1  1  1  1    1
(%o6)                  [-, -, -, --, ----]
                        2  3  8  69  6808


(%i7) apply ("+", %);
                               36
(%o7)                          --
                               37
```

See also: `fpprec`, `distribute_over`, `floor`.

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

### Function: conjugate (x)

Returns the complex conjugate of *x*.










```maxima
maxima

(%i1) declare ([aa, bb], real, cc, complex, ii, imaginary);
(%o1)                         done


(%i2) conjugate (aa + bb*%i);
(%o2)                      aa - %i bb


(%i3) conjugate (cc);
(%o3)                     conjugate(cc)


(%i4) conjugate (ii);
(%o4)                         - ii


(%i5) conjugate (xx + yy);
(%o5)                        yy + xx
```

### Function: decode_float (f)

`decode_float` takes a float *f* and returns a list of three
values that characterizes *f*, which must be either a `float`
or `bfloat`.  The first value has the same type as *f*, but
is a number in the range `[1, 2)`.  The second value is an
exponent.  The third value is a float of the same type as *f* and
has the value of 1 if *f* is greater than or equal to 0;
otherwise, -1.


If the returned list is `[mantissa, expo, sign]`, then
`scale_float(mantissa, exp)*sign` is identical to *f*.



```maxima
(%i1) decode_float(4e0);
(%o1)                            [1.0, 2, 1.0]
(%i2) decode_float(4b0);
(%o2)                          [1.0b0, 2, 1.0b0]
(%i3) decode_float(%pi);

decode_float is only defined for floats and bfloats: %pi
 -- an error. To debug this try: debugmode(true);
(%i4) decode_float(float(%pi));
(%o4)                     [1.570796326794897, 1, 1.0]
(%i5) decode_float(1.1e-5);
(%o5)                        [1.441792, - 17, 1.0]
(%i6) %[1]*2^%[2];
(%o6)                               1.1e-5
```


This is a relatively simple interface to Common Lisp
[http://www.lispworks.com/documentation/HyperSpec/Body/f_dec_fl.htmdecode_float]().  However we return a signficand in the range
`[1,2)` instead of `[0.5, 1)`.  The former matches
IEEE-754.  Of course, this is extended to support bfloats.

### Function: divsum (divsum, n, k, divsum, n)

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

### Function: entier (x)

Returns the largest integer less than or equal to *x* where *x* is
numeric.  `fix` (as in `fixnum`) is a synonym for this, so
`fix(x)` is precisely the same.

See also: `fix`.

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

### Function: evenp (expr)

Returns `true` if *expr* is a literal even integer, otherwise
`false`.


`evenp` returns `false` if *expr* is a symbol, even if *expr*
is declared `even`.

### Variable: factors_only

Default value: `false`


Controls the value returned by `ifactors`. The default `false` 
causes `ifactors` to provide information about multiplicities of the 
computed prime factors. If `factors_only` is set to `true`, 
`ifactors` returns nothing more than a list of prime factors.


Example: See `ifactors`.

See also: `ifactors`.

### Function: fib (n)

Returns the *n*’th Fibonacci number.
`fib(0)` is equal to 0 and `fib(1)` equal to 1, and 
`fib (-n)` equal to `(-1)^(n + 1) * fib(n)`.






```maxima
maxima

(%i1) map (fib, [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]);
(%o1)     [- 3, 2, - 1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
```

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

### Function: fix (x)

A synonym for `entier (x)`.

### Function: float (expr)

Converts integers, rational numbers and bigfloats in *expr* to floating
point numbers.  It is also an `evflag`, `float` causes
non-integral rational numbers and bigfloat numbers to be converted to floating
point.

See also: `evflag`.

### Variable: float2bf

Default value: `true`

 

When `float2bf` is `false`, a warning message is printed when
a floating point number is replaced by a bigfloat number with less precision.

See also: `float2bf`.

### Function: float_bits ()

Returns the number of bits of precision of a floating-point number.

### Function: float_eps ()

Returns the smallest floating-point value, `eps`, such that
`1+eps` is not equal to 1.

### Function: float_infinity_p (x)

Returns `true` if *x* is floating point positive infinity or floating point negative infinity,
and returns `false` for all other arguments;
arguments which are not numbers are allowed,
and `float_infinity_p` returns `false` for all such arguments.


Positive and negative floating point infinity may be distinguished by `sign`,
which returns `pos` for positive infinity and `neg` for negative infinity.


`float_infinity_p` is defined whether or not the Lisp implementation supports float infinity.
When float infinity does not exist in the Lisp implementation’s number system,
`float_infinity_p` returns `false` for all arguments.


A Lisp implementation may support more than one precision of floating point numbers.
`float_infinity_p` only recognizes double precision floating point infinity,
and not any other precision.

### Function: float_nan_p (x)

Returns `true` if *x* is a floating point not-a-number (NaN) value,
and returns `false` for all other arguments;
arguments which are not numbers are allowed,
and `float_nan_p` returns `false` for all such arguments.


`float_nan_p` is defined whether or not the Lisp implementation supports floating point not-a-number values.
When floating point not-a-number does not exist in the Lisp implementation’s number system,
`float_nan_p` returns `false` for all arguments.


A Lisp implementation may support more than one precision of floating point numbers.
`float_nan_p` only recognizes double precision floating point not-a-number,
and not any other precision.

### Function: float_precision (f)

Returns the number of bits of precision of a floating-point number,
which can be either a float or bigfloat.  This is basically the number
of bits used to represent the mantissa of a floating-point number.
For floats, this is 53 (for IEEE double-floats), but can be less when
denormal numbers occur.  For bigfloats, this is equal to
`fpprec`, when converted from digits to bits.

See also: `fpprec`.

### Function: float_sign (f)

Returns the sign of *f*.  It is $+1$ or $-1$ of the same
type as *f*.  It is an error if *f* is not a float or
bigfloat.  Note that some lisps do not support signed zeros for
floating-point numbers.  Bigfloats do not support signed zeroes.  The
examples below assume signed zeroes are supported.


```maxima
(%i1) float_sign(1.0);
(%o1)                                 1.0
(%i2) float_sign(-5.0);
(%o2)                                - 1.0
(%i3) float_sign(-0.0);
(%o3)                                - 1.0
(%i4) float_sign(1b0);
(%o4)                                1.0b0
(%i5) float_sign(-5b0);
(%o5)                               - 1.0b0
(%o6) float_sign(-0b0);
(%o6)                                1.0b0
(%i7) float_sign(%pi);

float_sign is only defined for floats and bfloats: %pi
 -- an error. To debug this try: debugmode(true);
```

### Function: floatnump (expr)

Returns `true` if *expr* is a floating point number, otherwise
`false`.

### Function: floor (x)

When *x* is a real number, return the largest integer that is less than or
equal to *x*.


If *x* is a constant expression (`10 * %pi`, for example), `floor`
evaluates *x* using big floating point numbers, and applies `floor` to
the resulting big float. Because `floor` uses floating point evaluation,
it’s possible, although unlikely, that `floor` could return an erroneous
value for constant inputs.  To guard against errors, the floating point
evaluation is done using three values for `fpprec`.


For non-constant inputs, `floor` tries to return a simplified value.  Here
are examples of the simplifications that `floor` knows about:












```maxima
maxima

(%i1) floor (ceiling (x));
(%o1)                      ceiling(x)


(%i2) floor (floor (x));
(%o2)                       floor(x)

(%i3) declare (n, integer)$

(%i4) [floor (n), floor (abs (n)), floor (min (n, 6))];
(%o4)                [n, abs(n), min(6, n)]

(%i5) assume (x > 0, x < 1)$

(%i6) floor (x);
(%o6)                           0


(%i7) tex (floor (a));
$$\left \lfloor a \right \rfloor$$
(%o7)                         false
```


The `floor` function distributes over lists, matrices and equations.
See `distribute_005fover`.


Finally, for all inputs that are manifestly complex, `floor` returns 
a noun form.


If the range of a function is a subset of the integers, it can be declared to
be `integervalued`.  Both the `ceiling` and `floor` functions
can use this information; for example:








```maxima
maxima
(%i1) declare (f, integervalued)$

(%i2) floor (f(x));
(%o2)                         f(x)


(%i3) ceiling (f(x) - 1);
(%o3)                       f(x) - 1
```

See also: `fpprec`, `distribute_over`, `ceiling`.

### Variable: fpprec

Default value: 16


`fpprec` is the number of significant digits for arithmetic on bigfloat
numbers.  `fpprec` does not affect computations on ordinary floating point
numbers.


See also `bfloat` and `fpprintprec`.

See also: `bfloat`, `fpprintprec`.

### Variable: fpprintprec

Default value: 0


`fpprintprec` is the number of digits to print when printing an ordinary
float or bigfloat number.


For ordinary floating point numbers,
when `fpprintprec` has a value between 2 and 16 (inclusive),
the number of digits printed is equal to `fpprintprec`.
Otherwise, `fpprintprec` is 0, or greater than 16,
and the number is printed "readably":
that is, it is printed with sufficient digits to exactly reconstruct the number on input.


For bigfloat numbers,
when `fpprintprec` has a value between 2 and `fpprec` (inclusive),
the number of digits printed is equal to `fpprintprec`.
Otherwise, `fpprintprec` is 0, or greater than `fpprec`,
and the number of digits printed is equal to `fpprec`.


For both ordinary floats and bigfloats,
trailing zero digits are suppressed.
The actual number of digits printed is less than `fpprintprec`
if there are trailing zero digits.


`fpprintprec` cannot be 1.

### Function: hstep (x)

The Heaviside unit step function, equal to 0 if *x* is negative,
equal to 1 if *x* is positive and equal to 1/2 if *x* is equal
to zero.


If you want a unit step function that takes on the value of 0 at *x*
equal to zero, use `unit_005fstep`.

See also: `unit_step`.

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

### Function: imagpart (expr)

Returns the imaginary part of the expression *expr*.


`imagpart` is a computational function, not a simplifying function.




See also `abs`, `carg`, `polarform`,
`rectform`, and `realpart`.


Example:









```maxima
maxima

(%i1) imagpart (a+b*%i);
(%o1)                           b


(%i2) imagpart (1+sqrt(2)*%i);
(%o2)                        sqrt(2)


(%i3) imagpart (1);
(%o3)                           0


(%i4) imagpart (sqrt(2)*%i);
(%o4)                        sqrt(2)
```

See also: `abs`, `carg`, `polarform`, `rectform`, `realpart`.

### Function: inrt (x, n)

Returns the integer *n*’th root of the absolute value of *x*.







```maxima
maxima
(%i1) l: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]$

(%i2) map (lambda ([a], inrt (10^a, 3)), l);
(%o2) [2, 4, 10, 21, 46, 100, 215, 464, 1000, 2154, 4641, 10000]
```

### Function: integer_decode_float (f)

`integer_decode_float` takes a float *f* and returns a list of three
values that characterizes *f*, which must be either a `float`
or `bfloat`.  The first value is an integer.  The second value is an
exponent.  The third value is 1 if *f* is positive or zero;
otherwise, -1.


If the returned list is `[mantissa, expo, sign]`, then
`scale_float(fl(mantissa), expo)*sign` is identical to *f*.
Here, `fl` is either `float` or `bfloat` depending on
whether *f* is a `float` or a `bfloat`.



```maxima
(%i1) integer_decode_float(4.0);
(%o1)                     [4503599627370496, - 50, 1]
(%i2) integer_decode_float(4b0);
(%o2)                    [36028797018963968, - 53, 1]
(%i3) scale_float(float(%o1[1]), %o1[2]);
(%o3)                                 4.0
(%i4) scale_float(bfloat(%o2[1]), %o2[2]);
(%o4)                                4.0b0
(%i5) integer_decode_float(4);

decode_float is only defined for floats and bfloats: 4
 -- an error. To debug this try: debugmode(true);
(%i6) integer_decode_float(1e-7);
(%o6)                     [7555786372591432, - 76, 1]
(%i7) integer_decode_float(1b-7);
(%o7)                    [60446290980731459, - 79, 1]
(%i8) scale_float(float(%o6[1]), %o6[2]);
(%o8)                               1.0e-7
```


For lisps that support denormal numbers, we have the following results.


```maxima
(%i1) integer_decode_float(least_positive_float);
(%o1)                           [1, - 1074, 1]
(%i2) integer_decode_float(100*least_positive_float);
(%o2)                          [100, - 1074, 1]
(%i3) integer_decode_float(least_positive_normalized_float);
(%o3)                    [4503599627370496, - 1074, 1]
```

The number of bits in the integer part decreases as the denormal
number decreases.  Bfloat numbers do not have denormals because the
exponent is not bounded.


This is a relatively simple interface to Common Lisp
[http://www.lispworks.com/documentation/HyperSpec/Body/f_dec_fl.htminteger_decode_float]().  However, the integer part can vary depending
on the Lisp implementation; we return the same value, independent of
the Lisp implementation.  Of course, this is extended to support bfloats.

### Function: integerp (expr)

Returns `true` if *expr* is a literal numeric integer, otherwise
`false`.


`integerp` returns `false` if *expr* is a symbol, even if *expr*
is declared `integer`.


Examples:














```maxima
(%i1) integerp (0);
(%o1)                         true
(%i2) integerp (1);
(%o2)                         true
(%i3) integerp (-17);
(%o3)                         true
(%i4) integerp (0.0);
(%o4)                         false
(%i5) integerp (1.0);
(%o5)                         false
(%i6) integerp (%pi);
(%o6)                         false
(%i7) integerp (n);
(%o7)                         false
(%i8) declare (n, integer);
(%o8)                         done
(%i9) integerp (n);
(%o9)                         false
```

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

### Function: is_power_of_two (n)

`is_power_to_two` returns `true` if *n* is a power of
two and `false` otherwise.  *n* may be an integer, a
rational, a float, or a big float.


Some examples:


```maxima
(%i1) is_power_of_two(0);
(%o1)                                false
(%i2) is_power_of_two(4);
(%o2)                                true
(%i3) is_power_of_two(355/113);
(%o3)                                false
(%i4) is_power_of_two(1/32);
(%o4)                                true
(%i5) is_power_of_two(1048576);
(%o5)                                true
(%i6) is_power_of_two(1048575);
(%o6)                                false
(%i7) is_power_of_two(0.0);
(%o7)                                false
(%i8) is_power_of_two(1048576.0);
(%o8)                                true
(%i9) is_power_of_two(1048575.0);
(%o9)                                false
(%i10) is_power_of_two(1/256.0);
(%o10)                               true
(%i11) is_power_of_two(0b0);
(%o11)                               false
(%i12) is_power_of_two(1048576b0);
(%o12)                               true
(%i13) is_power_of_two(1048575b0);
(%o13)                               false
(%i14) is_power_of_two(1/256b0);
(%o14)                               true
```

### Function: isqrt (x)

Returns the "integer square root" of the absolute value of *x*, which is an
integer.

### Function: jacobi (p, q)

Returns the Jacobi symbol of *p* and *q*.







```maxima
maxima
(%i1) l: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]$

(%i2) map (lambda ([a], jacobi (a, 9)), l);
(%o2)         [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
```

### Function: lcm (expr_1, ..., expr_n)

Returns the least common multiple of its arguments.
The arguments may be general expressions as well as integers.


`load ("functs")` loads this function.

### Function: lmax (L)

When *L* is a list or a set, return `apply ('max, args (L))`.
When *L* is not a list or a set, signal an error.
See also `lmin` and `max`.

See also: `lmin`, `max`.

### Function: lmin (L)

When *L* is a list or a set, return `apply ('min, args (L))`.
When *L* is not a list or a set, signal an error.
See also `lmax` and `min`.

See also: `lmax`, `min`.

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

### Variable: m1pbranch

Default value: `false`


`m1pbranch` is the principal branch for `-1` to a power.
Quantities such as `(-1)^(1/3)` (that is, an "odd" rational exponent) and 
`(-1)^(1/4)` (that is, an "even" rational exponent) are handled as follows:




```maxima
domain:real
                            
(-1)^(1/3):      -1         
(-1)^(1/4):   (-1)^(1/4)   

             domain:complex              
m1pbranch:false          m1pbranch:true
(-1)^(1/3)               1/2+%i*sqrt(3)/2
(-1)^(1/4)              sqrt(2)/2+%i*sqrt(2)/2
```

### Function: make_random_state (make_random_state, n, make_random_state, s, make_random_state, true, make_random_state, false)

A random state object represents the state of the random number generator.
The state comprises 627 32-bit words.


`make_random_state (n)` returns a new random state object
created from an integer seed value equal to *n* modulo 2^32.
*n* may be negative.






`make_random_state (s)` returns a copy of the random state *s*.


`make_random_state (true)` returns a new random state object,
using the current computer clock time as the seed.


`make_random_state (false)` returns a copy of the current state
of the random number generator.

### Function: max (x_1, ..., x_n)

Return a simplified value for the numerical maximum of the expressions *x_1* 
through *x_n*. For an empty argument list, `max` yields `minf`.


The option variable `maxmin_effort` controls which simplification methods are 
applied. Using the default value of *twelve* for `maxmin_effort`, 
`max` uses *all* available simplification methods. To to inhibit all 
simplifications, set `maxmin_effort` to zero.


When `maxmin_effort` is one or more, for an explicit list of real numbers, 
`max` returns a number. 


Unless `max` needs to simplify a lengthy list of expressions, we suggest using 
the default value of `maxmin_effort`. Setting `maxmin_effort` to zero 
(no simplifications), will cause problems for some Maxima functions; accordingly, 
generally `maxmin_effort` should be nonzero.


See also `min`, `lmax`., and `lmin`..


**Examples:**


In the first example, setting `maxmin_effort` to zero suppresses simplifications.


```maxima
(%i1) block([maxmin_effort : 0], max(1,2,x,x, max(a,b)));
(%o1) max(1,2,max(a,b),x,x)

(%i2) block([maxmin_effort : 1], max(1,2,x,x, max(a,b)));
(%o2) max(2,a,b,x)
```


When `maxmin_effort` is two or more, `max` compares pairs of members:


```maxima
(%i1) block([maxmin_effort : 1], max(x,x+1,x+3));
(%o1) max(x,x+1,x+3)

(%i2) block([maxmin_effort : 2], max(x,x+1,x+3));
(%o2) x+3
```


Finally, when `maxmin_effort` is three or more, `max` compares triples 
members and excludes those that are in between; for example


```maxima
(%i1) block([maxmin_effort : 4], max(x, 2*x, 3*x, 4*x));
(%o1) max(x,4*x)
```

See also: `min`, `lmax`, `lmin`.

### Function: min (x_1, ..., x_n)

Return a simplified value for the numerical minimum of the expressions *x_1* 
through *x_n*. For an empty argument list, `minf` yields `inf`.


The option variable `maxmin_effort` controls which simplification methods are 
applied. Using the default value of *twelve* for `maxmin_effort`, 
`max` uses *all* available simplification methods. To to inhibit all 
simplifications, set `maxmin_effort` to zero.


When `maxmin_effort` is one or more, for an explicit list of real numbers, 
`min` returns a number. 


Unless `min` needs to simplify a lengthy list of expressions, we suggest using 
the default value of `maxmin_effort`. Setting `maxmin_effort` to zero 
(no simplifications), will cause problems for some Maxima functions; accordingly, 
generally `maxmin_effort` should be nonzero.


See also `max`, `lmax`., and `lmin`..


**Examples:**


In the first example, setting `maxmin_effort` to zero suppresses simplifications.


```maxima
(%i1) block([maxmin_effort : 0], min(1,2,x,x, min(a,b)));
(%o1) min(1,2,a,b,x,x)

(%i2) block([maxmin_effort : 1], min(1,2,x,x, min(a,b)));
(%o2) min(1,a,b,x)
```


When `maxmin_effort` is two or more, `min` compares pairs of members:


```maxima
(%i1) block([maxmin_effort : 1], min(x,x+1,x+3));
(%o1) min(x,x+1,x+3)

(%i2) block([maxmin_effort : 2], min(x,x+1,x+3));
(%o2) x
```


Finally, when `maxmin_effort` is three or more, `min` compares triples 
members and excludes those that are in between; for example


```maxima
(%i1) block([maxmin_effort : 4], min(x, 2*x, 3*x, 4*x));
(%o1) max(x,4*x)
```

See also: `max`, `lmax`, `lmin`.

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

### Function: next_prime (n)

Returns the smallest prime bigger than *n*.






```maxima
maxima

(%i1) next_prime(27);
(%o1)                          29
```

### Function: nonnegintegerp (n)

Return `true` if and only if `n >= 0` and *n* is an integer.

### Function: numberp (expr)

Returns `true` if *expr* is a literal integer, rational number, 
floating point number, or bigfloat, otherwise `false`.


`numberp` returns `false` if *expr* is a symbol, even if *expr*
is a symbolic number such as `%pi` or `%i`, or declared to be
`even`, `odd`, `integer`, `rational`, `irrational`,
`real`, `imaginary`, or `complex`.


Examples:













```maxima
(%i1) numberp (42);
(%o1)                         true
(%i2) numberp (-13/19);
(%o2)                         true
(%i3) numberp (3.14159);
(%o3)                         true
(%i4) numberp (-1729b-4);
(%o4)                         true
(%i5) map (numberp, [%e, %pi, %i, %phi, inf, minf]);
(%o5)      [false, false, false, false, false, false]
(%i6) declare (a, even, b, odd, c, integer, d, rational,
     e, irrational, f, real, g, imaginary, h, complex);
(%o6)                         done
(%i7) map (numberp, [a, b, c, d, e, f, g, h]);
(%o7) [false, false, false, false, false, false, false, false]
```

### Variable: numer

`numer` causes some mathematical functions (including exponentiation)
with numerical arguments to be evaluated in floating point.  It causes
variables in `expr` which have been given numerals to be replaced by
their values.  It also sets the `float` switch on.


See also `_0025enumer`.


Examples:







```maxima
(%i1) [sqrt(2), sin(1), 1/(1+sqrt(3))];
                                        1
(%o1)            [sqrt(2), sin(1), -----------]
                                   sqrt(3) + 1


(%i2) [sqrt(2), sin(1), 1/(1+sqrt(3))],numer;
(%o2) [1.414213562373095, 0.8414709848078965, 0.3660254037844387]
```

See also: `float`, `%enumer`.

### Variable: numer_pbranch

Default value: `false`


The option variable `numer_pbranch` controls the numerical evaluation of 
the power of a negative integer, rational, or floating point number.  When
`numer_pbranch` is `true` and the exponent is a floating point number
or the option variable `numer` is `true` too, Maxima evaluates
the numerical result using the principal branch.  Otherwise a simplified, but
not an evaluated result is returned.


Examples:










```maxima
(%i1) (-2)^0.75;
                                 0.75
(%o1)                       (- 2)


(%i2) (-2)^0.75,numer_pbranch:true;
(%o2)       1.189207115002721 %i - 1.189207115002721


(%i3) (-2)^(3/4);
                               3/4  3/4
(%o3)                     (- 1)    2


(%i4) (-2)^(3/4),numer;
                                          0.75
(%o4)              1.681792830507429 (- 1)


(%i5) (-2)^(3/4),numer,numer_pbranch:true;
(%o5)       1.189207115002721 %i - 1.189207115002721
```

See also: `numer`.

### Function: numerval (x_1, expr_1, ..., var_n, expr_n)

Declares the variables `x_1`, ..., *x_n* to have
numeric values equal to `expr_1`, ..., `expr_n`.
The numeric value is evaluated and substituted for the variable
in any expressions in which the variable occurs if the `numer` flag is
`true`.  See also `ev`.


The expressions `expr_1`, ..., `expr_n` can be any expressions,
not necessarily numeric.

See also: `ev`.

### Function: oddp (expr)

Returns `true` if *expr* is a literal odd integer, otherwise
`false`.


`oddp` returns `false` if *expr* is a symbol, even if *expr*
is declared `odd`.

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

### Function: polarform (expr)

Returns an expression `r %e^(%i theta)` equivalent to *expr*,
such that `r` and `theta` are purely real.


Example:








```maxima
maxima

(%i1) polarform(a+b*%i);
                   %i atan2(b, a)       2    2
(%o1)            %e               sqrt(b  + a )


(%i2) polarform(1+%i);
                                  %i %pi
                                  ------
                                    4
(%o2)                   sqrt(2) %e


(%i3) polarform(1+2*%i);
                                %i atan(2)
(%o3)                 sqrt(5) %e
```

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

### Function: prev_prime (n)

Returns the greatest prime smaller than *n*.






```maxima
maxima

(%i1) prev_prime(27);
(%o1)                          23
```

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

### Variable: primep_number_of_tests

Default value: 25


Number of Miller-Rabin’s tests used in `primep`.

### Function: primes (start, end)

Returns the list of all primes from *start* to *end*.






```maxima
maxima

(%i1) primes(3, 7);
(%o1)                       [3, 5, 7]
```

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

### Function: random (x)

Returns a pseudorandom number.  If *x* is an integer,
`random (x)` returns an integer from 0 through `x - 1`
inclusive.  If *x* is a floating point number, `random (x)`
returns a nonnegative floating point number less than *x*.  `random`
complains with an error if *x* is neither an integer nor a float, or if
*x* is not positive.


The functions `make_random_state` and `set_random_state`
maintain the state of the random number generator.


The Maxima random number generator is an implementation of the Mersenne twister
MT 19937.


Examples:


















```maxima
maxima
(%i1) s1: make_random_state (654321)$

(%i2) set_random_state (s1);
(%o2)                         done


(%i3) random (1000);
(%o3)                          768


(%i4) random (9573684);
(%o4)                        7657880


(%i5) random (2^75);
(%o5)                11804491615036831636390

(%i6) s2: make_random_state (false)$

(%i7) random (1.0);
(%o7)                  0.2310127244107132


(%i8) random (10.0);
(%o8)                  4.3945536458708245


(%i9) random (100.0);
(%o9)                   32.28666704056853


(%i10) set_random_state (s2);
(%o10)                        done


(%i11) random (1.0);
(%o11)                 0.2310127244107132


(%i12) random (10.0);
(%o12)                 4.3945536458708245


(%i13) random (100.0);
(%o13)                  32.28666704056853
```

### Variable: ratepsilon

Default value: `2.0e-15`


`ratepsilon` is the tolerance used in the conversion
of floating point numbers to rational numbers, when the option variable
`bftorat` has the value `false`.  See `bftorat` for an example.

See also: `bftorat`.

### Function: rationalize (expr)

Convert all double floats and big floats in the Maxima expression *expr* to
their exact rational equivalents.  If you are not familiar with the binary
representation of floating point numbers, you might be surprised that
`rationalize (0.1)` does not equal 1/10.  This behavior isn’t special to
Maxima – the number 1/10 has a repeating, not a terminating, binary
representation.












```maxima
(%i1) rationalize (0.5);
                                1
(%o1)                           -
                                2


(%i2) rationalize (0.1);
                        3602879701896397
(%o2)                   -----------------
                        36028797018963968

(%i3) fpprec : 5$

(%i4) rationalize (0.1b0);
                             209715
(%o4)                        -------
                             2097152

(%i5) fpprec : 20$

(%i6) rationalize (0.1b0);
                     236118324143482260685
(%o6)                ----------------------
                     2361183241434822606848


(%i7) rationalize (sin (0.1*x + 5.6));
               3602879701896397 x   3152519739159347
(%o7)      sin(------------------ + ----------------)
               36028797018963968    562949953421312
```

### Function: ratnump (expr)

Returns `true` if *expr* is a literal integer or ratio of literal
integers, otherwise `false`.

### Function: realpart (expr)

Returns the real part of *expr*.  `realpart` and `imagpart` will
work on expressions involving trigonometric and hyperbolic functions,
as well as square root, logarithm, and exponentiation.


Example:









```maxima
maxima

(%i1) realpart (a+b*%i);
(%o1)                           a


(%i2) realpart (1+sqrt(2)*%i);
(%o2)                           1


(%i3) realpart (sqrt(2)*%i);
(%o3)                           0


(%i4) realpart (1);
(%o4)                           1
```

See also: `imagpart`.

### Function: rectform (expr)

Returns an expression `a + b %i` equivalent to *expr*,
such that *a* and *b* are purely real.


Example:








```maxima
maxima

(%i1) rectform(sqrt(2)*%e^(%i*%pi/4));
(%o1)                        %i + 1


(%i2) rectform(sqrt(b^2+a^2)*%e^(%i*atan2(b, a)));
(%o2)                       %i b + a


(%i3) rectform(sqrt(5)*%e^(%i*atan(2)));
(%o3)                       2 %i + 1
```

### Function: round (x)

When *x* is a real number, returns the closest integer to *x*.
Multiples of 1/2 are rounded to the nearest even integer.  Evaluation of
*x* is similar to `floor` and `ceiling`.


The `round` function distributes over lists, matrices and equations.
See `distribute_005fover`.

See also: `floor`, `ceiling`, `distribute_over`.

### Function: scale_float (f, n)

`scale_float` scales the float *f* by the value
`2^n`.  This is done carefully so that no round-off every
occurs.  If *f* is a float, then it is possible to underflow to 0
or overflow, depending on the value of *f* and *n*.  Bigfloats
cannot underflow or overflow.



```maxima
(%i1) scale_float(2d0, 2);
(%o1)                                 8.0
(%i2) scale_float(2d0, -2);
(%o2)                                 0.5
(%i3) scale_float(-2d0, -10);
(%o3)                            - 0.001953125
(%i4) scale_float(1d0, -2000);
(%o4)                                 0.0
(%i5) scale_float(2b0, 2);
(%o5)                                8.0b0
(%i6) scale_float(1b0, -2000);
(%o6)                       8.709809816217217b-603
(%i7) scale_float(1, 5);

scale_float: first arg must be a float or bfloat: 1
 -- an error. To debug this try: debugmode(true);
(%i8) scale_float(1.0, n);

scale_float: second arg must be an integer: n
 -- an error. To debug this try: debugmode(true);
```


This is a relatively simple interface to Common Lisp
[http://www.lispworks.com/documentation/HyperSpec/Body/f_dec_fl.htmscale_float]().  Of course, this is extended to support bfloats.

### Function: set_random_state (s)

Copies *s* to the random number generator state.


`set_random_state` always returns `done`.

### Function: signum (x)

For either real or complex numbers *x*, the signum function returns
0 if *x* is zero; for a nonzero numeric input *x*, the signum function
returns `x/abs(x)`.


For non-numeric inputs, Maxima attempts to determine the sign of the input.
When the sign is negative, zero, or positive, `signum` returns -1,0, 1,
respectively.  For all other values for the sign, `signum` a simplified but
equivalent form.  The simplifications include reflection (`signum(-x)`
gives `-signum(x)`) and multiplicative identity (`signum(x*y)` gives
`signum(x) * signum(y)`).


The `signum` function distributes over a list, a matrix, or an
equation.  See `sign` and `distribute_005fover`.

See also: `sign`, `distribute_over`.

### Function: solve_congruences (r_1, ..., r_n, m_1, ..., m_n)

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

### Function: totient (n)

Returns the number of integers less than or equal to *n* which
are relatively prime to *n*.

### Function: truncate (x)

When *x* is a real number, return the closest integer to *x* not
greater in absolute value than *x*.  Evaluation of *x* is similar
to `floor` and `ceiling`.


The `truncate` function distributes over lists, matrices and equations.
See `distribute_005fover`.

See also: `floor`, `ceiling`, `distribute_over`.

### Function: unit_in_last_place (n)

`unit_in_last_place` returns a value that is the gap between
*n* and the nearest other number.  See, for example,
[https://people.eecs.berkeley.edu/~wkahan/LOG10HAF.TXTKahan, FOOTNOTE 1]().  `unit_in_last_place` supports rational numbers,
floating-point numbers and bigfloat numbers.  For integer, the result
is always 1, and for rational numbers the result is always 0.


The examples below assume
[https://en.wikipedia.org/wiki/IEEE_754IEEE-754]() arithmetic that
supports
[https://en.wikipedia.org/wiki/IEEE_754-1985#Denormalized_numbersdenormal]()
numbers.  Some lisps like [https://clisp.sourceforge.io/Clisp]()
do not have denormal numbers.



```maxima
(%i1) unit_in_last_place(0);
(%o1)                                  1
(%i2) unit_in_last_place(-123);
(%o2)                                  1
(%i3) unit_in_last_place(2/3);
(%o3)                                  0
(%i4) unit_in_last_place(355/113);
(%o4)                                  0
(%i5) unit_in_last_place(0b0);
(%o5)                                0.0b0
(%i6) unit_in_last_place(0.0);
(%o6)                       4.940656458412465e-324
(%i7) unit_in_last_place(1.0);
(%o7)                        1.110223024625157e-16
(%i8) unit_in_last_place(1b0);
(%o8)                        1.387778780781446b-17
(%i9) unit_in_last_place(100.0);
(%o9)                         1.4210854715202e-14
(%i10) unit_in_last_place(100b0);
(%o10)                       1.77635683940025b-15
(%i11) fpprec:32;
(%o11)                                32
(%i12) unit_in_last_place(1b0);
(%o12)               1.5407439555097886824447823540679b-33
(%i13) unit_in_last_place(100b0);
(%o13)               1.972152263052529513529321413207b-31
```

### Variable: zerobern

Default value: `true`


When `zerobern` is `false`, `bern` excludes the Bernoulli numbers
and `euler` excludes the Euler numbers which are equal to zero.
See `bern` and `euler`.

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

### Function: zn_add_table (n)

Shows an addition table of all elements in (Z/*n*Z).


See also `zn_mult_table`,  `zn_005fpower_005ftable`.

See also: `zn_mult_table`, `zn_power_table`.

### Function: zn_carmichael_lambda (n)

Returns `1` if *n* is `1` and otherwise 
the greatest characteristic factor of the totient of *n*.


For remarks and examples see `zn_005fcharacteristic_005ffactors`.

See also: `zn_characteristic_factors`.

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

### Function: zn_factor_generators (n)

Returns a list containing factor generators corresponding to the 
characteristic factors of the totient of *n*.


For remarks and examples see `zn_005fcharacteristic_005ffactors`.

See also: `zn_characteristic_factors`.

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

### Function: zn_log (zn_log, a, g, n, zn_log, a, g, n, p1, e1, ..., pk, ek)

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

### Function: zn_mult_table (zn_mult_table, n, zn_mult_table, n, gcd)

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

### Function: zn_nth_root (zn_nth_root, x, n, m, zn_nth_root, x, n, m, p1, e1, ..., pk, ek)

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

### Function: zn_order (zn_order, x, n, zn_order, x, n, p1, e1, ..., pk, ek)

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

### Function: zn_power_table (zn_power_table, n, zn_power_table, n, gcd, zn_power_table, n, gcd, max_exp)

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

### Function: zn_primroot (zn_primroot, n, zn_primroot, n, p1, e1, ..., pk, ek)

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

### Variable: zn_primroot_limit

Default value: `1000` 


If `zn_primroot` cannot find a primitive root, it stops at this upper bound.
If the option variable `zn_primroot_verbose` (default: `false`) is 
set to `true`, a message will be printed when `zn_primroot_limit` is reached.

See also: `zn_primroot`, `zn_primroot_verbose`.

### Function: zn_primroot_p (zn_primroot_p, x, n, zn_primroot_p, x, n, p1, e1, ..., pk, ek)

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

### Variable: zn_primroot_verbose

Default value: `false` 


Controls whether `zn_primroot` prints a message when reaching 
`zn_005fprimroot_005flimit`.

See also: `zn_primroot`, `zn_primroot_limit`.

